# Phase 6 Action 6.4 - Startup and Service Relationship Trace
## Purpose
Trace startup configuration and relationships between major Onyx components
using static source and deployment evidence only.
No Onyx component was executed.
## Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Parent Action 6.3 SHA: `6715d2253db999012d4f57e289e42a5d457a5bc7`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx working tree clean: PASS
## Standard Compose Services
Observed services: 11
```text
api_server
background
web_server
inference_model_server
indexing_model_server
relational_db
opensearch
nginx
cache
minio
code-interpreter
```
## Service Blocks
```text

========================================
SERVICE: api_server
========================================
  api_server:
    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
    build:
      context: ../../backend
      dockerfile: Dockerfile
      # The shipped image; the Dockerfile's default (last) stage is the dev variant
      # with debugging tools (published with a -dev tag suffix).
      target: runtime
    command: >
      /bin/sh -c "alembic upgrade head &&
      echo \"Starting Onyx Api Server\" &&
      uvicorn onyx.main:app --host 0.0.0.0 --port 8080"
    # Check env.template and copy to .env for env vars
    env_file:
      - path: .env
        required: false
    depends_on:
      relational_db:
        condition: service_started
      opensearch:
        condition: service_started
      cache:
        condition: service_started
      inference_model_server:
        condition: service_started
      minio:
        condition: service_started
        required: false
    restart: unless-stopped
    # DEV: To expose ports, either:
    # 1. Use docker-compose.dev.yml: docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --wait
    # 2. Uncomment the ports below
    # ports:
    #   - "8080:8080"
    environment:
      # Auth Settings
      - AUTH_TYPE=${AUTH_TYPE:-basic}
      - FILE_STORE_BACKEND=${FILE_STORE_BACKEND:-s3}
      - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
      - OPENSEARCH_HOST=${OPENSEARCH_HOST:-opensearch}
      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
      - REDIS_HOST=${REDIS_HOST:-cache}
      - MODEL_SERVER_HOST=${MODEL_SERVER_HOST:-inference_model_server}
      - CODE_INTERPRETER_BASE_URL=${CODE_INTERPRETER_BASE_URL:-http://code-interpreter:8000}
      - S3_ENDPOINT_URL=${S3_ENDPOINT_URL:-http://minio:9000}
      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
      # Onyx Craft configuration (disabled by default, set ENABLE_CRAFT=true in .env to enable)
      # Use --include-craft with install script, or manually set in .env file
      - ENABLE_CRAFT=${ENABLE_CRAFT:-false}
    # PRODUCTION: Uncomment the line below to use if IAM_AUTH is true and you are using iam auth for postgres
    # volumes:
    #   - ./bundle.pem:/app/bundle.pem:ro
    extra_hosts:
      - "host.docker.internal:host-gateway"
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')",
        ]
      interval: 30s
      timeout: 20s
      retries: 3
      # Generous start_period so that `docker compose up --wait` does not flag
      # the container unhealthy while alembic migrations run on a fresh DB.
      # Healthy is reported as soon as /health responds, so this does not slow
      # down fast boots.
      start_period: 600s
    # Optional, only for debugging purposes
    volumes:
      - api_server_logs:/var/log/onyx
      # Shared volume for persistent document storage (Craft file-system mode)
      - file-system:/app/file-system


========================================
SERVICE: background
========================================
  background:
    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
    build:
      context: ../../backend
      dockerfile: Dockerfile
      # The shipped image; the Dockerfile's default (last) stage is the dev variant
      # with debugging tools (published with a -dev tag suffix).
      target: runtime
    command: >
      /bin/sh -c "
      if [ -f /etc/ssl/certs/custom-ca.crt ]; then
        update-ca-certificates;
      fi &&
      /app/scripts/supervisord_entrypoint.sh"
    env_file:
      - path: .env
        required: false
    depends_on:
      relational_db:
        condition: service_started
      opensearch:
        condition: service_started
      cache:
        condition: service_started
      inference_model_server:
        condition: service_started
      indexing_model_server:
        condition: service_started
    restart: unless-stopped
    environment:
      - FILE_STORE_BACKEND=${FILE_STORE_BACKEND:-s3}
      - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
      - OPENSEARCH_HOST=${OPENSEARCH_HOST:-opensearch}
      - OPENSEARCH_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
      - REDIS_HOST=${REDIS_HOST:-cache}
      - MODEL_SERVER_HOST=${MODEL_SERVER_HOST:-inference_model_server}
      - INDEXING_MODEL_SERVER_HOST=${INDEXING_MODEL_SERVER_HOST:-indexing_model_server}
      - S3_ENDPOINT_URL=${S3_ENDPOINT_URL:-http://minio:9000}
      - S3_AWS_ACCESS_KEY_ID=${S3_AWS_ACCESS_KEY_ID:-minioadmin}
      - S3_AWS_SECRET_ACCESS_KEY=${S3_AWS_SECRET_ACCESS_KEY:-minioadmin}
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN:-}
      - DISCORD_BOT_INVOKE_CHAR=${DISCORD_BOT_INVOKE_CHAR:-!}
      # API Server connection for Discord bot message processing
      - API_SERVER_PROTOCOL=${API_SERVER_PROTOCOL:-http}
      - API_SERVER_HOST=${API_SERVER_HOST:-api_server}
      # Onyx Craft configuration (set up automatically on container startup)
      - ENABLE_CRAFT=${ENABLE_CRAFT:-false}
    # PRODUCTION: Uncomment the line below to use if IAM_AUTH is true and you are using iam auth for postgres
    # volumes:
    #   - ./bundle.pem:/app/bundle.pem:ro
    extra_hosts:
      - "host.docker.internal:host-gateway"
    # Optional, only for debugging purposes
    volumes:
      - background_logs:/var/log/onyx
      # Shared volume for persistent document storage (Craft file-system mode)
      - file-system:/app/file-system
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    # PRODUCTION: Uncomment the following lines if you need to include a custom CA certificate
    # This section enables the use of a custom CA certificate
    # If present, the custom CA certificate is mounted as a volume
    # The container checks for its existence and updates the system's CA certificates
    # This allows for secure communication with services using custom SSL certificates
    # Optional volume mount for CA certificate
    # volumes:
    #   # Maps to the CA_CERT_PATH environment variable in the Dockerfile
    #   - ${CA_CERT_PATH:-./custom-ca.crt}:/etc/ssl/certs/custom-ca.crt:ro


========================================
SERVICE: web_server
========================================
  web_server:
    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
    build:
      context: ../../web
      dockerfile: Dockerfile
      args:
        - NEXT_PUBLIC_DISABLE_LOGOUT=${NEXT_PUBLIC_DISABLE_LOGOUT:-}
        - NEXT_PUBLIC_FORGOT_PASSWORD_ENABLED=${NEXT_PUBLIC_FORGOT_PASSWORD_ENABLED:-}
        # Enterprise Edition only
        - NEXT_PUBLIC_THEME=${NEXT_PUBLIC_THEME:-}
        # DO NOT TURN ON unless you have EXPLICIT PERMISSION from Onyx.
        - NEXT_PUBLIC_DO_NOT_USE_TOGGLE_OFF_DANSWER_POWERED=${NEXT_PUBLIC_DO_NOT_USE_TOGGLE_OFF_DANSWER_POWERED:-false}
        - NODE_OPTIONS=${NODE_OPTIONS:-"--max-old-space-size=4096"}
    env_file:
      - path: .env
        required: false
    depends_on:
      - api_server
    restart: unless-stopped
    environment:
      - INTERNAL_URL=${INTERNAL_URL:-http://api_server:8080}
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    healthcheck:
      test:
        [
          "CMD",
          "node",
          "-e",
          "require('http').get('http://127.0.0.1:3000/', (r) => process.exit(r.statusCode < 500 ? 0 : 1)).on('error', () => process.exit(1))",
        ]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

  # Uncomment the block below to enable the MCP server for Onyx.
  # mcp_server:
  #   image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
  #   build:
  #     context: ../../backend
  #     dockerfile: Dockerfile
  #     target: runtime
  #   command: >
  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
  #       exit 0;
  #     else
  #       exec python -m onyx.mcp_server_main;
  #     fi"
  #   env_file:
  #     - path: .env
  #       required: false
  #   depends_on:
  #     - relational_db
  #     - cache
  #   restart: "no"
  #   environment:
  #     - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
  #     - REDIS_HOST=${REDIS_HOST:-cache}
  #     # MCP Server Configuration
  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
  #     - MCP_SERVER_CORS_ORIGINS=${MCP_SERVER_CORS_ORIGINS:-}
  #     - API_SERVER_PROTOCOL=${API_SERVER_PROTOCOL:-http}
  #     - API_SERVER_HOST=${API_SERVER_HOST:-api_server}
  #   extra_hosts:
  #     - "host.docker.internal:host-gateway"
  #   logging:
  #     driver: json-file
  #     options:
  #       max-size: "50m"
  #       max-file: "6"
  #   # Optional, only for debugging purposes
  #   volumes:
  #     - mcp_server_logs:/var/log/onyx


========================================
SERVICE: inference_model_server
========================================
  inference_model_server:
    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
    build:
      context: ../../backend
      dockerfile: Dockerfile.model_server
    # GPU Support: Uncomment the following lines to enable GPU support
    # Requires nvidia-container-toolkit to be installed on the host
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]
    env_file:
      - path: .env
        required: false
    restart: unless-stopped
    volumes:
      # Not necessary, this is just to reduce download time during startup
      - model_cache_huggingface:/app/.cache/huggingface/
      # Optional, only for debugging purposes
      - inference_model_server_logs:/var/log/onyx
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
        ]
      interval: 20s
      timeout: 5s
      retries: 3
      # Generous start_period to absorb HuggingFace model downloads on first
      # boot. Healthy is reported as soon as /api/health responds.
      start_period: 600s


========================================
SERVICE: indexing_model_server
========================================
  indexing_model_server:
    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
    build:
      context: ../../backend
      dockerfile: Dockerfile.model_server
    # GPU Support: Uncomment the following lines to enable GPU support
    # Requires nvidia-container-toolkit to be installed on the host
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]
    env_file:
      - path: .env
        required: false
    restart: unless-stopped
    environment:
      - INDEXING_ONLY=True
    volumes:
      # Not necessary, this is just to reduce download time during startup
      - indexing_huggingface_model_cache:/app/.cache/huggingface/
      # Optional, only for debugging purposes
      - indexing_model_server_logs:/var/log/onyx
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
        ]
      interval: 20s
      timeout: 5s
      retries: 3
      # Generous start_period to absorb HuggingFace model downloads on first
      # boot. Healthy is reported as soon as /api/health responds.
      start_period: 600s


========================================
SERVICE: relational_db
========================================
  relational_db:
    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
    shm_size: 1g
    command: -c 'max_connections=250'
    env_file:
      - path: .env
        required: false
    restart: unless-stopped
    # PRODUCTION: Override the defaults by passing in the environment variables
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-postgres}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
    # DEV: To expose ports, either:
    # 1. Use docker-compose.dev.yml: docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --wait
    # 2. Uncomment the ports below
    # ports:
    #   - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-postgres}"]
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - db_volume:/var/lib/postgresql/data
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"


========================================
SERVICE: opensearch
========================================
  opensearch:
    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
    restart: unless-stopped
    # OpenSearch is the search backend and is enabled by default. To run against
    # an external OpenSearch instance, set OPENSEARCH_HOST in your env and
    # remove this service from the compose file (or skip it via the service list
    # when running `docker compose up`).
    environment:
      # We need discovery.type=single-node so that OpenSearch doesn't try
      # forming a cluster and waiting for other nodes to become live.
      - discovery.type=single-node
      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=${OPENSEARCH_ADMIN_PASSWORD:-StrongPassword123!}
      # This and the JVM config below come from the example in https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/
      # We do this to avoid unstable performance from page swaps.
      - bootstrap.memory_lock=true # Disable JVM heap memory swapping.
      # Java heap should be ~50% of memory limit. For now we assume a limit of
      # 4g although in practice the container can request more than this.
      # See https://opster.com/guides/opensearch/opensearch-basics/opensearch-heap-size-usage-and-jvm-garbage-collection/
      # Xms is the starting size, Xmx is the maximum size. These should be the
      # same.
      - "OPENSEARCH_JAVA_OPTS=-Xms2g -Xmx2g"
    volumes:
      - opensearch-data:/usr/share/opensearch/data
    # These come from the example in https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/
    ulimits:
      # Similarly to bootstrap.memory_lock, we don't want to impose limits on
      # how much memory a process can lock from being swapped.
      memlock:
        soft: -1 # Set memlock to unlimited (no soft or hard limit).
        hard: -1
      nofile:
        soft: 65536 # Maximum number of open files for the opensearch user - set to at least 65536.
        hard: 65536
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"


========================================
SERVICE: nginx
========================================
  nginx:
    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
    restart: unless-stopped
    # nginx will immediately crash with `nginx: [emerg] host not found in upstream`
    # if api_server / web_server are not up
    depends_on:
      api_server:
        condition: service_healthy
      web_server:
        condition: service_healthy
    env_file:
      - path: .env
        required: false
    environment:
      - DOMAIN=localhost
      # Nginx proxy timeout settings (in seconds)
      - NGINX_PROXY_CONNECT_TIMEOUT=${NGINX_PROXY_CONNECT_TIMEOUT:-300}
      - NGINX_PROXY_SEND_TIMEOUT=${NGINX_PROXY_SEND_TIMEOUT:-300}
      - NGINX_PROXY_READ_TIMEOUT=${NGINX_PROXY_READ_TIMEOUT:-300}
    ports:
      - "${HOST_PORT_80:-80}:80"
      - "${HOST_PORT:-3000}:80" # allow for localhost:3000 usage, since that is the norm
    volumes:
      # Mount templates read-only; the startup command copies them into
      # the writable /etc/nginx/conf.d/ inside the container.  This avoids
      # "Permission denied" errors on Windows Docker bind mounts.
      - ../data/nginx:/nginx-templates:ro
    # PRODUCTION: Add SSL certificate volumes for HTTPS support:
    #   - ../data/certbot/conf:/etc/letsencrypt
    #   - ../data/certbot/www:/var/www/certbot
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "6"
    # The specified script waits for the api_server to start up.
    # Without this we've seen issues where nginx shows no error logs but
    # does not receive any traffic
    # PRODUCTION: Change to app.conf.template.prod for production nginx config
    command: >
      /bin/sh -c "rm -f /etc/nginx/conf.d/default.conf
      && cp -a /nginx-templates/. /etc/nginx/conf.d/
      && sed 's/\r$//' /etc/nginx/conf.d/run-nginx.sh > /tmp/run-nginx.sh
      && chmod +x /tmp/run-nginx.sh
      && /tmp/run-nginx.sh app.conf.template"
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--quiet",
          "--tries=1",
          "--spider",
          "http://127.0.0.1/nginx-health",
        ]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s


========================================
SERVICE: cache
========================================
  cache:
    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
    restart: unless-stopped
    # DEV: To expose ports, either:
    # 1. Use docker-compose.dev.yml: docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --wait
    # 2. Uncomment the ports below
    # ports:
    #   - "6379:6379"
    # docker silently mounts /data even without an explicit volume mount, which enables
    # persistence. explicitly setting save and appendonly forces ephemeral behavior.
    command: redis-server --save "" --appendonly no
    env_file:
      - path: .env
        required: false
    # Use tmpfs to prevent creation of anonymous volumes for /data
    tmpfs:
      - /data


========================================
SERVICE: minio
========================================
  minio:
    # Docker Hub dropped minio/minio when MinIO archived its community edition,
    # so this does not go through BASE_IMAGE_REGISTRY (a Docker Hub mirror).
    # RELEASE.2025-09-07 is the last multi-arch build; -cpuv1 also runs on
    # x86-64-v1 CPUs. Pinned by digest.
    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
    profiles: ["s3-filestore"]
    restart: unless-stopped
    # DEV: To expose ports, either:
    # 1. Use docker-compose.dev.yml: docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --wait
    # 2. Uncomment the ports below
    # ports:
    #   - "9004:9000"
    #   - "9005:9001"
    env_file:
      - path: .env
        required: false
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}
      # Note: we've seen the default bucket creation logic not work in some cases
      MINIO_DEFAULT_BUCKETS: ${S3_FILE_STORE_BUCKET_NAME:-onyx-file-store-bucket}
    volumes:
      - minio_data:/data
    command: server /data --console-address ":9001"
    healthcheck:
      test: ["CMD", "mc", "ready", "local"]
      interval: 30s
      timeout: 20s
      retries: 3


========================================
SERVICE: code-interpreter
========================================
  code-interpreter:
    # The sandbox ships on its own release line, so IMAGE_TAG does not cover it.
    # Pinned so an upgrade cannot move it to an untested build. Bump with the
    # release that has been tested against it.
    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
    command: ["bash", "./entrypoint.sh", "code-interpreter-api"]
    restart: unless-stopped
    env_file:
      - path: .env
        required: false
    healthcheck:
      # /health probes the executor backend, not just the API process: it needs
      # the Docker daemon reachable and the executor image present on the host.
      # That image is pulled only during startup and `docker run --pull never`
      # is used per request, so a host that loses it (e.g. `docker system prune
      # --all`) stays broken until this container restarts. The service answers
      # 200 with status != ok in that state, so the body has to be read.
      test:
        [
          "CMD",
          "python",
          "-c",
          "import json,urllib.request; r = json.load(urllib.request.urlopen('http://localhost:8000/health', timeout=5)); raise SystemExit(0 if r['status'] == 'ok' else 1)",
        ]
      interval: 30s
      timeout: 10s
      retries: 3
      # First run pulls the executor image and does not serve until it lands.
      start_period: 120s

    # Below is needed for the `docker-out-of-docker` execution mode
    # For Linux rootless Docker, set DOCKER_SOCK_PATH=${XDG_RUNTIME_DIR}/docker.sock
    user: root
    volumes:
      - ${DOCKER_SOCK_PATH:-/var/run/docker.sock}:/var/run/docker.sock

    # uncomment below + comment out the above to use the `docker-in-docker` execution mode
    # privileged: true

  # PRODUCTION: Uncomment the following certbot service for SSL certificate management
  # certbot:
  #   image: certbot/certbot
  #   restart: unless-stopped
  #   volumes:
  #     - ../data/certbot/conf:/etc/letsencrypt
  #     - ../data/certbot/www:/var/www/certbot
  #   logging:
  #     driver: json-file
  #     options:
  #       max-size: "50m"
  #       max-file: "6"
  #   entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'"

volumes:
  # Necessary for persisting data for use
```
## Explicit Startup Dependencies
Observed dependency edges: 13
```text
api_server -> cache
api_server -> inference_model_server
api_server -> minio
api_server -> opensearch
api_server -> relational_db
background -> cache
background -> indexing_model_server
background -> inference_model_server
background -> opensearch
background -> relational_db
nginx -> api_server
nginx -> web_server
web_server -> api_server
```
A Compose dependency demonstrates startup/configuration ordering only.
It does not by itself prove application data flow or a security trust boundary.
## Startup Configuration
```text
48:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
49:    build:
55:    command: >
75:    restart: unless-stopped
130:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
131:    build:
137:    command: >
157:    restart: unless-stopped
202:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
203:    build:
219:    restart: unless-stopped
282:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
283:    build:
298:    restart: unless-stopped
325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
326:    build:
341:    restart: unless-stopped
370:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
372:    command: -c 'max_connections=250'
376:    restart: unless-stopped
400:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
401:    restart: unless-stopped
439:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
440:    restart: unless-stopped
477:    command: >
499:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
500:    restart: unless-stopped
508:    command: redis-server --save "" --appendonly no
521:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
522:    profiles: ["s3-filestore"]
523:    restart: unless-stopped
540:    command: server /data --console-address ":9001"
551:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
552:    command: ["bash", "./entrypoint.sh", "code-interpreter-api"]
553:    restart: unless-stopped
```
## Backend API Startup
Evidence lines: 105
```text
HEAD:backend/ee/onyx/main.py:55:    include_router_with_global_prefix_prepended,
HEAD:backend/ee/onyx/main.py:58:from onyx.main import lifespan as lifespan_base
HEAD:backend/ee/onyx/main.py:68:async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
HEAD:backend/ee/onyx/main.py:69:    """Small wrapper around the lifespan of the MIT application.
HEAD:backend/ee/onyx/main.py:70:    Basically just calls the base lifespan, and then adds EE-only
HEAD:backend/ee/onyx/main.py:73:    async with lifespan_base(app):
HEAD:backend/ee/onyx/main.py:88:    application = get_application_base(lifespan_override=lifespan)
HEAD:backend/ee/onyx/main.py:133:    include_router_with_global_prefix_prepended(application, user_group_router)
HEAD:backend/ee/onyx/main.py:135:    include_router_with_global_prefix_prepended(application, analytics_router)
HEAD:backend/ee/onyx/main.py:136:    include_router_with_global_prefix_prepended(application, query_history_router)
HEAD:backend/ee/onyx/main.py:138:    include_router_with_global_prefix_prepended(application, query_router)
HEAD:backend/ee/onyx/main.py:139:    include_router_with_global_prefix_prepended(application, ee_query_router)
HEAD:backend/ee/onyx/main.py:140:    include_router_with_global_prefix_prepended(application, search_router)
HEAD:backend/ee/onyx/main.py:141:    include_router_with_global_prefix_prepended(application, standard_answer_router)
HEAD:backend/ee/onyx/main.py:142:    include_router_with_global_prefix_prepended(application, ee_oauth_router)
HEAD:backend/ee/onyx/main.py:143:    include_router_with_global_prefix_prepended(application, ee_document_cc_pair_router)
HEAD:backend/ee/onyx/main.py:144:    include_router_with_global_prefix_prepended(application, evals_router)
HEAD:backend/ee/onyx/main.py:145:    include_router_with_global_prefix_prepended(application, hook_router)
HEAD:backend/ee/onyx/main.py:146:    include_router_with_global_prefix_prepended(application, llm_gateway_router)
HEAD:backend/ee/onyx/main.py:149:    include_router_with_global_prefix_prepended(
HEAD:backend/ee/onyx/main.py:153:    include_router_with_global_prefix_prepended(
HEAD:backend/ee/onyx/main.py:156:    include_router_with_global_prefix_prepended(application, enterprise_settings_router)
HEAD:backend/ee/onyx/main.py:157:    include_router_with_global_prefix_prepended(application, usage_export_router)
HEAD:backend/ee/onyx/main.py:159:    include_router_with_global_prefix_prepended(application, log_export_router)
HEAD:backend/ee/onyx/main.py:161:    include_router_with_global_prefix_prepended(application, license_router)
HEAD:backend/ee/onyx/main.py:165:    include_router_with_global_prefix_prepended(application, billing_router)
HEAD:backend/ee/onyx/main.py:169:        include_router_with_global_prefix_prepended(application, tenants_router)
HEAD:backend/ee/onyx/main.py:174:    application.include_router(scim_router)
HEAD:backend/onyx/main.py:265:def include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:281:    application.include_router(router, **final_kwargs)
HEAD:backend/onyx/main.py:292:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:344:async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: ARG001
HEAD:backend/onyx/main.py:516:def get_application(lifespan_override: Lifespan | None = None) -> FastAPI:
HEAD:backend/onyx/main.py:517:    application = FastAPI(
HEAD:backend/onyx/main.py:530:        lifespan=lifespan_override or lifespan,
HEAD:backend/onyx/main.py:552:    include_router_with_global_prefix_prepended(application, password_router)
HEAD:backend/onyx/main.py:553:    include_router_with_global_prefix_prepended(application, chat_router)
HEAD:backend/onyx/main.py:554:    include_router_with_global_prefix_prepended(application, query_router)
HEAD:backend/onyx/main.py:555:    include_router_with_global_prefix_prepended(application, document_router)
HEAD:backend/onyx/main.py:556:    include_router_with_global_prefix_prepended(application, user_router)
HEAD:backend/onyx/main.py:557:    include_router_with_global_prefix_prepended(application, oauth_test_admin_router)
HEAD:backend/onyx/main.py:558:    include_router_with_global_prefix_prepended(application, admin_query_router)
HEAD:backend/onyx/main.py:559:    include_router_with_global_prefix_prepended(application, admin_router)
HEAD:backend/onyx/main.py:560:    include_router_with_global_prefix_prepended(application, connector_router)
HEAD:backend/onyx/main.py:561:    include_router_with_global_prefix_prepended(application, credential_router)
HEAD:backend/onyx/main.py:562:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:565:    include_router_with_global_prefix_prepended(application, input_prompt_router)
HEAD:backend/onyx/main.py:566:    include_router_with_global_prefix_prepended(application, admin_input_prompt_router)
HEAD:backend/onyx/main.py:567:    include_router_with_global_prefix_prepended(application, cc_pair_router)
HEAD:backend/onyx/main.py:568:    include_router_with_global_prefix_prepended(application, targeted_reindex_router)
HEAD:backend/onyx/main.py:569:    include_router_with_global_prefix_prepended(application, projects_router)
HEAD:backend/onyx/main.py:570:    include_router_with_global_prefix_prepended(application, public_build_router)
HEAD:backend/onyx/main.py:571:    include_router_with_global_prefix_prepended(application, build_router)
HEAD:backend/onyx/main.py:572:    include_router_with_global_prefix_prepended(application, build_admin_router)
HEAD:backend/onyx/main.py:573:    include_router_with_global_prefix_prepended(application, image_generation_router)
HEAD:backend/onyx/main.py:574:    include_router_with_global_prefix_prepended(application, document_set_router)
HEAD:backend/onyx/main.py:575:    include_router_with_global_prefix_prepended(application, hierarchy_router)
HEAD:backend/onyx/main.py:576:    include_router_with_global_prefix_prepended(application, search_api_router)
HEAD:backend/onyx/main.py:577:    include_router_with_global_prefix_prepended(application, search_settings_router)
HEAD:backend/onyx/main.py:578:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:581:    include_router_with_global_prefix_prepended(application, discord_bot_router)
HEAD:backend/onyx/main.py:582:    include_router_with_global_prefix_prepended(application, persona_router)
HEAD:backend/onyx/main.py:583:    include_router_with_global_prefix_prepended(application, admin_persona_router)
HEAD:backend/onyx/main.py:584:    include_router_with_global_prefix_prepended(application, agents_router)
HEAD:backend/onyx/main.py:585:    include_router_with_global_prefix_prepended(application, admin_agents_router)
HEAD:backend/onyx/main.py:586:    include_router_with_global_prefix_prepended(application, default_assistant_router)
HEAD:backend/onyx/main.py:587:    include_router_with_global_prefix_prepended(application, notification_router)
HEAD:backend/onyx/main.py:588:    include_router_with_global_prefix_prepended(application, admin_banner_router)
HEAD:backend/onyx/main.py:589:    include_router_with_global_prefix_prepended(application, tool_router)
HEAD:backend/onyx/main.py:590:    include_router_with_global_prefix_prepended(application, admin_tool_router)
HEAD:backend/onyx/main.py:591:    include_router_with_global_prefix_prepended(application, oauth_config_router)
HEAD:backend/onyx/main.py:592:    include_router_with_global_prefix_prepended(application, admin_oauth_config_router)
HEAD:backend/onyx/main.py:593:    include_router_with_global_prefix_prepended(application, user_oauth_token_router)
HEAD:backend/onyx/main.py:594:    include_router_with_global_prefix_prepended(application, state_router)
HEAD:backend/onyx/main.py:595:    include_router_with_global_prefix_prepended(application, onyx_api_router)
HEAD:backend/onyx/main.py:596:    include_router_with_global_prefix_prepended(application, settings_router)
HEAD:backend/onyx/main.py:597:    include_router_with_global_prefix_prepended(application, settings_admin_router)
HEAD:backend/onyx/main.py:598:    include_router_with_global_prefix_prepended(application, security_admin_router)
HEAD:backend/onyx/main.py:599:    include_router_with_global_prefix_prepended(application, sso_admin_router)
HEAD:backend/onyx/main.py:600:    include_router_with_global_prefix_prepended(application, llm_admin_router)
HEAD:backend/onyx/main.py:601:    include_router_with_global_prefix_prepended(application, kg_admin_router)
HEAD:backend/onyx/main.py:602:    include_router_with_global_prefix_prepended(application, llm_router)
HEAD:backend/onyx/main.py:603:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:606:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:609:    include_router_with_global_prefix_prepended(application, embedding_admin_router)
HEAD:backend/onyx/main.py:610:    include_router_with_global_prefix_prepended(application, embedding_router)
HEAD:backend/onyx/main.py:611:    include_router_with_global_prefix_prepended(application, web_search_router)
HEAD:backend/onyx/main.py:612:    include_router_with_global_prefix_prepended(application, web_search_admin_router)
HEAD:backend/onyx/main.py:613:    include_router_with_global_prefix_prepended(application, tracing_admin_router)
HEAD:backend/onyx/main.py:614:    include_router_with_global_prefix_prepended(application, voice_admin_router)
HEAD:backend/onyx/main.py:615:    include_router_with_global_prefix_prepended(application, voice_router)
HEAD:backend/onyx/main.py:616:    include_router_with_global_prefix_prepended(application, voice_websocket_router)
HEAD:backend/onyx/main.py:617:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:620:    include_router_with_global_prefix_prepended(application, cost_override_router)
HEAD:backend/onyx/main.py:621:    include_router_with_global_prefix_prepended(application, user_usage_router)
HEAD:backend/onyx/main.py:622:    include_router_with_global_prefix_prepended(application, admin_usage_router)
HEAD:backend/onyx/main.py:623:    include_router_with_global_prefix_prepended(application, api_key_router)
HEAD:backend/onyx/main.py:624:    include_router_with_global_prefix_prepended(application, standard_oauth_router)
HEAD:backend/onyx/main.py:625:    include_router_with_global_prefix_prepended(application, federated_router)
HEAD:backend/onyx/main.py:626:    include_router_with_global_prefix_prepended(application, mcp_router)
HEAD:backend/onyx/main.py:627:    include_router_with_global_prefix_prepended(application, mcp_admin_router)
HEAD:backend/onyx/main.py:628:    include_router_with_global_prefix_prepended(application, skill_router)
HEAD:backend/onyx/main.py:630:    include_router_with_global_prefix_prepended(application, pat_router)
HEAD:backend/onyx/main.py:631:    include_router_with_global_prefix_prepended(application, captcha_router)
HEAD:backend/onyx/main.py:811:    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
```
## Background Worker Startup
Evidence lines: 400
```text
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:2:from onyx.background.celery.apps.docfetching import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:2:from onyx.background.celery.apps.docprocessing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:2:from onyx.background.celery.apps.heavy import celery_app
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/light.py:2:from onyx.background.celery.apps.light import celery_app
HEAD:backend/ee/onyx/background/celery/apps/light.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:2:from onyx.background.celery.apps.monitoring import celery_app
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/primary.py:2:from onyx.background.celery.apps.primary import celery_app
HEAD:backend/ee/onyx/background/celery/apps/primary.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:2:from onyx.background.celery.apps.scheduled_tasks import celery_app
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:2:from onyx.background.celery.apps.user_file_processing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:5:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:6:    BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:9:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:10:    beat_cloud_tasks as base_beat_system_tasks,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:12:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:13:    beat_task_templates as base_beat_task_templates,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:15:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:18:from onyx.configs.constants import OnyxCeleryPriority, OnyxCeleryQueues, OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:21:ee_beat_system_tasks: list[dict] = []
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:23:ee_beat_task_templates: list[dict] = [
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:30:            "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:39:            "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:48:            "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:49:            "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:58:            "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:76:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:85:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:94:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:103:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:112:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:113:                "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:124:                "expires": BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:125:                # Cleanup belongs on the heavy worker; it shares the queue the
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:128:                "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:134:def get_cloud_tasks_to_schedule(beat_multiplier: float) -> list[dict[str, Any]]:
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:135:    beat_system_tasks = ee_beat_system_tasks + base_beat_system_tasks
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:136:    beat_task_templates = ee_beat_task_templates + base_beat_task_templates
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:138:        beat_system_tasks, beat_task_templates, beat_multiplier
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:9:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:11:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:72:    name=OnyxCeleryTask.CLOUD_BEAT_TASK_GENERATOR,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:77:def cloud_beat_task_generator(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:80:    queue: str = OnyxCeleryTask.DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:82:    expires: int = BEAT_EXPIRES_DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:86:    """a lightweight task used to kick off individual beat tasks per tenant."""
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:91:    lock_beat: RedisLock = redis_client.lock(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:92:        f"{OnyxRedisLocks.CLOUD_BEAT_TASK_GENERATOR_LOCK}:{task_name}",
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:93:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:97:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:115:        # reaches the finally that releases the beat lock.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:160:        # `skip_gated=False` from the beat schedule.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:169:            if current_time - last_lock_time >= (CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:170:                lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:197:                queue=queue,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:209:        task_logger.exception("Unexpected exception during cloud_beat_task_generator")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:211:        if not lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:213:                "cloud_beat_task_generator - Lock not owned on completion"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:215:            redis_lock_dump(lock_beat, redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:217:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:221:        f"cloud_beat_task_generator finished: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:30:    celery_get_queue_length,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:31:    celery_get_queued_task_ids,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:34:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:37:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:43:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:81:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:126:    Base expiration is 300 seconds, multiplied by the beat multiplier only in MULTI_TENANT mode.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:134:        beat_multiplier = OnyxRuntime.get_beat_multiplier()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:136:        beat_multiplier = CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:138:    return int(base_expiration * beat_multiplier)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:220:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:222:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:226:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:246:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:259:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:262:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:282:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:311:        if lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:312:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:450:    # the primary worker sends the task and it is immediately executed
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:451:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:795:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:798:    # validating until the queue is small
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:801:    queue_len = celery_get_queue_length(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:807:    queued_upsert_tasks = celery_get_queued_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:815:    lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:826:            queued_upsert_tasks,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:832:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:840:    queued_tasks: set[str],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:846:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:852:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:863:    whether a task is in the queue or currently executing.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:865:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:866:    and the time it actually starts on the worker.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:919:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:924:        # the celery task was prefetched and is reserved within a worker
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:928:    # look up every task in the current taskset in the celery queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:929:    # every entry in the taskset should have an associated entry in the celery task queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:947:        if member_str in queued_tasks:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1038:                CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:36:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:41:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:44:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:103:    Base expiration is 300 seconds, multiplied by the beat multiplier only in MULTI_TENANT mode.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:111:        beat_multiplier = OnyxRuntime.get_beat_multiplier()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:113:        beat_multiplier = CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:115:    return int(base_expiration * beat_multiplier)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:175:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:177:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:181:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:220:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:229:                f"External group sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:233:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:236:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:264:        if lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:265:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:326:            queue=OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:374:    # the primary worker sends the task and it is immediately executed
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:375:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:681:    celery_app: Celery,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:685:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:688:        OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:692:    lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:707:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:718:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:724:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:735:    whether a task is in the queue or currently executing.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:737:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:738:    and the time it actually starts on the worker.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:786:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:17:# Supervisord captures each worker program's stdout to
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:25:# queue delivers each collect task to exactly ONE consumer, so with HPA-scaled
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:26:# workers (replicas > 1) only one pod per worker type is sampled, and nothing
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:40:    worker_name: str,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:48:        worker_name=worker_name,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:53:        "Log export collection finished: export_id=%s worker_name=%s "
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:56:        worker_name,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:69:    tenant_id: str,  # noqa: ARG001  # Injected into every beat task by ``DynamicTenantScheduler``.
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:25:    """Fanned out per tenant by cloud_beat_task_generator. The re-projection is
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:16:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:39:    queue=OnyxCeleryQueues.MONITORING,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:11:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:26:# (and whose chain a later beat has replaced) from extending someone else's lease.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:64:    # Defaulted for rollout compatibility: a message enqueued by the pre-upgrade
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:66:    # such a message harmlessly no-ops below and the beat starts a fresh chain.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:74:    expired sessions and exits, so it occupies a single light-worker thread for
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:75:    only one short batch and interleaves with the other light-queue work. If a
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:76:    full batch is deleted (more sessions likely remain) it enqueues the next task
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:82:    lease and the beat starts a replacement chain, the superseded task can neither
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:84:    per tenant at a time, so at most one light-worker thread does TTL work.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:136:                queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:173:    # active task may not be sitting in the queue), so don't start another.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:190:            queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:195:        # Roll back the claim so the next beat can start the chain.
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:22:    """This function is likely to move in the worker refactor happening next."""
HEAD:backend/onyx/background/README.md:9:5. Reporting metrics on things like queue length for monitoring purposes
HEAD:backend/onyx/background/README.md:11:## Worker → Queue Mapping
HEAD:backend/onyx/background/README.md:13:| Worker                    | File                           | Queues                                                                                                               |
HEAD:backend/onyx/background/README.md:22:| Background (consolidated) | `apps/background.py`           | All queues above except `celery`                                                                                     |
HEAD:backend/onyx/background/README.md:24:## Non-Worker Apps
HEAD:backend/onyx/background/README.md:28:| **Beat**   | `beat.py`   | Celery beat scheduler with `DynamicTenantScheduler` that generates per-tenant periodic task schedules |
HEAD:backend/onyx/background/README.md:29:| **Client** | `client.py` | Minimal app for task submission from non-worker processes (e.g., API server)                          |
HEAD:backend/onyx/background/README.md:39:## Worker Details
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
HEAD:backend/onyx/background/README.md:53:Then it cycles through its tasks as scheduled by Celery Beat:
HEAD:backend/onyx/background/README.md:57:| `check_for_indexing`              | 15s       | Scans for connectors needing indexing → dispatches to `DOCFETCHING` queue                  |
HEAD:backend/onyx/background/README.md:58:| `check_for_vespa_sync_task`       | 20s       | Finds stale documents/document sets → dispatches sync tasks to `VESPA_METADATA_SYNC` queue |
HEAD:backend/onyx/background/README.md:59:| `check_for_pruning`               | 20s       | Finds connectors due for pruning → dispatches to `CONNECTOR_PRUNING` queue                 |
HEAD:backend/onyx/background/README.md:60:| `check_for_connector_deletion`    | 20s       | Processes deletion requests → dispatches to `CONNECTOR_DELETION` queue                     |
HEAD:backend/onyx/background/README.md:61:| `check_for_user_file_processing`  | 20s       | Checks for user uploads → dispatches to `USER_FILE_PROCESSING` queue                       |
HEAD:backend/onyx/background/README.md:64:| `celery_beat_heartbeat`           | 1m        | Heartbeat for Beat watchdog                                                                |
HEAD:backend/onyx/background/README.md:66:Watchdog is a separate Python process managed by supervisord which runs alongside celery workers. It checks the ONYX_CELERY_BEAT_HEARTBEAT_KEY in
HEAD:backend/onyx/background/README.md:67:Redis to ensure Celery Beat is not dead. Beat schedules the celery_beat_heartbeat for Primary to touch the key and share that it's still alive.
HEAD:backend/onyx/background/README.md:73:Can have 24 concurrent workers, each with a prefetch of 8 for a total of 192 tasks in flight at once.
HEAD:backend/onyx/background/README.md:103:- Queue lengths, connector success/failure, connector latencies
HEAD:backend/onyx/background/README.md:104:- Memory of supervisor managed processes (workers, beat, slack)
HEAD:backend/onyx/background/README.md:109:Workers can expose Prometheus metrics via a standalone HTTP server. Currently docfetching and docprocessing have push-based task lifecycle metrics; the monitoring worker runs pull-based collectors for queue depth and connector health.
HEAD:backend/onyx/background/README.md:111:For the full metric reference, integration guide, and PromQL examples, see [`docs/METRICS.md`](../../../docs/METRICS.md#celery-worker-metrics).
HEAD:backend/onyx/background/celery/apps/app_base.py:13:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/app_base.py:17:from celery.worker import strategy
HEAD:backend/onyx/background/celery/apps/app_base.py:18:from celery.worker.control import control_command
HEAD:backend/onyx/background/celery/apps/app_base.py:30:    celery_is_worker_primary,
HEAD:backend/onyx/background/celery/apps/app_base.py:92:    """Remote command to wipe this worker's in-memory revoked-task set.
HEAD:backend/onyx/background/celery/apps/app_base.py:94:    The set lives only in memory, propagates between workers via mingle, and its
HEAD:backend/onyx/background/celery/apps/app_base.py:102:    from celery.worker import state as worker_state
HEAD:backend/onyx/background/celery/apps/app_base.py:104:    count = len(worker_state.revoked)
HEAD:backend/onyx/background/celery/apps/app_base.py:105:    worker_state.revoked.clear()
HEAD:backend/onyx/background/celery/apps/app_base.py:127:            # so it does not leak into any subsequent tasks on the same worker process
HEAD:backend/onyx/background/celery/apps/app_base.py:137:    workers can compute queue wait time (time between publish and execution)."""
HEAD:backend/onyx/background/celery/apps/app_base.py:139:        headers["enqueued_at"] = time.time()
HEAD:backend/onyx/background/celery/apps/app_base.py:152:    # from a previous task executed in the same worker process do not leak
HEAD:backend/onyx/background/celery/apps/app_base.py:178:    This also does not fire if a worker with acks_late=False crashes (which all of our
HEAD:backend/onyx/background/celery/apps/app_base.py:179:    long running workers are)
HEAD:backend/onyx/background/celery/apps/app_base.py:294:    """The first signal sent on celery worker startup"""
HEAD:backend/onyx/background/celery/apps/app_base.py:322:    # Initialize tracing in workers if credentials are available.
HEAD:backend/onyx/background/celery/apps/app_base.py:328:    Will raise WorkerShutdown to kill the celery worker if the timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:362:        raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:370:    Will raise WorkerShutdown to kill the celery worker if the timeout is reached."""
HEAD:backend/onyx/background/celery/apps/app_base.py:403:        raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:409:def on_secondary_worker_init(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:410:    logger.info("Running as a secondary celery worker: pid=%s", os.getpid())
HEAD:backend/onyx/background/celery/apps/app_base.py:412:    # Set up variables for waiting on primary worker
HEAD:backend/onyx/background/celery/apps/app_base.py:418:    logger.info("Waiting for primary worker to be ready...")
HEAD:backend/onyx/background/celery/apps/app_base.py:420:        if r.exists(OnyxRedisLocks.PRIMARY_WORKER):
HEAD:backend/onyx/background/celery/apps/app_base.py:425:            "Primary worker is not ready yet. elapsed=%s timeout=%s",
HEAD:backend/onyx/background/celery/apps/app_base.py:430:            msg = f"Primary worker was not ready within the timeout. ({WAIT_LIMIT} seconds). Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:432:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:436:    logger.info("Wait for primary worker completed successfully. Continuing...")
HEAD:backend/onyx/background/celery/apps/app_base.py:440:def on_worker_ready(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:441:    task_logger.info("worker_ready signal received.")
HEAD:backend/onyx/background/celery/apps/app_base.py:453:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:460:    if not celery_is_worker_primary(sender):
HEAD:backend/onyx/background/celery/apps/app_base.py:463:    if not hasattr(sender, "primary_worker_lock"):
HEAD:backend/onyx/background/celery/apps/app_base.py:464:        # primary_worker_lock will not exist when MULTI_TENANT is True
HEAD:backend/onyx/background/celery/apps/app_base.py:467:    if not sender.primary_worker_lock:
HEAD:backend/onyx/background/celery/apps/app_base.py:470:    logger.info("Releasing primary worker lock.")
HEAD:backend/onyx/background/celery/apps/app_base.py:471:    lock: RedisLock = sender.primary_worker_lock
HEAD:backend/onyx/background/celery/apps/app_base.py:476:                sender.primary_worker_lock = None
HEAD:backend/onyx/background/celery/apps/app_base.py:478:                logger.exception("Failed to release primary worker lock")
HEAD:backend/onyx/background/celery/apps/app_base.py:480:        logger.exception("Failed to check if primary worker lock is owned")
HEAD:backend/onyx/background/celery/apps/app_base.py:506:    Returns the (level, human-readable explanation) for celery worker logging.
HEAD:backend/onyx/background/celery/apps/app_base.py:509:    default. An operator-supplied CLI flag is treated as a per-worker
HEAD:backend/onyx/background/celery/apps/app_base.py:511:    server, model servers, and all Celery workers.
HEAD:backend/onyx/background/celery/apps/app_base.py:582:    # this worker actually runs at.
HEAD:backend/onyx/background/celery/apps/app_base.py:674:    Raises WorkerShutdown if the timeout is reached.
HEAD:backend/onyx/background/celery/apps/app_base.py:688:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:691:        # Imported here: opensearchpy costs ~18 MB and not every worker needs it.
HEAD:backend/onyx/background/celery/apps/app_base.py:699:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:702:# File for validating worker liveness
HEAD:backend/onyx/background/celery/apps/app_base.py:704:    requires = {"celery.worker.components:Timer"}
HEAD:backend/onyx/background/celery/apps/app_base.py:706:    def __init__(self, worker: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/app_base.py:707:        super().__init__(worker, **kwargs)
HEAD:backend/onyx/background/celery/apps/app_base.py:710:        self.path = make_probe_path("liveness", worker.hostname)
HEAD:backend/onyx/background/celery/apps/app_base.py:712:    def start(self, worker: Any) -> None:  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/background/celery/apps/app_base.py:713:        self.task_tref = worker.timer.call_repeatedly(
HEAD:backend/onyx/background/celery/apps/app_base.py:716:            (worker,),
HEAD:backend/onyx/background/celery/apps/app_base.py:720:    def stop(self, worker: Any) -> None:  # noqa: ARG002  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/background/celery/apps/app_base.py:725:    def update_liveness_file(self, worker: Any) -> None:  # noqa: ARG002
HEAD:backend/onyx/background/celery/apps/app_base.py:749:# above. It contains celery_beat_heartbeat (which only writes to Redis) alongside
HEAD:backend/onyx/background/celery/apps/beat.py:6:from celery.beat import PersistentScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:7:from celery.signals import beat_init
HEAD:backend/onyx/background/celery/apps/beat.py:12:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:13:from onyx.configs.constants import POSTGRES_CELERY_BEAT_APP_NAME
HEAD:backend/onyx/background/celery/apps/beat.py:22:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/beat.py:23:celery_app.config_from_object("onyx.background.celery.configs.beat")
HEAD:backend/onyx/background/celery/apps/beat.py:35:        self.last_beat_multiplier = CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:49:        self._liveness_probe_path = make_probe_path("liveness", "beat@hostname")
HEAD:backend/onyx/background/celery/apps/beat.py:52:        # do it in beat_init after the db engine is initialized
HEAD:backend/onyx/background/celery/apps/beat.py:82:        self, tenant_ids: list[str] | list[None], beat_multiplier: float
HEAD:backend/onyx/background/celery/apps/beat.py:84:        """Given a list of tenant id's, generates a new beat schedule for celery."""
HEAD:backend/onyx/background/celery/apps/beat.py:88:            # cloud tasks are system wide and thus only need to be on the beat schedule
HEAD:backend/onyx/background/celery/apps/beat.py:91:                "onyx.background.celery.tasks.beat_schedule",
HEAD:backend/onyx/background/celery/apps/beat.py:96:                beat_multiplier
HEAD:backend/onyx/background/celery/apps/beat.py:112:        # regular task beats are multiplied across all tenants
HEAD:backend/onyx/background/celery/apps/beat.py:115:        # to schedule a single cloud beat task to dispatch per tenant tasks.
HEAD:backend/onyx/background/celery/apps/beat.py:117:            "onyx.background.celery.tasks.beat_schedule", "get_tasks_to_schedule"
HEAD:backend/onyx/background/celery/apps/beat.py:155:        """Only updates the actual beat schedule on the celery app when it changes"""
HEAD:backend/onyx/background/celery/apps/beat.py:168:            beat_multiplier = OnyxRuntime.get_beat_multiplier()
HEAD:backend/onyx/background/celery/apps/beat.py:170:            beat_multiplier = CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:172:        new_schedule = self._generate_schedule(tenant_ids, beat_multiplier)
HEAD:backend/onyx/background/celery/apps/beat.py:174:        # if the schedule or beat multiplier has changed, update
HEAD:backend/onyx/background/celery/apps/beat.py:176:            if beat_multiplier != self.last_beat_multiplier:
HEAD:backend/onyx/background/celery/apps/beat.py:191:                "_try_updating_schedule - Schedule unchanged: tasks=%s beat_multiplier=%s",
HEAD:backend/onyx/background/celery/apps/beat.py:193:                beat_multiplier,
HEAD:backend/onyx/background/celery/apps/beat.py:228:            "prev_beat_multiplier=%s "
HEAD:backend/onyx/background/celery/apps/beat.py:230:            "beat_multiplier=%s",
HEAD:backend/onyx/background/celery/apps/beat.py:232:            self.last_beat_multiplier,
HEAD:backend/onyx/background/celery/apps/beat.py:234:            beat_multiplier,
HEAD:backend/onyx/background/celery/apps/beat.py:237:        self.last_beat_multiplier = beat_multiplier
HEAD:backend/onyx/background/celery/apps/beat.py:250:@beat_init.connect
HEAD:backend/onyx/background/celery/apps/beat.py:251:def on_beat_init(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/beat.py:252:    task_logger.info("beat_init signal received.")
HEAD:backend/onyx/background/celery/apps/beat.py:254:    # Celery beat shouldn't touch the db at all. But just setting a low minimum here.
HEAD:backend/onyx/background/celery/apps/beat.py:255:    SqlEngine.set_app_name(POSTGRES_CELERY_BEAT_APP_NAME)
HEAD:backend/onyx/background/celery/apps/beat.py:259:    path = make_probe_path("readiness", "beat@hostname")
HEAD:backend/onyx/background/celery/apps/beat.py:275:celery_app.conf.beat_scheduler = DynamicTenantScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:276:celery_app.conf.task_default_base = app_base.TenantAwareTask
HEAD:backend/onyx/background/celery/apps/client.py:5:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/client.py:6:celery_app.config_from_object("onyx.background.celery.configs.client")
HEAD:backend/onyx/background/celery/apps/client.py:7:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docfetching.py:7:    worker_init,
HEAD:backend/onyx/background/celery/apps/docfetching.py:8:    worker_ready,
HEAD:backend/onyx/background/celery/apps/docfetching.py:9:    worker_shutdown,
HEAD:backend/onyx/background/celery/apps/docfetching.py:10:    worker_shutting_down,
HEAD:backend/onyx/background/celery/apps/docfetching.py:14:from onyx.background.celery.tasks.docfetching.worker_shutdown import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:15:    signal_worker_shutting_down,
HEAD:backend/onyx/background/celery/apps/docfetching.py:17:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docfetching.py:36:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docfetching.py:37:celery_app.config_from_object("onyx.background.celery.configs.docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:38:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:108:@worker_init.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:109:def on_worker_init(sender: Worker, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:110:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/apps/docfetching.py:112:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docfetching.py:124:    app_base.on_secondary_worker_init(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:127:@worker_ready.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:128:def on_worker_ready(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:130:    app_base.on_worker_ready(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:133:@worker_shutting_down.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:134:def on_worker_shutting_down(**kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/docfetching.py:136:    # in-flight attempt for a fast checkpoint resume, not the heartbeat timeout.
HEAD:backend/onyx/background/celery/apps/docfetching.py:138:        "worker_shutting_down received, flagging docfetching for graceful interrupt."
HEAD:backend/onyx/background/celery/apps/docfetching.py:140:    signal_worker_shutting_down()
HEAD:backend/onyx/background/celery/apps/docfetching.py:143:@worker_shutdown.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:144:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:145:    app_base.on_worker_shutdown(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:157:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docfetching.py:159:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docprocessing.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docprocessing.py:7:    worker_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:8:    worker_process_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:9:    worker_ready,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:10:    worker_shutdown,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:18:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docprocessing.py:37:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:38:celery_app.config_from_object("onyx.background.celery.configs.docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:39:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docprocessing.py:111:@worker_init.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:112:def on_worker_init(sender: Worker, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:113:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:115:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:132:    app_base.on_secondary_worker_init(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:135:@worker_ready.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:136:def on_worker_ready(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:138:    app_base.on_worker_ready(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:141:@worker_shutdown.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:142:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:143:    app_base.on_worker_shutdown(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:146:# Note: worker_process_init only fires in prefork pool mode. Docprocessing uses
HEAD:backend/onyx/background/celery/apps/docprocessing.py:147:# worker_pool="threads" (see configs/docprocessing.py), so this handler is
HEAD:backend/onyx/background/celery/apps/docprocessing.py:152:@worker_process_init.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:153:def init_worker(**kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/docprocessing.py:166:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:168:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/heavy.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/heavy.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/heavy.py:8:from onyx.configs.constants import POSTGRES_CELERY_WORKER_HEAVY_APP_NAME
HEAD:backend/onyx/background/celery/apps/heavy.py:23:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/heavy.py:24:celery_app.config_from_object("onyx.background.celery.configs.heavy")
HEAD:backend/onyx/background/celery/apps/heavy.py:25:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/heavy.py:89:@worker_init.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:90:def on_worker_init(sender: Worker, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:91:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/apps/heavy.py:93:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_HEAVY_APP_NAME)
HEAD:backend/onyx/background/celery/apps/heavy.py:105:    app_base.on_secondary_worker_init(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:108:@worker_ready.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:109:def on_worker_ready(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:111:    app_base.on_worker_ready(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:114:@worker_shutdown.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:115:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:116:    app_base.on_worker_shutdown(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:128:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/heavy.py:130:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/light.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/light.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/light.py:14:from onyx.configs.constants import POSTGRES_CELERY_WORKER_LIGHT_APP_NAME
HEAD:backend/onyx/background/celery/apps/light.py:29:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/light.py:30:celery_app.config_from_object("onyx.background.celery.configs.light")
HEAD:backend/onyx/background/celery/apps/light.py:31:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/light.py:96:@worker_init.connect
HEAD:backend/onyx/background/celery/apps/light.py:97:def on_worker_init(sender: Worker, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/light.py:100:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/apps/light.py:107:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_LIGHT_APP_NAME)
HEAD:backend/onyx/background/celery/apps/light.py:132:    app_base.on_secondary_worker_init(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/light.py:135:@worker_ready.connect
HEAD:backend/onyx/background/celery/apps/light.py:136:def on_worker_ready(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/light.py:138:    app_base.on_worker_ready(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/light.py:141:@worker_shutdown.connect
HEAD:backend/onyx/background/celery/apps/light.py:142:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/light.py:143:    app_base.on_worker_shutdown(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/light.py:155:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/light.py:157:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/monitoring.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/monitoring.py:8:from onyx.configs.constants import POSTGRES_CELERY_WORKER_MONITORING_APP_NAME
HEAD:backend/onyx/background/celery/apps/monitoring.py:15:celery_app = Celery(__name__)
```
## Model Server Startup
Evidence lines: 22
```text
HEAD:backend/model_server/__main__.py:3:The `DISABLE_MODEL_SERVER` gate runs here, ahead of `model_server.main`'s heavy ML
HEAD:backend/model_server/__main__.py:10:from shared_configs.configs import DISABLE_MODEL_SERVER
HEAD:backend/model_server/__main__.py:16:    if DISABLE_MODEL_SERVER:
HEAD:backend/model_server/__main__.py:18:        # container has nothing to run. Exit cleanly instead of starting uvicorn.
HEAD:backend/model_server/__main__.py:19:        logger.notice("DISABLE_MODEL_SERVER is set; skipping model server startup.")
HEAD:backend/model_server/__main__.py:23:    from model_server.main import run_server
HEAD:backend/model_server/__main__.py:25:    run_server()
HEAD:backend/model_server/__main__.py:27:    # uvicorn.run() only returns once the server has stopped serving, so treat any
HEAD:backend/model_server/legacy/custom_models.py:19:# from shared_configs.configs import INDEXING_ONLY
HEAD:backend/model_server/legacy/custom_models.py:546:#     if INDEXING_ONLY:
HEAD:backend/model_server/legacy/custom_models.py:562:#     if INDEXING_ONLY:
HEAD:backend/model_server/legacy/reranker.py:10:# from shared_configs.configs import INDEXING_ONLY
HEAD:backend/model_server/legacy/reranker.py:57:#     if INDEXING_ONLY:
HEAD:backend/model_server/main.py:9:import uvicorn
HEAD:backend/model_server/main.py:21:from onyx.utils.logger import setup_logger, setup_uvicorn_logger
HEAD:backend/model_server/main.py:27:    INDEXING_ONLY,
HEAD:backend/model_server/main.py:48:setup_uvicorn_logger(shared_file_handlers=file_handlers)
HEAD:backend/model_server/main.py:119:    application = FastAPI(
HEAD:backend/model_server/main.py:136:    if INDEXING_ONLY:
HEAD:backend/model_server/main.py:151:def run_server() -> None:
HEAD:backend/model_server/main.py:163:    uvicorn.run(app, host=host, port=MODEL_SERVER_PORT)
HEAD:backend/model_server/main.py:167:    run_server()
```
## Nginx Routing
Evidence lines: 43
```text
10:upstream api_server {
11:    # fail_timeout=0 means we always retry an upstream even if it failed
22:upstream web_server {
26:# Conditionally include MCP upstream configuration
27:include /etc/nginx/conf.d/mcp_upstream.conf.inc;
36:    listen 80 default_server;
42:    # Conditionally include MCP location configuration
45:    # First-party health probe served directly by nginx (no upstreams),
47:    location = /nginx-health {
55:    location ~ ^/auth/saml(/.*)?$ {
56:        proxy_set_header X-Real-IP $remote_addr;
57:        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
58:        proxy_set_header X-Forwarded-Proto $scheme;
59:        proxy_set_header X-Forwarded-Host $host;
60:        proxy_set_header X-Forwarded-Port $server_port;
61:        proxy_set_header Host $host;
65:        proxy_pass http://api_server;
68:    location ~ ^/scim(/.*)?$ {
69:        proxy_set_header X-Real-IP $remote_addr;
70:        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
71:        proxy_set_header X-Forwarded-Proto $scheme;
72:        proxy_set_header X-Forwarded-Host $host;
73:        proxy_set_header X-Forwarded-Port $server_port;
74:        proxy_set_header Host $host;
81:        proxy_pass http://api_server;
85:    location ~ ^/(api|openapi.json)(/.*)?$ {
90:        proxy_set_header X-Real-IP $remote_addr;
91:        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
92:        proxy_set_header X-Forwarded-Proto $scheme;
93:        proxy_set_header X-Forwarded-Host $host;
94:        proxy_set_header X-Forwarded-Port $server_port;
95:        proxy_set_header Host $host;
99:        proxy_set_header Upgrade $http_upgrade;
100:        proxy_set_header Connection $connection_upgrade;
111:        proxy_pass http://api_server;
114:    location / {
116:        proxy_set_header X-Real-IP $remote_addr;
117:        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
118:        proxy_set_header X-Forwarded-Proto $scheme;
119:        proxy_set_header X-Forwarded-Host $host;
120:        proxy_set_header X-Forwarded-Port $server_port;
121:        proxy_set_header Host $host;
133:        proxy_pass http://web_server;
```
## Web Startup
Evidence lines: 8
```text
10:    "dev": "next dev",
11:    "dev:profile": "NEXT_PUBLIC_ENABLE_STATS=true next dev",
12:    "dev:clean": "bun run clean && next dev",
14:    "build": "next build",
15:    "build:fast": "SKIP_TYPE_CHECK=1 next build",
16:    "start": "next start",
76:    "next": "16.3.3",
81:    "react": "19.2.8",
```
## Internal Endpoint References
Evidence lines: 29
```text
85:      - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
86:      - OPENSEARCH_HOST=${OPENSEARCH_HOST:-opensearch}
88:      - REDIS_HOST=${REDIS_HOST:-cache}
89:      - MODEL_SERVER_HOST=${MODEL_SERVER_HOST:-inference_model_server}
90:      - CODE_INTERPRETER_BASE_URL=${CODE_INTERPRETER_BASE_URL:-http://code-interpreter:8000}
91:      - S3_ENDPOINT_URL=${S3_ENDPOINT_URL:-http://minio:9000}
113:          "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')",
160:      - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
161:      - OPENSEARCH_HOST=${OPENSEARCH_HOST:-opensearch}
163:      - REDIS_HOST=${REDIS_HOST:-cache}
164:      - MODEL_SERVER_HOST=${MODEL_SERVER_HOST:-inference_model_server}
165:      - INDEXING_MODEL_SERVER_HOST=${INDEXING_MODEL_SERVER_HOST:-indexing_model_server}
166:      - S3_ENDPOINT_URL=${S3_ENDPOINT_URL:-http://minio:9000}
173:      - API_SERVER_HOST=${API_SERVER_HOST:-api_server}
221:      - INTERNAL_URL=${INTERNAL_URL:-http://api_server:8080}
233:          "require('http').get('http://127.0.0.1:3000/', (r) => process.exit(r.statusCode < 500 ? 0 : 1)).on('error', () => process.exit(1))",
262:  #     - POSTGRES_HOST=${POSTGRES_HOST:-relational_db}
263:  #     - REDIS_HOST=${REDIS_HOST:-cache}
266:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
269:  #     - API_SERVER_HOST=${API_SERVER_HOST:-api_server}
315:          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
360:          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
411:      # This and the JVM config below come from the example in https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/
416:      # See https://opster.com/guides/opensearch/opensearch-basics/opensearch-heap-size-usage-and-jvm-garbage-collection/
422:    # These come from the example in https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/
452:      - DOMAIN=localhost
459:      - "${HOST_PORT:-3000}:80" # allow for localhost:3000 usage, since that is the norm
491:          "http://127.0.0.1/nginx-health",
569:          "import json,urllib.request; r = json.load(urllib.request.urlopen('http://localhost:8000/health', timeout=5)); raise SystemExit(0 if r['status'] == 'ok' else 1)",
```
## MCP Startup and API Relationship
Evidence lines: 62
```text
HEAD:backend/onyx/mcp_server/README.md:27:- **Framework**: FastMCP with FastAPI wrapper
HEAD:backend/onyx/mcp_server/README.md:32:The MCP server is built on [FastMCP](https://github.com/jlowin/fastmcp) and runs alongside the main Onyx API server:
HEAD:backend/onyx/mcp_server/README.md:166:- `MCP_SERVER_ENABLED`: Enable MCP server (set to "true" to enable, default: disabled)
HEAD:backend/onyx/mcp_server/README.md:167:- `MCP_SERVER_PORT`: Port for MCP server (default: 8090)
HEAD:backend/onyx/mcp_server/README.md:173:- `API_SERVER_URL_OVERRIDE_FOR_HTTP_REQUESTS`: Optional override URL. If set, takes precedence over the protocol/host variables. Used for self-hosting the MCP server with Onyx Cloud as the backend.
HEAD:backend/onyx/mcp_server/api.py:9:from fastmcp import FastMCP
HEAD:backend/onyx/mcp_server/api.py:29:# (python -m onyx.mcp_server_main, uvicorn onyx.mcp_server.api:mcp_app, etc.).
HEAD:backend/onyx/mcp_server/api.py:34:mcp_server = FastMCP(
HEAD:backend/onyx/mcp_server/api.py:55:        """Ensure Accept header includes types required by FastMCP streamable HTTP."""
HEAD:backend/onyx/mcp_server/api.py:100:    # Authentication is handled by FastMCP's OnyxTokenVerifier (see auth.py)
HEAD:backend/onyx/mcp_server/auth.py:5:from fastmcp.server.auth.auth import AccessToken, TokenVerifier
HEAD:backend/onyx/mcp_server/auth.py:10:from onyx.utils.variable_functionality import build_api_server_url_for_http_requests
HEAD:backend/onyx/mcp_server/auth.py:22:                f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/me",
HEAD:backend/onyx/mcp_server/resources/agents.py:39:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/resources/document_sets.py:38:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:35:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/tools/search.py:10:from fastmcp.server.auth.auth import AccessToken
HEAD:backend/onyx/mcp_server/tools/search.py:44:from onyx.utils.variable_functionality import build_api_server_url_for_http_requests
HEAD:backend/onyx/mcp_server/tools/search.py:352:    # Get authenticated user from FastMCP's access token
HEAD:backend/onyx/mcp_server/tools/search.py:394:        endpoint = f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/search"
HEAD:backend/onyx/mcp_server/tools/search.py:446:            f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/web-search/search-lite",
HEAD:backend/onyx/mcp_server/tools/search.py:505:            f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/web-search/open-urls",
HEAD:backend/onyx/mcp_server/utils.py:6:from fastmcp.server.auth.auth import AccessToken
HEAD:backend/onyx/mcp_server/utils.py:7:from fastmcp.server.dependencies import get_access_token
HEAD:backend/onyx/mcp_server/utils.py:11:from onyx.utils.variable_functionality import build_api_server_url_for_http_requests
HEAD:backend/onyx/mcp_server/utils.py:89:            f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/manage/indexed-sources",
HEAD:backend/onyx/mcp_server/utils.py:124:            f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/manage/document-set",
HEAD:backend/onyx/mcp_server/utils.py:153:            f"{build_api_server_url_for_http_requests(respect_env_override_if_set=True)}/persona",
HEAD:backend/onyx/mcp_server_main.py:6:    MCP_SERVER_ENABLED,
HEAD:backend/onyx/mcp_server_main.py:8:    MCP_SERVER_PORT,
HEAD:backend/onyx/mcp_server_main.py:19:    if not MCP_SERVER_ENABLED:
HEAD:backend/onyx/mcp_server_main.py:20:        logger.info("MCP server is disabled (MCP_SERVER_ENABLED=false)")
HEAD:backend/onyx/mcp_server_main.py:25:    logger.info("Starting MCP server on %s:%s", MCP_SERVER_HOST, MCP_SERVER_PORT)
HEAD:backend/onyx/mcp_server_main.py:32:        port=MCP_SERVER_PORT,
HEAD:deployment/data/nginx/run-nginx.sh:24:if [ "${MCP_SERVER_ENABLED}" = "True" ] || [ "${MCP_SERVER_ENABLED}" = "true" ]; then
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:64:      - MCP_SERVER_PORT=${MCP_TEST_SERVER_PORT:-8004}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:207:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:208:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:211:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:224:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:225:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.prod.yml:207:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.prod.yml:208:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.prod.yml:211:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.prod.yml:224:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.prod.yml:225:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.template.yml:291:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.template.yml:292:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.template.yml:295:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.template.yml:308:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.template.yml:309:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.yml:248:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.yml:249:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.yml:252:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.yml:265:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.yml:266:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/env.template:209:# MCP_SERVER_ENABLED=false
HEAD:deployment/docker_compose/env.template:211:# MCP_SERVER_PORT=8090
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:60:          command: [{{ include "onyx.customCACerts.commandPrefix" . }}"python", "onyx/mcp_server_main.py"]
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:91:            - name: MCP_SERVER_ENABLED
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:93:            - name: MCP_SERVER_PORT
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:103:            - name: API_SERVER_URL_OVERRIDE_FOR_HTTP_REQUESTS
```
## Current Relationship Model
Static evidence supports the presence of:
- ingress/reverse proxy;
- web application;
- backend API;
- background asynchronous processing;
- relational persistence;
- Redis/cache/queue infrastructure;
- search/index infrastructure;
- object/blob storage;
- indexing model service;
- inference model service;
- code-interpreter service;
- MCP integration surface.
## Security Interpretation Rule
Keep these separate:
1. startup dependency;
2. application data flow;
3. trust boundary.
One does not automatically prove the others.
## Remaining Unverified Areas
- actual runtime request paths;
- runtime ports/listeners;
- authentication flow;
- tenant-context propagation;
- route authorization decisions;
- connector credential propagation;
- RAG/document flow;
- LLM/provider flow;
- tool execution flow;
- MCP token propagation;
- code-interpreter isolation.
## Safety Record
- Application execution: NO
- Docker execution: NO
- Containers started: NO
- Dependencies installed: NO
- Database started: NO
- Network probing: NO
- External AI calls: NO
- Production credentials: NO
- Production/customer data: NO
- Onyx source modification: NO
## Result
Action 6.4 startup and service relationship trace: **PASS**.
