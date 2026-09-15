# Phase 6 Action 6.10 - Security Asset, Data, Secret and Dependency Inventory
## Purpose
Create an evidence-backed inventory of security-relevant assets and
dependencies in the exact pinned Onyx source revision.
This action identifies what later security testing must protect.
No secret values were intentionally collected.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.9 parent: `1c78c2d930942e0fb48903fa2994abb40f04f543`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Persistent and Cache Stores
Evidence lines: 600
```text
HEAD:backend/ee/onyx/access/access.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/access/hierarchy_access.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:5:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:15:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:18:from onyx.redis.redis_pool import get_redis_client, redis_lock_dump
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:19:from onyx.redis.redis_tenant_work_gating import (
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:26:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:34:    redis_client: TenantRedisClient, task_name: str, interval_seconds: int
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:44:        raw = redis_client.get(key)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:48:        # tenant during a Redis hiccup.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:63:            redis_client.set(key, str(now_ms))
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:89:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:91:    lock_beat: RedisLock = redis_client.lock(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:92:        f"{OnyxRedisLocks.CLOUD_BEAT_TASK_GENERATOR_LOCK}:{task_name}",
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:125:                redis_failed = False
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:130:                    redis_client, task_name, interval_s
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:147:                        redis_failed = True
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:149:                # Only refresh the gauge when Redis is known-reachable —
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:150:                # skip the ZCARD if we just failed open due to a Redis error.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:151:                if not redis_failed:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:215:            redis_lock_dump(lock_beat, redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:11:from redis import Redis
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:12:from redis.exceptions import LockError
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:13:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:14:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:27:from onyx.background.celery.celery_redis import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:40:    DANSWER_REDIS_FUNCTION_LOCK_PREFIX,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:45:    OnyxRedisConstants,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:46:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:47:    OnyxRedisSignals,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:80:from onyx.db.utils import DocumentRow, SortOrder, is_retryable_sqlalchemy_error
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:82:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:83:from onyx.redis.redis_connector_doc_perm_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:87:from onyx.redis.redis_pool import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:88:    get_redis_client,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:89:    get_redis_replica_client,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:90:    redis_lock_dump,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:92:from onyx.redis.redis_tenant_work_gating import maybe_mark_tenant_active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:93:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:215:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:217:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:218:    r_replica = get_redis_replica_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:220:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:262:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:283:        keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:288:                r.srem(OnyxRedisConstants.ACTIVE_FENCES, key_bytes)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:320:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:331:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:347:        if redis_connector.prune.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:350:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:351:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:368:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:447:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:467:        payload = redis_connector.permissions.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:492:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:494:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:571:            payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:584:                redis_connector, lock, r, timeout_seconds=JOB_TIMEOUT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:635:            result = redis_connector.permissions.update_db(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:666:        redis_connector.permissions.generator_complete = tasks_generated
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:687:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:688:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:703:    retry=retry_if_exception(is_retryable_sqlalchemy_error),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:792:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:793:    r_replica: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:794:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:795:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:816:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:842:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:843:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:852:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:865:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:892:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:901:        redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:919:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:920:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:925:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:943:    for member in r.sscan_iter(redis_connector.permissions.taskset_key):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:961:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:965:    # if redis_connector_index.generator_locked():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:972:    if redis_connector.permissions.active():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:984:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:993:        redis_connector: RedisConnector,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:994:        redis_lock: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:995:        redis_client: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:999:        self.redis_connector: RedisConnector = redis_connector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1000:        self.redis_lock: RedisLock = redis_lock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1001:        self.redis_client = redis_client
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1004:        self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1013:        if self.redis_connector.stop.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1026:                    self.redis_connector.cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1034:            self.redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1040:                self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1048:                self.redis_lock.timeout,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1055:            redis_lock_dump(self.redis_lock, self.redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1065:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1082:    initial = redis_connector.permissions.generator_complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1087:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1097:    remaining = redis_connector.permissions.get_remaining()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1136:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:10:from redis import Redis
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:11:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:31:from onyx.background.celery.celery_redis import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:46:    OnyxRedisConstants,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:47:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:48:    OnyxRedisSignals,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:66:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:67:from onyx.redis.redis_connector_ext_group_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:68:    RedisConnectorExternalGroupSync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:69:    RedisConnectorExternalGroupSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:71:from onyx.redis.redis_pool import get_redis_client, get_redis_replica_client
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:72:from onyx.redis.redis_tenant_work_gating import maybe_mark_tenant_active
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:73:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:170:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:172:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:173:    r_replica = get_redis_replica_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:175:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:234:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:236:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:249:                OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:274:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:285:        if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:292:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:293:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:308:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:310:        payload = RedisConnectorExternalGroupSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:316:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:318:        custom_task_id = f"{redis_connector.external_group_sync.taskset_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:332:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:371:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:381:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:386:        if not redis_connector.external_group_sync.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:389:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:394:        payload = redis_connector.external_group_sync.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:403:                redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:410:            redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:415:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:416:        OnyxRedisLocks.CONNECTOR_EXTERNAL_GROUP_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:417:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:430:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:465:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:466:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:470:        redis_connector.external_group_sync.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:682:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:683:    r_replica: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:684:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:685:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:693:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:715:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:724:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:737:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:761:        payload = redis_connector.external_group_sync.payload
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:772:        redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:786:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:787:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:792:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:799:    if redis_connector.external_group_sync.active():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:814:    redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:21:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:39:        raw = get_redis_client().get(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:56:        return bool(get_redis_client().set(key, "1", nx=True, ex=interval))
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:68:        redis_client = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:70:            redis_client.delete(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:74:        pipe = redis_client.pipeline()
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:10:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:18:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:24:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:58:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:59:    lock_check: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:60:        OnyxRedisLocks.CHECK_AVAILABLE_TENANTS_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:188:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:189:    lock_provision: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:190:        OnyxRedisLocks.CLOUD_PRE_PROVISION_TENANT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:13:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:17:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:18:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:28:if redis.call('get', KEYS[1]) == ARGV[1] then
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:29:    return redis.call('expire', KEYS[1], ARGV[2])
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:37:if redis.call('get', KEYS[1]) == ARGV[1] then
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:38:    return redis.call('del', KEYS[1])
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:45:def _release_chain_if_owned(redis_client: TenantRedisClient, chain_token: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:47:    redis_client.eval(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:49:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:92:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:95:    owns_chain = redis_client.eval(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:97:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:141:            _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:144:        _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:170:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:174:    if not redis_client.set(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:175:        OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:196:        _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:12:from onyx.redis.redis_usergroup import RedisUserGroup
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:13:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:20:    tenant_id: str, key_bytes: bytes, r: TenantRedisClient, db_session: Session
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:24:    usergroup_id_str = RedisUserGroup.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:35:    rug = RedisUserGroup(tenant_id, usergroup_id)
HEAD:backend/ee/onyx/background/celery_utils.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/configs/multi_tenant_gating_config.py:7:`gated_tenants` Redis set (control-plane marks `application_status =
HEAD:backend/ee/onyx/db/analytics.py:5:from sqlalchemy import Date, case, cast, func, or_, select
HEAD:backend/ee/onyx/db/analytics.py:6:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/connector.py:1:from sqlalchemy import distinct
HEAD:backend/ee/onyx/db/connector.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/connector_credential_pair.py:1:from sqlalchemy import delete
HEAD:backend/ee/onyx/db/connector_credential_pair.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/document.py:3:from sqlalchemy import select
HEAD:backend/ee/onyx/db/document.py:4:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/document_set.py:4:from sqlalchemy import func, select
HEAD:backend/ee/onyx/db/document_set.py:5:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/external_perm.py:5:from sqlalchemy import delete, select, update
HEAD:backend/ee/onyx/db/external_perm.py:6:from sqlalchemy.dialects.postgresql import insert as pg_insert
HEAD:backend/ee/onyx/db/external_perm.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/hierarchy.py:5:from sqlalchemy import String, and_, any_, cast, or_, select
HEAD:backend/ee/onyx/db/hierarchy.py:6:from sqlalchemy.dialects import postgresql
HEAD:backend/ee/onyx/db/hierarchy.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/hierarchy.py:8:from sqlalchemy.sql.elements import ColumnElement
HEAD:backend/ee/onyx/db/hierarchy.py:63:                cast(postgresql.array(external_group_ids), postgresql.ARRAY(String))
HEAD:backend/ee/onyx/db/license.py:10:from sqlalchemy import func, select, text
HEAD:backend/ee/onyx/db/license.py:11:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/license.py:229:# Redis Cache Operations
HEAD:backend/ee/onyx/db/mcp.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/persona.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/query_history.py:5:from sqlalchemy import BinaryExpression, ColumnElement, asc, desc, distinct
HEAD:backend/ee/onyx/db/query_history.py:6:from sqlalchemy.orm import Session, contains_eager, joinedload
HEAD:backend/ee/onyx/db/query_history.py:7:from sqlalchemy.sql import case, func, select
HEAD:backend/ee/onyx/db/query_history.py:8:from sqlalchemy.sql.expression import UnaryExpression, literal
HEAD:backend/ee/onyx/db/saml.py:5:from sqlalchemy import and_, func, select
HEAD:backend/ee/onyx/db/saml.py:6:from sqlalchemy.ext.asyncio import AsyncSession
HEAD:backend/ee/onyx/db/saml.py:7:from sqlalchemy.orm import Session, selectinload
HEAD:backend/ee/onyx/db/scim.py:28:from sqlalchemy import Select, SQLColumnExpression, func, select
HEAD:backend/ee/onyx/db/scim.py:29:from sqlalchemy import delete as sa_delete
HEAD:backend/ee/onyx/db/scim.py:30:from sqlalchemy.dialects.postgresql import insert as pg_insert
HEAD:backend/ee/onyx/db/scim.py:786:    """Apply a SCIM string filter operator using SQLAlchemy column operators.
HEAD:backend/ee/onyx/db/scim.py:789:    SQLAlchemy's operators handle LIKE-pattern escaping internally.
HEAD:backend/ee/onyx/db/search.py:5:from sqlalchemy import select
HEAD:backend/ee/onyx/db/search.py:6:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/standard_answer.py:5:from sqlalchemy import select
HEAD:backend/ee/onyx/db/standard_answer.py:6:from sqlalchemy.exc import IntegrityError
HEAD:backend/ee/onyx/db/standard_answer.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/standard_answer.py:128:    the association table go with the category, which SQLAlchemy removes itself
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:20:from sqlalchemy import delete, select
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:21:from sqlalchemy.exc import IntegrityError
HEAD:backend/ee/onyx/db/token_limit.py:3:from sqlalchemy import Row, select
HEAD:backend/ee/onyx/db/token_limit.py:4:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/usage_export.py:6:from fastapi_users_db_sqlalchemy import UUID_ID
HEAD:backend/ee/onyx/db/usage_export.py:7:from sqlalchemy import cast
HEAD:backend/ee/onyx/db/usage_export.py:8:from sqlalchemy.dialects.postgresql import UUID
HEAD:backend/ee/onyx/db/usage_export.py:9:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/db/user_group.py:7:from sqlalchemy import Select, delete, func, select
HEAD:backend/ee/onyx/db/user_group.py:8:from sqlalchemy.dialects.postgresql import insert
HEAD:backend/ee/onyx/db/user_group.py:9:from sqlalchemy.orm import Session, selectinload
HEAD:backend/ee/onyx/db/user_group.py:294:        db_session (Session): The SQLAlchemy session used to query the database.
HEAD:backend/ee/onyx/db/user_group.py:578:    A removed cc_pair keeps a stale ``is_current=False`` row until the Vespa sync
HEAD:backend/ee/onyx/db/user_group.py:795:    That will be processed by check_for_vespa_user_groups_sync_task and trigger
HEAD:backend/ee/onyx/db/user_group.py:796:    a long running background sync to Vespa.
HEAD:backend/ee/onyx/db/user_group.py:980:    # CC pair documents in Vespa contain the group name, so we need to
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:11:from sqlalchemy import or_, select, tuple_
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:12:from sqlalchemy.dialects.postgresql import insert as pg_insert
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:13:from sqlalchemy.sql.elements import ColumnElement
HEAD:backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja:37:        <config name="vespa.config.search.summary.juniperrc">
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/hooks/executor.py:54:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/onyxbot/slack/handlers/handle_standard_answers.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/search/process_search_query.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/analytics/api.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/billing/api.py:29:from redis.exceptions import RedisError
HEAD:backend/ee/onyx/server/billing/api.py:30:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/billing/api.py:71:from onyx.redis.redis_pool import get_redis_client, get_shared_redis_client
HEAD:backend/ee/onyx/server/billing/api.py:72:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/server/billing/api.py:85:# Redis key for billing circuit breaker (self-hosted only)
HEAD:backend/ee/onyx/server/billing/api.py:93:# cloud data plane. A short shared Redis cache absorbs the polling without
HEAD:backend/ee/onyx/server/billing/api.py:104:        redis_client = get_shared_redis_client()
HEAD:backend/ee/onyx/server/billing/api.py:105:        is_open = bool(redis_client.exists(BILLING_CIRCUIT_BREAKER_KEY))
HEAD:backend/ee/onyx/server/billing/api.py:122:        redis_client = get_shared_redis_client()
HEAD:backend/ee/onyx/server/billing/api.py:123:        redis_client.set(
HEAD:backend/ee/onyx/server/billing/api.py:129:        exists = redis_client.exists(BILLING_CIRCUIT_BREAKER_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:144:        redis_client = get_shared_redis_client()
HEAD:backend/ee/onyx/server/billing/api.py:145:        redis_client.delete(BILLING_CIRCUIT_BREAKER_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:245:def _billing_cache_client() -> TenantRedisClient | None:
HEAD:backend/ee/onyx/server/billing/api.py:246:    """Best-effort Redis client for the billing-info cache.
HEAD:backend/ee/onyx/server/billing/api.py:256:            return get_redis_client(tenant_id=get_current_tenant_id())
HEAD:backend/ee/onyx/server/billing/api.py:257:        return get_shared_redis_client()
HEAD:backend/ee/onyx/server/billing/api.py:271:    redis_client = _billing_cache_client()
HEAD:backend/ee/onyx/server/billing/api.py:272:    if redis_client is not None:
HEAD:backend/ee/onyx/server/billing/api.py:274:            redis_client.delete(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:275:        except RedisError as exc:
HEAD:backend/ee/onyx/server/billing/api.py:293:    A 5-minute Redis cache absorbs admin-page polling so each instance does
HEAD:backend/ee/onyx/server/billing/api.py:311:    redis_client = _billing_cache_client()
HEAD:backend/ee/onyx/server/billing/api.py:312:    if redis_client is not None:
HEAD:backend/ee/onyx/server/billing/api.py:314:            cached = redis_client.get(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:315:        except RedisError as exc:
HEAD:backend/ee/onyx/server/billing/api.py:344:    if redis_client is not None:
HEAD:backend/ee/onyx/server/billing/api.py:346:            redis_client.set(
HEAD:backend/ee/onyx/server/billing/api.py:351:        except RedisError as exc:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:1:"""Redis-backed cache for control-plane billing lookups.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:14:  1. Redis hit  → return the cached payload.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:15:  2. Redis miss → control-plane fetch, write through, return.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:16:  3. Redis error (read or write) → log and fall through to an uncached
HEAD:backend/ee/onyx/server/billing/billing_cache.py:17:     control-plane fetch. Preserves availability when Redis blips.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:24:from redis.exceptions import RedisError
HEAD:backend/ee/onyx/server/billing/billing_cache.py:29:from onyx.redis.redis_pool import get_shared_redis_client
HEAD:backend/ee/onyx/server/billing/billing_cache.py:39:# Discriminator used to round-trip the union return type through Redis without
HEAD:backend/ee/onyx/server/billing/billing_cache.py:83:    """Return billing info for a tenant, preferring the per-tenant Redis
HEAD:backend/ee/onyx/server/billing/billing_cache.py:89:    loudly rather than silently open a Redis/control-plane connection that a
HEAD:backend/ee/onyx/server/billing/billing_cache.py:97:    redis = get_shared_redis_client()
HEAD:backend/ee/onyx/server/billing/billing_cache.py:101:        raw = redis.get(key)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:102:    except RedisError as e:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:128:        redis.setex(key, BILLING_CACHE_TTL_SECONDS, _serialize(info))
HEAD:backend/ee/onyx/server/billing/billing_cache.py:129:    except RedisError as e:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:161:        get_shared_redis_client().delete(_cache_key(tenant_id))
HEAD:backend/ee/onyx/server/billing/billing_cache.py:163:    except RedisError as e:
HEAD:backend/ee/onyx/server/documents/cc_pair.py:4:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/documents/cc_pair.py:22:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/server/documents/cc_pair.py:23:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/documents/cc_pair.py:78:    r = get_redis_client()
HEAD:backend/ee/onyx/server/documents/cc_pair.py:80:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:81:    if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/server/documents/cc_pair.py:157:    r = get_redis_client()
HEAD:backend/ee/onyx/server/documents/cc_pair.py:159:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:160:    if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/features/hooks/api.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/gateway/api.py:14:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/license/api.py:10:Cloud licensing is managed via the control plane and gated_tenants Redis key.
HEAD:backend/ee/onyx/server/license/api.py:15:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/license/models.py:82:    """Cached license metadata stored in Redis."""
HEAD:backend/ee/onyx/server/log_export/api.py:99:    "light": OnyxCeleryQueues.VESPA_METADATA_SYNC,
HEAD:backend/ee/onyx/server/log_export/api.py:170:        # overlaps the api_server's. When redis is absent by design (the
HEAD:backend/ee/onyx/server/log_export/api.py:176:        if CACHE_BACKEND != CacheBackendType.REDIS:
HEAD:backend/ee/onyx/server/manage/standard_answer.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:63:from sqlalchemy.exc import SQLAlchemyError
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:143:                except SQLAlchemyError as db_error:
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:151:                # Off the event loop: it does Redis and broker I/O with no
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:18:from onyx.redis.redis_pool import (
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:20:    retrieve_auth_token_data_from_redis,
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:48:            # send probes through the Redis session lookup.
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:61:            # GATED_ACCESS` in the cloud control plane → `gated_tenants` Redis
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:76:                    # `is_tenant_gated` uses the sync Redis client; offload so
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:80:                    # Fail open on Redis errors — don't lock paying tenants out
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:120:    the Redis session token, or the anonymous-user cookie.
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:132:        # Look up the session token data in Redis. Web clients send it as the
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:135:        token_data = await retrieve_auth_token_data_from_redis(request)
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:176:            "Token data not found or expired in Redis, defaulting to POSTGRES_DEFAULT_SCHEMA"
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:80:        # `get_tier` is sync: Redis read on every request, plus a blocking
HEAD:backend/ee/onyx/server/oauth/api.py:16:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/oauth/api.py:85:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:10:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:30:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:42:        """Stored in redis to be looked up on callback"""
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:127:        """Temporary state to store in redis. to be looked up on auth response.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:162:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:10:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/oauth/google_drive.py:35:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/oauth/google_drive.py:45:        """Stored in redis to be looked up on callback"""
HEAD:backend/ee/onyx/server/oauth/google_drive.py:96:        """Temporary state to store in redis. to be looked up on auth response.
HEAD:backend/ee/onyx/server/oauth/google_drive.py:124:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/oauth/slack.py:9:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/oauth/slack.py:24:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/oauth/slack.py:34:        """Stored in redis to be looked up on callback"""
HEAD:backend/ee/onyx/server/oauth/slack.py:85:        """Temporary state to store in redis. to be looked up on auth response.
HEAD:backend/ee/onyx/server/oauth/slack.py:113:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:16:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:36:from onyx.configs.app_configs import ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:130:    If hybrid_alpha is unset and ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:138:    if request.hybrid_alpha is None and ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH:
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:4:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/query_history/api.py:9:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:8:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:9:from fastapi_users_db_sqlalchemy import UUID_ID
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:10:from sqlalchemy import cast
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:11:from sqlalchemy.dialects.postgresql import UUID
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:12:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:32:from onyx.file_store.file_store import FileStore, get_default_file_store
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:54:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:111:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:142:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:197:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:248:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:13:from onyx.file_store.file_store import FileStore
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:31:def _read_logo(file_store: FileStore, file_id: str) -> bytes | None:
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:51:def load_report_branding(file_store: FileStore) -> ReportBranding:
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:8:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/scim/api.py:21:from sqlalchemy import func
HEAD:backend/ee/onyx/server/scim/api.py:22:from sqlalchemy.exc import IntegrityError
HEAD:backend/ee/onyx/server/scim/api.py:23:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/scim/auth.py:25:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/seeding.py:7:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/settings/api.py:3:from redis.exceptions import RedisError
HEAD:backend/ee/onyx/server/settings/api.py:4:from sqlalchemy.exc import SQLAlchemyError
HEAD:backend/ee/onyx/server/settings/api.py:53:            except SQLAlchemyError as db_error:
HEAD:backend/ee/onyx/server/settings/api.py:59:    except RedisError as e:
HEAD:backend/ee/onyx/server/settings/api.py:61:        # Fail closed - if Redis is down, other things will break anyway
HEAD:backend/ee/onyx/server/settings/api.py:94:        # Cloud tier lives in a separate Redis hash, fetched via get_tier().
HEAD:backend/ee/onyx/server/settings/api.py:109:            except SQLAlchemyError as db_error:
HEAD:backend/ee/onyx/server/tenants/admin_api.py:7:from onyx.auth.users import User, auth_backend, get_redis_strategy
HEAD:backend/ee/onyx/server/tenants/admin_api.py:88:        token = await get_redis_strategy().write_token(user_to_impersonate)
HEAD:backend/ee/onyx/server/tenants/anonymous_user_path.py:1:from sqlalchemy import select
HEAD:backend/ee/onyx/server/tenants/anonymous_user_path.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:2:from sqlalchemy.exc import IntegrityError
HEAD:backend/ee/onyx/server/tenants/billing.py:6:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/billing_api.py:23:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/billing_api.py:139:    # Redis SET, so a retry only re-attempts the drop.
HEAD:backend/ee/onyx/server/tenants/product_gating.py:3:from onyx.redis.redis_pool import get_redis_client, get_redis_replica_client
HEAD:backend/ee/onyx/server/tenants/product_gating.py:17:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:21:        redis_client.sadd(GATED_TENANTS_KEY, tenant_id)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:23:        redis_client.srem(GATED_TENANTS_KEY, tenant_id)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:36:        # Store gated tenant information in Redis
HEAD:backend/ee/onyx/server/tenants/product_gating.py:46:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:48:    pipeline = redis_client.pipeline()
HEAD:backend/ee/onyx/server/tenants/product_gating.py:62:    redis_client = get_redis_replica_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:63:    gated_tenants_bytes = redis_client.smembers(GATED_TENANTS_KEY)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:69:    redis_client = get_redis_replica_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/server/tenants/product_gating.py:70:    return bool(redis_client.sismember(GATED_TENANTS_KEY, tenant_id))
HEAD:backend/ee/onyx/server/tenants/provisioning.py:8:from sqlalchemy import select
HEAD:backend/ee/onyx/server/tenants/provisioning.py:9:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/proxy.py:27:from redis.exceptions import RedisError
HEAD:backend/ee/onyx/server/tenants/proxy.py:35:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/server/tenants/proxy.py:36:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/server/tenants/proxy.py:54:        get_redis_client(tenant_id=tenant_id).delete(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/tenants/proxy.py:55:    except RedisError as exc:
HEAD:backend/ee/onyx/server/tenants/proxy.py:383:    Caches the response in Redis per tenant for BILLING_INFO_CACHE_TTL_SEC.
HEAD:backend/ee/onyx/server/tenants/proxy.py:394:    redis_client: TenantRedisClient | None = None
HEAD:backend/ee/onyx/server/tenants/proxy.py:397:        redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/tenants/proxy.py:398:        cached = redis_client.get(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/tenants/proxy.py:399:    except RedisError as exc:
HEAD:backend/ee/onyx/server/tenants/proxy.py:424:    if redis_client is not None:
HEAD:backend/ee/onyx/server/tenants/proxy.py:426:            redis_client.setex(
HEAD:backend/ee/onyx/server/tenants/proxy.py:431:        except RedisError as exc:
HEAD:backend/ee/onyx/server/tenants/schema_management.py:7:from sqlalchemy import text
HEAD:backend/ee/onyx/server/tenants/schema_management.py:8:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/schema_management.py:9:from sqlalchemy.schema import CreateSchema
HEAD:backend/ee/onyx/server/tenants/schema_management.py:49:        # than `sqlalchemy.url`, which env.py ignores by design.
HEAD:backend/ee/onyx/server/tenants/schema_management.py:116:    from sqlalchemy import text
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:2:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/tenants/tier_management.py:12:from onyx.redis.redis_pool import get_redis_client, get_redis_replica_client
HEAD:backend/ee/onyx/server/tenants/tier_management.py:54:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/tenants/tier_management.py:61:    redis_client.set(TENANT_TIER_KEY, payload, ex=TENANT_TIER_CACHE_TTL_SECONDS)
HEAD:backend/ee/onyx/server/tenants/tier_management.py:65:    redis_client = get_redis_replica_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/tenants/tier_management.py:66:    raw = redis_client.get(TENANT_TIER_KEY)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:4:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/usage_limits.py:15:    in Redis (see ``ee.onyx.server.billing.billing_cache``) and the trial
HEAD:backend/ee/onyx/server/user_group/api.py:2:from sqlalchemy.exc import IntegrityError
HEAD:backend/ee/onyx/server/user_group/api.py:3:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/server/user_group/api.py:606:            OnyxCeleryTask.CHECK_FOR_VESPA_SYNC_TASK,
HEAD:backend/ee/onyx/utils/license.py:17:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/utils/license.py:31:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/utils/license.py:38:# stale license. Redis key TTL is the debounce. Redis rather than the cache
HEAD:backend/ee/onyx/utils/license.py:72:    Fails open: a Redis outage should not stop an admin from recovering a
HEAD:backend/ee/onyx/utils/license.py:76:        return not get_redis_client().set(
HEAD:backend/ee/onyx/utils/license.py:95:        get_redis_client().delete(_LICENSE_CLAIM_COOLDOWN_KEY)
HEAD:backend/ee/onyx/utils/license.py:355:    # Commit inside the lock, publish outside it: the Redis cache backend has
HEAD:backend/ee/onyx/utils/license.py:493:        get_redis_client().delete(_LICENSE_RECLAIM_DEBOUNCE_KEY)
HEAD:backend/ee/onyx/utils/license.py:522:    # Both the debounce and the broker behind send_task are this Redis. Where
HEAD:backend/ee/onyx/utils/license.py:524:    if CACHE_BACKEND != CacheBackendType.REDIS:
HEAD:backend/ee/onyx/utils/license.py:534:        redis_client = get_redis_client()
HEAD:backend/ee/onyx/utils/license.py:537:        if not redis_client.set(
HEAD:backend/ee/onyx/utils/license.py:555:            redis_client.delete(_LICENSE_RECLAIM_DEBOUNCE_KEY)
HEAD:backend/ee/onyx/utils/license_expiry.py:40:# Where doubling reaches the cap. Also bounds the shift on a Redis-read counter.
HEAD:backend/ee/onyx/utils/license_notifications.py:13:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/utils/tier.py:3:Cloud: Redis HGET → CP lazy-refresh on miss → BUSINESS fallback.
HEAD:backend/ee/onyx/utils/tier.py:18:from redis.exceptions import RedisError
HEAD:backend/ee/onyx/utils/tier.py:19:from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
HEAD:backend/ee/onyx/utils/tier.py:56:    so they don't both have to read Redis when one already has the metadata
HEAD:backend/ee/onyx/utils/tier.py:81:    except RedisError as e:
HEAD:backend/ee/onyx/utils/tier.py:95:        except SQLAlchemyError as e:
HEAD:backend/ee/onyx/utils/tier.py:141:    except RedisError as e:
HEAD:backend/ee/onyx/utils/tier.py:144:            "Tier Redis read failed for tenant %s; falling back to BUSINESS: %s",
HEAD:backend/ee/onyx/utils/tier.py:158:        except RedisError as e:
HEAD:backend/ee/onyx/utils/tier.py:160:                "Tier Redis write failed for tenant %s after CP refresh: %s",
HEAD:backend/onyx/access/access.py:4:from sqlalchemy import cast as sa_cast
HEAD:backend/onyx/access/access.py:5:from sqlalchemy import or_, select
HEAD:backend/onyx/access/access.py:6:from sqlalchemy.dialects import postgresql
HEAD:backend/onyx/access/access.py:7:from sqlalchemy.orm import Session
HEAD:backend/onyx/access/access.py:378:                sa_cast([file_id], postgresql.JSONB)
HEAD:backend/onyx/access/hierarchy_access.py:1:from sqlalchemy.orm import Session
HEAD:backend/onyx/access/models.py:73:    together. It's used for syncing document permissions to Vespa.
HEAD:backend/onyx/auth/captcha.py:36:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/captcha.py:117:    the TTL returns False → raise. Redis errors fail open so a blip does
HEAD:backend/onyx/auth/captcha.py:120:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/captcha.py:121:        claimed = await redis.set(
HEAD:backend/onyx/auth/captcha.py:143:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/captcha.py:144:        await redis.delete(_replay_cache_key(token))
HEAD:backend/onyx/auth/login_claims_capture.py:9:attribute set into Redis at login time and derives a "directory profile"
HEAD:backend/onyx/auth/login_claims_capture.py:42:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/login_claims_capture.py:50:# Redis HASH per (tenant, email): field = provider name, value = snapshot JSON.
HEAD:backend/onyx/auth/login_claims_capture.py:59:# flow, so a slow userinfo/Graph endpoint or an unreachable Redis must never
HEAD:backend/onyx/auth/login_claims_capture.py:155:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/login_claims_capture.py:157:    old_raw = await cast(Awaitable[Any], redis.hget(key, provider))
HEAD:backend/onyx/auth/login_claims_capture.py:185:    pipe = redis.pipeline()
HEAD:backend/onyx/auth/login_claims_capture.py:284:    """Snapshot the claims the IdP sent for this login into Redis.
HEAD:backend/onyx/auth/login_claims_capture.py:492:    and the tenant-prefixing TenantRedisClient would look up a different key
HEAD:backend/onyx/auth/login_claims_capture.py:495:    from onyx.redis.redis_pool import get_raw_redis_client
HEAD:backend/onyx/auth/login_claims_capture.py:497:    redis = get_raw_redis_client()
HEAD:backend/onyx/auth/login_claims_capture.py:498:    raw_map = redis.hgetall(_idp_claims_key(get_current_tenant_id(), email))
HEAD:backend/onyx/auth/login_claims_capture.py:561:    """Both derived views of the directory profile from one Redis read.
HEAD:backend/onyx/auth/login_claims_capture.py:564:    nothing is captured, or Redis is unavailable. Callers must treat the
HEAD:backend/onyx/auth/login_claims_capture.py:600:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/login_claims_capture.py:601:    # redis-py types hash commands as a sync-or-async union. This is the async client.
HEAD:backend/onyx/auth/login_claims_capture.py:604:        redis.hgetall(_idp_claims_key(get_current_tenant_id(), email)),
HEAD:backend/onyx/auth/mobile_sso/code_store.py:1:"""One-time, PKCE-bound SSO code store (Redis).
HEAD:backend/onyx/auth/mobile_sso/code_store.py:5:Redis under a short-lived, single-use code bound to an app-supplied PKCE
HEAD:backend/onyx/auth/mobile_sso/code_store.py:16:Redis is core infra (always available, even when ``AUTH_BACKEND=jwt``), so this
HEAD:backend/onyx/auth/mobile_sso/code_store.py:27:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/mobile_sso/code_store.py:41:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/mobile_sso/code_store.py:42:    await redis.set(
HEAD:backend/onyx/auth/mobile_sso/code_store.py:59:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/mobile_sso/code_store.py:60:    # Atomic get-and-delete enforces single use (Redis 6.2+).
HEAD:backend/onyx/auth/mobile_sso/code_store.py:61:    raw = await redis.getdel(f"{MOBILE_SSO_CODE_PREFIX}{code}")
HEAD:backend/onyx/auth/mobile_sso/tokens.py:5:strategy's ``write_token``) — server-revocable under the redis/postgres backends,
HEAD:backend/onyx/auth/oauth_refresher.py:12:from sqlalchemy.ext.asyncio import AsyncSession
HEAD:backend/onyx/auth/oauth_token_manager.py:8:from sqlalchemy.orm import Session
HEAD:backend/onyx/auth/schemas.py:69:    REDIS = "redis"
HEAD:backend/onyx/auth/scoped_permissions.py:12:from sqlalchemy.orm import Session
HEAD:backend/onyx/auth/session_tokens.py:1:"""Redis session-token value format and rejection classification.
HEAD:backend/onyx/auth/session_tokens.py:6:(no entry: cookie outlived the grace window, or Redis dropped the key),
HEAD:backend/onyx/auth/session_tokens.py:12:bearer transport and legitimately miss in Redis), so the classification is
HEAD:backend/onyx/auth/session_tokens.py:219:            "Presented session token has no Redis entry: the cookie outlived "
HEAD:backend/onyx/auth/session_tokens.py:220:            "the grace window, or Redis dropped the key (restart/eviction/flush)."
HEAD:backend/onyx/auth/signup_rate_limit.py:10:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/signup_rate_limit.py:19:_REDIS_KEY_PREFIX = "signup_rate:"
HEAD:backend/onyx/auth/signup_rate_limit.py:36:    return f"{_REDIS_KEY_PREFIX}{ip}:{bucket}"
HEAD:backend/onyx/auth/signup_rate_limit.py:48:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/signup_rate_limit.py:49:        pipe = redis.pipeline()
HEAD:backend/onyx/auth/signup_rate_limit.py:55:        logger.error("Signup rate-limit Redis error: %s", e)
HEAD:backend/onyx/auth/users.py:43:    RedisStrategy,  # ty: ignore[possibly-missing-import]
HEAD:backend/onyx/auth/users.py:55:from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
HEAD:backend/onyx/auth/users.py:60:from sqlalchemy.exc import IntegrityError
HEAD:backend/onyx/auth/users.py:61:from sqlalchemy.ext.asyncio import AsyncSession
HEAD:backend/onyx/auth/users.py:62:from sqlalchemy.orm import Session
HEAD:backend/onyx/auth/users.py:103:    REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:119:    OnyxRedisLocks,
HEAD:backend/onyx/auth/users.py:155:from onyx.redis.redis_pool import get_async_redis_connection, retrieve_ws_token_data
HEAD:backend/onyx/auth/users.py:292:    value = cache.get(OnyxRedisLocks.ANONYMOUS_USER_ENABLED)
HEAD:backend/onyx/auth/users.py:590:    user_db: SQLAlchemyUserDatabase[User, uuid.UUID]
HEAD:backend/onyx/auth/users.py:601:                self.user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:615:                tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:664:                tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:793:                    tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:1568:            tenant_user_db: SQLAlchemyUserDatabase = SQLAlchemyUserDatabase(
HEAD:backend/onyx/auth/users.py:1637:    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
HEAD:backend/onyx/auth/users.py:1679:class TenantAwareRedisStrategy(RedisStrategy[User, uuid.UUID]):
HEAD:backend/onyx/auth/users.py:1681:    A custom strategy that fetches the actual async Redis connection inside each method.
HEAD:backend/onyx/auth/users.py:1682:    We do NOT pass a synchronous or "coroutine" redis object to the constructor.
HEAD:backend/onyx/auth/users.py:1691:        key_prefix: str = REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:1697:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1705:        await redis.set(
HEAD:backend/onyx/auth/users.py:1723:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1724:        raw_value = await redis.get(f"{self.key_prefix}{token}")
HEAD:backend/onyx/auth/users.py:1747:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1749:        previous_raw_value = await redis.get(token_key)
HEAD:backend/onyx/auth/users.py:1750:        await redis.set(
HEAD:backend/onyx/auth/users.py:1759:        """Refreshes a token by extending its expiration time in Redis."""
HEAD:backend/onyx/auth/users.py:1764:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1767:        raw_value = await redis.get(token_key)
HEAD:backend/onyx/auth/users.py:1775:        await redis.set(
HEAD:backend/onyx/auth/users.py:1824:    Tokens are self-contained and verified via signature — no Redis or DB
```
## High-Value Application Data
Evidence lines: 650
```text
HEAD:backend/ee/onyx/db/analytics.py:73:        .join(ChatSession, ChatSession.id == ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/analytics.py:110:            ChatMessage.chat_session_id.label("chat_session_id"),
HEAD:backend/ee/onyx/db/analytics.py:113:        .join(ChatSession, ChatSession.id == ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/analytics.py:122:        .group_by(ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/analytics.py:158:            ChatSession.id == subquery_first_ai_response.c.chat_session_id,
HEAD:backend/ee/onyx/db/analytics.py:197:            ChatMessage.chat_session_id == ChatSession.id,
HEAD:backend/ee/onyx/db/analytics.py:226:            ChatMessage.chat_session_id == ChatSession.id,
HEAD:backend/ee/onyx/db/analytics.py:257:            ChatMessage.chat_session_id == ChatSession.id,
HEAD:backend/ee/onyx/db/analytics.py:288:            ChatMessage.chat_session_id == ChatSession.id,
HEAD:backend/ee/onyx/db/analytics.py:318:            ChatMessage.chat_session_id == ChatSession.id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:5:from onyx.db.connector_credential_pair import get_connector_credential_pair
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:20:    cc_pair = get_connector_credential_pair(
HEAD:backend/ee/onyx/db/document_set.py:105:                    DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/ee/onyx/db/document_set.py:207:                == DocumentSet__ConnectorCredentialPair.connector_credential_pair_id,
HEAD:backend/ee/onyx/db/hierarchy.py:11:from onyx.db.connector_credential_pair import build_user_cc_pair_access_filter
HEAD:backend/ee/onyx/db/persona.py:13:    mark_persona_user_files_for_sync,
HEAD:backend/ee/onyx/db/persona.py:202:        mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/ee/onyx/db/query_history.py:39:            select(ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/query_history.py:41:            .group_by(ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/query_history.py:68:def get_total_filtered_chat_sessions_count(
HEAD:backend/ee/onyx/db/query_history.py:83:def get_page_of_chat_sessions(
HEAD:backend/ee/onyx/db/query_history.py:105:        .outerjoin(ChatMessage, ChatSession.id == ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/query_history.py:123:def fetch_persisting_chat_session_by_id(
HEAD:backend/ee/onyx/db/query_history.py:124:    chat_session_id: UUID,
HEAD:backend/ee/onyx/db/query_history.py:133:    chat_session = db_session.scalar(
HEAD:backend/ee/onyx/db/query_history.py:135:            ChatSession.id == chat_session_id,
HEAD:backend/ee/onyx/db/query_history.py:139:    if chat_session is None:
HEAD:backend/ee/onyx/db/query_history.py:140:        raise ValueError(f"Chat session with id '{chat_session_id}' does not exist.")
HEAD:backend/ee/onyx/db/query_history.py:141:    return chat_session
HEAD:backend/ee/onyx/db/query_history.py:144:def fetch_chat_sessions_eagerly_by_time(
HEAD:backend/ee/onyx/db/query_history.py:176:        .outerjoin(ChatMessage, ChatSession.id == ChatMessage.chat_session_id)
HEAD:backend/ee/onyx/db/query_history.py:187:    chat_sessions = query.all()
HEAD:backend/ee/onyx/db/query_history.py:189:    return chat_sessions
HEAD:backend/ee/onyx/db/usage_export.py:11:from ee.onyx.db.query_history import fetch_chat_sessions_eagerly_by_time
HEAD:backend/ee/onyx/db/usage_export.py:36:    chat_sessions = fetch_chat_sessions_eagerly_by_time(
HEAD:backend/ee/onyx/db/usage_export.py:45:    for chat_session in chat_sessions:
HEAD:backend/ee/onyx/db/usage_export.py:46:        flow_type = FlowType.SLACK if chat_session.onyxbot_flow else FlowType.CHAT
HEAD:backend/ee/onyx/db/usage_export.py:53:        for message in chat_session.messages:
HEAD:backend/ee/onyx/db/usage_export.py:62:        for message in chat_session.messages:
HEAD:backend/ee/onyx/db/usage_export.py:68:            user_email = chat_session.user.email if chat_session.user else None
HEAD:backend/ee/onyx/db/usage_export.py:72:            if chat_session.persona:
HEAD:backend/ee/onyx/db/usage_export.py:73:                assistant_name = chat_session.persona.name
HEAD:backend/ee/onyx/db/usage_export.py:94:                        chat_session_id=chat_session.id,
HEAD:backend/ee/onyx/db/usage_export.py:96:                            str(chat_session.user_id) if chat_session.user_id else None
HEAD:backend/ee/onyx/db/usage_export.py:106:    if len(chat_sessions) == 0:
HEAD:backend/ee/onyx/db/usage_export.py:109:    return chat_sessions[-1].time_created, message_skeletons
HEAD:backend/ee/onyx/db/user_group.py:24:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/db/user_group.py:26:    get_connector_credential_pair_from_id,
HEAD:backend/ee/onyx/db/user_group.py:229:            selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:246:                selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:256:            selectinload(Persona.user_files),
HEAD:backend/ee/onyx/db/user_group.py:341:def construct_document_id_select_by_usergroup(
HEAD:backend/ee/onyx/db/user_group.py:380:    last_document_id: str | None = None,
HEAD:backend/ee/onyx/db/user_group.py:410:    if last_document_id is not None:
HEAD:backend/ee/onyx/db/user_group.py:411:        stmt = stmt.where(Document.id > last_document_id)
HEAD:backend/ee/onyx/db/user_group.py:420:    document_ids: list[str],
HEAD:backend/ee/onyx/db/user_group.py:451:        .where(Document.id.in_(document_ids))
HEAD:backend/ee/onyx/db/user_group.py:1098:    connector_credential_pair_id matches the given cc_pair_id.
HEAD:backend/ee/onyx/db/user_group.py:1101:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/chat.py:41:def get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:42:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:49:    stmt = select(ChatSession).where(ChatSession.id == chat_session_id)
HEAD:backend/onyx/db/chat.py:55:                selectinload(Persona.user_files),
HEAD:backend/onyx/db/chat.py:74:    chat_session = result.scalar_one_or_none()
HEAD:backend/onyx/db/chat.py:76:    if not chat_session:
HEAD:backend/onyx/db/chat.py:79:    if not include_deleted and chat_session.deleted:
HEAD:backend/onyx/db/chat.py:82:    return chat_session
HEAD:backend/onyx/db/chat.py:85:def get_chat_sessions_by_slack_thread_id(
HEAD:backend/onyx/db/chat.py:122:def get_chat_sessions_by_user(
HEAD:backend/onyx/db/chat.py:167:    chat_sessions = list(result.scalars().all())
HEAD:backend/onyx/db/chat.py:169:    if not include_failed_chats and chat_sessions:
HEAD:backend/onyx/db/chat.py:174:        session_ids = [cs.id for cs in chat_sessions if cs.time_created < leeway]
HEAD:backend/onyx/db/chat.py:178:                select(ChatMessage.chat_session_id)
HEAD:backend/onyx/db/chat.py:179:                .where(ChatMessage.chat_session_id.in_(session_ids))
HEAD:backend/onyx/db/chat.py:187:            chat_sessions = [
HEAD:backend/onyx/db/chat.py:189:                for cs in chat_sessions
HEAD:backend/onyx/db/chat.py:194:            chat_sessions = chat_sessions[:limit]
HEAD:backend/onyx/db/chat.py:196:    return chat_sessions
HEAD:backend/onyx/db/chat.py:211:def delete_messages_and_files_from_chat_session(
HEAD:backend/onyx/db/chat.py:212:    chat_session_id: UUID, db_session: Session
HEAD:backend/onyx/db/chat.py:218:                ChatMessage.chat_session_id == chat_session_id,
HEAD:backend/onyx/db/chat.py:228:            if file_info.get("user_file_id"):
HEAD:backend/onyx/db/chat.py:236:        delete(ChatMessage).where(ChatMessage.chat_session_id == chat_session_id)
HEAD:backend/onyx/db/chat.py:243:def create_chat_session(
HEAD:backend/onyx/db/chat.py:256:    chat_session = ChatSession(
HEAD:backend/onyx/db/chat.py:271:    db_session.add(chat_session)
HEAD:backend/onyx/db/chat.py:274:    return chat_session
HEAD:backend/onyx/db/chat.py:277:def duplicate_chat_session_for_user_from_slack(
HEAD:backend/onyx/db/chat.py:280:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:289:    chat_session = get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:290:        chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:294:    if chat_session.incognito_record_mode is not None:
HEAD:backend/onyx/db/chat.py:296:    if not chat_session:
HEAD:backend/onyx/db/chat.py:303:        persona_id=chat_session.persona_id,
HEAD:backend/onyx/db/chat.py:306:    return create_chat_session(
HEAD:backend/onyx/db/chat.py:312:        llm_override=chat_session.llm_override,
HEAD:backend/onyx/db/chat.py:313:        prompt_override=chat_session.prompt_override,
HEAD:backend/onyx/db/chat.py:321:def update_chat_session(
HEAD:backend/onyx/db/chat.py:324:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:328:    chat_session = get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:329:        chat_session_id=chat_session_id, user_id=user_id, db_session=db_session
HEAD:backend/onyx/db/chat.py:332:    if chat_session.deleted:
HEAD:backend/onyx/db/chat.py:339:        chat_session.incognito_record_mode
HEAD:backend/onyx/db/chat.py:341:        chat_session.description = description
HEAD:backend/onyx/db/chat.py:343:        chat_session.shared_status = sharing_status
HEAD:backend/onyx/db/chat.py:347:    return chat_session
HEAD:backend/onyx/db/chat.py:350:def delete_all_chat_sessions_for_user(
HEAD:backend/onyx/db/chat.py:355:    chat_sessions = (
HEAD:backend/onyx/db/chat.py:362:        for chat_session in chat_sessions:
HEAD:backend/onyx/db/chat.py:363:            delete_messages_and_files_from_chat_session(chat_session.id, db_session)
HEAD:backend/onyx/db/chat.py:379:def delete_chat_session(
HEAD:backend/onyx/db/chat.py:381:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:386:    chat_session = get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:387:        chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:393:    if chat_session.deleted and not include_deleted:
HEAD:backend/onyx/db/chat.py:397:        delete_messages_and_files_from_chat_session(chat_session_id, db_session)
HEAD:backend/onyx/db/chat.py:398:        db_session.execute(delete(ChatSession).where(ChatSession.id == chat_session_id))
HEAD:backend/onyx/db/chat.py:400:        chat_session = get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:401:            chat_session_id=chat_session_id, user_id=user_id, db_session=db_session
HEAD:backend/onyx/db/chat.py:403:        chat_session.deleted = True
HEAD:backend/onyx/db/chat.py:408:def get_chat_sessions_older_than(
HEAD:backend/onyx/db/chat.py:426:        A list of tuples, where each tuple contains the user_id (can be None) and the chat_session_id of an old chat session.
HEAD:backend/onyx/db/chat.py:435:        .outerjoin(ChatMessage, ChatMessage.chat_session_id == ChatSession.id)
HEAD:backend/onyx/db/chat.py:466:    chat_user = chat_message.chat_session.user
HEAD:backend/onyx/db/chat.py:479:def get_chat_session_by_message_id(
HEAD:backend/onyx/db/chat.py:498:    return chat_message.chat_session
HEAD:backend/onyx/db/chat.py:502:    chat_session_ids: list[UUID],
HEAD:backend/onyx/db/chat.py:508:        for chat_session_id in chat_session_ids:
HEAD:backend/onyx/db/chat.py:509:            get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:510:                chat_session_id=chat_session_id, user_id=user_id, db_session=db_session
HEAD:backend/onyx/db/chat.py:514:        .where(ChatMessage.chat_session_id.in_(chat_session_ids))
HEAD:backend/onyx/db/chat.py:522:    slack_chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:523:    new_chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:525:    source_session = db_session.get(ChatSession, slack_chat_session_id)
HEAD:backend/onyx/db/chat.py:529:        chat_session_id=new_chat_session_id,
HEAD:backend/onyx/db/chat.py:534:        chat_session_ids=[slack_chat_session_id],
HEAD:backend/onyx/db/chat.py:544:            chat_session_id=new_chat_session_id,
HEAD:backend/onyx/db/chat.py:573:def add_search_docs_to_tool_call(
HEAD:backend/onyx/db/chat.py:574:    tool_call_id: int, search_doc_ids: list[int], db_session: Session
HEAD:backend/onyx/db/chat.py:577:    Link SearchDocs to a ToolCall by creating entries in the tool_call__search_doc junction table.
HEAD:backend/onyx/db/chat.py:580:        tool_call_id: The ID of the tool call
HEAD:backend/onyx/db/chat.py:587:        tool_call_search_doc = ToolCall__SearchDoc(
HEAD:backend/onyx/db/chat.py:588:            tool_call_id=tool_call_id, search_doc_id=search_doc_id
HEAD:backend/onyx/db/chat.py:590:        db_session.add(tool_call_search_doc)
HEAD:backend/onyx/db/chat.py:594:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:598:    prefetch_top_two_level_tool_calls: bool = True,
HEAD:backend/onyx/db/chat.py:603:        get_chat_session_by_id(
HEAD:backend/onyx/db/chat.py:604:            chat_session_id=chat_session_id, user_id=user_id, db_session=db_session
HEAD:backend/onyx/db/chat.py:609:        .where(ChatMessage.chat_session_id == chat_session_id)
HEAD:backend/onyx/db/chat.py:621:    if prefetch_top_two_level_tool_calls:
HEAD:backend/onyx/db/chat.py:622:        # Load tool_calls and their direct children (one level deep)
HEAD:backend/onyx/db/chat.py:624:            selectinload(ChatMessage.tool_calls).selectinload(
HEAD:backend/onyx/db/chat.py:625:                ToolCall.tool_call_children
HEAD:backend/onyx/db/chat.py:636:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:643:                ChatMessage.chat_session_id == chat_session_id,
HEAD:backend/onyx/db/chat.py:657:            chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:671:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:678:        chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:707:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:720:            chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:791:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:809:        existing_message.chat_session_id = chat_session_id
HEAD:backend/onyx/db/chat.py:821:            chat_session_id=chat_session_id,
HEAD:backend/onyx/db/chat.py:870:        document_id=sanitize_string(server_search_doc.document_id),
HEAD:backend/onyx/db/chat.py:921:def get_db_search_doc_by_document_id(
HEAD:backend/onyx/db/chat.py:922:    document_id: str, db_session: Session
HEAD:backend/onyx/db/chat.py:924:    """Get SearchDoc by document_id field. There are no safety checks here like user permission etc., use with caution"""
HEAD:backend/onyx/db/chat.py:927:        .filter(DBSearchDoc.document_id == document_id)
HEAD:backend/onyx/db/chat.py:940:        document_id=db_search_doc.document_id,
HEAD:backend/onyx/db/chat.py:974:    # Convert citations from {citation_num: db_doc_id} to {citation_num: document_id}
HEAD:backend/onyx/db/chat.py:977:        # Build lookup map: db_doc_id -> document_id
HEAD:backend/onyx/db/chat.py:978:        db_doc_id_to_document_id = {
HEAD:backend/onyx/db/chat.py:979:            doc.id: doc.document_id for doc in chat_message.search_docs
HEAD:backend/onyx/db/chat.py:984:            document_id = db_doc_id_to_document_id.get(db_doc_id)
HEAD:backend/onyx/db/chat.py:985:            if document_id:
HEAD:backend/onyx/db/chat.py:986:                converted_citations[citation_num] = document_id
HEAD:backend/onyx/db/chat.py:998:        chat_session_id=chat_message.chat_session_id,
HEAD:backend/onyx/db/chat.py:1020:def update_chat_session_updated_at_timestamp(
HEAD:backend/onyx/db/chat.py:1021:    chat_session_id: UUID, db_session: Session
HEAD:backend/onyx/db/chat.py:1031:        .where(ChatSession.id == chat_session_id)
HEAD:backend/onyx/db/chat.py:1049:        document_id=inference_section.center_chunk.document_id,
HEAD:backend/onyx/db/chat.py:1086:        document_id=saved_search_doc.document_id,
HEAD:backend/onyx/db/chat.py:1112:    chat_session_id: UUID,
HEAD:backend/onyx/db/chat.py:1126:            ChatMessage.chat_session_id == chat_session_id,
HEAD:backend/onyx/db/chat_search.py:11:def search_chat_sessions(
HEAD:backend/onyx/db/chat_search.py:80:        select(ChatMessage.chat_session_id)
HEAD:backend/onyx/db/chat_search.py:81:        .join(ChatSession, ChatMessage.chat_session_id == ChatSession.id)
HEAD:backend/onyx/db/chunk.py:17:        chunk_data: List of dicts containing chunk_id, document_id, and boost_score
HEAD:backend/onyx/db/chunk.py:28:        chunk_document_id = f"{data.document_id}__{chunk_in_doc_id}"
HEAD:backend/onyx/db/chunk.py:32:                ChunkStats.id == chunk_document_id,
HEAD:backend/onyx/db/chunk.py:49:                document_id=data.document_id,
HEAD:backend/onyx/db/chunk.py:56:def delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/chunk.py:57:    db_session: Session, document_ids: list[str]
HEAD:backend/onyx/db/chunk.py:60:    stmt = delete(ChunkStats).where(ChunkStats.document_id.in_(document_ids))
HEAD:backend/onyx/db/connector.py:38:def check_user_files_exist(db_session: Session) -> bool:
HEAD:backend/onyx/db/connector.py:174:def get_connector_credential_ids(
HEAD:backend/onyx/db/connector.py:219:            IndexAttempt.connector_credential_pair_id,
HEAD:backend/onyx/db/connector.py:223:        .group_by(IndexAttempt.connector_credential_pair_id)
HEAD:backend/onyx/db/connector.py:233:            IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/connector.py:234:            == alias.connector_credential_pair_id,
HEAD:backend/onyx/db/connector_credential_pair.py:93:    USER_FILE = "user_file"
HEAD:backend/onyx/db/connector_credential_pair.py:243:def get_connector_credential_pairs_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:304:def get_connector_credential_pairs_for_user_parallel(
HEAD:backend/onyx/db/connector_credential_pair.py:317:        return get_connector_credential_pairs_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:332:def get_connector_credential_pairs(
HEAD:backend/onyx/db/connector_credential_pair.py:348:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/connector_credential_pair.py:399:def get_connector_credential_pair_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:414:def get_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:426:def get_connector_credential_pair_from_id_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:452:def get_cc_pair_ids_for_document(db_session: Session, document_id: str) -> set[int]:
HEAD:backend/onyx/db/connector_credential_pair.py:465:            .where(DocumentByConnectorCredentialPair.id == document_id)
HEAD:backend/onyx/db/connector_credential_pair.py:495:def get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/connector_credential_pair.py:513:def get_connector_credential_pairs_for_source(
HEAD:backend/onyx/db/connector_credential_pair.py:549:            IndexAttempt.connector_credential_pair_id == ConnectorCredentialPair.id,
HEAD:backend/onyx/db/connector_credential_pair.py:576:def _update_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:605:def update_connector_credential_pair_from_id(
HEAD:backend/onyx/db/connector_credential_pair.py:612:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/connector_credential_pair.py:623:    _update_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:632:def update_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:640:    cc_pair = get_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:653:    _update_connector_credential_pair(
HEAD:backend/onyx/db/connector_credential_pair.py:676:def delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/connector_credential_pair.py:857:    association = get_connector_credential_pair_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:888:def fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/db/connector_credential_pair.py:921:    fetch_indexable_standard_connector_credential_pair_ids the reindex/swap use, so a
HEAD:backend/onyx/db/connector_credential_pair.py:927:        fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/db/connector_credential_pair.py:967:def fetch_connector_credential_pair_for_connector(
HEAD:backend/onyx/db/connector_credential_pair.py:984:    Updates state stored in the connector_credential_pair table based on the
HEAD:backend/onyx/db/connector_credential_pair.py:1003:                IndexAttempt.connector_credential_pair_id == ConnectorCredentialPair.id,
HEAD:backend/onyx/db/deletion_attempt.py:9:    connector_credential_pair: ConnectorCredentialPair,
HEAD:backend/onyx/db/deletion_attempt.py:21:        f"Connector with ID '{connector_credential_pair.connector_id}' and credential ID "
HEAD:backend/onyx/db/deletion_attempt.py:22:        f"'{connector_credential_pair.credential_id}' is not deletable."
HEAD:backend/onyx/db/deletion_attempt.py:25:    if connector_credential_pair.status.is_active():
HEAD:backend/onyx/db/deletion_attempt.py:28:    connector_id = connector_credential_pair.connector_id
HEAD:backend/onyx/db/deletion_attempt.py:29:    credential_id = connector_credential_pair.credential_id
HEAD:backend/onyx/db/document.py:30:from onyx.db.chunk import delete_chunk_stats_by_connector_credential_pair__no_commit
HEAD:backend/onyx/db/document.py:31:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/onyx/db/document.py:107:def document_has_indexable_cc_pair(db_session: Session, document_id: str) -> bool:
HEAD:backend/onyx/db/document.py:125:                DocumentByConnectorCredentialPair.id == document_id,
HEAD:backend/onyx/db/document.py:187:def construct_document_id_select_by_needs_sync_or_secondary_pending() -> CompoundSelect:
HEAD:backend/onyx/db/document.py:214:def construct_document_id_select_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:229:def construct_document_select_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:246:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/document.py:252:    stmt = construct_document_select_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:258:def get_document_ids_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:270:def get_document_ids_for_cc_pair_batch(
HEAD:backend/onyx/db/document.py:284:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/document.py:307:def get_max_document_id_for_cc_pair(db_session: Session, cc_pair_id: int) -> str | None:
HEAD:backend/onyx/db/document.py:311:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/document.py:324:def filter_existing_cc_pair_document_ids(
HEAD:backend/onyx/db/document.py:327:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:329:    """Of `document_ids`, the subset still linked to this cc_pair. The reindex port
HEAD:backend/onyx/db/document.py:332:    if not document_ids:
HEAD:backend/onyx/db/document.py:334:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/db/document.py:342:        DocumentByConnectorCredentialPair.id.in_(document_ids),
HEAD:backend/onyx/db/document.py:347:def get_documents_for_connector_credential_pair_limited_columns(
HEAD:backend/onyx/db/document.py:387:def get_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:404:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:406:    stmt = select(DbDocument).where(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:459:    cursor_document_id: str | None,
HEAD:backend/onyx/db/document.py:468:    if not cursor_last_modified or not cursor_document_id:
HEAD:backend/onyx/db/document.py:475:        id_cmp = DbDocument.id > cursor_document_id
HEAD:backend/onyx/db/document.py:479:        id_cmp = DbDocument.id < cursor_document_id
HEAD:backend/onyx/db/document.py:528:    cursor_document_id: str | None,
HEAD:backend/onyx/db/document.py:531:    if not cursor_name or not cursor_document_id:
HEAD:backend/onyx/db/document.py:538:                DbDocument.id > cursor_document_id,
HEAD:backend/onyx/db/document.py:547:    cursor_document_id: str | None,
HEAD:backend/onyx/db/document.py:550:    if not cursor_name or not cursor_document_id:
HEAD:backend/onyx/db/document.py:557:                DbDocument.id < cursor_document_id,
HEAD:backend/onyx/db/document.py:579:    cursor_document_id: str | None = None,
HEAD:backend/onyx/db/document.py:591:            stmt = _apply_name_cursor_filter_asc(stmt, cursor_name, cursor_document_id)
HEAD:backend/onyx/db/document.py:594:            stmt = _apply_name_cursor_filter_desc(stmt, cursor_name, cursor_document_id)
HEAD:backend/onyx/db/document.py:603:                cursor_document_id,
HEAD:backend/onyx/db/document.py:616:                cursor_document_id,
HEAD:backend/onyx/db/document.py:631:def filter_existing_document_ids(
HEAD:backend/onyx/db/document.py:633:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:639:        document_ids: List of document IDs to check for existence
HEAD:backend/onyx/db/document.py:644:    if not document_ids:
HEAD:backend/onyx/db/document.py:646:    stmt = select(DbDocument.id).where(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:650:def fetch_document_ids_by_links(
HEAD:backend/onyx/db/document.py:665:    document_id: str,
HEAD:backend/onyx/db/document.py:667:    results = get_document_connector_counts(db_session, [document_id])
HEAD:backend/onyx/db/document.py:676:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:683:        .where(DocumentByConnectorCredentialPair.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:763:    document_id: str,
HEAD:backend/onyx/db/document.py:769:        document_id (str): The document ID to fetch access info for.
HEAD:backend/onyx/db/document.py:774:    results = get_access_info_for_documents(db_session, [document_id])
HEAD:backend/onyx/db/document.py:783:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:801:    ).where(DocumentByConnectorCredentialPair.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:842:        doc_id = document_metadata.document_id
HEAD:backend/onyx/db/document.py:856:                    id=doc.document_id,
HEAD:backend/onyx/db/document.py:932:def upsert_document_by_connector_credential_pair(
HEAD:backend/onyx/db/document.py:933:    db_session: Session, connector_id: int, credential_id: int, document_ids: list[str]
HEAD:backend/onyx/db/document.py:936:    if not document_ids:
HEAD:backend/onyx/db/document.py:937:        logger.info("`document_ids` is empty. Skipping.")
HEAD:backend/onyx/db/document.py:950:            for doc_id in document_ids
HEAD:backend/onyx/db/document.py:965:    document_ids: Iterable[str],
HEAD:backend/onyx/db/document.py:974:                DocumentByConnectorCredentialPair.id.in_(document_ids),
HEAD:backend/onyx/db/document.py:1037:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1041:        db_session.query(DbDocument).filter(DbDocument.id.in_(document_ids)).all()
HEAD:backend/onyx/db/document.py:1050:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1055:        db_session.query(DbDocument).filter(DbDocument.id.in_(document_ids)).all()
HEAD:backend/onyx/db/document.py:1075:    document_id: str,
HEAD:backend/onyx/db/document.py:1078:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1081:        raise ValueError(f"No document with ID: {document_id}")
HEAD:backend/onyx/db/document.py:1089:    document_id: str,
HEAD:backend/onyx/db/document.py:1096:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1099:        raise ValueError(f"No document with ID: {document_id}")
HEAD:backend/onyx/db/document.py:1111:    document_id: str,
HEAD:backend/onyx/db/document.py:1120:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1123:        raise ValueError(f"No document with ID: {document_id}")
HEAD:backend/onyx/db/document.py:1132:def delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1134:    document_id: str,
HEAD:backend/onyx/db/document.py:1135:    connector_credential_pair_identifier: (
HEAD:backend/onyx/db/document.py:1144:    delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1146:        document_ids=[document_id],
HEAD:backend/onyx/db/document.py:1147:        connector_credential_pair_identifier=connector_credential_pair_identifier,
HEAD:backend/onyx/db/document.py:1151:def delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1153:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1154:    connector_credential_pair_identifier: (
HEAD:backend/onyx/db/document.py:1164:        DocumentByConnectorCredentialPair.id.in_(document_ids)
HEAD:backend/onyx/db/document.py:1166:    if connector_credential_pair_identifier:
HEAD:backend/onyx/db/document.py:1170:                == connector_credential_pair_identifier.connector_id,
HEAD:backend/onyx/db/document.py:1172:                == connector_credential_pair_identifier.credential_id,
HEAD:backend/onyx/db/document.py:1178:def delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1200:def delete_documents__no_commit(db_session: Session, document_ids: list[str]) -> None:
HEAD:backend/onyx/db/document.py:1201:    db_session.execute(delete(DbDocument).where(DbDocument.id.in_(document_ids)))
HEAD:backend/onyx/db/document.py:1204:def get_file_ids_for_document_ids(
HEAD:backend/onyx/db/document.py:1206:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1209:    if not document_ids:
HEAD:backend/onyx/db/document.py:1213:        .filter(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:1220:def get_document_id_to_file_id_map(
HEAD:backend/onyx/db/document.py:1222:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1224:    """Return a `{document_id: file_id}` map for docs that have a file_id."""
HEAD:backend/onyx/db/document.py:1225:    if not document_ids:
HEAD:backend/onyx/db/document.py:1229:        .filter(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:1237:    db_session: Session, document_ids: list[str]
HEAD:backend/onyx/db/document.py:1245:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1250:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1255:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1260:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1264:    delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1266:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1269:    delete_documents_by_connector_credential_pair__no_commit(db_session, document_ids)
HEAD:backend/onyx/db/document.py:1271:        document_ids=document_ids, db_session=db_session
HEAD:backend/onyx/db/document.py:1274:        document_ids=document_ids, db_session=db_session
HEAD:backend/onyx/db/document.py:1276:    delete_documents__no_commit(db_session, document_ids)
HEAD:backend/onyx/db/document.py:1281:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1288:    file_ids_to_delete = get_file_ids_for_document_ids(
HEAD:backend/onyx/db/document.py:1290:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1294:        document_ids=document_ids,
HEAD:backend/onyx/db/document.py:1300:def delete_all_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:1326:        document_ids = db_session.scalars(stmt).all()
HEAD:backend/onyx/db/document.py:1328:        if not document_ids:
HEAD:backend/onyx/db/document.py:1332:            db_session=db_session, document_ids=list(document_ids)
HEAD:backend/onyx/db/document.py:1339:def acquire_document_locks(db_session: Session, document_ids: list[str]) -> bool:
HEAD:backend/onyx/db/document.py:1341:    called with large list of document_ids (an exception could be made if the
HEAD:backend/onyx/db/document.py:1350:        .where(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:1357:    if len(documents) != len(set(document_ids)):
HEAD:backend/onyx/db/document.py:1371:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1395:                    db_session=db_session, document_ids=document_ids
HEAD:backend/onyx/db/document.py:1428:            f"Failed to acquire locks after {_NUM_LOCK_ATTEMPTS} attempts for documents: {document_ids}"
HEAD:backend/onyx/db/document.py:1466:    document_id: str,
HEAD:backend/onyx/db/document.py:1469:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1476:    document_id: str,
HEAD:backend/onyx/db/document.py:1489:        .where(DocumentByConnectorCredentialPair.id == document_id)
HEAD:backend/onyx/db/document.py:1496:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1520:        .where(DocumentByConnectorCredentialPair.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:1529:    document_ids: list[str],
HEAD:backend/onyx/db/document.py:1533:    Return a list of (document_id, chunk_count) tuples.
HEAD:backend/onyx/db/document.py:1534:    If a document_id is not found in the database, it will be returned with a chunk_count of 0.
HEAD:backend/onyx/db/document.py:1537:        DbDocument.id.in_(document_ids)
HEAD:backend/onyx/db/document.py:1542:    # Create a dictionary of document_id to chunk_count
HEAD:backend/onyx/db/document.py:1548:    return [(doc_id, chunk_counts.get(doc_id, 0)) for doc_id in document_ids]
HEAD:backend/onyx/db/document.py:1552:    document_id: str,
HEAD:backend/onyx/db/document.py:1555:    stmt = select(DbDocument.chunk_count).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1607:def get_kg_extracted_document_ids(db_session: Session) -> list[str]:
HEAD:backend/onyx/db/document.py:1621:    db_session: Session, document_id: str, kg_stage: KGStage
HEAD:backend/onyx/db/document.py:1626:        document_id (str): The ID of the document to update
HEAD:backend/onyx/db/document.py:1633:        .where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1644:    document_id: str,
HEAD:backend/onyx/db/document.py:1648:        update(DbDocument).where(DbDocument.id == document_id).values(kg_stage=kg_stage)
HEAD:backend/onyx/db/document.py:1677:    db_session: Session, document_ids: list[str]
HEAD:backend/onyx/db/document.py:1679:    stmt = select(DbDocument).where(DbDocument.id.in_(document_ids))
HEAD:backend/onyx/db/document.py:1694:    document_id: str,
HEAD:backend/onyx/db/document.py:1699:        document_id (str): The ID of the document to query
HEAD:backend/onyx/db/document.py:1705:    stmt = select(DbDocument.doc_updated_at).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1775:#     db_session: Session, document_id: str, entity_type: str
HEAD:backend/onyx/db/document.py:1783:#         .filter(Document.id == document_id)
HEAD:backend/onyx/db/document.py:1792:#             semantic_entity_name=f"{entity_type}:{document_id}",
HEAD:backend/onyx/db/document.py:1793:#             semantic_linked_entity_name=f"{entity_type}:{document_id}",
HEAD:backend/onyx/db/document.py:1797:#         doc_id=document_id,
HEAD:backend/onyx/db/document.py:1908:    db_session: Session, document_id: str
HEAD:backend/onyx/db/document.py:1914:        db_session.query(KGEntity).filter(KGEntity.document_id == document_id).all()
HEAD:backend/onyx/db/document.py:1926:                KGRelationship.source_document == document_id,
HEAD:backend/onyx/db/document.py:1934:def get_num_chunks_for_document(db_session: Session, document_id: str) -> int:
HEAD:backend/onyx/db/document.py:1935:    stmt = select(DbDocument.chunk_count).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1941:    document_id: str,
HEAD:backend/onyx/db/document.py:1950:        document_id: The ID of the document to update
HEAD:backend/onyx/db/document.py:1955:        .where(DbDocument.id == document_id)
HEAD:backend/onyx/db/document.py:1963:    document_id: str,
HEAD:backend/onyx/db/document.py:1973:    delete_documents_complete__no_commit(db_session, [document_id])
HEAD:backend/onyx/db/document_access.py:10:from onyx.db.connector_credential_pair import build_user_cc_pair_access_filter
HEAD:backend/onyx/db/document_access.py:63:    document_ids: list[str],
HEAD:backend/onyx/db/document_access.py:69:    if not document_ids:
HEAD:backend/onyx/db/document_access.py:72:    stmt = select(Document).where(Document.id.in_(document_ids))
HEAD:backend/onyx/db/document_set.py:10:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/db/document_set.py:12:    get_connector_credential_pairs,
HEAD:backend/onyx/db/document_set.py:192:            selectinload(DocumentSetDBModel.connector_credential_pairs),
HEAD:backend/onyx/db/document_set.py:314:        cc_pairs = get_connector_credential_pairs(
HEAD:backend/onyx/db/document_set.py:376:                connector_credential_pair_id=cc_pair_id,
HEAD:backend/onyx/db/document_set.py:484:                connector_credential_pair_id=cc_pair_id,
HEAD:backend/onyx/db/document_set.py:600:    connector_credential_pair_id matches the given cc_pair_id."""
HEAD:backend/onyx/db/document_set.py:605:            DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/onyx/db/document_set.py:632:            == DocumentSet__ConnectorCredentialPair.connector_credential_pair_id,
HEAD:backend/onyx/db/document_set.py:678:            selectinload(DocumentSetDBModel.connector_credential_pairs).selectinload(
HEAD:backend/onyx/db/document_set.py:696:    last_document_id: str | None = None,
HEAD:backend/onyx/db/document_set.py:716:            DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/onyx/db/document_set.py:728:    if last_document_id is not None:
HEAD:backend/onyx/db/document_set.py:729:        stmt = stmt.where(Document.id > last_document_id)
HEAD:backend/onyx/db/document_set.py:740:def construct_document_id_select_by_docset(
HEAD:backend/onyx/db/document_set.py:765:            DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/onyx/db/document_set.py:787:    document_id: str,
HEAD:backend/onyx/db/document_set.py:793:    :param document_id: The ID of the document to fetch sets for.
HEAD:backend/onyx/db/document_set.py:797:    result = fetch_document_sets_for_documents([document_id], db_session)
HEAD:backend/onyx/db/document_set.py:804:    document_ids: list[str],
HEAD:backend/onyx/db/document_set.py:807:    """Gives back a list of (document_id, list[document_set_names]) tuples"""
HEAD:backend/onyx/db/document_set.py:811:    # returned row for each specified document_id. Basically, we want to do the filters first,
HEAD:backend/onyx/db/document_set.py:858:            == valid_document_set__cc_pairs_subquery.connector_credential_pair_id,
HEAD:backend/onyx/db/document_set.py:865:        .where(Document.id.in_(document_ids))
HEAD:backend/onyx/db/document_set.py:901:    connector_credential_pair_ids = (
HEAD:backend/onyx/db/document_set.py:903:            DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/onyx/db/document_set.py:915:                connector_credential_pair_ids  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/db/entities.py:21:    document_id: str | None = None,
HEAD:backend/onyx/db/entities.py:32:        document_id: ID of the document the entity belongs to
HEAD:backend/onyx/db/entities.py:63:            document_id=document_id,
HEAD:backend/onyx/db/entities.py:83:    # Update the document's kg_stage if document_id is provided
HEAD:backend/onyx/db/entities.py:84:    if document_id is not None:
HEAD:backend/onyx/db/entities.py:85:        db_session.query(Document).filter(Document.id == document_id).update(
HEAD:backend/onyx/db/entities.py:119:            document_id=entity.document_id,
HEAD:backend/onyx/db/entities.py:125:            index_elements=["name", "entity_type_id_name", "document_id"],
HEAD:backend/onyx/db/entities.py:143:    # Update the document's kg_stage if document_id is provided
HEAD:backend/onyx/db/entities.py:144:    if entity.document_id is not None:
HEAD:backend/onyx/db/entities.py:147:            document_id=entity.document_id,
HEAD:backend/onyx/db/entities.py:174:    # check we're not merging two entities with different document_ids
HEAD:backend/onyx/db/entities.py:176:        parent.document_id is not None
HEAD:backend/onyx/db/entities.py:177:        and child.document_id is not None
HEAD:backend/onyx/db/entities.py:178:        and parent.document_id != child.document_id
HEAD:backend/onyx/db/entities.py:181:            "Overwriting the document_id of an entity with a document_id already is not allowed"
HEAD:backend/onyx/db/entities.py:184:    # update the parent entity (only document_id, alternative_names, occurrences)
HEAD:backend/onyx/db/entities.py:185:    setting_doc = parent.document_id is None and child.document_id is not None
HEAD:backend/onyx/db/entities.py:186:    document_id = child.document_id if setting_doc else parent.document_id
HEAD:backend/onyx/db/entities.py:196:            document_id=document_id,
HEAD:backend/onyx/db/entities.py:210:    # Update the document's kg_stage if document_id is set
HEAD:backend/onyx/db/entities.py:211:    if setting_doc and child.document_id is not None:
HEAD:backend/onyx/db/entities.py:214:            document_id=child.document_id,
HEAD:backend/onyx/db/entities.py:227:def get_kg_entity_by_document(db: Session, document_id: str) -> KGEntity | None:
HEAD:backend/onyx/db/entities.py:229:    Check if a document_id exists in the kg_entities table and return its id_name if found.
HEAD:backend/onyx/db/entities.py:233:        document_id: The document ID to search for
HEAD:backend/onyx/db/entities.py:238:    query = select(KGEntity).where(KGEntity.document_id == document_id)
HEAD:backend/onyx/db/entities.py:264:def get_document_id_for_entity(db_session: Session, entity_id_name: str) -> str | None:
HEAD:backend/onyx/db/entities.py:277:    return entity.document_id if entity else None
HEAD:backend/onyx/db/entities.py:281:    db_session: Session, document_ids: list[str]
HEAD:backend/onyx/db/entities.py:285:        KGEntityExtractionStaging.document_id.in_(document_ids)
HEAD:backend/onyx/db/entities.py:290:    db_session: Session, document_ids: list[str]
HEAD:backend/onyx/db/entities.py:293:    db_session.query(KGEntity).filter(KGEntity.document_id.in_(document_ids)).delete(
HEAD:backend/onyx/db/enums.py:202:class MCPServerStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:248:class ChatSessionSharedStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:294:class UserFileStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:730:class PersonaSharePermission(str, PyEnum):
HEAD:backend/onyx/db/enums.py:754:class PersonaAccessLevel(str, PyEnum):
HEAD:backend/onyx/db/enums.py:764:class PersonaSharingStatus(str, PyEnum):
HEAD:backend/onyx/db/federated.py:49:def validate_federated_connector_credentials(
HEAD:backend/onyx/db/federated.py:73:    if not validate_federated_connector_credentials(source, credentials):
HEAD:backend/onyx/db/federated.py:290:        if not validate_federated_connector_credentials(
HEAD:backend/onyx/db/feedback.py:119:    document_id: str,
HEAD:backend/onyx/db/feedback.py:123:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/feedback.py:141:    document_id: str,
HEAD:backend/onyx/db/feedback.py:145:    stmt = select(DbDocument).where(DbDocument.id == document_id)
HEAD:backend/onyx/db/feedback.py:163:    document_id: str,
HEAD:backend/onyx/db/feedback.py:170:    db_doc = _fetch_db_doc_by_id(document_id, db_session)
HEAD:backend/onyx/db/feedback.py:174:        document_id=document_id,
HEAD:backend/onyx/db/feedback.py:206:    document_ids: list[str], db_session: Session
HEAD:backend/onyx/db/feedback.py:211:        DocumentRetrievalFeedback.document_id.in_(document_ids)
HEAD:backend/onyx/db/file_record.py:159:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/hierarchy.py:118:        document_id=None,
HEAD:backend/onyx/db/hierarchy.py:428:    document_ids: list[str],
HEAD:backend/onyx/db/hierarchy.py:436:    AND documents, we need to set the document_id field on hierarchy nodes after the
HEAD:backend/onyx/db/hierarchy.py:438:    and the FK constraint on document_id requires the document to exist first.
HEAD:backend/onyx/db/hierarchy.py:442:        document_ids: List of document IDs that were just created/updated
HEAD:backend/onyx/db/hierarchy.py:453:    if not document_ids:
HEAD:backend/onyx/db/hierarchy.py:456:    # Find hierarchy nodes where raw_node_id matches a document_id
HEAD:backend/onyx/db/hierarchy.py:460:        HierarchyNode.raw_node_id.in_(document_ids),
HEAD:backend/onyx/db/hierarchy.py:461:        HierarchyNode.document_id.is_(None),  # Only update if not already linked
HEAD:backend/onyx/db/hierarchy.py:465:    # Update document_id for each matching node
HEAD:backend/onyx/db/hierarchy.py:467:        node.document_id = node.raw_node_id
HEAD:backend/onyx/db/hierarchy.py:671:    document_ids: list[str],
HEAD:backend/onyx/db/hierarchy.py:678:        document_ids: List of document IDs to look up
HEAD:backend/onyx/db/hierarchy.py:681:        Dict mapping document_id -> parent_hierarchy_node_id (or None if not set)
HEAD:backend/onyx/db/hierarchy.py:684:    if not document_ids:
HEAD:backend/onyx/db/hierarchy.py:688:        Document.id.in_(document_ids)
HEAD:backend/onyx/db/hierarchy.py:707:        doc_parent_map: Mapping of document_id → desired parent_hierarchy_node_id
HEAD:backend/onyx/db/incognito.py:40:    db_session: Session, chat_session_id: UUID, user_id: UUID
HEAD:backend/onyx/db/incognito.py:50:            ChatSession.id == chat_session_id
HEAD:backend/onyx/db/incognito.py:59:def mark_user_files_deleting(db_session: Session, file_ids: Sequence[UUID]) -> None:
HEAD:backend/onyx/db/incognito.py:70:def mark_incognito_user_files_deleting(
HEAD:backend/onyx/db/incognito.py:71:    db_session: Session, chat_session_id: UUID, user_id: UUID | None = None
HEAD:backend/onyx/db/incognito.py:80:        UserFile.incognito_session_id == chat_session_id,
HEAD:backend/onyx/db/incognito.py:86:    mark_user_files_deleting(db_session, file_ids)
HEAD:backend/onyx/db/incognito.py:94:        # Matches ix_user_file_incognito_sweep's partial predicate.
HEAD:backend/onyx/db/incognito.py:148:    db_session: Session, chat_session_ids: Sequence[UUID]
HEAD:backend/onyx/db/incognito.py:156:    if not chat_session_ids:
HEAD:backend/onyx/db/incognito.py:161:            UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/incognito.py:169:    db_session: Session, chat_session_ids: Sequence[UUID]
HEAD:backend/onyx/db/incognito.py:172:    if not chat_session_ids:
HEAD:backend/onyx/db/incognito.py:178:                UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/index_attempt.py:37:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:54:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:74:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:91:            joinedload(IndexAttempt.connector_credential_pair).joinedload(
HEAD:backend/onyx/db/index_attempt.py:96:            joinedload(IndexAttempt.connector_credential_pair).joinedload(
HEAD:backend/onyx/db/index_attempt.py:135:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:142:        connector_credential_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:155:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:169:        connector_credential_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:191:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:199:        connector_credential_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:223:            IndexAttempt.connector_credential_pair.has(connector_id=connector_id)
HEAD:backend/onyx/db/index_attempt.py:300:                "cc_pair_id": index_attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:329:                "cc_pair_id": attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:369:                "cc_pair_id": attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:412:                "cc_pair_id": attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:457:                "cc_pair_id": attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:508:                "cc_pair_id": attempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:588:    Retrieves the most recent index attempt with the specified status for each connector_credential_pair.
HEAD:backend/onyx/db/index_attempt.py:590:    Returns a sequence of IndexAttempt objects, one for each unique connector_credential_pair.
HEAD:backend/onyx/db/index_attempt.py:594:            IndexAttempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:611:        IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:617:            IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:618:            == latest_failed_attempts.c.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:645:        IndexAttempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:657:    ids_stmt = ids_stmt.group_by(IndexAttempt.connector_credential_pair_id)
HEAD:backend/onyx/db/index_attempt.py:664:            IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:665:            == ids_subquery.c.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:675:            joinedload(IndexAttempt.connector_credential_pair),
HEAD:backend/onyx/db/index_attempt.py:706:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:713:        IndexAttempt.connector_credential_pair_id == connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:729:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:739:        IndexAttempt.connector_credential_pair_id == connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:770:                IndexAttempt.connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:788:            IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:794:                IndexAttempt.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:795:                == latest_ids.c.connector_credential_pair_id
HEAD:backend/onyx/db/index_attempt.py:810:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:858:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:924:                IndexAttempt.connector_credential_pair_id == cc_pair_id
HEAD:backend/onyx/db/index_attempt.py:931:        IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/index_attempt.py:975:        .where(IndexAttempt.connector_credential_pair_id == cc_pair_id)
HEAD:backend/onyx/db/index_attempt.py:1041:        db_session.query(IndexAttempt.connector_credential_pair_id)
HEAD:backend/onyx/db/index_attempt.py:1066:        db_session.query(IndexAttempt.connector_credential_pair_id)
HEAD:backend/onyx/db/index_attempt.py:1083:    connector_credential_pair_id: int,
HEAD:backend/onyx/db/index_attempt.py:1090:        connector_credential_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/db/index_attempt.py:1091:        document_id=(
HEAD:backend/onyx/db/index_attempt.py:1092:            failure.failed_document.document_id if failure.failed_document else None
HEAD:backend/onyx/db/index_attempt.py:1138:        .where(IndexAttemptError.connector_credential_pair_id == cc_pair_id)
HEAD:backend/onyx/db/index_attempt.py:1155:        IndexAttemptError.connector_credential_pair_id == cc_pair_id
HEAD:backend/onyx/db/index_attempt.py:1187:        stmt = stmt.where(IndexAttemptError.connector_credential_pair_id == cc_pair_id)
HEAD:backend/onyx/db/index_attempt.py:1189:            IndexAttemptError.connector_credential_pair_id == cc_pair_id
HEAD:backend/onyx/db/indexing_coordination.py:59:                    IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/db/indexing_coordination.py:80:                connector_credential_pair_id=cc_pair_id,
HEAD:backend/onyx/db/kg_temp_view.py:63:#         SELECT document_id as kg_used_doc_id
HEAD:backend/onyx/db/kg_temp_view.py:65:#         WHERE document_id IS NOT NULL
HEAD:backend/onyx/db/kg_temp_view.py:76:#         FROM "{tenant_id}".document_by_connector_credential_pair d
HEAD:backend/onyx/db/kg_temp_view.py:78:#         JOIN "{tenant_id}".connector_credential_pair ccp ON
HEAD:backend/onyx/db/kg_temp_view.py:89:#         FROM "{tenant_id}".document_by_connector_credential_pair d
HEAD:backend/onyx/db/kg_temp_view.py:90:#         JOIN "{tenant_id}".connector_credential_pair ccp ON
HEAD:backend/onyx/db/kg_temp_view.py:93:#         JOIN "{tenant_id}".user_group__connector_credential_pair ugccp ON
HEAD:backend/onyx/db/kg_temp_view.py:164:#            kge.document_id as source_document,
HEAD:backend/onyx/db/kg_temp_view.py:167:#     INNER JOIN {allowed_docs_view_name} AD on AD.allowed_doc_id = kge.document_id
HEAD:backend/onyx/db/kg_temp_view.py:168:#     JOIN "{tenant_id}".document d on d.id = kge.document_id
HEAD:backend/onyx/db/memory.py:18:class UserInfo(BaseModel):
HEAD:backend/onyx/db/memory.py:34:class UserMemoryContext(BaseModel):
HEAD:backend/onyx/db/models.py:332:class User(SQLAlchemyBaseUserTableUUID, Base):
HEAD:backend/onyx/db/models.py:470:    chat_sessions: Mapped[list["ChatSession"]] = relationship(
HEAD:backend/onyx/db/models.py:575:class PersonalAccessToken(Base):
HEAD:backend/onyx/db/models.py:672:class Persona__DocumentSet(Base):
HEAD:backend/onyx/db/models.py:681:class User__PinnedPersona(Base):
HEAD:backend/onyx/db/models.py:700:class Persona__User(Base):
HEAD:backend/onyx/db/models.py:741:class UserSkillPreference(Base):
HEAD:backend/onyx/db/models.py:771:class DocumentSet__User(Base):
HEAD:backend/onyx/db/models.py:782:class DocumentSet__ConnectorCredentialPair(Base):
HEAD:backend/onyx/db/models.py:783:    __tablename__ = "document_set__connector_credential_pair"
HEAD:backend/onyx/db/models.py:788:    connector_credential_pair_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:789:        ForeignKey("connector_credential_pair.id"), primary_key=True
HEAD:backend/onyx/db/models.py:806:class ChatMessage__SearchDoc(Base):
HEAD:backend/onyx/db/models.py:817:class ToolCall__SearchDoc(Base):
HEAD:backend/onyx/db/models.py:818:    __tablename__ = "tool_call__search_doc"
HEAD:backend/onyx/db/models.py:820:    tool_call_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:821:        ForeignKey("tool_call.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:828:class Document__Tag(Base):
HEAD:backend/onyx/db/models.py:831:    document_id: Mapped[str] = mapped_column(
HEAD:backend/onyx/db/models.py:839:class Persona__Tool(Base):
HEAD:backend/onyx/db/models.py:880:class ChatMessage__StandardAnswer(Base):
HEAD:backend/onyx/db/models.py:902:    __tablename__ = "connector_credential_pair"
HEAD:backend/onyx/db/models.py:907:        Sequence("connector_credential_pair_id_seq"),
HEAD:backend/onyx/db/models.py:989:            (DocumentSet__ConnectorCredentialPair.connector_credential_pair_id == id)
HEAD:backend/onyx/db/models.py:992:        back_populates="connector_credential_pairs",
HEAD:backend/onyx/db/models.py:996:        "IndexAttempt", back_populates="connector_credential_pair"
HEAD:backend/onyx/db/models.py:1022:    In these cases, `document_id` will be set.
HEAD:backend/onyx/db/models.py:1069:    document_id: Mapped[str | None] = mapped_column(
HEAD:backend/onyx/db/models.py:1081:        "Document", back_populates="hierarchy_node", foreign_keys=[document_id]
HEAD:backend/onyx/db/models.py:1112:class Document(Base):
HEAD:backend/onyx/db/models.py:1234:        foreign_keys="HierarchyNode.document_id",
HEAD:backend/onyx/db/models.py:1269:    document_id: Mapped[str] = mapped_column(
HEAD:backend/onyx/db/models.py:1601:    document_id: Mapped[str | None] = mapped_column(NullFilteredString, nullable=True)
HEAD:backend/onyx/db/models.py:1671:    document_id: Mapped[str | None] = mapped_column(NullFilteredString, nullable=True)
HEAD:backend/onyx/db/models.py:1931:            f"{context.get_current_parameters()['document_id']}__{context.get_current_parameters()['chunk_in_doc_id']}"
HEAD:backend/onyx/db/models.py:1936:    document_id: Mapped[str] = mapped_column(
HEAD:backend/onyx/db/models.py:1963:            "document_id", "chunk_in_doc_id", name="uq_chunk_stats_doc_chunk"
HEAD:backend/onyx/db/models.py:2063:class Credential(Base):
HEAD:backend/onyx/db/models.py:2106:class CredentialCapabilityReportRow(Base):
HEAD:backend/onyx/db/models.py:2252:class SearchSettings(Base):
HEAD:backend/onyx/db/models.py:2512:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2515:    document_id: Mapped[str] = mapped_column(Text, primary_key=True)
HEAD:backend/onyx/db/models.py:2526:            "document_id",
HEAD:backend/onyx/db/models.py:2550:    connector_credential_pair_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:2551:        ForeignKey("connector_credential_pair.id"),
HEAD:backend/onyx/db/models.py:2651:    connector_credential_pair: Mapped[ConnectorCredentialPair] = relationship(
HEAD:backend/onyx/db/models.py:2673:            "ix_index_attempt_latest_for_connector_credential_pair",
HEAD:backend/onyx/db/models.py:2674:            "connector_credential_pair_id",
HEAD:backend/onyx/db/models.py:2679:            "connector_credential_pair_id",
HEAD:backend/onyx/db/models.py:2686:            "connector_credential_pair_id",
HEAD:backend/onyx/db/models.py:2694:            "connector_credential_pair_id",
HEAD:backend/onyx/db/models.py:2730:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2792:    connector_credential_pair: Mapped["ConnectorCredentialPair | None"] = relationship(
HEAD:backend/onyx/db/models.py:2847:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2857:    document_id: Mapped[str] = mapped_column(String, nullable=False)
HEAD:backend/onyx/db/models.py:2874:            "document_id",
HEAD:backend/onyx/db/models.py:2882:            "document_id",
HEAD:backend/onyx/db/models.py:2898:    connector_credential_pair_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:2899:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2931:    connector_credential_pair: Mapped["ConnectorCredentialPair"] = relationship(
HEAD:backend/onyx/db/models.py:2938:            connector_credential_pair_id,
HEAD:backend/onyx/db/models.py:2953:    connector_credential_pair_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:2954:        ForeignKey("connector_credential_pair.id"),
HEAD:backend/onyx/db/models.py:2959:    document_id: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:3092:    __tablename__ = "hierarchy_node_by_connector_credential_pair"
HEAD:backend/onyx/db/models.py:3104:                "connector_credential_pair.connector_id",
HEAD:backend/onyx/db/models.py:3105:                "connector_credential_pair.credential_id",
```
## Identity and Authorization Assets
Evidence lines: 600
```text
HEAD:backend/ee/onyx/access/access.py:11:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/access/access.py:102:        # If its censored, then it's public anywhere during the search and then permissions are
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:38:def _domain_token(tenant_id: str, domain: str) -> str:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:43:    message = f"sso-domain:{tenant_id}:{domain}".encode()
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:48:def verification_record(tenant_id: str, domain: str) -> tuple[str, str]:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:52:    return host, f"{_VALUE_PREFIX}{_domain_token(tenant_id, domain)}"
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:77:def verify_domain_via_dns(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:86:    if not is_claimed_domain(tenant_id, domain):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:92:    host, expected = verification_record(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:94:        mark_domain_verified(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:99:def _proof_still_present(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:105:    host, expected = verification_record(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:109:def revalidate_tenant_domains(tenant_id: str) -> None:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:119:    for record in list_login_domains(tenant_id):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:123:            if _proof_still_present(tenant_id, record.domain):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:125:            mark_domain_unverified(tenant_id, record.domain)
HEAD:backend/ee/onyx/auth/users.py:4:import jwt
HEAD:backend/ee/onyx/auth/users.py:9:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/auth/users.py:11:from onyx.db.enums import Permission
HEAD:backend/ee/onyx/auth/users.py:27:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/auth/users.py:45:def generate_anonymous_user_jwt_token(tenant_id: str) -> str:
HEAD:backend/ee/onyx/auth/users.py:47:        "tenant_id": tenant_id,
HEAD:backend/ee/onyx/auth/users.py:52:    return jwt.encode(payload, USER_AUTH_SECRET, algorithm="HS256")
HEAD:backend/ee/onyx/auth/users.py:55:def decode_anonymous_user_jwt_token(token: str) -> dict:
HEAD:backend/ee/onyx/auth/users.py:56:    return jwt.decode(token, USER_AUTH_SECRET, algorithms=["HS256"])
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:21:def export_query_history_cleanup_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:22:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:12:    ONYX_CLOUD_TENANT_ID,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:17:from onyx.db.engine.tenant_utils import get_all_tenant_ids
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:89:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:101:    tenant_ids: list[str] = []
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:154:        tenant_ids = get_all_tenant_ids()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:163:        for tenant_id in tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:164:            if tenant_id in gated_tenants:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:174:            if IGNORED_SYNCING_TENANT_LIST and tenant_id in IGNORED_SYNCING_TENANT_LIST:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:182:                    active_tenants is not None and tenant_id not in active_tenants
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:195:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:231:        f"num_tenants={len(tenant_ids)} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:24:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:69:    update_hierarchy_node_permissions as db_update_hierarchy_node_permissions,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:113:DOCUMENT_PERMISSIONS_UPDATE_MAX_RETRIES = 3
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:114:DOCUMENT_PERMISSIONS_UPDATE_STOP_AFTER = 10 * 60
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:115:DOCUMENT_PERMISSIONS_UPDATE_MAX_WAIT = 60
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:141:"""Jobs / utils for kicking off doc permissions sync tasks."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:149:    docs_with_permission_errors: int = 0,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:159:            docs_with_permission_errors=docs_with_permission_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:164:    """Returns boolean indicating if external doc permissions sync is due."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:169:    # skip doc permissions sync if not active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:196:    source_sync_period *= int(OnyxRuntime.get_doc_permission_sync_multiplier())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:212:def check_for_doc_permissions_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:238:                if _is_external_doc_permissions_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:242:        # whenever doc-permission sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:244:            maybe_mark_tenant_active(tenant_id, caller="doc_permission_sync")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:248:            payload_id = try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:249:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:261:            # clear any permission fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:294:                    monitor_ccpair_permissions_taskset(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:295:                        tenant_id, key_bytes, r, db_session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:317:def try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:321:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:350:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:351:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:362:                    sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:368:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:381:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:420:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:467:        payload = redis_connector.permissions.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:571:            payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:583:            callback = PermissionSyncCallback(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:630:                    f"Permission sync task timed out or stop signal detected: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:635:            result = redis_connector.permissions.update_db(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:637:                new_permissions=[doc_external_access],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:660:                docs_with_permission_errors=docs_with_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:663:            f"Completed doc permission sync attempt {attempt_id}: {tasks_generated} docs, {docs_with_errors} errors"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:666:        redis_connector.permissions.generator_complete = tasks_generated
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:684:            docs_with_permission_errors=docs_with_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:687:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:688:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:705:        multiplier=1, max=DOCUMENT_PERMISSIONS_UPDATE_MAX_WAIT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:707:    stop=stop_after_delay(DOCUMENT_PERMISSIONS_UPDATE_STOP_AFTER),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:709:def element_update_permissions(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:710:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:711:    permissions: ElementExternalAccess,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:716:    """Update permissions for a document or hierarchy node."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:718:    external_access = permissions.external_access
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:721:    if isinstance(permissions, DocExternalAccess):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:722:        element_id = permissions.doc_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:725:        element_id = permissions.raw_node_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:729:        with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:737:            if isinstance(permissions, DocExternalAccess):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:738:                # Document permission update
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:741:                    doc_id=permissions.doc_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:752:                        document_ids=[permissions.doc_id],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:755:                # Hierarchy node permission update
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:756:                db_update_hierarchy_node_permissions(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:758:                    raw_node_id=permissions.raw_node_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:759:                    source=DocumentSource(permissions.source),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:775:                f"{element_type}={element_id} action=update_permissions elapsed={elapsed:.2f}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:784:            f"element_update_permissions completed: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:791:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:814:    # validate all existing permission sync jobs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:824:            tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:838:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:892:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:901:        redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:920:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:925:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:930:    # because we get the celery tasks first, the entries in our own permissions taskset
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:943:    for member in r.sscan_iter(redis_connector.permissions.taskset_key):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:961:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:972:    if redis_connector.permissions.active():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:984:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1006:        self.last_tag: str = "PermissionSyncCallback.__init__"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1034:            self.redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1059:"""Monitoring CCPair permissions utils"""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1062:def monitor_ccpair_permissions_taskset(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1063:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1072:            f"monitor_ccpair_permissions_taskset: could not parse cc_pair_id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1082:    initial = redis_connector.permissions.generator_complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1087:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1097:    remaining = redis_connector.permissions.get_remaining()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1110:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1125:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1131:        sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1136:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:3:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:26:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:59:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:169:def check_for_external_group_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:218:            maybe_mark_tenant_active(tenant_id, caller="external_group_sync")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:223:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:260:            f"Unexpected check_for_external_group_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:262:        task_logger.exception(f"Unexpected exception: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:267:    task_logger.info(f"check_for_external_group_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:275:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:324:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:362:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:434:            tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:481:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:501:            tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:511:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:575:            external_user_group_generator = ext_group_sync_func(tenant_id, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:680:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:701:            tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:712:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:20:def hook_execution_log_cleanup_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:29:def check_license_expiry_notifications_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:87:def reclaim_license_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:120:                payload.tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:132:                "Failed to reclaim license for tenant %s: %s", payload.tenant_id, e
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:69:    tenant_id: str,  # noqa: ARG001  # Injected into every beat task by ``DynamicTenantScheduler``.
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:43:    # Need to include the tenant_id since the TenantAwareTask needs this
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:44:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:24:def revalidate_sso_domains_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:31:        reproject_tenant_login_domains(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:33:        logger.exception("Failed to re-project login domains for %s", tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:34:    revalidate_tenant_domains(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:15:    ONYX_CLOUD_TENANT_ID,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:25:from shared_configs.configs import MULTI_TENANT, TENANT_ID_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:58:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:139:        tenant_ids = [t.tenant_id for t in pool_tenants]
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:141:    if not tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:145:        f"Checking {len(tenant_ids)} pool tenant(s) for pending migrations"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:148:    for tenant_id in tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:150:            run_alembic_migrations(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:151:            new_version = get_current_alembic_version(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:155:                    .filter_by(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:160:                        f"Migrated pool tenant {tenant_id}: {tenant.alembic_version} -> {new_version}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:166:                f"Failed to migrate pool tenant {tenant_id}, skipping"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:188:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:201:    tenant_id: str | None = None
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:204:        tenant_id = TENANT_ID_PREFIX + str(uuid.uuid4())
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:206:        task_logger.info(f"Pre-provisioning tenant {tenant_id} on shard {shard_name}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:209:        record_tenant_placement(tenant_id, shard_name)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:212:        schema_created = create_schema_if_not_exists(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:214:            task_logger.debug(f"Created schema for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:216:            task_logger.debug(f"Schema already exists for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:219:        task_logger.debug(f"Setting up tenant configuration: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:220:        asyncio.run(setup_tenant(tenant_id))
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:221:        task_logger.debug(f"Tenant configuration completed: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:224:        alembic_version = get_current_alembic_version(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:226:            f"Tenant {tenant_id} using Alembic version: {alembic_version}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:230:        task_logger.debug(f"Storing pre-provisioned tenant in database: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:236:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:243:                task_logger.info(f"Successfully pre-provisioned tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:248:                    f"Failed to store pre-provisioned tenant: {tenant_id}",
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:255:        # If we have a tenant_id, attempt to rollback any partially completed provisioning
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:256:        if tenant_id:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:258:                f"Rolling back failed tenant provisioning for: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:265:                asyncio.run(rollback_tenant_provisioning(tenant_id))
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:267:                task_logger.exception(f"Error during rollback for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:69:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:92:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:134:                    "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:154:def check_ttl_management_task(self: Task, *, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:170:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:188:                "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:24:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:20:    tenant_id: str, key_bytes: bytes, r: TenantRedisClient, db_session: Session
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:35:    rug = RedisUserGroup(tenant_id, usergroup_id)
HEAD:backend/ee/onyx/background/task_name_builders.py:10:    tenant_id: str | None = None,  # noqa: ARG001
HEAD:backend/ee/onyx/configs/app_configs.py:5:# Auto Permission Sync
HEAD:backend/ee/onyx/configs/app_configs.py:7:# should generally only be used for sources that support polling of permissions
HEAD:backend/ee/onyx/configs/app_configs.py:8:# e.g. can pull in only permission changes rather than having to go through all
HEAD:backend/ee/onyx/configs/app_configs.py:10:DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:11:    os.environ.get("DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:20:CONFLUENCE_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:21:    os.environ.get("CONFLUENCE_PERMISSION_GROUP_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:24:CONFLUENCE_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:25:    os.environ.get("CONFLUENCE_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:40:JIRA_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:41:    os.environ.get("JIRA_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:44:JIRA_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:45:    os.environ.get("JIRA_PERMISSION_GROUP_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:53:CANVAS_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:54:    os.environ.get("CANVAS_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:57:CANVAS_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:58:    os.environ.get("CANVAS_PERMISSION_GROUP_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:68:BOX_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:69:    os.environ.get("BOX_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:71:BOX_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:72:    os.environ.get("BOX_PERMISSION_GROUP_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:79:GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:80:    os.environ.get("GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:88:GITHUB_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:89:    os.environ.get("GITHUB_PERMISSION_DOC_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:92:GITHUB_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:93:    os.environ.get("GITHUB_PERMISSION_GROUP_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:100:SLACK_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:101:    os.environ.get("SLACK_PERMISSION_DOC_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:104:NUM_PERMISSION_WORKERS = int(os.environ.get("NUM_PERMISSION_WORKERS") or 2)
HEAD:backend/ee/onyx/configs/app_configs.py:111:TEAMS_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:112:    os.environ.get("TEAMS_PERMISSION_DOC_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:119:SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:120:    os.environ.get("SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:124:SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:125:    os.environ.get("SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:139:# JWT Public Key URL
HEAD:backend/ee/onyx/configs/app_configs.py:140:JWT_PUBLIC_KEY_URL: str | None = os.getenv("JWT_PUBLIC_KEY_URL", None)
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:32:#   /mcp/oauth/client-metadata - Public OAuth client identity
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:50:        "/mcp/oauth/client-metadata",
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:82:    "/manage/admin/user-group": Tier.BUSINESS,  # groups + RBAC (Curator roles, group-scoped access)
HEAD:backend/ee/onyx/connectors/capability_applicability.py:10:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/connectors/capability_applicability.py:24:        applicable.add(CredentialCapability.DOC_PERMISSION_SYNC)
HEAD:backend/ee/onyx/connectors/capability_checks.py:20:    build_slack_doc_permission_sync_checks,
HEAD:backend/ee/onyx/connectors/capability_checks.py:26:_DOC_PERMISSION_SYNC_CHECKS_BY_SOURCE: dict[DocumentSource, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/connectors/capability_checks.py:27:    DocumentSource.SLACK: build_slack_doc_permission_sync_checks(),
HEAD:backend/ee/onyx/connectors/capability_checks.py:53:            display_name="Permission sync validation",
HEAD:backend/ee/onyx/connectors/capability_checks.py:81:        CredentialCapability.DOC_PERMISSION_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:82:            _DOC_PERMISSION_SYNC_CHECKS_BY_SOURCE.get(source, [])
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:16:    connector.probe_account_user_listing_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:21:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:23:    For Confluence Data Center 9.1+, the REST space-permissions endpoint
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:27:    actionable InsufficientPermissionsError -- instead of as a
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:30:    connector.probe_rest_space_permissions_admin_access()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:35:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:41:    connector.probe_directory_admin_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:51:    connector.probe_group_listing_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:56:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:58:    Two distinct permission surfaces are needed for SharePoint perm sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:60:      1. SharePoint REST 'Sites.FullControl.All' to enumerate RoleAssignments.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:62:         Azure AD groups attached to those RoleAssignments.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:66:    connector.probe_role_assignments_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:67:    connector.probe_group_members_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:86:    Override this if your connector needs to validate permissions syncing.
HEAD:backend/ee/onyx/db/document.py:19:    This sets the permissions for a document in postgres.
HEAD:backend/ee/onyx/db/document.py:59:    This sets the permissions for a document in postgres. Returns True if the
HEAD:backend/ee/onyx/db/document.py:78:        # The upsert function in the indexing pipeline does not overwrite the permissions fields
HEAD:backend/ee/onyx/db/document_set.py:15:    User__UserGroup,
HEAD:backend/ee/onyx/db/document_set.py:174:        .join(User__UserGroup, UserGroup.id == User__UserGroup.user_group_id)
HEAD:backend/ee/onyx/db/document_set.py:175:        .filter(User__UserGroup.user_id == user_id)
HEAD:backend/ee/onyx/db/hierarchy.py:1:"""EE hierarchy access control for source and connector permissions."""
HEAD:backend/ee/onyx/db/license.py:21:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/db/license.py:39:def _advisory_lock_id(namespace: str, tenant_id: str) -> int:
HEAD:backend/ee/onyx/db/license.py:40:    digest = hashlib.sha256(f"{namespace}:{tenant_id}".encode()).digest()
HEAD:backend/ee/onyx/db/license.py:45:def seat_lock_id_for_tenant(tenant_id: str) -> int:
HEAD:backend/ee/onyx/db/license.py:46:    return _advisory_lock_id(_SEAT_LOCK_NAMESPACE, tenant_id)
HEAD:backend/ee/onyx/db/license.py:58:        _advisory_lock_id(_LICENSE_STORE_LOCK_NAMESPACE, get_current_tenant_id()),
HEAD:backend/ee/onyx/db/license.py:62:def acquire_seat_lock(db_session: Session, tenant_id: str | None = None) -> None:
HEAD:backend/ee/onyx/db/license.py:69:        db_session, seat_lock_id_for_tenant(tenant_id or get_current_tenant_id())
HEAD:backend/ee/onyx/db/license.py:197:def get_used_seats(tenant_id: str | None = None) -> int:
HEAD:backend/ee/onyx/db/license.py:210:        return get_tenant_count(tenant_id or get_current_tenant_id())
HEAD:backend/ee/onyx/db/license.py:233:def get_cached_license_metadata(tenant_id: str | None = None) -> LicenseMetadata | None:
HEAD:backend/ee/onyx/db/license.py:238:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:243:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:258:def invalidate_license_cache(tenant_id: str | None = None) -> None:
HEAD:backend/ee/onyx/db/license.py:267:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:269:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:277:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:287:    used_seats = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/db/license.py:301:        tenant_id=payload.tenant_id,
HEAD:backend/ee/onyx/db/license.py:327:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:334:    metadata, ttl = build_license_metadata(payload, grace_period_end, tenant_id)
HEAD:backend/ee/onyx/db/license.py:335:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:352:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:372:    with _license_cache_lock(tenant_id, wait_for_lock) as lock:
HEAD:backend/ee/onyx/db/license.py:376:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:382:            metadata, _ = build_license_metadata(payload, tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:384:        metadata = update_license_cache(payload, tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:390:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:396:    tenant_id: str | None, wait: bool
HEAD:backend/ee/onyx/db/license.py:406:        candidate = get_cache_backend(tenant_id=tenant_id).lock(
HEAD:backend/ee/onyx/db/license.py:429:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:436:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:445:            db_session, tenant_id=tenant_id, wait_for_lock=False
HEAD:backend/ee/onyx/db/license.py:449:        invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:455:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:462:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:468:    cached = get_cached_license_metadata(tenant_id)
HEAD:backend/ee/onyx/db/license.py:473:    return refresh_license_cache(db_session, tenant_id)
HEAD:backend/ee/onyx/db/license.py:479:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:487:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:494:    metadata = get_license_metadata(db_session, tenant_id)
HEAD:backend/ee/onyx/db/license.py:501:    current_used = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/db/mcp.py:5:from onyx.db.models import MCPServer__User, MCPServer__UserGroup
HEAD:backend/ee/onyx/db/mcp.py:17:        db_session.query(MCPServer__User).filter(
HEAD:backend/ee/onyx/db/mcp.py:18:            MCPServer__User.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:21:            db_session.add(MCPServer__User(mcp_server_id=server_id, user_id=user_id))
HEAD:backend/ee/onyx/db/mcp.py:25:        db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/mcp.py:26:            MCPServer__UserGroup.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:30:                MCPServer__UserGroup(mcp_server_id=server_id, user_group_id=group_id)
HEAD:backend/ee/onyx/db/persona.py:5:from onyx.auth.permissions import has_global_permission, has_permission
HEAD:backend/ee/onyx/db/persona.py:6:from onyx.auth.scoped_permissions import assert_within_scope
HEAD:backend/ee/onyx/db/persona.py:7:from onyx.db.enums import Permission, PermissionAuthority, PersonaSharePermission
HEAD:backend/ee/onyx/db/persona.py:8:from onyx.db.models import Persona, Persona__UserGroup, User
HEAD:backend/ee/onyx/db/persona.py:24:    group_shares: dict[int, PersonaSharePermission] | None,
HEAD:backend/ee/onyx/db/persona.py:26:) -> dict[int, PersonaSharePermission] | None:
HEAD:backend/ee/onyx/db/persona.py:28:    VIEWER) so pre-permission callers can't downgrade editor groups."""
HEAD:backend/ee/onyx/db/persona.py:34:        row.user_group_id: row.permission
HEAD:backend/ee/onyx/db/persona.py:35:        for row in db_session.query(Persona__UserGroup)
HEAD:backend/ee/onyx/db/persona.py:36:        .filter(Persona__UserGroup.persona_id == persona_id)
HEAD:backend/ee/onyx/db/persona.py:40:        group_id: existing.get(group_id, PersonaSharePermission.VIEWER)
HEAD:backend/ee/onyx/db/persona.py:47:    desired_shares: dict[int, PersonaSharePermission],
HEAD:backend/ee/onyx/db/persona.py:54:        db_session.query(Persona__UserGroup)
HEAD:backend/ee/onyx/db/persona.py:55:        .filter(Persona__UserGroup.persona_id == persona_id)
HEAD:backend/ee/onyx/db/persona.py:65:        elif row.permission != desired_shares[group_id]:
HEAD:backend/ee/onyx/db/persona.py:66:            row.permission = desired_shares[group_id]
HEAD:backend/ee/onyx/db/persona.py:68:    for group_id, permission in desired_shares.items():
HEAD:backend/ee/onyx/db/persona.py:71:                Persona__UserGroup(
HEAD:backend/ee/onyx/db/persona.py:74:                    permission=permission,
HEAD:backend/ee/onyx/db/persona.py:82:    desired_group_shares: dict[int, PersonaSharePermission],
HEAD:backend/ee/onyx/db/persona.py:95:    if has_global_permission(acting_user, Permission.MANAGE_USER_GROUPS):
HEAD:backend/ee/onyx/db/persona.py:98:        row.user_group_id: row.permission
HEAD:backend/ee/onyx/db/persona.py:99:        for row in db_session.query(Persona__UserGroup)
HEAD:backend/ee/onyx/db/persona.py:100:        .filter(Persona__UserGroup.persona_id == persona_id)
HEAD:backend/ee/onyx/db/persona.py:119:        has_permission(acting_user, Permission.MANAGE_AGENTS)
HEAD:backend/ee/onyx/db/persona.py:120:        is not PermissionAuthority.SCOPED
HEAD:backend/ee/onyx/db/persona.py:126:        permission=Permission.MANAGE_AGENTS,
HEAD:backend/ee/onyx/db/persona.py:141:    user_shares: dict[UUID, PersonaSharePermission] | None = None,
HEAD:backend/ee/onyx/db/persona.py:142:    group_shares: dict[int, PersonaSharePermission] | None = None,
HEAD:backend/ee/onyx/db/persona.py:143:    public_permission: PersonaSharePermission | None = None,
HEAD:backend/ee/onyx/db/persona.py:167:    if is_public is not None or public_permission is not None:
HEAD:backend/ee/onyx/db/persona.py:172:            if public_permission is not None:
HEAD:backend/ee/onyx/db/persona.py:173:                persona.public_permission = public_permission
HEAD:backend/ee/onyx/db/scim.py:35:from onyx.db.enums import AccountType, GrantSource, Permission
HEAD:backend/ee/onyx/db/scim.py:37:    PermissionGrant,
HEAD:backend/ee/onyx/db/scim.py:42:    User__UserGroup,
HEAD:backend/ee/onyx/db/scim.py:425:            select(User__UserGroup).where(User__UserGroup.user_id == user_id)
HEAD:backend/ee/onyx/db/scim.py:452:            select(User__UserGroup).where(User__UserGroup.user_id.in_(user_ids))
HEAD:backend/ee/onyx/db/scim.py:567:    def add_permission_grant_to_group(
HEAD:backend/ee/onyx/db/scim.py:570:        permission: Permission,
HEAD:backend/ee/onyx/db/scim.py:573:        """Grant a permission to a group and flush."""
HEAD:backend/ee/onyx/db/scim.py:575:            PermissionGrant(
HEAD:backend/ee/onyx/db/scim.py:577:                permission=permission,
HEAD:backend/ee/onyx/db/scim.py:647:            select(User__UserGroup).where(User__UserGroup.user_group_id == group_id)
HEAD:backend/ee/onyx/db/scim.py:698:            pg_insert(User__UserGroup)
HEAD:backend/ee/onyx/db/scim.py:702:                    User__UserGroup.user_group_id,
HEAD:backend/ee/onyx/db/scim.py:703:                    User__UserGroup.user_id,
HEAD:backend/ee/onyx/db/scim.py:721:                select(User__UserGroup.user_id).where(
HEAD:backend/ee/onyx/db/scim.py:722:                    User__UserGroup.user_group_id == group_id
HEAD:backend/ee/onyx/db/scim.py:735:            sa_delete(User__UserGroup).where(
HEAD:backend/ee/onyx/db/scim.py:736:                User__UserGroup.user_group_id == group_id,
HEAD:backend/ee/onyx/db/scim.py:737:                User__UserGroup.user_id.in_(user_ids),
HEAD:backend/ee/onyx/db/scim.py:744:            sa_delete(User__UserGroup).where(User__UserGroup.user_group_id == group.id)
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:45:def lookup_tenant_id_for_email_domain(email: str) -> str | None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:57:            select(TenantSSODomain.tenant_id).where(
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:64:def is_email_domain_verified(tenant_id: str, email: str) -> bool:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:82:                select(TenantSSODomain.tenant_id).where(
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:83:                    TenantSSODomain.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:92:def claim_email_domains(tenant_id: str, domains: list[str]) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:108:                    TenantSSODomain.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:117:                    TenantSSODomain.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:123:            db_session.add(TenantSSODomain(tenant_id=tenant_id, domain=domain))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:133:def list_login_domains(tenant_id: str) -> list[LoginDomainRecord]:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:141:                TenantSSODomain.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:151:def is_claimed_domain(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:156:            db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:161:def mark_domain_verified(tenant_id: str, domain: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:168:        row = db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:186:def mark_domain_unverified(tenant_id: str, domain: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:193:        row = db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:200:def reproject_tenant_login_domains(tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:204:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:206:    claim_email_domains(tenant_id, sorted(domains))
HEAD:backend/ee/onyx/db/user_group.py:15:from onyx.auth.permissions import (
HEAD:backend/ee/onyx/db/user_group.py:16:    NON_TOGGLEABLE_PERMISSIONS,
HEAD:backend/ee/onyx/db/user_group.py:17:    get_effective_permissions,
HEAD:backend/ee/onyx/db/user_group.py:18:    has_global_permission,
HEAD:backend/ee/onyx/db/user_group.py:19:    has_permission,
HEAD:backend/ee/onyx/db/user_group.py:20:    resolve_effective_permissions,
HEAD:backend/ee/onyx/db/user_group.py:22:from onyx.auth.scoped_permissions import assert_manages_group, assert_within_scope
HEAD:backend/ee/onyx/db/user_group.py:33:    Permission,
HEAD:backend/ee/onyx/db/user_group.py:34:    PermissionAuthority,
HEAD:backend/ee/onyx/db/user_group.py:46:    MCPServer__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:47:    PermissionGrant,
HEAD:backend/ee/onyx/db/user_group.py:50:    Persona__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:53:    User__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:57:from onyx.db.permissions import (
HEAD:backend/ee/onyx/db/user_group.py:58:    recompute_permissions_for_group__no_commit,
HEAD:backend/ee/onyx/db/user_group.py:59:    recompute_user_permissions__no_commit,
HEAD:backend/ee/onyx/db/user_group.py:92:    where_clause = User__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:94:        where_clause &= User__UserGroup.user_id.in_(user_ids)
HEAD:backend/ee/onyx/db/user_group.py:97:        select(User__UserGroup).where(where_clause)
HEAD:backend/ee/onyx/db/user_group.py:126:    db_session.query(Persona__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:127:        Persona__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:135:    db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:136:        MCPServer__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:262:                Persona__UserGroup.user_group
HEAD:backend/ee/onyx/db/user_group.py:327:        .join(User__UserGroup, User__UserGroup.user_group_id == UserGroup.id)
HEAD:backend/ee/onyx/db/user_group.py:330:            User.id == User__UserGroup.user_id,  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/db/user_group.py:486:        insert(User__UserGroup)
HEAD:backend/ee/onyx/db/user_group.py:494:            index_elements=[User__UserGroup.user_group_id, User__UserGroup.user_id]
HEAD:backend/ee/onyx/db/user_group.py:535:    # Every group gets the "basic" permission by default
HEAD:backend/ee/onyx/db/user_group.py:537:        PermissionGrant(
HEAD:backend/ee/onyx/db/user_group.py:539:            permission=Permission.BASIC_ACCESS,
HEAD:backend/ee/onyx/db/user_group.py:556:    recompute_user_permissions__no_commit(user_group.user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:652:    group_permissions = set(
HEAD:backend/ee/onyx/db/user_group.py:654:            select(PermissionGrant.permission).where(
HEAD:backend/ee/onyx/db/user_group.py:655:                PermissionGrant.group_id == user_group_id,
HEAD:backend/ee/onyx/db/user_group.py:656:                PermissionGrant.is_deleted.is_(False),
HEAD:backend/ee/onyx/db/user_group.py:661:    group_permissions.discard(Permission.BASIC_ACCESS)
HEAD:backend/ee/onyx/db/user_group.py:662:    excess = group_permissions - get_effective_permissions(user)
HEAD:backend/ee/onyx/db/user_group.py:665:            OnyxErrorCode.INSUFFICIENT_PERMISSIONS,
HEAD:backend/ee/onyx/db/user_group.py:666:            "You can't add members to a group that grants permissions you don't "
HEAD:backend/ee/onyx/db/user_group.py:667:            "hold: " + ", ".join(sorted(permission.value for permission in excess)),
HEAD:backend/ee/onyx/db/user_group.py:699:    if not has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS):
HEAD:backend/ee/onyx/db/user_group.py:701:            OnyxErrorCode.INSUFFICIENT_PERMISSIONS,
HEAD:backend/ee/onyx/db/user_group.py:727:        has_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/db/user_group.py:728:        is not PermissionAuthority.SCOPED
HEAD:backend/ee/onyx/db/user_group.py:756:            permission=Permission.MANAGE_CONNECTORS,
HEAD:backend/ee/onyx/db/user_group.py:768:    Reads grants directly rather than ``effective_permissions``, which still reflects the
HEAD:backend/ee/onyx/db/user_group.py:771:        permission.value
HEAD:backend/ee/onyx/db/user_group.py:772:        for permission in db_session.scalars(
HEAD:backend/ee/onyx/db/user_group.py:773:            select(PermissionGrant.permission)
HEAD:backend/ee/onyx/db/user_group.py:775:                User__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:776:                User__UserGroup.user_group_id == PermissionGrant.group_id,
HEAD:backend/ee/onyx/db/user_group.py:779:                User__UserGroup.user_id == user.id,
HEAD:backend/ee/onyx/db/user_group.py:780:                User__UserGroup.user_group_id != group_id,
HEAD:backend/ee/onyx/db/user_group.py:781:                PermissionGrant.is_deleted.is_(False),
HEAD:backend/ee/onyx/db/user_group.py:785:    return Permission.MANAGE_USER_GROUPS.value in resolve_effective_permissions(granted)
HEAD:backend/ee/onyx/db/user_group.py:848:    # effective_permissions is derived from group grants — so leaving can revoke the very
HEAD:backend/ee/onyx/db/user_group.py:901:    recompute_user_permissions__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:936:        select(User__UserGroup).where(
HEAD:backend/ee/onyx/db/user_group.py:937:            User__UserGroup.user_id == user_id,
HEAD:backend/ee/onyx/db/user_group.py:938:            User__UserGroup.user_group_id == group_id,
HEAD:backend/ee/onyx/db/user_group.py:946:    recompute_user_permissions__no_commit([user_id], db_session)
HEAD:backend/ee/onyx/db/user_group.py:1004:            select(User__UserGroup.user_id).where(
HEAD:backend/ee/onyx/db/user_group.py:1005:                User__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:1025:            select(User__UserGroup.user_id).where(
HEAD:backend/ee/onyx/db/user_group.py:1026:                User__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:1068:    # Recompute permissions for affected users now that their
HEAD:backend/ee/onyx/db/user_group.py:1070:    recompute_user_permissions__no_commit(affected_user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:1119:class PermissionChange(NamedTuple):
HEAD:backend/ee/onyx/db/user_group.py:1125:    enabled: list[Permission]
HEAD:backend/ee/onyx/db/user_group.py:1126:    added: list[Permission]
HEAD:backend/ee/onyx/db/user_group.py:1127:    removed: list[Permission]
HEAD:backend/ee/onyx/db/user_group.py:1130:def set_group_permissions_bulk__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:1132:    desired_permissions: set[Permission],
HEAD:backend/ee/onyx/db/user_group.py:1135:) -> PermissionChange:
HEAD:backend/ee/onyx/db/user_group.py:1136:    """Set the full desired permission state for a group in one pass.
HEAD:backend/ee/onyx/db/user_group.py:1138:    Enables permissions in `desired_permissions`, disables any toggleable
HEAD:backend/ee/onyx/db/user_group.py:1139:    permission not in the set. Non-toggleable permissions are ignored.
HEAD:backend/ee/onyx/db/user_group.py:1149:            select(PermissionGrant)
HEAD:backend/ee/onyx/db/user_group.py:1150:            .where(PermissionGrant.group_id == group_id)
HEAD:backend/ee/onyx/db/user_group.py:1157:    grant_map: dict[Permission, PermissionGrant] = {
HEAD:backend/ee/onyx/db/user_group.py:1158:        g.permission: g for g in existing_grants
HEAD:backend/ee/onyx/db/user_group.py:1163:    desired_permissions = desired_permissions - NON_TOGGLEABLE_PERMISSIONS
HEAD:backend/ee/onyx/db/user_group.py:1165:    added: list[Permission] = []
HEAD:backend/ee/onyx/db/user_group.py:1166:    removed: list[Permission] = []
HEAD:backend/ee/onyx/db/user_group.py:1168:    # Enable desired permissions
HEAD:backend/ee/onyx/db/user_group.py:1169:    for perm in desired_permissions:
HEAD:backend/ee/onyx/db/user_group.py:1179:                PermissionGrant(
HEAD:backend/ee/onyx/db/user_group.py:1181:                    permission=perm,
HEAD:backend/ee/onyx/db/user_group.py:1188:    # Disable toggleable permissions not in the desired set
```
## AI and Model Assets
Evidence lines: 650
```text
HEAD:backend/ee/onyx/db/user_group.py:45:    LLMProvider__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:117:    db_session.query(LLMProvider__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:118:        LLMProvider__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:46:from onyx.server.manage.llm.models import LLMProviderView, ModelConfigurationView
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:85:def is_anthropic_passthrough_eligible(provider: LLMProviderView) -> bool:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:90:def _append_api_path(provider: LLMProviderView, suffix: str) -> str:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:96:def _messages_url(provider: LLMProviderView) -> str:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:100:def _count_tokens_url(provider: LLMProviderView) -> str:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:113:    model_name: str,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:127:    body["model"] = model_name
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:142:    provider: LLMProviderView, http_request: Request
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:243:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:256:    llm = llm_from_provider(model_name=model_config.name, llm_provider=provider)
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:274:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:371:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:484:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/api.py:112:from onyx.server.manage.llm.models import LLMProviderView, ModelConfigurationView
HEAD:backend/ee/onyx/server/gateway/api.py:158:) -> tuple[LLMProviderView, ModelConfigurationView]:
HEAD:backend/ee/onyx/server/gateway/api.py:164:    provider_id_text, separator, model_name = requested_model.partition("/")
HEAD:backend/ee/onyx/server/gateway/api.py:169:    if not separator or not model_name or provider_id < 0:
HEAD:backend/ee/onyx/server/gateway/api.py:172:            "(expected '<provider_id>/<model_name>')",
HEAD:backend/ee/onyx/server/gateway/api.py:184:            if model.is_visible and model.name == model_name
HEAD:backend/ee/onyx/server/gateway/api.py:322:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:364:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/api.py:369:        model_name=model_config.name,
HEAD:backend/ee/onyx/server/gateway/api.py:396:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:620:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:730:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/api.py:741:        model_name=model_config.name,
HEAD:backend/ee/onyx/server/gateway/api.py:775:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:1120:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:1287:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/api.py:1292:        model_name=model_config.name,
HEAD:backend/ee/onyx/server/gateway/api.py:1324:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:27:from onyx.llm.constants import LlmProviderNames
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:44:from onyx.server.manage.llm.models import LLMProviderView, ModelConfigurationView
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:73:    provider: LLMProviderView, model_config: ModelConfigurationView
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:77:    if provider.provider == LlmProviderNames.AZURE:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:84:def _base_url(provider: LLMProviderView) -> str:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:91:def _responses_url(provider: LLMProviderView) -> str:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:104:    model_name: str,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:183:    body["model"] = model_name
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:197:def _build_upstream_headers(provider: LLMProviderView) -> dict[str, str]:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:271:    provider: LLMProviderView,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:283:    llm = llm_from_provider(model_name=model_config.name, llm_provider=provider)
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:301:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:428:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/seeding.py:26:from onyx.server.manage.llm.models import LLMProviderUpsertRequest, LLMProviderView
HEAD:backend/ee/onyx/server/seeding.py:55:    llms: list[LLMProviderUpsertRequest] | None = None
HEAD:backend/ee/onyx/server/seeding.py:118:    db_session: Session, llm_upsert_requests: list[LLMProviderUpsertRequest]
HEAD:backend/ee/onyx/server/seeding.py:136:    seeded_providers: list[LLMProviderView] = []
HEAD:backend/ee/onyx/server/seeding.py:163:        model_name=default_config.name,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:49:    upsert_cloud_embedding_provider,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:74:    LLMProviderUpsertRequest,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:382:    def _upsert(request: LLMProviderUpsertRequest, default_model: str) -> None:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:411:        default_model_name = default_model.name if default_model else "gpt-5.2"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:413:        openai_provider = LLMProviderUpsertRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:423:        _upsert(openai_provider, default_model_name)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:446:        default_model_name = (
HEAD:backend/ee/onyx/server/tenants/provisioning.py:450:        anthropic_provider = LLMProviderUpsertRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:460:        _upsert(anthropic_provider, default_model_name)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:475:        default_model_name = default_model.name if default_model else "gemini-2.5-pro"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:483:        vertexai_provider = LLMProviderUpsertRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:493:        _upsert(vertexai_provider, default_model_name)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:507:        default_model_name = default_model.name if default_model else "z-ai/glm-4.7"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:522:        openrouter_provider = LLMProviderUpsertRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:530:        _upsert(openrouter_provider, default_model_name)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:539:        cloud_embedding_provider = CloudEmbeddingProviderCreationRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:546:            upsert_cloud_embedding_provider(db_session, cloud_embedding_provider)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:559:                current_search_settings.model_name = (
HEAD:backend/onyx/background/celery/configs/base.py:180:# def pickle_bz2_encoder(data):
HEAD:backend/onyx/background/celery/configs/base.py:188:# serialization.register('pickle-bzip2', pickle_bz2_encoder, pickle_bz2_decoder, 'application/x-pickle-bz2', 'binary')
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:140:    INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:141:    INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:869:        warm_up_bi_encoder,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:929:                    embedding_model = EmbeddingModel.from_db_model(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:931:                        server_host=INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:932:                        server_port=INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:936:                    warm_up_bi_encoder(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:937:                        embedding_model=embedding_model,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1796:            embedding_model = DefaultIndexingEmbedder.from_db_search_settings(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1858:            embedder=embedding_model,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:421:        embedding_model = DefaultIndexingEmbedder.from_db_search_settings(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:435:                embedder=embedding_model,
HEAD:backend/onyx/chat/compression.py:270:    - No caching or LLMConfig-specific behavior needed
HEAD:backend/onyx/chat/incognito.py:45:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/chat/incognito.py:182:    if provider == LlmProviderNames.PORTKEY.value:
HEAD:backend/onyx/chat/incognito.py:184:    if provider == LlmProviderNames.LITELLM_PROXY.value:
HEAD:backend/onyx/chat/incognito.py:203:        LlmProviderNames.OPENAI.value,
HEAD:backend/onyx/chat/incognito.py:204:        LlmProviderNames.AZURE.value,
HEAD:backend/onyx/chat/incognito.py:208:    if provider == LlmProviderNames.OPENROUTER.value:
HEAD:backend/onyx/chat/llm_loop.py:47:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/chat/llm_loop.py:153:    provider = llm.config.model_provider
HEAD:backend/onyx/chat/llm_loop.py:154:    model = llm.config.model_name
HEAD:backend/onyx/chat/llm_loop.py:162:            " (e.g. Claude Opus 4.8)" if provider == LlmProviderNames.ANTHROPIC else ""
HEAD:backend/onyx/chat/llm_loop.py:184:        and provider == LlmProviderNames.OPENAI
HEAD:backend/onyx/chat/llm_loop.py:822:            llm.config.model_name, llm.config.model_provider, llm.config.deployment_name
HEAD:backend/onyx/chat/llm_step.py:23:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/chat/llm_step.py:27:    LLMConfig,
HEAD:backend/onyx/chat/llm_step.py:794:def _get_history_message_formatter(llm_config: LLMConfig) -> _HistoryMessageFormatter:
HEAD:backend/onyx/chat/llm_step.py:795:    if llm_config.model_provider == LlmProviderNames.OLLAMA_CHAT:
HEAD:backend/onyx/chat/llm_step.py:808:def _is_azure_provider(model_provider: str) -> bool:
HEAD:backend/onyx/chat/llm_step.py:810:    return model_provider.startswith("azure")
HEAD:backend/onyx/chat/llm_step.py:813:def resolve_image_cap(model_provider: str) -> int | None:
HEAD:backend/onyx/chat/llm_step.py:817:    if ENABLE_AZURE_IMAGE_CAP and _is_azure_provider(model_provider):
HEAD:backend/onyx/chat/llm_step.py:856:    llm_config: LLMConfig,
HEAD:backend/onyx/chat/llm_step.py:878:            llm_config.model_name,
HEAD:backend/onyx/chat/llm_step.py:879:            llm_config.model_provider,
HEAD:backend/onyx/chat/llm_step.py:890:        resolve_image_cap(llm_config.model_provider) if supports_image_input else None
HEAD:backend/onyx/chat/llm_step.py:901:                llm_config.model_provider,
HEAD:backend/onyx/chat/llm_step.py:902:                llm_config.model_name,
HEAD:backend/onyx/chat/llm_step.py:1036:        llm_config.model_name, llm_config.deployment_name
HEAD:backend/onyx/chat/llm_step.py:1187:        model=llm.config.model_name,
HEAD:backend/onyx/chat/llm_step.py:1473:                llm.config.model_provider,
HEAD:backend/onyx/chat/llm_step.py:1474:                llm.config.model_name,
HEAD:backend/onyx/chat/llm_step.py:1557:            llm.config.model_provider,
HEAD:backend/onyx/chat/llm_step.py:1558:            llm.config.model_name,
HEAD:backend/onyx/chat/process_message.py:963:                ModelResponseSlot(message_id=m.id, model_name=name)
HEAD:backend/onyx/chat/process_message.py:1138:        "model": llm.config.model_name,
HEAD:backend/onyx/chat/process_message.py:1139:        "provider": llm.config.model_provider,
HEAD:backend/onyx/chat/process_message.py:1857:                    "model": llm.config.model_name,
HEAD:backend/onyx/chat/process_message.py:1858:                    "provider": llm.config.model_provider,
HEAD:backend/onyx/chat/process_message.py:1917:    Falls back to the configured ``llm.config.model_name`` when no override is
HEAD:backend/onyx/chat/process_message.py:1925:    return llm.config.model_name
HEAD:backend/onyx/chat/token_budget.py:53:    for model_name in model_identity_names(config.model_name, config.deployment_name):
HEAD:backend/onyx/chat/token_budget.py:54:        model_obj = find_model_obj(model_map, config.model_provider, model_name) or {}
HEAD:backend/onyx/configs/agent_configs.py:4:AGENT_DEFAULT_RERANKING_HITS = 10
HEAD:backend/onyx/configs/agent_configs.py:31:# Reranking agent configs
HEAD:backend/onyx/configs/agent_configs.py:32:AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS = int(
HEAD:backend/onyx/configs/agent_configs.py:33:    os.environ.get("AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS")
HEAD:backend/onyx/configs/agent_configs.py:34:    or AGENT_DEFAULT_RERANKING_HITS
HEAD:backend/onyx/configs/app_configs.py:59:BLURB_SIZE = 128  # Number Encoder Tokens included in the chunk blurb
HEAD:backend/onyx/configs/app_configs.py:605:# Number of documents in a batch during indexing (further batching done by chunks before passing to bi-encoder)
HEAD:backend/onyx/configs/app_configs.py:1528:INDEXING_EMBEDDING_MODEL_NUM_THREADS = int(
HEAD:backend/onyx/configs/app_configs.py:1529:    os.environ.get("INDEXING_EMBEDDING_MODEL_NUM_THREADS") or 8
HEAD:backend/onyx/configs/app_configs.py:1633:# Should match the rerank-count value set in
HEAD:backend/onyx/configs/app_configs.py:1635:RERANK_COUNT = int(os.environ.get("RERANK_COUNT") or 1000)
HEAD:backend/onyx/configs/app_configs.py:1709:# Opt-in cap on outgoing image-count for Azure providers (any model_provider
HEAD:backend/onyx/configs/app_configs.py:1863:IMAGE_MODEL_NAME = os.environ.get("IMAGE_MODEL_NAME", "gpt-image-1")
HEAD:backend/onyx/configs/app_configs.py:1864:IMAGE_MODEL_PROVIDER = os.environ.get("IMAGE_MODEL_PROVIDER", "openai")
HEAD:backend/onyx/configs/app_configs.py:2127:# Whether tenant provisioning auto-creates LLMProvider rows seeded with the
HEAD:backend/onyx/configs/embedding_configs.py:22:_BASE_EMBEDDING_MODELS = [
HEAD:backend/onyx/configs/embedding_configs.py:143:SUPPORTED_EMBEDDING_MODELS = [
HEAD:backend/onyx/configs/embedding_configs.py:152:        for model in _BASE_EMBEDDING_MODELS
HEAD:backend/onyx/configs/embedding_configs.py:164:        for model in _BASE_EMBEDDING_MODELS
HEAD:backend/onyx/configs/kg_configs.py:93:_KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:95:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:97:_KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:99:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:101:_KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:103:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT", "0.5"))),
HEAD:backend/onyx/configs/kg_configs.py:105:_KG_NORMALIZATION_RERANK_NGRAM_SUMS: float = (
HEAD:backend/onyx/configs/kg_configs.py:106:    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:107:    + _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:108:    + _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:111:KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS: tuple[float, float, float] = (
HEAD:backend/onyx/configs/kg_configs.py:112:    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:113:    _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:114:    _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:118:KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:120:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:124:KG_NORMALIZATION_RERANK_THRESHOLD: float = float(
HEAD:backend/onyx/configs/kg_configs.py:125:    os.environ.get("KG_NORMALIZATION_RERANK_THRESHOLD", "0.3")
HEAD:backend/onyx/configs/model_configs.py:4:from shared_configs.configs import DEFAULT_DOCUMENT_ENCODER_MODEL
HEAD:backend/onyx/configs/model_configs.py:7:# Embedding/Reranking Model Configs
HEAD:backend/onyx/configs/model_configs.py:13:# https://huggingface.co/DOCUMENT_ENCODER_MODEL
HEAD:backend/onyx/configs/model_configs.py:17:DOCUMENT_ENCODER_MODEL = (
HEAD:backend/onyx/configs/model_configs.py:18:    os.environ.get("DOCUMENT_ENCODER_MODEL") or DEFAULT_DOCUMENT_ENCODER_MODEL
HEAD:backend/onyx/configs/model_configs.py:27:OLD_DEFAULT_DOCUMENT_ENCODER_MODEL = "thenlper/gte-small"
HEAD:backend/onyx/configs/model_configs.py:31:# These are only used if reranking is turned off, to normalize the direct retrieval scores for display
HEAD:backend/onyx/context/search/federated/slack_search.py:1285:        tokenizer=embedder.embedding_model.tokenizer,
HEAD:backend/onyx/context/search/models.py:46:            model_name=search_settings.model_name,
HEAD:backend/onyx/context/search/pipeline.py:281:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/pipeline.py:333:        embedding_model=embedding_model,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:55:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:60:        embedding_model=embedding_model,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:94:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:149:                    (query_request, document_index, db_session, embedding_model),
HEAD:backend/onyx/context/search/utils.py:29:from shared_configs.configs import MODEL_SERVER_HOST, MODEL_SERVER_PORT
HEAD:backend/onyx/context/search/utils.py:31:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/context/search/utils.py:87:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/utils.py:90:    if embedding_model is None:
HEAD:backend/onyx/context/search/utils.py:92:            raise ValueError("Either db_session or embedding_model must be provided")
HEAD:backend/onyx/context/search/utils.py:94:        embedding_model = EmbeddingModel.from_db_model(
HEAD:backend/onyx/context/search/utils.py:96:            server_host=MODEL_SERVER_HOST,
HEAD:backend/onyx/context/search/utils.py:97:            server_port=MODEL_SERVER_PORT,
HEAD:backend/onyx/context/search/utils.py:101:        # supplied an embedding_model.
HEAD:backend/onyx/context/search/utils.py:110:            record_cache_skipped(embedding_model.provider_type, count=len(queries))
HEAD:backend/onyx/context/search/utils.py:111:        result = embedding_model.encode(queries, text_type=EmbedTextType.QUERY)
HEAD:backend/onyx/context/search/utils.py:121:        provider_type=embedding_model.provider_type,
HEAD:backend/onyx/context/search/utils.py:134:    fresh_embeddings = embedding_model.encode(
HEAD:backend/onyx/context/search/utils.py:142:        provider_type=embedding_model.provider_type,
HEAD:backend/onyx/context/search/utils.py:162:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/utils.py:165:        [query], db_session=db_session, embedding_model=embedding_model
HEAD:backend/onyx/db/image_generation.py:4:from onyx.db.models import ImageGenerationConfig, LLMProvider, ModelConfiguration
HEAD:backend/onyx/db/image_generation.py:12:DEFAULT_IMAGE_MODEL_NAME = "gpt-image-1"
HEAD:backend/onyx/db/image_generation.py:169:    model_name: str = DEFAULT_IMAGE_MODEL_NAME,
HEAD:backend/onyx/db/image_generation.py:181:        model_name: Model name for image generation (default: gpt-image-1)
HEAD:backend/onyx/db/image_generation.py:195:        new_provider = LLMProvider(
HEAD:backend/onyx/db/image_generation.py:209:            model_name=model_name,
HEAD:backend/onyx/db/image_generation.py:210:            model_provider=provider,
HEAD:backend/onyx/db/image_generation.py:215:            name=model_name,
HEAD:backend/onyx/db/llm.py:14:    LLMProvider__Persona,
HEAD:backend/onyx/db/llm.py:15:    LLMProvider__UserGroup,
HEAD:backend/onyx/db/llm.py:23:from onyx.db.models import LLMProvider as LLMProviderModel
HEAD:backend/onyx/db/llm.py:37:    LLMProviderUpsertRequest,
HEAD:backend/onyx/db/llm.py:38:    LLMProviderView,
HEAD:backend/onyx/db/llm.py:58:    db_session.query(LLMProvider__UserGroup).filter(
HEAD:backend/onyx/db/llm.py:59:        LLMProvider__UserGroup.llm_provider_id == llm_provider_id
HEAD:backend/onyx/db/llm.py:65:            LLMProvider__UserGroup(
HEAD:backend/onyx/db/llm.py:81:        delete(LLMProvider__Persona).where(
HEAD:backend/onyx/db/llm.py:82:            LLMProvider__Persona.llm_provider_id == llm_provider_id
HEAD:backend/onyx/db/llm.py:88:            LLMProvider__Persona(
HEAD:backend/onyx/db/llm.py:119:    provider: LLMProviderModel,
HEAD:backend/onyx/db/llm.py:279:def upsert_cloud_embedding_provider(
HEAD:backend/onyx/db/llm.py:315:    llm_provider_upsert_request: LLMProviderUpsertRequest,
HEAD:backend/onyx/db/llm.py:317:) -> LLMProviderView:
HEAD:backend/onyx/db/llm.py:318:    existing_llm_provider: LLMProviderModel | None = None
HEAD:backend/onyx/db/llm.py:329:        existing_llm_provider = LLMProviderModel(name=llm_provider_upsert_request.name)
HEAD:backend/onyx/db/llm.py:503:                model_name=model_config.name,
HEAD:backend/onyx/db/llm.py:535:    full_llm_provider = LLMProviderView.from_model(existing_llm_provider)
HEAD:backend/onyx/db/llm.py:580:                model_name=model.name,
HEAD:backend/onyx/db/llm.py:615:def fetch_existing_embedding_providers(
HEAD:backend/onyx/db/llm.py:657:) -> list[LLMProviderModel]:
HEAD:backend/onyx/db/llm.py:667:    stmt = select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:676:        stmt = stmt.where(LLMProviderModel.id.in_(providers_with_flows))
HEAD:backend/onyx/db/llm.py:682:        stmt = stmt.where(~LLMProviderModel.id.in_(image_gen_provider_ids))
HEAD:backend/onyx/db/llm.py:685:        selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:686:        selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:687:        selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:700:) -> LLMProviderModel | None:
HEAD:backend/onyx/db/llm.py:707:        select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:708:        .where(LLMProviderModel.provider == provider_type)
HEAD:backend/onyx/db/llm.py:711:                LLMProviderModel.id,
HEAD:backend/onyx/db/llm.py:712:                LLMProviderModel.is_public,
HEAD:backend/onyx/db/llm.py:714:            selectinload(LLMProviderModel.groups).load_only(UserGroup.id),
HEAD:backend/onyx/db/llm.py:715:            selectinload(LLMProviderModel.personas).load_only(Persona.id),
HEAD:backend/onyx/db/llm.py:717:        .order_by(LLMProviderModel.id.asc())
HEAD:backend/onyx/db/llm.py:741:) -> list[LLMProviderView]:
HEAD:backend/onyx/db/llm.py:747:        select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:748:        .order_by(LLMProviderModel.id.asc())
HEAD:backend/onyx/db/llm.py:750:            selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:751:            selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:752:            selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:760:        LLMProviderView.from_model(p, include_api_key=False)
HEAD:backend/onyx/db/llm.py:770:) -> list[LLMProviderView]:
HEAD:backend/onyx/db/llm.py:785:    def is_accessible(provider: LLMProviderModel) -> bool:
HEAD:backend/onyx/db/llm.py:799:        LLMProviderView.from_model(provider, include_api_key=False)
HEAD:backend/onyx/db/llm.py:807:) -> LLMProviderModel | None:
HEAD:backend/onyx/db/llm.py:810:        select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:811:        .where(LLMProviderModel.name == name)
HEAD:backend/onyx/db/llm.py:812:        .order_by(LLMProviderModel.id)
HEAD:backend/onyx/db/llm.py:814:            selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:815:            selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:816:            selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:825:) -> LLMProviderModel | None:
HEAD:backend/onyx/db/llm.py:827:        select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:828:        .where(LLMProviderModel.id == id)
HEAD:backend/onyx/db/llm.py:830:            selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:831:            selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:832:            selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:841:) -> LLMProviderView | None:
HEAD:backend/onyx/db/llm.py:855:    return LLMProviderView.from_model(provider_model)
HEAD:backend/onyx/db/llm.py:860:) -> LLMProviderModel | None:
HEAD:backend/onyx/db/llm.py:869:            select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:871:                LLMProviderModel.name == name,
HEAD:backend/onyx/db/llm.py:872:                LLMProviderModel.provider == provider_type,
HEAD:backend/onyx/db/llm.py:875:                selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:876:                selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:877:                selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:894:) -> LLMProviderModel | None:
HEAD:backend/onyx/db/llm.py:902:            select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:904:                LLMProviderModel.provider == provider_type,
HEAD:backend/onyx/db/llm.py:905:                LLMProviderModel.name.is_(None),
HEAD:backend/onyx/db/llm.py:908:                selectinload(LLMProviderModel.model_configurations),
HEAD:backend/onyx/db/llm.py:909:                selectinload(LLMProviderModel.groups),
HEAD:backend/onyx/db/llm.py:910:                selectinload(LLMProviderModel.personas),
HEAD:backend/onyx/db/llm.py:924:def fetch_embedding_provider(
HEAD:backend/onyx/db/llm.py:1010:) -> LLMProviderView | None:
HEAD:backend/onyx/db/llm.py:1016:    return LLMProviderView.from_model(provider_model)
HEAD:backend/onyx/db/llm.py:1019:def remove_embedding_provider(
HEAD:backend/onyx/db/llm.py:1039:    provider = db_session.get(LLMProviderModel, provider_id)
HEAD:backend/onyx/db/llm.py:1070:        delete(LLMProvider__UserGroup).where(
HEAD:backend/onyx/db/llm.py:1071:            LLMProvider__UserGroup.llm_provider_id == provider_id
HEAD:backend/onyx/db/llm.py:1075:        delete(LLMProviderModel).where(LLMProviderModel.id == provider_id)
HEAD:backend/onyx/db/llm.py:1084:    provider_id: int, model_name: str, db_session: Session
HEAD:backend/onyx/db/llm.py:1089:        model_name,
HEAD:backend/onyx/db/llm.py:1098:        select(LLMProviderModel).where(
HEAD:backend/onyx/db/llm.py:1099:            LLMProviderModel.id == provider_id,
HEAD:backend/onyx/db/llm.py:1125:        select(LLMProviderModel).where(
HEAD:backend/onyx/db/llm.py:1126:            LLMProviderModel.id == provider_id,
HEAD:backend/onyx/db/llm.py:1142:    provider_id: int, model_name: str, db_session: Session
HEAD:backend/onyx/db/llm.py:1149:            ModelConfiguration.name == model_name,
HEAD:backend/onyx/db/llm.py:1154:            f"Model '{model_name}' is not a valid model for provider_id={provider_id}"
HEAD:backend/onyx/db/llm.py:1167:        model_name,
HEAD:backend/onyx/db/llm.py:1245:def fetch_auto_mode_providers(db_session: Session) -> list[LLMProviderModel]:
HEAD:backend/onyx/db/llm.py:1248:        select(LLMProviderModel)
HEAD:backend/onyx/db/llm.py:1249:        .where(LLMProviderModel.is_auto_mode.is_(True))
HEAD:backend/onyx/db/llm.py:1250:        .options(selectinload(LLMProviderModel.model_configurations))
HEAD:backend/onyx/db/llm.py:1257:    provider: LLMProviderModel,
HEAD:backend/onyx/db/llm.py:1284:    recommended_visible_model_names = [
HEAD:backend/onyx/db/llm.py:1319:                model_name=model_config.name,
HEAD:backend/onyx/db/llm.py:1366:        name for name in existing_models if name not in recommended_visible_model_names
HEAD:backend/onyx/db/llm.py:1449:    model_name: str,
HEAD:backend/onyx/db/llm.py:1463:            name=model_name,
HEAD:backend/onyx/db/models.py:2256:    model_name: Mapped[str] = mapped_column(String)
HEAD:backend/onyx/db/models.py:2267:        ForeignKey("embedding_provider.provider_type"), nullable=True
HEAD:backend/onyx/db/models.py:2351:            "ix_embedding_model_present_unique",
HEAD:backend/onyx/db/models.py:2357:            "ix_embedding_model_future_unique",
HEAD:backend/onyx/db/models.py:2371:        return f"<EmbeddingModel(model_name='{self.model_name}', status='{self.status}',\
HEAD:backend/onyx/db/models.py:2407:            self.multipass_indexing, self.model_name, self.provider_type
HEAD:backend/onyx/db/models.py:2416:        multipass: bool, model_name: str, provider_type: EmbeddingProvider | None
HEAD:backend/onyx/db/models.py:2426:            and model_name.startswith("nomic-ai")
HEAD:backend/onyx/db/models.py:3610:class LLMProvider(Base):
HEAD:backend/onyx/db/models.py:3628:    default_model_name: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:3718:    llm_provider: Mapped["LLMProvider"] = relationship(
HEAD:backend/onyx/db/models.py:3719:        "LLMProvider",
HEAD:backend/onyx/db/models.py:3853:    __tablename__ = "embedding_provider"
HEAD:backend/onyx/db/models.py:4298:    allowed_by_llm_providers: Mapped[list["LLMProvider"]] = relationship(
HEAD:backend/onyx/db/models.py:4299:        "LLMProvider",
HEAD:backend/onyx/db/models.py:5139:class LLMProvider__Persona(Base):
HEAD:backend/onyx/db/models.py:5155:class LLMProvider__UserGroup(Base):
HEAD:backend/onyx/db/search_settings.py:6:    DEFAULT_DOCUMENT_ENCODER_MODEL,
HEAD:backend/onyx/db/search_settings.py:7:    DOCUMENT_ENCODER_MODEL,
HEAD:backend/onyx/db/search_settings.py:10:from onyx.db.llm import fetch_embedding_provider
HEAD:backend/onyx/db/search_settings.py:56:    embedding_model = SearchSettings(
HEAD:backend/onyx/db/search_settings.py:57:        model_name=search_settings.model_name,
HEAD:backend/onyx/db/search_settings.py:79:    db_session.add(embedding_model)
HEAD:backend/onyx/db/search_settings.py:85:    return embedding_model
HEAD:backend/onyx/db/search_settings.py:88:def get_embedding_provider_from_provider_type(
HEAD:backend/onyx/db/search_settings.py:98:def get_current_db_embedding_provider(
HEAD:backend/onyx/db/search_settings.py:106:    embedding_provider = fetch_embedding_provider(
HEAD:backend/onyx/db/search_settings.py:110:    if embedding_provider is None:
HEAD:backend/onyx/db/search_settings.py:113:    current_embedding_provider = ServerCloudEmbeddingProvider.from_request(
HEAD:backend/onyx/db/search_settings.py:114:        cloud_provider_model=embedding_provider
HEAD:backend/onyx/db/search_settings.py:117:    return current_embedding_provider
HEAD:backend/onyx/db/search_settings.py:285:def user_has_overridden_embedding_model() -> bool:
HEAD:backend/onyx/db/search_settings.py:286:    return DOCUMENT_ENCODER_MODEL != DEFAULT_DOCUMENT_ENCODER_MODEL
HEAD:backend/onyx/deep_research/dr_loop.py:422:                llm.config.model_name, llm.config.model_provider
HEAD:backend/onyx/document_index/disabled.py:21:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/document_index_utils.py:38:        multipass, search_settings.model_name, search_settings.provider_type
HEAD:backend/onyx/document_index/interfaces_new.py:15:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/opensearch/constants.py:38:# as the final 10 (worse than just a miss at the reranking step).
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:74:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/opensearch/port_copy.py:50:        model_name=future_search_settings.model_name,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:66:        model_name=llm.config.model_name,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:67:        provider_type=llm.config.model_provider,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:185:            model_name=present_search_settings.model_name,
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:282:            rerank-count: 1000
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:351:            rerank-count: 1000
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:23:    RERANK_COUNT,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:96:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:913:        # Avoid over-fetching a very large candidate set for global-phase reranking.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:915:        target_hits = min(max(4 * num_to_retrieve, 100), RERANK_COUNT)
HEAD:backend/onyx/evals/README.md:83:- `model_provider`: Model provider (e.g., "openai", "anthropic")
HEAD:backend/onyx/evals/README.md:103:    "model_provider": "anthropic"
HEAD:backend/onyx/evals/README.md:146:- `model_provider`: Model provider override for this turn
HEAD:backend/onyx/evals/eval.py:162:            - 'model_provider' (optional): Model provider (e.g., "openai", "anthropic")
HEAD:backend/onyx/evals/eval.py:201:            input_model_provider = eval_input.get("model_provider")
HEAD:backend/onyx/evals/eval.py:204:            if input_model or input_model_provider or input_temperature is not None:
HEAD:backend/onyx/evals/eval.py:207:                    model_provider=input_model_provider or llm_override.model_provider,
HEAD:backend/onyx/evals/eval.py:282:                - 'model_provider' (optional): Provider override for this turn
HEAD:backend/onyx/evals/eval.py:301:            model_provider=msg_data.get("model_provider"),
HEAD:backend/onyx/evals/eval.py:366:                if msg.model or msg.model_provider or msg.temperature is not None:
HEAD:backend/onyx/evals/eval.py:368:                        model_provider=msg.model_provider
HEAD:backend/onyx/evals/eval.py:369:                        or llm_override.model_provider,
HEAD:backend/onyx/evals/models.py:64:    model_provider: str | None = None
HEAD:backend/onyx/evals/models.py:88:        model_provider=None,
HEAD:backend/onyx/evals/providers/braintrust.py:140:                            "model_provider": item.get("model_provider"),
HEAD:backend/onyx/evals/providers/local.py:153:            "model_provider": item.get("model_provider"),
HEAD:backend/onyx/external_apps/presentation/payload_decoders.py:67:    """base64url-decode, restoring the padding Gmail's encoder strips."""
HEAD:backend/onyx/federated_connectors/models.py:66:    # Pydantic V2 automatically serializes datetime to ISO format, so no custom encoder needed
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:19:    _DALL_E_2_MODEL_NAME = "dall-e-2"
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:71:    def _normalize_model_name(self, model: str) -> str:
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:75:        normalized_model = self._normalize_model_name(model)
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:78:            or normalized_model == self._DALL_E_2_MODEL_NAME
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:92:        model_name = f"azure/{deployment}"
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:100:            normalized_model = self._normalize_model_name(model)
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:102:                normalized_model == self._DALL_E_2_MODEL_NAME
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:121:                    model=model_name,
HEAD:backend/onyx/image_gen/providers/azure_img_gen.py:142:                model=model_name,
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:19:    _DALL_E_2_MODEL_NAME = "dall-e-2"
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:57:    def _normalize_model_name(self, model: str) -> str:
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:61:        normalized_model = self._normalize_model_name(model)
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:64:            or normalized_model == self._DALL_E_2_MODEL_NAME
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:77:        normalized_model = self._normalize_model_name(model)
HEAD:backend/onyx/image_gen/providers/openai_img_gen.py:89:                normalized_model == self._DALL_E_2_MODEL_NAME
HEAD:backend/onyx/image_gen/providers/vertex_img_gen.py:175:        model_name = model.replace("vertex_ai/", "")
HEAD:backend/onyx/image_gen/providers/vertex_img_gen.py:178:            model=model_name,
HEAD:backend/onyx/image_gen/providers/vertex_img_gen.py:184:                model=model_name,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:182:                model_name=llm.config.model_name,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:183:                provider_type=llm.config.model_provider,
HEAD:backend/onyx/indexing/embedder.py:23:    INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/indexing/embedder.py:24:    INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/indexing/embedder.py:27:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/indexing/embedder.py:38:        model_name: str,
HEAD:backend/onyx/indexing/embedder.py:50:        self.model_name = model_name
HEAD:backend/onyx/indexing/embedder.py:60:        self.embedding_model = EmbeddingModel(
HEAD:backend/onyx/indexing/embedder.py:61:            model_name=model_name,
HEAD:backend/onyx/indexing/embedder.py:72:            server_host=INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/indexing/embedder.py:73:            server_port=INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/indexing/embedder.py:91:        model_name: str,
HEAD:backend/onyx/indexing/embedder.py:104:            model_name,
HEAD:backend/onyx/indexing/embedder.py:152:        embeddings = self.embedding_model.encode(
HEAD:backend/onyx/indexing/embedder.py:172:            title_embeddings = self.embedding_model.encode(
HEAD:backend/onyx/indexing/embedder.py:209:                    title_embedding = self.embedding_model.encode(
HEAD:backend/onyx/indexing/embedder.py:237:            model_name=search_settings.model_name,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1474:            model_name=llm.config.model_name,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1475:            provider_type=llm.config.model_provider,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1700:        tokenizer=embedder.embedding_model.tokenizer,
HEAD:backend/onyx/indexing/models.py:13:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/indexing/models.py:148:    model_name: str
HEAD:backend/onyx/indexing/models.py:173:            model_name=search_settings.model_name,
HEAD:backend/onyx/indexing/models.py:216:            model_name=search_settings.model_name,
HEAD:backend/onyx/kg/clustering/normalizations.py:11:    KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT,
HEAD:backend/onyx/kg/clustering/normalizations.py:12:    KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS,
HEAD:backend/onyx/kg/clustering/normalizations.py:13:    KG_NORMALIZATION_RERANK_THRESHOLD,
HEAD:backend/onyx/kg/clustering/normalizations.py:150:    # step 2: do a weighted ngram analysis and damerau levenshtein distance to rerank
HEAD:backend/onyx/kg/clustering/normalizations.py:166:        W_n1, W_n2, W_n3 = KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS
HEAD:backend/onyx/kg/clustering/normalizations.py:175:        W_leven = KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT
HEAD:backend/onyx/kg/clustering/normalizations.py:183:            filter(lambda x: x[2] > KG_NORMALIZATION_RERANK_THRESHOLD, candidates),
HEAD:backend/onyx/kg/utils/embeddings.py:11:from shared_configs.configs import MODEL_SERVER_HOST, MODEL_SERVER_PORT
HEAD:backend/onyx/kg/utils/embeddings.py:19:            server_host=MODEL_SERVER_HOST,
HEAD:backend/onyx/kg/utils/embeddings.py:20:            server_port=MODEL_SERVER_PORT,
HEAD:backend/onyx/llm/api_surfaces.py:10:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/llm/api_surfaces.py:38:    LlmProviderNames.OPENAI_COMPATIBLE: LlmApiSurface.OPENAI_CHAT_COMPLETIONS,
HEAD:backend/onyx/llm/api_surfaces.py:39:    LlmProviderNames.NEBIUS_TOKENFACTORY: LlmApiSurface.OPENAI_CHAT_COMPLETIONS,
HEAD:backend/onyx/llm/api_surfaces.py:44:    LlmProviderNames.PORTKEY: (
HEAD:backend/onyx/llm/api_surfaces.py:55:    LlmProviderNames.BIFROST: (
HEAD:backend/onyx/llm/api_surfaces.py:72:    model_provider: str, custom_config: dict[str, str] | None
HEAD:backend/onyx/llm/api_surfaces.py:76:    selectable = _SELECTABLE_SURFACES.get(model_provider)
HEAD:backend/onyx/llm/api_surfaces.py:81:    return _STATIC_SURFACES.get(model_provider)
HEAD:backend/onyx/llm/constants.py:11:class LlmProviderNames(str, Enum):
HEAD:backend/onyx/llm/constants.py:36:        f"{LlmProviderNames.OPENAI}/" gives back "openai/" instead of "LlmProviderNames.OPENAI/"
HEAD:backend/onyx/llm/constants.py:42:    LlmProviderNames.OPENAI,
HEAD:backend/onyx/llm/constants.py:43:    LlmProviderNames.ANTHROPIC,
HEAD:backend/onyx/llm/constants.py:44:    LlmProviderNames.VERTEX_AI,
HEAD:backend/onyx/llm/constants.py:45:    LlmProviderNames.BEDROCK,
HEAD:backend/onyx/llm/constants.py:46:    LlmProviderNames.OPENROUTER,
HEAD:backend/onyx/llm/constants.py:47:    LlmProviderNames.AZURE,
HEAD:backend/onyx/llm/constants.py:48:    LlmProviderNames.OLLAMA_CHAT,
HEAD:backend/onyx/llm/constants.py:49:    LlmProviderNames.LM_STUDIO,
HEAD:backend/onyx/llm/constants.py:50:    LlmProviderNames.LITELLM_PROXY,
HEAD:backend/onyx/llm/constants.py:51:    LlmProviderNames.BIFROST,
HEAD:backend/onyx/llm/constants.py:52:    LlmProviderNames.OPENAI_COMPATIBLE,
HEAD:backend/onyx/llm/constants.py:53:    LlmProviderNames.NEBIUS_TOKENFACTORY,
HEAD:backend/onyx/llm/constants.py:54:    LlmProviderNames.PORTKEY,
HEAD:backend/onyx/llm/constants.py:60:    LlmProviderNames.OPENAI: "OpenAI",
HEAD:backend/onyx/llm/constants.py:61:    LlmProviderNames.ANTHROPIC: "Anthropic",
HEAD:backend/onyx/llm/constants.py:62:    LlmProviderNames.GOOGLE: "Google",
HEAD:backend/onyx/llm/constants.py:63:    LlmProviderNames.BEDROCK: "Bedrock",
HEAD:backend/onyx/llm/constants.py:64:    LlmProviderNames.BEDROCK_CONVERSE: "Bedrock",
HEAD:backend/onyx/llm/constants.py:65:    LlmProviderNames.VERTEX_AI: "Vertex AI",
HEAD:backend/onyx/llm/constants.py:66:    LlmProviderNames.OPENROUTER: "OpenRouter",
HEAD:backend/onyx/llm/constants.py:67:    LlmProviderNames.AZURE: "Azure",
HEAD:backend/onyx/llm/constants.py:69:    LlmProviderNames.OLLAMA_CHAT: "Ollama",
HEAD:backend/onyx/llm/constants.py:70:    LlmProviderNames.LM_STUDIO: "LM Studio",
HEAD:backend/onyx/llm/constants.py:71:    LlmProviderNames.LITELLM_PROXY: "LiteLLM Proxy",
HEAD:backend/onyx/llm/constants.py:72:    LlmProviderNames.BIFROST: "Bifrost",
HEAD:backend/onyx/llm/constants.py:73:    LlmProviderNames.OPENAI_COMPATIBLE: "OpenAI-Compatible",
HEAD:backend/onyx/llm/constants.py:74:    LlmProviderNames.NEBIUS_TOKENFACTORY: "Nebius TokenFactory",
HEAD:backend/onyx/llm/constants.py:75:    LlmProviderNames.PORTKEY: "Portkey",
HEAD:backend/onyx/llm/constants.py:80:    LlmProviderNames.MISTRAL: "Mistral",
HEAD:backend/onyx/llm/constants.py:157:    LlmProviderNames.BEDROCK,
HEAD:backend/onyx/llm/constants.py:158:    LlmProviderNames.BEDROCK_CONVERSE,
HEAD:backend/onyx/llm/constants.py:159:    LlmProviderNames.OPENROUTER,
HEAD:backend/onyx/llm/constants.py:160:    LlmProviderNames.OLLAMA_CHAT,
HEAD:backend/onyx/llm/constants.py:161:    LlmProviderNames.LM_STUDIO,
HEAD:backend/onyx/llm/constants.py:162:    LlmProviderNames.VERTEX_AI,
HEAD:backend/onyx/llm/constants.py:163:    LlmProviderNames.AZURE,
HEAD:backend/onyx/llm/constants.py:164:    LlmProviderNames.LITELLM_PROXY,
HEAD:backend/onyx/llm/constants.py:165:    LlmProviderNames.BIFROST,
HEAD:backend/onyx/llm/constants.py:166:    LlmProviderNames.OPENAI_COMPATIBLE,
HEAD:backend/onyx/llm/constants.py:167:    LlmProviderNames.NEBIUS_TOKENFACTORY,
HEAD:backend/onyx/llm/constants.py:168:    LlmProviderNames.PORTKEY,
HEAD:backend/onyx/llm/constants.py:175:        LlmProviderNames.OPENROUTER,
HEAD:backend/onyx/llm/constants.py:176:        LlmProviderNames.BEDROCK,
HEAD:backend/onyx/llm/constants.py:177:        LlmProviderNames.OLLAMA_CHAT,
HEAD:backend/onyx/llm/constants.py:178:        LlmProviderNames.LM_STUDIO,
HEAD:backend/onyx/llm/constants.py:179:        LlmProviderNames.BIFROST,
HEAD:backend/onyx/llm/constants.py:180:        LlmProviderNames.OPENAI_COMPATIBLE,
HEAD:backend/onyx/llm/constants.py:186:BEDROCK_MODEL_NAME_MAPPINGS: dict[str, str] = {
HEAD:backend/onyx/llm/constants.py:199:OLLAMA_MODEL_NAME_MAPPINGS: dict[str, str] = {
HEAD:backend/onyx/llm/constants.py:303:HYPHENATED_MODEL_NAMES: set[str] = {
HEAD:backend/onyx/llm/custom_config_mapping.py:14:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/llm/custom_config_mapping.py:55:    LlmProviderNames.BEDROCK: _BEDROCK_CUSTOM_CONFIG_KWARGS,
HEAD:backend/onyx/llm/custom_config_mapping.py:56:    LlmProviderNames.BEDROCK_CONVERSE: _BEDROCK_CUSTOM_CONFIG_KWARGS,
HEAD:backend/onyx/llm/custom_config_mapping.py:57:    LlmProviderNames.LM_STUDIO: {LM_STUDIO_API_KEY_CONFIG_KEY: "api_key"},
HEAD:backend/onyx/llm/custom_config_mapping.py:58:    LlmProviderNames.AZURE: {
HEAD:backend/onyx/llm/custom_config_mapping.py:114:    model_provider: str,
HEAD:backend/onyx/llm/custom_config_mapping.py:132:    if model_provider == LlmProviderNames.VERTEX_AI:
HEAD:backend/onyx/llm/custom_config_mapping.py:138:    provider_kwargs = _PROVIDER_CUSTOM_CONFIG_KWARGS.get(model_provider, {})
HEAD:backend/onyx/llm/custom_config_mapping.py:145:    provider_normalized = _normalize_key(model_provider)
HEAD:backend/onyx/llm/custom_config_mapping.py:163:    model_provider: str,
HEAD:backend/onyx/llm/custom_config_mapping.py:170:        model_provider=model_provider,
HEAD:backend/onyx/llm/factory.py:20:from onyx.db.models import LLMProvider as LLMProviderModel
HEAD:backend/onyx/llm/factory.py:22:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/llm/factory.py:35:from onyx.server.manage.llm.models import LLMProviderView, ModelConfigurationView
HEAD:backend/onyx/llm/factory.py:59:    elif provider == LlmProviderNames.OPENROUTER:
HEAD:backend/onyx/llm/factory.py:69:    llm_provider: LLMProviderView,
HEAD:backend/onyx/llm/factory.py:70:    model_name: str,
HEAD:backend/onyx/llm/factory.py:73:        if model_configuration.name == model_name:
HEAD:backend/onyx/llm/factory.py:84:        provider == LlmProviderNames.OLLAMA_CHAT
HEAD:backend/onyx/llm/factory.py:98:) -> tuple[LLMProviderModel, str] | None:
HEAD:backend/onyx/llm/factory.py:99:    """Resolve the (provider, model_name) pair for get_llm_for_persona.
HEAD:backend/onyx/llm/factory.py:126:            model_name: str | None = model_version_override
HEAD:backend/onyx/llm/factory.py:131:            model_name = mc.name if mc else None
HEAD:backend/onyx/llm/factory.py:133:            model_name = None
HEAD:backend/onyx/llm/factory.py:147:        model_name = model_version_override or model_config.name
HEAD:backend/onyx/llm/factory.py:149:    if not provider_model or not model_name:
HEAD:backend/onyx/llm/factory.py:151:    return provider_model, model_name
HEAD:backend/onyx/llm/factory.py:176:    provider_name_override = llm_override.model_provider if llm_override else None
HEAD:backend/onyx/llm/factory.py:231:        llm_provider = LLMProviderView.from_model(provider_model)
HEAD:backend/onyx/llm/factory.py:234:        model_name=model,
HEAD:backend/onyx/llm/factory.py:255:    def create_vision_llm(provider: LLMProviderView, model: str) -> LLM:
HEAD:backend/onyx/llm/factory.py:258:            model_name=model,
HEAD:backend/onyx/llm/factory.py:281:                    LLMProviderView.from_model(default_model.llm_provider),
HEAD:backend/onyx/llm/factory.py:307:                provider_map[model.llm_provider_id] = LLMProviderView.from_model(
HEAD:backend/onyx/llm/factory.py:349:    model_name: str,
HEAD:backend/onyx/llm/factory.py:350:    llm_provider: LLMProviderView,
HEAD:backend/onyx/llm/factory.py:358:        llm_provider=llm_provider, model_name=model_name
HEAD:backend/onyx/llm/factory.py:371:            llm_provider=llm_provider, model_name=model_name
HEAD:backend/onyx/llm/factory.py:385:        model=model_name,
HEAD:backend/onyx/llm/factory.py:422:            model_name=mc.name,
HEAD:backend/onyx/llm/factory.py:423:            llm_provider=LLMProviderView.from_model(mc.llm_provider),
HEAD:backend/onyx/llm/factory.py:454:            model_name=model.name,
HEAD:backend/onyx/llm/factory.py:455:            llm_provider=LLMProviderView.from_model(model.llm_provider),
HEAD:backend/onyx/llm/factory.py:505:        model_provider=provider,
HEAD:backend/onyx/llm/factory.py:506:        model_name=model,
HEAD:backend/onyx/llm/factory.py:532:    llm_provider = llm.config.model_provider
HEAD:backend/onyx/llm/factory.py:533:    llm_model_name = llm.config.model_name
HEAD:backend/onyx/llm/factory.py:536:        model_name=llm_model_name,
HEAD:backend/onyx/llm/interfaces.py:33:class LLMConfig(BaseModel):
HEAD:backend/onyx/llm/interfaces.py:34:    model_provider: str
HEAD:backend/onyx/llm/interfaces.py:35:    model_name: str
HEAD:backend/onyx/llm/interfaces.py:87:    def config(self) -> LLMConfig:
HEAD:backend/onyx/llm/litellm_singleton/config.py:153:            from onyx.llm.model_name_parser import parse_litellm_model_name
HEAD:backend/onyx/llm/litellm_singleton/config.py:155:            parse_litellm_model_name.cache_clear()
HEAD:backend/onyx/llm/model_capabilities.py:8:Helpers that layer DB or `LLMProviderView` lookups on top of these live in
HEAD:backend/onyx/llm/model_capabilities.py:27:from onyx.llm.constants import BEDROCK_MODEL_TOKEN_LIMITS, LlmProviderNames
HEAD:backend/onyx/llm/model_capabilities.py:34:_TWELVE_LABS_PEGASUS_MODEL_NAMES = [
HEAD:backend/onyx/llm/model_capabilities.py:42:    model_name: {
HEAD:backend/onyx/llm/model_capabilities.py:49:    for model_name in _TWELVE_LABS_PEGASUS_MODEL_NAMES
HEAD:backend/onyx/llm/model_capabilities.py:78:    for model_name, model_metadata in CUSTOM_LITELLM_MODEL_OVERRIDES.items():
HEAD:backend/onyx/llm/model_capabilities.py:79:        if model_name in starting_map:
HEAD:backend/onyx/llm/model_capabilities.py:81:        starting_map[model_name] = copy.deepcopy(model_metadata)
HEAD:backend/onyx/llm/model_capabilities.py:89:    # for model_name in [
HEAD:backend/onyx/llm/model_capabilities.py:96:    #     starting_map[f"ollama/{model_name}"] = {
HEAD:backend/onyx/llm/model_capabilities.py:105:def _strip_extra_provider_from_model_name(model_name: str) -> str:
HEAD:backend/onyx/llm/model_capabilities.py:106:    return model_name.split("/")[1] if "/" in model_name else model_name
HEAD:backend/onyx/llm/model_capabilities.py:109:def _strip_colon_from_model_name(model_name: str) -> str:
HEAD:backend/onyx/llm/model_capabilities.py:110:    return ":".join(model_name.split(":")[:-1]) if ":" in model_name else model_name
HEAD:backend/onyx/llm/model_capabilities.py:113:def find_model_obj(model_map: dict, provider: str, model_name: str) -> dict | None:
HEAD:backend/onyx/llm/model_capabilities.py:114:    stripped_model_name = _strip_extra_provider_from_model_name(model_name)
HEAD:backend/onyx/llm/model_capabilities.py:116:    model_names = [
HEAD:backend/onyx/llm/model_capabilities.py:117:        model_name,
HEAD:backend/onyx/llm/model_capabilities.py:118:        _strip_extra_provider_from_model_name(model_name),
HEAD:backend/onyx/llm/model_capabilities.py:122:        _strip_colon_from_model_name(model_name),
HEAD:backend/onyx/llm/model_capabilities.py:123:        _strip_colon_from_model_name(stripped_model_name),
HEAD:backend/onyx/llm/model_capabilities.py:127:    filtered_model_names = [name for name in model_names if name]
HEAD:backend/onyx/llm/model_capabilities.py:130:    for model_name in filtered_model_names:
HEAD:backend/onyx/llm/model_capabilities.py:131:        model_obj = model_map.get(f"{provider}/{model_name}")
HEAD:backend/onyx/llm/model_capabilities.py:136:    for model_name in filtered_model_names:
HEAD:backend/onyx/llm/model_capabilities.py:137:        model_obj = model_map.get(model_name)
HEAD:backend/onyx/llm/model_capabilities.py:146:    model_name: str,
HEAD:backend/onyx/llm/model_capabilities.py:147:    model_provider: str,
HEAD:backend/onyx/llm/model_capabilities.py:157:        model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:158:        model_name,
HEAD:backend/onyx/llm/model_capabilities.py:163:            model_name,
HEAD:backend/onyx/llm/model_capabilities.py:178:        model_name,
HEAD:backend/onyx/llm/model_capabilities.py:186:    model_name: str,
HEAD:backend/onyx/llm/model_capabilities.py:187:    model_provider: str,
HEAD:backend/onyx/llm/model_capabilities.py:192:    model_obj = find_model_obj(model_map, model_provider, model_name)
HEAD:backend/onyx/llm/model_capabilities.py:197:            model_name,
HEAD:backend/onyx/llm/model_capabilities.py:213:        model_name,
HEAD:backend/onyx/llm/model_capabilities.py:220:    model_name: str,
HEAD:backend/onyx/llm/model_capabilities.py:221:    model_provider: str,
HEAD:backend/onyx/llm/model_capabilities.py:234:            model_name=model_name,
HEAD:backend/onyx/llm/model_capabilities.py:235:            model_provider=model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:296:    model_name: str, model_provider: str
HEAD:backend/onyx/llm/model_capabilities.py:302:        model_obj = find_model_obj(get_model_map(), model_provider, model_name)
HEAD:backend/onyx/llm/model_capabilities.py:306:                model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:307:                model_name,
HEAD:backend/onyx/llm/model_capabilities.py:314:            "Failed to get model object for %s/%s", model_provider, model_name
HEAD:backend/onyx/llm/model_capabilities.py:333:def _reasoning_cache_key(full_model_name: str) -> str:
HEAD:backend/onyx/llm/model_capabilities.py:334:    return f"{get_current_tenant_id()}:{full_model_name}"
HEAD:backend/onyx/llm/model_capabilities.py:347:def _litellm_supports_reasoning(full_model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:354:    cache_key = _reasoning_cache_key(full_model_name)
HEAD:backend/onyx/llm/model_capabilities.py:371:            result = bool(litellm.supports_reasoning(model=full_model_name))
HEAD:backend/onyx/llm/model_capabilities.py:374:                "Failed to check if %s supports reasoning", full_model_name
HEAD:backend/onyx/llm/model_capabilities.py:382:def model_is_reasoning_model(model_name: str, model_provider: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:387:            model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:388:            model_name,
HEAD:backend/onyx/llm/model_capabilities.py:396:                model_name,
HEAD:backend/onyx/llm/model_capabilities.py:397:                model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:401:        full_model_name = (
HEAD:backend/onyx/llm/model_capabilities.py:402:            f"{model_provider}/{model_name}"
HEAD:backend/onyx/llm/model_capabilities.py:403:            if model_provider not in model_name
HEAD:backend/onyx/llm/model_capabilities.py:404:            else model_name
HEAD:backend/onyx/llm/model_capabilities.py:406:        return _litellm_supports_reasoning(full_model_name)
HEAD:backend/onyx/llm/model_capabilities.py:410:            "Failed to get model object for %s/%s", model_provider, model_name
HEAD:backend/onyx/llm/model_capabilities.py:423:def openai_model_rejects_reasoning_effort(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:430:    base_model_name = model_name.lower().split("/")[-1]
HEAD:backend/onyx/llm/model_capabilities.py:431:    return base_model_name.startswith(_OPENAI_MODELS_REJECTING_REASONING_EFFORT)
HEAD:backend/onyx/llm/model_capabilities.py:437:    {LlmProviderNames.OPENAI, LlmProviderNames.LITELLM_PROXY, LlmProviderNames.AZURE}
HEAD:backend/onyx/llm/model_capabilities.py:441:def is_true_openai_model(model_provider: str, model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:452:    if model_provider not in OPENAI_API_PROVIDERS:
HEAD:backend/onyx/llm/model_capabilities.py:457:    def _check_if_model_name_is_openai_provider(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:458:        if model_name not in model_map:
HEAD:backend/onyx/llm/model_capabilities.py:460:        return model_map[model_name].get("litellm_provider") == LlmProviderNames.OPENAI
HEAD:backend/onyx/llm/model_capabilities.py:465:        if f"{LlmProviderNames.OPENAI}/{model_name}" in model_map:
HEAD:backend/onyx/llm/model_capabilities.py:468:        if _check_if_model_name_is_openai_provider(model_name):
HEAD:backend/onyx/llm/model_capabilities.py:471:        if model_name.startswith(f"{LlmProviderNames.AZURE}/"):
HEAD:backend/onyx/llm/model_capabilities.py:472:            model_name_with_azure_removed = "/".join(model_name.split("/")[1:])
HEAD:backend/onyx/llm/model_capabilities.py:473:            if _check_if_model_name_is_openai_provider(model_name_with_azure_removed):
HEAD:backend/onyx/llm/model_capabilities.py:481:            model_provider,
HEAD:backend/onyx/llm/model_capabilities.py:482:            model_name,
HEAD:backend/onyx/llm/model_capabilities.py:487:def is_openai_registry_model_name(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:495:    base_model_name = model_name.split("/")[-1]
HEAD:backend/onyx/llm/model_capabilities.py:496:    if not base_model_name:
HEAD:backend/onyx/llm/model_capabilities.py:501:        if f"{LlmProviderNames.OPENAI}/{base_model_name}" in model_map:
HEAD:backend/onyx/llm/model_capabilities.py:503:        entry = model_map.get(base_model_name)
HEAD:backend/onyx/llm/model_capabilities.py:504:        return bool(entry) and entry.get("litellm_provider") == LlmProviderNames.OPENAI
HEAD:backend/onyx/llm/model_capabilities.py:506:        logger.exception("Failed to check %s against the OpenAI registry", model_name)
HEAD:backend/onyx/llm/model_capabilities.py:510:def openai_chat_variant_rejects_reasoning(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:514:    return "-chat" in model_name and is_openai_registry_model_name(model_name)
HEAD:backend/onyx/llm/model_capabilities.py:528:def parse_openai_gpt_version(model_name: str) -> tuple[int, int] | None:
HEAD:backend/onyx/llm/model_capabilities.py:531:    match = _OPENAI_GPT_VERSION_PATTERN.search(model_name.lower())
HEAD:backend/onyx/llm/model_capabilities.py:540:def openai_chat_tools_require_reasoning_none(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:544:    version = parse_openai_gpt_version(model_name)
HEAD:backend/onyx/llm/model_capabilities.py:572:def parse_anthropic_model_version(model_name: str) -> tuple[int, int] | None:
HEAD:backend/onyx/llm/model_capabilities.py:582:    name = model_name.lower()
HEAD:backend/onyx/llm/model_capabilities.py:611:def _anthropic_meets_version(model_name: str, min_version: tuple[int, int]) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:612:    version = parse_anthropic_model_version(model_name)
HEAD:backend/onyx/llm/model_capabilities.py:616:def anthropic_uses_adaptive_thinking(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:618:        model_name, _ANTHROPIC_ADAPTIVE_THINKING_MIN_VERSION
HEAD:backend/onyx/llm/model_capabilities.py:622:def anthropic_supports_thinking(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:623:    return _anthropic_meets_version(model_name, _ANTHROPIC_THINKING_MIN_VERSION)
HEAD:backend/onyx/llm/model_capabilities.py:626:def anthropic_omits_sampling_params(model_name: str) -> bool:
HEAD:backend/onyx/llm/model_capabilities.py:628:        model_name, _ANTHROPIC_ADAPTIVE_THINKING_MIN_VERSION
HEAD:backend/onyx/llm/model_capabilities.py:632:def model_identity_names(model_name: str, deployment_name: str | None) -> list[str]:
HEAD:backend/onyx/llm/model_capabilities.py:633:    """Every string that could carry a model's identity: model_name, plus a
HEAD:backend/onyx/llm/model_capabilities.py:636:    return [name for name in (model_name, deployment_name) if name]
HEAD:backend/onyx/llm/model_capabilities.py:654:    model_provider: str,
HEAD:backend/onyx/llm/model_capabilities.py:655:    model_names: Sequence[str],
HEAD:backend/onyx/llm/model_capabilities.py:665:    is_claude_model = any("claude" in name.lower() for name in model_names)
HEAD:backend/onyx/llm/model_capabilities.py:672:    if any(is_true_openai_model(model_provider, name) for name in model_names):
HEAD:backend/onyx/llm/model_capabilities.py:676:        or any(is_openai_registry_model_name(name) for name in model_names)
HEAD:backend/onyx/llm/model_capabilities.py:681:        if any(anthropic_uses_adaptive_thinking(name) for name in model_names):
HEAD:backend/onyx/llm/model_capabilities.py:697:    model_provider: str,
```
## RAG and Derived-Data Assets
Evidence lines: 650
```text
HEAD:backend/ee/onyx/access/access.py:15:from onyx.access.access import _get_acl_for_user as get_acl_for_user_without_groups
HEAD:backend/ee/onyx/access/access.py:138:    """EE version: extends the MIT user file ACL with user group names
HEAD:backend/ee/onyx/access/access.py:184:def _get_acl_for_user(user: User, db_session: Session) -> set[str]:
HEAD:backend/ee/onyx/access/access.py:185:    """Returns a list of ACL entries that the user has access to. This is meant to be
HEAD:backend/ee/onyx/access/access.py:187:    user should have access to a document if at least one entry in the document's ACL
HEAD:backend/ee/onyx/access/access.py:208:    user_acl = set(prefixed_user_groups + prefixed_external_groups)
HEAD:backend/ee/onyx/access/access.py:209:    user_acl.update(get_acl_for_user_without_groups(user, db_session))
HEAD:backend/ee/onyx/access/access.py:211:    return user_acl
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:68:    # A TXT record is one or more quoted chunks, joined before matching.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:716:    """Update permissions for a document or hierarchy node."""
HEAD:backend/ee/onyx/connectors/capability_checks.py:26:_DOC_PERMISSION_SYNC_CHECKS_BY_SOURCE: dict[DocumentSource, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/db/document.py:19:    This sets the permissions for a document in postgres.
HEAD:backend/ee/onyx/db/document.py:59:    This sets the permissions for a document in postgres. Returns True if the
HEAD:backend/ee/onyx/db/document_set.py:7:from onyx.configs.app_configs import DISABLE_VECTOR_DB
HEAD:backend/ee/onyx/db/document_set.py:8:from onyx.db.document_set import check_if_cc_pairs_are_owned_by_groups
HEAD:backend/ee/onyx/db/document_set.py:22:    document_set_id: int,
HEAD:backend/ee/onyx/db/document_set.py:30:        DocumentSet__User.document_set_id == document_set_id
HEAD:backend/ee/onyx/db/document_set.py:33:        DocumentSet__UserGroup.document_set_id == document_set_id
HEAD:backend/ee/onyx/db/document_set.py:39:                DocumentSet__User(document_set_id=document_set_id, user_id=user_uuid)
HEAD:backend/ee/onyx/db/document_set.py:46:                    document_set_id=document_set_id, user_group_id=group_id
HEAD:backend/ee/onyx/db/document_set.py:51:def set_document_set_group_membership__no_commit(
HEAD:backend/ee/onyx/db/document_set.py:59:    off that. Re-applies update_document_set's constraint that a private set's connectors
HEAD:backend/ee/onyx/db/document_set.py:62:        row.document_set_id: row
HEAD:backend/ee/onyx/db/document_set.py:65:                DocumentSet__UserGroup.document_set_id.in_(
HEAD:backend/ee/onyx/db/document_set.py:66:                    [document_set.id for document_set in (*to_attach, *to_detach)]
HEAD:backend/ee/onyx/db/document_set.py:75:        document_set for document_set in to_attach if document_set.id not in existing
HEAD:backend/ee/onyx/db/document_set.py:78:        document_set for document_set in to_detach if document_set.id in existing
HEAD:backend/ee/onyx/db/document_set.py:85:            document_set
HEAD:backend/ee/onyx/db/document_set.py:86:            for document_set in (*attaching, *detaching)
HEAD:backend/ee/onyx/db/document_set.py:87:            if not document_set.is_up_to_date
HEAD:backend/ee/onyx/db/document_set.py:99:        document_set.id for document_set in attaching if not document_set.is_public
HEAD:backend/ee/onyx/db/document_set.py:107:                    DocumentSet__ConnectorCredentialPair.document_set_id.in_(
HEAD:backend/ee/onyx/db/document_set.py:120:    for document_set in attaching:
HEAD:backend/ee/onyx/db/document_set.py:123:                document_set_id=document_set.id, user_group_id=user_group_id
HEAD:backend/ee/onyx/db/document_set.py:126:    for document_set in detaching:
HEAD:backend/ee/onyx/db/document_set.py:127:        db_session.delete(existing[document_set.id])
HEAD:backend/ee/onyx/db/document_set.py:129:    for document_set in (*attaching, *detaching):
HEAD:backend/ee/onyx/db/document_set.py:130:        if not DISABLE_VECTOR_DB:
HEAD:backend/ee/onyx/db/document_set.py:131:            document_set.is_up_to_date = False
HEAD:backend/ee/onyx/db/document_set.py:132:        document_set.time_last_modified_by_user = func.now()
HEAD:backend/ee/onyx/db/document_set.py:136:def delete_document_set_privacy__no_commit(
HEAD:backend/ee/onyx/db/document_set.py:137:    document_set_id: int, db_session: Session
HEAD:backend/ee/onyx/db/document_set.py:140:        DocumentSet__User.document_set_id == document_set_id
HEAD:backend/ee/onyx/db/document_set.py:144:        DocumentSet__UserGroup.document_set_id == document_set_id
HEAD:backend/ee/onyx/db/document_set.py:148:def fetch_document_sets(
HEAD:backend/ee/onyx/db/document_set.py:156:    public_document_sets = (
HEAD:backend/ee/onyx/db/document_set.py:163:    shared_document_sets = (
HEAD:backend/ee/onyx/db/document_set.py:165:        .join(DocumentSet__User, DocumentSet.id == DocumentSet__User.document_set_id)
HEAD:backend/ee/onyx/db/document_set.py:179:    group_document_sets = []
HEAD:backend/ee/onyx/db/document_set.py:181:        group_document_sets.extend(
HEAD:backend/ee/onyx/db/document_set.py:185:                DocumentSet.id == DocumentSet__UserGroup.document_set_id,
HEAD:backend/ee/onyx/db/document_set.py:192:    all_document_sets = list(
HEAD:backend/ee/onyx/db/document_set.py:193:        set(public_document_sets + shared_document_sets + group_document_sets)
HEAD:backend/ee/onyx/db/document_set.py:196:    document_set_with_cc_pairs: list[
HEAD:backend/ee/onyx/db/document_set.py:200:    for document_set in all_document_sets:
HEAD:backend/ee/onyx/db/document_set.py:210:                DocumentSet__ConnectorCredentialPair.document_set_id == document_set.id,
HEAD:backend/ee/onyx/db/document_set.py:215:        document_set_with_cc_pairs.append((document_set, cc_pairs))
HEAD:backend/ee/onyx/db/document_set.py:217:    return document_set_with_cc_pairs
HEAD:backend/ee/onyx/db/external_perm.py:166:        chunk = user_group_mappings_deduped[i : i + _UPSERT_BATCH_SIZE]
HEAD:backend/ee/onyx/db/external_perm.py:167:        stmt = pg_insert(User__ExternalUserGroupId).values(chunk)
HEAD:backend/ee/onyx/db/external_perm.py:184:        chunk = public_group_mappings_deduped[i : i + _UPSERT_BATCH_SIZE]
HEAD:backend/ee/onyx/db/external_perm.py:185:        stmt = pg_insert(PublicExternalUserGroup).values(chunk)
HEAD:backend/ee/onyx/db/hierarchy.py:53:    """Grant access through the node ACL or an associated connector."""
HEAD:backend/ee/onyx/db/hierarchy.py:99:    """EE version: ACL-filtered case-insensitive display_name search."""
HEAD:backend/ee/onyx/db/persona.py:200:    # When sharing changes, user file ACLs need to be updated in the vector DB
HEAD:backend/ee/onyx/db/scim.py:271:        replaced address keeps reaching documents whose indexed ACLs still name
HEAD:backend/ee/onyx/db/user_group.py:23:from onyx.configs.app_configs import DISABLE_VECTOR_DB
HEAD:backend/ee/onyx/db/user_group.py:197:def _cleanup_document_set__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:228:        selectinload(UserGroup.document_sets).options(
HEAD:backend/ee/onyx/db/user_group.py:245:            selectinload(Persona.document_sets).options(
HEAD:backend/ee/onyx/db/user_group.py:530:        is_up_to_date=DISABLE_VECTOR_DB,
HEAD:backend/ee/onyx/db/user_group.py:724:    # The cc_pair re-attach vector only applies to scoped managers; a global
HEAD:backend/ee/onyx/db/user_group.py:895:    if cc_pairs_updated and not DISABLE_VECTOR_DB:
HEAD:backend/ee/onyx/db/user_group.py:985:    if not DISABLE_VECTOR_DB:
HEAD:backend/ee/onyx/db/user_group.py:1047:    _cleanup_document_set__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja:18:            <!-- <document type="danswer_chunk" mode="index" /> -->
HEAD:backend/ee/onyx/external_permissions/github/utils.py:327:    #    forcing full permission syncs for all documents every time, which is inefficient.
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:51:    Adds the external permissions to the documents and hierarchy nodes in postgres.
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:81:                logger.warning("No permissions found for document %s", slim_doc.id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:238:                    "Permission is type `user` but no email address is provided for document %s\n %s",
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:248:                    "Permission is type `group` but no email address is provided for document %s\n %s",
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:254:                permission, company_domain, f"document {doc_id}"
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:382:    Adds the external permissions to the documents and hierarchy nodes in postgres.
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:17:    Fetches permissions for a document based on a list of permission IDs.
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:33:    # Fetch all permissions for the document
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:57:            "Could not find all requested permission IDs for document %s. Missing IDs: %s",
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:497:            "static Onyx ACLs; unsupported_holder_counts=%s all_holder_counts=%s",
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:65:    failed id lookup yields the literal ``None`` suffix. Persisted ACLs already
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:10:from onyx.context.search.models import InferenceChunk
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:68:# list of chunks to be censored and the user email. returns censored chunks
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:69:CensoringFuncType = Callable[[list[InferenceChunk], str], list[InferenceChunk]]
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:7:from onyx.context.search.pipeline import InferenceChunk
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:22:    all chunks for that source will be censored, even if the connector that
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:23:    indexed that chunk is not sync. This was done to avoid getting the cc_pair
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:24:    for every single chunk.
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:37:def _post_query_chunk_censoring(
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:38:    chunks: list[InferenceChunk],
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:40:) -> list[InferenceChunk]:
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:42:    This function checks all chunks to see if they need to be sent to a censoring
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:44:    censored chunks. If they don't, it returns the original chunks.
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:50:        return [chunk for chunk in chunks if chunk.source_type not in sources_to_censor]
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:52:    final_chunk_dict: dict[str, InferenceChunk] = {}
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:53:    chunks_to_process: dict[DocumentSource, list[InferenceChunk]] = {}
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:54:    for chunk in chunks:
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:55:        # Separate out chunks that require permission post-processing by source
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:56:        if chunk.source_type in sources_to_censor:
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:57:            chunks_to_process.setdefault(chunk.source_type, []).append(chunk)
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:59:            final_chunk_dict[chunk.unique_id] = chunk
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:61:    # For each source, filter out the chunks using the permission
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:64:    for source, chunks_for_source in chunks_to_process.items():
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:69:        censor_chunks_for_source = sync_config.censoring_config.chunk_censoring_func
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:71:            censored_chunks = censor_chunks_for_source(chunks_for_source, user.email)
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:74:                "Failed to censor chunks for source %s so throwing out all chunks for this source and continuing: %s",
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:80:        for censored_chunk in censored_chunks:
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:81:            final_chunk_dict[censored_chunk.unique_id] = censored_chunk
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:83:    # IMPORTANT: make sure to retain the same ordering as the original `chunks` passed in
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:84:    # only if the chunk is in the final censored chunks, add it to the final list
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:86:    final_chunk_list: list[InferenceChunk] = [
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:87:        final_chunk_dict[chunk.unique_id]
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:88:        for chunk in chunks
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:89:        if chunk.unique_id in final_chunk_dict
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:92:    return final_chunk_list
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:10:from onyx.context.search.models import InferenceChunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:18:ChunkKey = tuple[str, int]  # (doc_id, chunk_id)
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:26:    chunks: list[InferenceChunk],  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:38:    chunks: list[InferenceChunk],
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:46:    first_doc_id = chunks[0].document_id
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:77:def _get_object_ranges_for_chunk(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:78:    chunk: InferenceChunk,
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:81:    Given a chunk, return a dictionary of salesforce object ids and the content ranges
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:82:    for that object id in the current chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:84:    if chunk.source_links is None:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:90:        chunk.source_links.items(), key=lambda x: x[0], reverse=True
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:101:def _create_empty_censored_chunk(uncensored_chunk: InferenceChunk) -> InferenceChunk:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:103:    Create a copy of the unfiltered chunk where potentially sensitive content is removed
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:106:    empty_censored_chunk = InferenceChunk(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:107:        **uncensored_chunk.model_dump(),
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:109:    empty_censored_chunk.content = ""
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:110:    empty_censored_chunk.blurb = ""
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:111:    empty_censored_chunk.source_links = {}
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:112:    return empty_censored_chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:115:def _update_censored_chunk(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:116:    censored_chunk: InferenceChunk,
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:117:    uncensored_chunk: InferenceChunk,
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:119:) -> InferenceChunk:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:121:    Update the filtered chunk with the content and source links from the unfiltered chunk using the content ranges
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:125:    # Update the content of the filtered chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:126:    permitted_content = uncensored_chunk.content[start_index:end_index]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:127:    permitted_section_start_index = len(censored_chunk.content)
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:128:    censored_chunk.content = permitted_content + censored_chunk.content
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:130:    # Update the source links of the filtered chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:131:    if uncensored_chunk.source_links is not None:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:132:        if censored_chunk.source_links is None:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:133:            censored_chunk.source_links = {}
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:134:        link_content = uncensored_chunk.source_links[start_index]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:135:        censored_chunk.source_links[permitted_section_start_index] = link_content
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:137:    # Update the blurb of the filtered chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:138:    censored_chunk.blurb = censored_chunk.content[:BLURB_SIZE]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:140:    return censored_chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:144:def censor_salesforce_chunks(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:145:    chunks: list[InferenceChunk],
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:149:) -> list[InferenceChunk]:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:150:    # object_id -> list[((doc_id, chunk_id), (start_index, end_index))]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:151:    object_to_content_map: dict[str, list[tuple[ChunkKey, ContentRange]]] = {}
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:153:    # (doc_id, chunk_id) -> chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:154:    uncensored_chunks: dict[ChunkKey, InferenceChunk] = {}
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:160:    for chunk in chunks:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:161:        chunk_key = (chunk.document_id, chunk.chunk_id)
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:162:        # create a dictionary to quickly look up the unfiltered chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:163:        uncensored_chunks[chunk_key] = chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:165:        # for each chunk, get a dictionary of object ids and the content ranges
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:166:        # for that object id in the current chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:167:        object_ranges_for_chunk = _get_object_ranges_for_chunk(chunk)
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:168:        for object_id, ranges in object_ranges_for_chunk.items():
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:172:                    (chunk_key, (start_index, end_index))
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:180:            chunks=chunks,
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:184:            # so we should just return an empty list because no chunks will be
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:188:    censored_chunks: dict[ChunkKey, InferenceChunk] = {}
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:191:        # access_map, do not include its content in the filtered chunks
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:196:        # the filtered chunk(s) for this object
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:197:        # NOTE: we only create a censored chunk if the user has access to some
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:198:        # part of the chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:199:        for chunk_key, content_range in content_list:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:200:            if chunk_key not in censored_chunks:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:201:                censored_chunks[chunk_key] = _create_empty_censored_chunk(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:202:                    uncensored_chunks[chunk_key]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:205:            uncensored_chunk = uncensored_chunks[chunk_key]
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:206:            censored_chunk = _update_censored_chunk(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:207:                censored_chunk=censored_chunks[chunk_key],
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:208:                uncensored_chunk=uncensored_chunk,
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:211:            censored_chunks[chunk_key] = censored_chunk
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:213:    return list(censored_chunks.values())
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:64:# can stream the entire collection in one chunked response which has been
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:66:# (ChunkedEncodingError: Response ended prematurely) on items with many
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:239:    Adds the external permissions to the documents in postgres if the document
HEAD:backend/ee/onyx/external_permissions/sync_params.py:36:    from onyx.context.search.models import InferenceChunk  # noqa
HEAD:backend/ee/onyx/external_permissions/sync_params.py:66:    def run(chunks: list["InferenceChunk"], user_email: str) -> list["InferenceChunk"]:
HEAD:backend/ee/onyx/external_permissions/sync_params.py:67:        return load()(chunks, user_email)
HEAD:backend/ee/onyx/external_permissions/sync_params.py:150:def _load_censor_salesforce_chunks() -> CensoringFuncType:
HEAD:backend/ee/onyx/external_permissions/sync_params.py:152:        censor_salesforce_chunks,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:155:    return censor_salesforce_chunks
HEAD:backend/ee/onyx/external_permissions/sync_params.py:195:    chunk_censoring_func: CensoringFuncType
HEAD:backend/ee/onyx/external_permissions/sync_params.py:203:    # None means we don't perform a chunk_censoring
HEAD:backend/ee/onyx/external_permissions/sync_params.py:309:            chunk_censoring_func=_lazy_censoring(_load_censor_salesforce_chunks),
HEAD:backend/ee/onyx/external_permissions/sync_params.py:397:def source_should_fetch_permissions_during_indexing(source: DocumentSource) -> bool:
HEAD:backend/ee/onyx/external_permissions/utils.py:4:from ee.onyx.external_permissions.perm_sync_types import FetchAllDocumentsIdsFunction
HEAD:backend/ee/onyx/search/process_search_query.py:8:    SearchDocWithContent,
HEAD:backend/ee/onyx/search/process_search_query.py:14:    SearchDocsPacket,
HEAD:backend/ee/onyx/search/process_search_query.py:18:from onyx.context.search.models import BaseFilters, ChunkSearchRequest, InferenceChunk
HEAD:backend/ee/onyx/search/process_search_query.py:19:from onyx.context.search.pipeline import merge_individual_chunks, search_pipeline
HEAD:backend/ee/onyx/search/process_search_query.py:22:from onyx.document_index.factory import get_default_document_index
HEAD:backend/ee/onyx/search/process_search_query.py:23:from onyx.document_index.interfaces_new import DocumentIndex
HEAD:backend/ee/onyx/search/process_search_query.py:44:    document_index: DocumentIndex,
HEAD:backend/ee/onyx/search/process_search_query.py:49:) -> list[InferenceChunk]:
HEAD:backend/ee/onyx/search/process_search_query.py:50:    """Execute a single search query and return chunks."""
HEAD:backend/ee/onyx/search/process_search_query.py:51:    chunk_search_request = ChunkSearchRequest(
HEAD:backend/ee/onyx/search/process_search_query.py:59:        chunk_search_request=chunk_search_request,
HEAD:backend/ee/onyx/search/process_search_query.py:60:        document_index=document_index,
HEAD:backend/ee/onyx/search/process_search_query.py:64:        # Search UI is the only surface that enforces FORCED_DOCUMENT_SET_NAMES.
HEAD:backend/ee/onyx/search/process_search_query.py:65:        force_configured_document_set_scope=True,
HEAD:backend/ee/onyx/search/process_search_query.py:74:    SearchQueriesPacket | SearchDocsPacket | LLMSelectedDocsPacket | SearchErrorPacket,
HEAD:backend/ee/onyx/search/process_search_query.py:85:    document_index = get_default_document_index(search_settings, None, db_session)
HEAD:backend/ee/onyx/search/process_search_query.py:121:        chunks = _run_single_search(
HEAD:backend/ee/onyx/search/process_search_query.py:124:            document_index=document_index,
HEAD:backend/ee/onyx/search/process_search_query.py:139:                    document_index,
HEAD:backend/ee/onyx/search/process_search_query.py:150:        all_search_results: list[list[InferenceChunk]] = (
HEAD:backend/ee/onyx/search/process_search_query.py:166:        valid_results: list[list[InferenceChunk]] = []
HEAD:backend/ee/onyx/search/process_search_query.py:180:            chunks = []
HEAD:backend/ee/onyx/search/process_search_query.py:182:            chunks = weighted_reciprocal_rank_fusion(
HEAD:backend/ee/onyx/search/process_search_query.py:185:                id_extractor=lambda chunk: f"{chunk.document_id}_{chunk.chunk_id}",
HEAD:backend/ee/onyx/search/process_search_query.py:188:    # Merge chunks into sections
HEAD:backend/ee/onyx/search/process_search_query.py:189:    sections = merge_individual_chunks(chunks)
HEAD:backend/ee/onyx/search/process_search_query.py:221:                    section.center_chunk.document_id for section in selected_sections
HEAD:backend/ee/onyx/search/process_search_query.py:238:    # Convert to SearchDocWithContent list, optionally including content
HEAD:backend/ee/onyx/search/process_search_query.py:239:    search_docs = SearchDocWithContent.from_inference_sections(
HEAD:backend/ee/onyx/search/process_search_query.py:249:    yield SearchDocsPacket(search_docs=search_docs)
HEAD:backend/ee/onyx/search/process_search_query.py:264:        | SearchDocsPacket
HEAD:backend/ee/onyx/search/process_search_query.py:275:    search_docs: list[SearchDocWithContent] = []
HEAD:backend/ee/onyx/search/process_search_query.py:282:        elif isinstance(packet, SearchDocsPacket):
HEAD:backend/ee/onyx/server/billing/billing_cache.py:5:`_check_chunk_usage_limit` → `check_usage_and_raise` → `is_tenant_on_trial`
HEAD:backend/ee/onyx/server/gateway/api.py:90:    ChatCompletionChunk,
HEAD:backend/ee/onyx/server/gateway/api.py:346:            for chunk in state.upstream:
HEAD:backend/ee/onyx/server/gateway/api.py:349:                state.observe(chunk)
HEAD:backend/ee/onyx/server/gateway/api.py:350:                payload = ChatCompletionChunk.from_stream_chunk(
HEAD:backend/ee/onyx/server/gateway/api.py:351:                    chunk, model, include_role=not sent_role
HEAD:backend/ee/onyx/server/gateway/api.py:641:            for chunk in state.upstream:
HEAD:backend/ee/onyx/server/gateway/api.py:644:                state.observe(chunk)
HEAD:backend/ee/onyx/server/gateway/api.py:645:                if not chunk.choice.delta.content:
HEAD:backend/ee/onyx/server/gateway/api.py:671:                        delta=chunk.choice.delta.content,
HEAD:backend/ee/onyx/server/gateway/api.py:1213:            for chunk in state.upstream:
HEAD:backend/ee/onyx/server/gateway/api.py:1216:                state.observe(chunk)
HEAD:backend/ee/onyx/server/gateway/api.py:1217:                if chunk.choice.finish_reason is not None:
HEAD:backend/ee/onyx/server/gateway/api.py:1218:                    finish_reason = chunk.choice.finish_reason
HEAD:backend/ee/onyx/server/gateway/api.py:1219:                delta = chunk.choice.delta
HEAD:backend/ee/onyx/server/gateway/api.py:1220:                # Anthropic-family chunks carry reasoning_content mirroring
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:138:            # Requires org-scoped vector_store_ids no gateway caller can
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:139:            # own; we do not proxy /v1/vector_stores.
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:65:    def observe(self, chunk: ModelResponseStream) -> None:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:66:        if chunk.usage:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:67:            self.usage = chunk.usage
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:68:        if chunk.choice.delta.content:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:69:            self.content.append(chunk.choice.delta.content)
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:70:        if chunk.choice.delta.reasoning_content:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:71:            self.reasoning.append(chunk.choice.delta.reasoning_content)
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:72:        for delta_tc in chunk.choice.delta.tool_calls:
HEAD:backend/ee/onyx/server/log_export/api.py:40:from onyx.file_store.constants import STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/log_export/api.py:293:            while chunk := zip_buffer.read(STANDARD_CHUNK_SIZE):
HEAD:backend/ee/onyx/server/log_export/api.py:294:                yield chunk
HEAD:backend/ee/onyx/server/log_export/storage.py:33:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE, STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/log_export/storage.py:170:    chunks so large pieces never fully load into memory.
HEAD:backend/ee/onyx/server/log_export/storage.py:195:                shutil.copyfileobj(piece_stream, destination, STANDARD_CHUNK_SIZE)
HEAD:backend/ee/onyx/server/query_and_chat/models.py:6:from onyx.context.search.models import BaseFilters, InferenceSection, SearchDoc
HEAD:backend/ee/onyx/server/query_and_chat/models.py:42:class SearchDocWithContent(SearchDoc):
HEAD:backend/ee/onyx/server/query_and_chat/models.py:53:    ) -> list["SearchDocWithContent"]:
HEAD:backend/ee/onyx/server/query_and_chat/models.py:54:        """Convert InferenceSections to SearchDocWithContent objects.
HEAD:backend/ee/onyx/server/query_and_chat/models.py:62:            List of SearchDocWithContent with optional content
HEAD:backend/ee/onyx/server/query_and_chat/models.py:69:                document_id=(chunk := section.center_chunk).document_id,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:70:                chunk_ind=chunk.chunk_id,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:71:                semantic_identifier=chunk.semantic_identifier or "Unknown",
HEAD:backend/ee/onyx/server/query_and_chat/models.py:72:                link=chunk.source_links[0] if chunk.source_links else None,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:73:                blurb=chunk.blurb,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:74:                source_type=chunk.source_type,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:75:                boost=chunk.boost,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:76:                hidden=chunk.hidden,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:77:                metadata=chunk.metadata,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:78:                score=chunk.score,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:79:                match_highlights=chunk.match_highlights,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:80:                updated_at=chunk.updated_at,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:81:                primary_owners=chunk.primary_owners,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:82:                secondary_owners=chunk.secondary_owners,
HEAD:backend/ee/onyx/server/query_and_chat/models.py:92:    search_docs: list[SearchDocWithContent]
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:44:from onyx.server.utils_vector_db import require_vector_db
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:99:    dependencies=[Depends(require_vector_db)],
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:5:from ee.onyx.server.query_and_chat.models import SearchDocWithContent
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:15:class SearchDocsPacket(BaseModel):
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:19:    search_docs: list[SearchDocWithContent]
HEAD:backend/ee/onyx/server/query_history/models.py:14:class AbridgedSearchDoc(BaseModel):
HEAD:backend/ee/onyx/server/query_history/models.py:15:    """A subset of the info present in `SearchDoc`"""
HEAD:backend/ee/onyx/server/query_history/models.py:26:    documents: list[AbridgedSearchDoc]
HEAD:backend/ee/onyx/server/query_history/models.py:57:                AbridgedSearchDoc(
HEAD:backend/ee/onyx/server/query_history/models.py:161:    retrieved_documents: list[AbridgedSearchDoc]
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:24:from onyx.file_store.constants import STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:84:            chunk = file.read(STANDARD_CHUNK_SIZE)
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:85:            if not chunk:
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:87:            yield chunk
HEAD:backend/ee/onyx/server/scim/filtering.py:27:from dataclasses import dataclass
HEAD:backend/ee/onyx/server/scim/filtering.py:39:@dataclass(frozen=True, slots=True)
HEAD:backend/ee/onyx/server/scim/models.py:10:from dataclasses import dataclass
HEAD:backend/ee/onyx/server/scim/models.py:87:@dataclass
HEAD:backend/ee/onyx/server/scim/patch.py:19:from dataclasses import dataclass, field
HEAD:backend/ee/onyx/server/scim/patch.py:107:@dataclass
HEAD:backend/ee/onyx/server/seeding.py:177:                    document_set_ids=persona.document_set_ids,
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:97:        chunks_indexed_trial=NO_LIMIT,
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:98:        chunks_indexed_paid=NO_LIMIT,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:49:    upsert_cloud_embedding_provider,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:72:from onyx.server.manage.embedding.models import CloudEmbeddingProviderCreationRequest
HEAD:backend/ee/onyx/server/tenants/provisioning.py:85:from shared_configs.enums import EmbeddingProvider
HEAD:backend/ee/onyx/server/tenants/provisioning.py:537:    # Configure Cohere embedding provider
HEAD:backend/ee/onyx/server/tenants/provisioning.py:539:        cloud_embedding_provider = CloudEmbeddingProviderCreationRequest(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:540:            provider_type=EmbeddingProvider.COHERE,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:545:            logger.info("Attempting to upsert Cohere cloud embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:546:            upsert_cloud_embedding_provider(db_session, cloud_embedding_provider)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:547:            logger.info("Successfully upserted Cohere cloud embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:549:            logger.info("Updating search settings with Cohere embedding model details")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:565:                current_search_settings.provider_type = EmbeddingProvider.COHERE
HEAD:backend/ee/onyx/server/tenants/provisioning.py:567:                    "danswer_chunk_cohere_embed_english_v3_0"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:586:            logger.exception("Failed to configure Cohere embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:589:            "COHERE_DEFAULT_API_KEY not set, skipping Cohere embedding provider configuration"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:759:                and current_search_settings.provider_type == EmbeddingProvider.COHERE
HEAD:backend/ee/onyx/server/usage_limits.py:17:    ``_check_chunk_usage_limit`` therefore don't fan out to the control plane
HEAD:backend/ee/onyx/server/user_group/api.py:5:from ee.onyx.db.document_set import set_document_set_group_membership__no_commit
HEAD:backend/ee/onyx/server/user_group/api.py:55:from onyx.configs.app_configs import DISABLE_VECTOR_DB
HEAD:backend/ee/onyx/server/user_group/api.py:57:from onyx.db.document_set import (
HEAD:backend/ee/onyx/server/user_group/api.py:58:    get_document_sets_by_ids,
HEAD:backend/ee/onyx/server/user_group/api.py:59:    get_group_ids_for_document_sets,
HEAD:backend/ee/onyx/server/user_group/api.py:450:    if DISABLE_VECTOR_DB:
HEAD:backend/ee/onyx/server/user_group/api.py:527:def update_group_document_sets(
HEAD:backend/ee/onyx/server/user_group/api.py:537:    gated on MANAGE_DOCUMENT_SETS, which a groups admin doesn't hold."""
HEAD:backend/ee/onyx/server/user_group/api.py:547:    attach_ids = set(request.added_document_set_ids)
HEAD:backend/ee/onyx/server/user_group/api.py:548:    detach_ids = set(request.removed_document_set_ids)
HEAD:backend/ee/onyx/server/user_group/api.py:557:    document_sets = {
HEAD:backend/ee/onyx/server/user_group/api.py:558:        document_set.id: document_set
HEAD:backend/ee/onyx/server/user_group/api.py:559:        for document_set in get_document_sets_by_ids(
HEAD:backend/ee/onyx/server/user_group/api.py:563:    missing = sorted((attach_ids | detach_ids) - document_sets.keys())
HEAD:backend/ee/onyx/server/user_group/api.py:566:            OnyxErrorCode.DOCUMENT_SET_NOT_FOUND,
HEAD:backend/ee/onyx/server/user_group/api.py:573:        groups_by_document_set = get_group_ids_for_document_sets(
HEAD:backend/ee/onyx/server/user_group/api.py:574:            db_session, list(document_sets)
HEAD:backend/ee/onyx/server/user_group/api.py:576:        for document_set_id, document_set in document_sets.items():
HEAD:backend/ee/onyx/server/user_group/api.py:577:            current_group_ids = groups_by_document_set[document_set_id]
HEAD:backend/ee/onyx/server/user_group/api.py:580:                if document_set_id in attach_ids
HEAD:backend/ee/onyx/server/user_group/api.py:586:                permission=Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/ee/onyx/server/user_group/api.py:589:                is_non_public=not document_set.is_public,
HEAD:backend/ee/onyx/server/user_group/api.py:593:        changed = set_document_set_group_membership__no_commit(
HEAD:backend/ee/onyx/server/user_group/api.py:596:            to_attach=[document_sets[ds_id] for ds_id in attach_ids],
HEAD:backend/ee/onyx/server/user_group/api.py:597:            to_detach=[document_sets[ds_id] for ds_id in detach_ids],
HEAD:backend/ee/onyx/server/user_group/api.py:604:    if changed and not DISABLE_VECTOR_DB:
HEAD:backend/ee/onyx/server/user_group/models.py:12:from onyx.server.features.document_set.models import DocumentSet
HEAD:backend/ee/onyx/server/user_group/models.py:23:    document_sets: list[DocumentSet]
HEAD:backend/ee/onyx/server/user_group/models.py:84:            document_sets=[
HEAD:backend/ee/onyx/server/user_group/models.py:88:                for ds in user_group_model.document_sets
HEAD:backend/ee/onyx/server/user_group/models.py:149:    added_document_set_ids: list[int]
HEAD:backend/ee/onyx/server/user_group/models.py:150:    removed_document_set_ids: list[int]
HEAD:backend/onyx/context/search/federated/models.py:1:from dataclasses import dataclass
HEAD:backend/onyx/context/search/federated/models.py:10:@dataclass(frozen=True)
HEAD:backend/onyx/context/search/federated/slack_search.py:33:from onyx.context.search.models import ChunkIndexRequest, InferenceChunk
HEAD:backend/onyx/context/search/federated/slack_search.py:37:from onyx.document_index.document_index_utils import get_multipass_config
HEAD:backend/onyx/context/search/federated/slack_search.py:39:from onyx.indexing.chunker import Chunker
HEAD:backend/onyx/context/search/federated/slack_search.py:41:from onyx.indexing.models import DocAwareChunk
HEAD:backend/onyx/context/search/federated/slack_search.py:998:    query: ChunkIndexRequest,
HEAD:backend/onyx/context/search/federated/slack_search.py:1010:) -> list[InferenceChunk]:
HEAD:backend/onyx/context/search/federated/slack_search.py:1032:        List of InferenceChunk objects
HEAD:backend/onyx/context/search/federated/slack_search.py:1249:    # For queries without highlights (e.g., empty recency queries), we should keep all chunks
HEAD:backend/onyx/context/search/federated/slack_search.py:1271:    # chunk index docs into doc aware chunks
HEAD:backend/onyx/context/search/federated/slack_search.py:1272:    # a single index doc can get split into multiple chunks
HEAD:backend/onyx/context/search/federated/slack_search.py:1284:    chunker = Chunker(
HEAD:backend/onyx/context/search/federated/slack_search.py:1285:        tokenizer=embedder.embedding_model.tokenizer,
HEAD:backend/onyx/context/search/federated/slack_search.py:1287:        enable_large_chunks=multipass_config.enable_large_chunks,
HEAD:backend/onyx/context/search/federated/slack_search.py:1290:    chunks = chunker.chunk(index_docs)
HEAD:backend/onyx/context/search/federated/slack_search.py:1292:    # prune chunks without any highlighted texts
HEAD:backend/onyx/context/search/federated/slack_search.py:1293:    # BUT: for recency queries without keywords, keep all chunks
HEAD:backend/onyx/context/search/federated/slack_search.py:1294:    relevant_chunks: list[DocAwareChunk] = []
HEAD:backend/onyx/context/search/federated/slack_search.py:1295:    chunkid_to_match_highlight: dict[str, str] = {}
HEAD:backend/onyx/context/search/federated/slack_search.py:1298:        # No highlighted terms - keep all chunks (recency query)
HEAD:backend/onyx/context/search/federated/slack_search.py:1299:        for chunk in chunks:
HEAD:backend/onyx/context/search/federated/slack_search.py:1300:            chunk_id = f"{chunk.source_document.id}__{chunk.chunk_id}"
HEAD:backend/onyx/context/search/federated/slack_search.py:1301:            relevant_chunks.append(chunk)
HEAD:backend/onyx/context/search/federated/slack_search.py:1302:            chunkid_to_match_highlight[chunk_id] = chunk.content  # No highlighting
HEAD:backend/onyx/context/search/federated/slack_search.py:1303:            if limit and len(relevant_chunks) >= limit:
HEAD:backend/onyx/context/search/federated/slack_search.py:1306:        # Prune chunks that don't contain highlighted terms
HEAD:backend/onyx/context/search/federated/slack_search.py:1307:        for chunk in chunks:
HEAD:backend/onyx/context/search/federated/slack_search.py:1308:            match_highlight = chunk.content
HEAD:backend/onyx/context/search/federated/slack_search.py:1314:            # if nothing got replaced, the chunk is irrelevant
HEAD:backend/onyx/context/search/federated/slack_search.py:1315:            if len(match_highlight) == len(chunk.content):
HEAD:backend/onyx/context/search/federated/slack_search.py:1318:            chunk_id = f"{chunk.source_document.id}__{chunk.chunk_id}"
HEAD:backend/onyx/context/search/federated/slack_search.py:1319:            relevant_chunks.append(chunk)
HEAD:backend/onyx/context/search/federated/slack_search.py:1320:            chunkid_to_match_highlight[chunk_id] = match_highlight
HEAD:backend/onyx/context/search/federated/slack_search.py:1321:            if limit and len(relevant_chunks) >= limit:
HEAD:backend/onyx/context/search/federated/slack_search.py:1324:    # convert to inference chunks
HEAD:backend/onyx/context/search/federated/slack_search.py:1325:    top_chunks: list[InferenceChunk] = []
HEAD:backend/onyx/context/search/federated/slack_search.py:1326:    for chunk in relevant_chunks:
HEAD:backend/onyx/context/search/federated/slack_search.py:1327:        document_id = chunk.source_document.id
HEAD:backend/onyx/context/search/federated/slack_search.py:1328:        chunk_id = f"{document_id}__{chunk.chunk_id}"
HEAD:backend/onyx/context/search/federated/slack_search.py:1330:        top_chunks.append(
HEAD:backend/onyx/context/search/federated/slack_search.py:1331:            InferenceChunk(
HEAD:backend/onyx/context/search/federated/slack_search.py:1332:                chunk_id=chunk.chunk_id,
HEAD:backend/onyx/context/search/federated/slack_search.py:1333:                blurb=chunk.blurb,
HEAD:backend/onyx/context/search/federated/slack_search.py:1334:                content=chunk.content,
HEAD:backend/onyx/context/search/federated/slack_search.py:1335:                source_links=chunk.source_links,
HEAD:backend/onyx/context/search/federated/slack_search.py:1336:                image_file_id=chunk.image_file_id,
HEAD:backend/onyx/context/search/federated/slack_search.py:1337:                section_continuation=chunk.section_continuation,
HEAD:backend/onyx/context/search/federated/slack_search.py:1341:                title=chunk.title_prefix,
HEAD:backend/onyx/context/search/federated/slack_search.py:1348:                match_highlights=[chunkid_to_match_highlight[chunk_id]],
HEAD:backend/onyx/context/search/federated/slack_search.py:1350:                chunk_context="",
HEAD:backend/onyx/context/search/federated/slack_search.py:1356:    return top_chunks
HEAD:backend/onyx/context/search/federated/slack_search_utils.py:11:from onyx.context.search.models import ChunkIndexRequest
HEAD:backend/onyx/context/search/federated/slack_search_utils.py:679:    query: ChunkIndexRequest,
HEAD:backend/onyx/context/search/forced_document_set.py:3:When ``FORCED_DOCUMENT_SET_NAMES`` is set, the Onyx Search UI is hard-restricted to
HEAD:backend/onyx/context/search/forced_document_set.py:4:those document sets. The vector index stores document set NAMES, so the configured
HEAD:backend/onyx/context/search/forced_document_set.py:7:Fail-closed by construction: a name that doesn't exist matches no chunk, so the
HEAD:backend/onyx/context/search/forced_document_set.py:15:from onyx.configs.app_configs import FORCED_DOCUMENT_SET_NAMES
HEAD:backend/onyx/context/search/forced_document_set.py:16:from onyx.db.document_set import get_document_sets_by_name
HEAD:backend/onyx/context/search/forced_document_set.py:23:def get_forced_document_set_names(db_session: Session | None) -> list[str] | None:
HEAD:backend/onyx/context/search/forced_document_set.py:25:    (multitenant, or ``FORCED_DOCUMENT_SET_NAMES`` empty).
HEAD:backend/onyx/context/search/forced_document_set.py:30:    if MULTI_TENANT or not FORCED_DOCUMENT_SET_NAMES:
HEAD:backend/onyx/context/search/forced_document_set.py:36:            for ds in get_document_sets_by_name(db_session, FORCED_DOCUMENT_SET_NAMES)
HEAD:backend/onyx/context/search/forced_document_set.py:38:        missing = [name for name in FORCED_DOCUMENT_SET_NAMES if name not in existing]
HEAD:backend/onyx/context/search/forced_document_set.py:41:                "FORCED_DOCUMENT_SET_NAMES references document sets that do not exist: "
HEAD:backend/onyx/context/search/forced_document_set.py:46:    return FORCED_DOCUMENT_SET_NAMES
HEAD:backend/onyx/context/search/models.py:10:from onyx.indexing.models import BaseChunk, IndexingSetting
HEAD:backend/onyx/context/search/models.py:54:            embedding_precision=search_settings.embedding_precision,
HEAD:backend/onyx/context/search/models.py:106:    document_set: list[str] | None = None
HEAD:backend/onyx/context/search/models.py:131:    # context window and must be searched via vector DB instead of being loaded
HEAD:backend/onyx/context/search/models.py:142:    are searched (in addition to ACL filtering).
HEAD:backend/onyx/context/search/models.py:148:    # Matches chunks where ancestor_hierarchy_node_ids contains any of these.
HEAD:backend/onyx/context/search/models.py:154:    # DocumentAccess::to_acl.
HEAD:backend/onyx/context/search/models.py:155:    access_control_list: list[str] | None
HEAD:backend/onyx/context/search/models.py:159:    # `document_set` (a user/persona OR-scope). Set only on the Search UI path
HEAD:backend/onyx/context/search/models.py:160:    # (from FORCED_DOCUMENT_SET_NAMES); None = no restriction.
HEAD:backend/onyx/context/search/models.py:161:    forced_document_set: list[str] | None = None
HEAD:backend/onyx/context/search/models.py:164:class BasicChunkRequest(BaseModel):
HEAD:backend/onyx/context/search/models.py:176:class ChunkSearchRequest(BasicChunkRequest):
HEAD:backend/onyx/context/search/models.py:181:    bypass_acl: bool = False
HEAD:backend/onyx/context/search/models.py:186:class ChunkIndexRequest(BasicChunkRequest):
HEAD:backend/onyx/context/search/models.py:200:class InferenceChunk(BaseChunk):
HEAD:backend/onyx/context/search/models.py:213:    # Matched sections in the chunk. Uses Vespa syntax e.g. <hi>TEXT</hi>
HEAD:backend/onyx/context/search/models.py:218:    chunk_context: str
HEAD:backend/onyx/context/search/models.py:224:    large_chunk_reference_ids: list[int] = Field(default_factory=list)
HEAD:backend/onyx/context/search/models.py:228:    # `Document.file_id` for the doc this chunk belongs to. Populated post-
HEAD:backend/onyx/context/search/models.py:234:        return f"{self.document_id}__{self.chunk_id}"
HEAD:backend/onyx/context/search/models.py:246:        return f"Inference Chunk: {self.document_id} - {short_blurb}..."
HEAD:backend/onyx/context/search/models.py:249:        if not isinstance(other, InferenceChunk):
HEAD:backend/onyx/context/search/models.py:251:        return (self.document_id, self.chunk_id) == (other.document_id, other.chunk_id)
HEAD:backend/onyx/context/search/models.py:254:        return hash((self.document_id, self.chunk_id))
HEAD:backend/onyx/context/search/models.py:257:        if not isinstance(other, InferenceChunk):
HEAD:backend/onyx/context/search/models.py:261:                return self.chunk_id > other.chunk_id
HEAD:backend/onyx/context/search/models.py:266:            return self.chunk_id > other.chunk_id
HEAD:backend/onyx/context/search/models.py:270:        if not isinstance(other, InferenceChunk):
HEAD:backend/onyx/context/search/models.py:277:            return self.chunk_id < other.chunk_id
HEAD:backend/onyx/context/search/models.py:281:class InferenceChunkUncleaned(InferenceChunk):
HEAD:backend/onyx/context/search/models.py:284:    def to_inference_chunk(self) -> InferenceChunk:
HEAD:backend/onyx/context/search/models.py:287:        inference_chunk_data = {
HEAD:backend/onyx/context/search/models.py:293:        return InferenceChunk(**inference_chunk_data)
HEAD:backend/onyx/context/search/models.py:297:    """Section list of chunks with a combined content. A section could be a single chunk, several
HEAD:backend/onyx/context/search/models.py:298:    chunks from the same document or the entire document."""
HEAD:backend/onyx/context/search/models.py:300:    center_chunk: InferenceChunk
HEAD:backend/onyx/context/search/models.py:301:    chunks: list[InferenceChunk]
HEAD:backend/onyx/context/search/models.py:305:class SearchDoc(BaseModel):
HEAD:backend/onyx/context/search/models.py:307:    chunk_ind: int
HEAD:backend/onyx/context/search/models.py:331:    # Mirrors `InferenceChunk.file_id`. Only present once sections have been
HEAD:backend/onyx/context/search/models.py:336:    def from_chunks_or_sections(
HEAD:backend/onyx/context/search/models.py:338:        items: "Sequence[InferenceChunk | InferenceSection] | None",
HEAD:backend/onyx/context/search/models.py:339:    ) -> list["SearchDoc"]:
HEAD:backend/onyx/context/search/models.py:340:        """Convert a sequence of InferenceChunk or InferenceSection objects to SearchDoc objects."""
HEAD:backend/onyx/context/search/models.py:347:                    chunk := (
HEAD:backend/onyx/context/search/models.py:348:                        item.center_chunk
HEAD:backend/onyx/context/search/models.py:353:                chunk_ind=chunk.chunk_id,
HEAD:backend/onyx/context/search/models.py:354:                semantic_identifier=chunk.semantic_identifier or "Unknown",
HEAD:backend/onyx/context/search/models.py:355:                link=chunk.source_links[0] if chunk.source_links else None,
HEAD:backend/onyx/context/search/models.py:356:                blurb=chunk.blurb,
HEAD:backend/onyx/context/search/models.py:357:                source_type=chunk.source_type,
HEAD:backend/onyx/context/search/models.py:358:                boost=chunk.boost,
HEAD:backend/onyx/context/search/models.py:359:                hidden=chunk.hidden,
HEAD:backend/onyx/context/search/models.py:360:                metadata=chunk.metadata,
HEAD:backend/onyx/context/search/models.py:361:                score=chunk.score,
HEAD:backend/onyx/context/search/models.py:362:                match_highlights=chunk.match_highlights,
HEAD:backend/onyx/context/search/models.py:363:                updated_at=chunk.updated_at,
HEAD:backend/onyx/context/search/models.py:364:                primary_owners=chunk.primary_owners,
HEAD:backend/onyx/context/search/models.py:365:                secondary_owners=chunk.secondary_owners,
HEAD:backend/onyx/context/search/models.py:367:                file_id=chunk.file_id,
HEAD:backend/onyx/context/search/models.py:376:    def from_saved_search_doc(cls, saved_search_doc: "SavedSearchDoc") -> "SearchDoc":
HEAD:backend/onyx/context/search/models.py:377:        """Convert a SavedSearchDoc to SearchDoc by dropping the db_doc_id field."""
HEAD:backend/onyx/context/search/models.py:379:        # Remove db_doc_id as it's not part of SearchDoc
HEAD:backend/onyx/context/search/models.py:385:        cls, saved_search_docs: list["SavedSearchDoc"]
HEAD:backend/onyx/context/search/models.py:386:    ) -> list["SearchDoc"]:
HEAD:backend/onyx/context/search/models.py:405:class SearchDocsResponse(BaseModel):
HEAD:backend/onyx/context/search/models.py:406:    search_docs: list[SearchDoc]
HEAD:backend/onyx/context/search/models.py:414:    displayed_docs: list[SearchDoc] | None = None
HEAD:backend/onyx/context/search/models.py:420:        value: list[SearchDoc] | None,
HEAD:backend/onyx/context/search/models.py:421:    ) -> list[SearchDoc] | None:
HEAD:backend/onyx/context/search/models.py:425:class SavedSearchDoc(SearchDoc):
HEAD:backend/onyx/context/search/models.py:431:        cls, search_doc: SearchDoc, db_doc_id: int = 0
HEAD:backend/onyx/context/search/models.py:432:    ) -> "SavedSearchDoc":
HEAD:backend/onyx/context/search/models.py:435:        providing this if the SavedSearchDoc will not be used in the future"""
HEAD:backend/onyx/context/search/models.py:441:    def from_dict(cls, data: dict[str, Any]) -> "SavedSearchDoc":
HEAD:backend/onyx/context/search/models.py:442:        """Create SavedSearchDoc from serialized dictionary data (e.g., from database JSON)"""
HEAD:backend/onyx/context/search/models.py:446:    def from_url(cls, url: str) -> "SavedSearchDoc":
HEAD:backend/onyx/context/search/models.py:447:        """Create a SavedSearchDoc from a URL for internet search documents.
HEAD:backend/onyx/context/search/models.py:456:            chunk_ind=0,
HEAD:backend/onyx/context/search/models.py:475:        if not isinstance(other, SavedSearchDoc):
HEAD:backend/onyx/context/search/models.py:482:class SavedSearchDocWithContent(SavedSearchDoc):
HEAD:backend/onyx/context/search/models.py:496:    document_set_names: list[str]
HEAD:backend/onyx/context/search/pipeline.py:6:from onyx.context.search.forced_document_set import get_forced_document_set_names
HEAD:backend/onyx/context/search/pipeline.py:9:    ChunkIndexRequest,
HEAD:backend/onyx/context/search/pipeline.py:10:    ChunkSearchRequest,
HEAD:backend/onyx/context/search/pipeline.py:12:    InferenceChunk,
HEAD:backend/onyx/context/search/pipeline.py:20:from onyx.context.search.retrieval.search_runner import search_chunks
HEAD:backend/onyx/context/search/pipeline.py:21:from onyx.context.search.utils import inference_section_from_chunks
HEAD:backend/onyx/context/search/pipeline.py:22:from onyx.db.document_set import filter_document_set_names_by_user_access
HEAD:backend/onyx/context/search/pipeline.py:24:from onyx.document_index.interfaces_new import DocumentIndex
HEAD:backend/onyx/context/search/pipeline.py:29:from onyx.natural_language_processing.search_nlp_models import EmbeddingModel
HEAD:backend/onyx/context/search/pipeline.py:42:    user: User,  # Used for ACLs, anonymous users only see public docs
HEAD:backend/onyx/context/search/pipeline.py:45:    persona_document_sets: list[str] | None,
HEAD:backend/onyx/context/search/pipeline.py:48:    bypass_acl: bool = False,
HEAD:backend/onyx/context/search/pipeline.py:52:    # Pre-fetched ACL filters (skips DB query when provided)
HEAD:backend/onyx/context/search/pipeline.py:53:    acl_filters: list[str] | None = None,
HEAD:backend/onyx/context/search/pipeline.py:55:    # (FORCED_DOCUMENT_SET_NAMES) as a hard AND restriction. Left False for chat and
HEAD:backend/onyx/context/search/pipeline.py:57:    force_configured_document_set_scope: bool = False,
HEAD:backend/onyx/context/search/pipeline.py:64:    # Skipped when bypass_acl is set (system callers) or when no db_session is
HEAD:backend/onyx/context/search/pipeline.py:67:        base_filters.document_set is not None
HEAD:backend/onyx/context/search/pipeline.py:68:        and not bypass_acl
HEAD:backend/onyx/context/search/pipeline.py:72:        accessible_names = filter_document_set_names_by_user_access(
HEAD:backend/onyx/context/search/pipeline.py:74:            document_set_names=base_filters.document_set,
HEAD:backend/onyx/context/search/pipeline.py:78:            name for name in base_filters.document_set if name not in accessible_names
HEAD:backend/onyx/context/search/pipeline.py:86:    document_set_filter = (
HEAD:backend/onyx/context/search/pipeline.py:87:        base_filters.document_set
HEAD:backend/onyx/context/search/pipeline.py:88:        if base_filters.document_set is not None
HEAD:backend/onyx/context/search/pipeline.py:89:        else persona_document_sets
HEAD:backend/onyx/context/search/pipeline.py:110:    if bypass_acl:
HEAD:backend/onyx/context/search/pipeline.py:111:        user_acl_filters = None
HEAD:backend/onyx/context/search/pipeline.py:112:    elif acl_filters is not None:
HEAD:backend/onyx/context/search/pipeline.py:113:        user_acl_filters = acl_filters
HEAD:backend/onyx/context/search/pipeline.py:116:            raise ValueError("Either db_session or acl_filters must be provided")
HEAD:backend/onyx/context/search/pipeline.py:117:        user_acl_filters = build_access_filters_for_user(user, db_session)
HEAD:backend/onyx/context/search/pipeline.py:120:    forced_document_set = (
HEAD:backend/onyx/context/search/pipeline.py:121:        get_forced_document_set_names(db_session)
HEAD:backend/onyx/context/search/pipeline.py:122:        if force_configured_document_set_scope
HEAD:backend/onyx/context/search/pipeline.py:130:        document_set=document_set_filter,
HEAD:backend/onyx/context/search/pipeline.py:134:        access_control_list=user_acl_filters,
HEAD:backend/onyx/context/search/pipeline.py:139:        forced_document_set=forced_document_set,
HEAD:backend/onyx/context/search/pipeline.py:145:def merge_individual_chunks(
HEAD:backend/onyx/context/search/pipeline.py:146:    chunks: list[InferenceChunk],
HEAD:backend/onyx/context/search/pipeline.py:148:    """Merge adjacent chunks from the same document into sections.
HEAD:backend/onyx/context/search/pipeline.py:150:    Chunks are considered adjacent if their chunk_ids differ by 1 and they
HEAD:backend/onyx/context/search/pipeline.py:152:    first chunk in the original list.
HEAD:backend/onyx/context/search/pipeline.py:154:    if not chunks:
HEAD:backend/onyx/context/search/pipeline.py:157:    # Create a mapping from (document_id, chunk_id) to original index
HEAD:backend/onyx/context/search/pipeline.py:158:    # This helps us find the chunk that appears first in the original list
HEAD:backend/onyx/context/search/pipeline.py:159:    chunk_to_original_index: dict[tuple[str, int], int] = {}
HEAD:backend/onyx/context/search/pipeline.py:160:    for idx, chunk in enumerate(chunks):
HEAD:backend/onyx/context/search/pipeline.py:161:        chunk_to_original_index[(chunk.document_id, chunk.chunk_id)] = idx
HEAD:backend/onyx/context/search/pipeline.py:163:    # Group chunks by document_id
HEAD:backend/onyx/context/search/pipeline.py:164:    doc_chunks: dict[str, list[InferenceChunk]] = defaultdict(list)
HEAD:backend/onyx/context/search/pipeline.py:165:    for chunk in chunks:
HEAD:backend/onyx/context/search/pipeline.py:166:        doc_chunks[chunk.document_id].append(chunk)
HEAD:backend/onyx/context/search/pipeline.py:168:    # For each document, sort chunks by chunk_id to identify adjacent chunks
HEAD:backend/onyx/context/search/pipeline.py:169:    for doc_id in doc_chunks:
HEAD:backend/onyx/context/search/pipeline.py:170:        doc_chunks[doc_id].sort(key=lambda c: c.chunk_id)
HEAD:backend/onyx/context/search/pipeline.py:172:    # Create a mapping from (document_id, chunk_id) to the section it belongs to
HEAD:backend/onyx/context/search/pipeline.py:174:    chunk_to_section: dict[tuple[str, int], InferenceSection] = {}
HEAD:backend/onyx/context/search/pipeline.py:176:    # Process each document's chunks
HEAD:backend/onyx/context/search/pipeline.py:177:    for doc_chunk_list in doc_chunks.values():
HEAD:backend/onyx/context/search/pipeline.py:178:        if not doc_chunk_list:
HEAD:backend/onyx/context/search/pipeline.py:181:        # Group adjacent chunks into sections
HEAD:backend/onyx/context/search/pipeline.py:182:        current_section_chunks = [doc_chunk_list[0]]
HEAD:backend/onyx/context/search/pipeline.py:184:        for i in range(1, len(doc_chunk_list)):
HEAD:backend/onyx/context/search/pipeline.py:185:            prev_chunk = doc_chunk_list[i - 1]
HEAD:backend/onyx/context/search/pipeline.py:186:            curr_chunk = doc_chunk_list[i]
HEAD:backend/onyx/context/search/pipeline.py:188:            # Check if chunks are adjacent (chunk_id difference is 1)
HEAD:backend/onyx/context/search/pipeline.py:189:            if curr_chunk.chunk_id == prev_chunk.chunk_id + 1:
HEAD:backend/onyx/context/search/pipeline.py:191:                current_section_chunks.append(curr_chunk)
HEAD:backend/onyx/context/search/pipeline.py:193:                # Create section from previous chunks
HEAD:backend/onyx/context/search/pipeline.py:194:                # Find the chunk that appears first in the original list
HEAD:backend/onyx/context/search/pipeline.py:195:                center_chunk = min(
HEAD:backend/onyx/context/search/pipeline.py:196:                    current_section_chunks,
HEAD:backend/onyx/context/search/pipeline.py:197:                    key=lambda c: chunk_to_original_index.get(
HEAD:backend/onyx/context/search/pipeline.py:198:                        (c.document_id, c.chunk_id), float("inf")
HEAD:backend/onyx/context/search/pipeline.py:201:                section = inference_section_from_chunks(
HEAD:backend/onyx/context/search/pipeline.py:202:                    center_chunk=center_chunk,
HEAD:backend/onyx/context/search/pipeline.py:203:                    chunks=current_section_chunks.copy(),
HEAD:backend/onyx/context/search/pipeline.py:206:                    for chunk in current_section_chunks:
HEAD:backend/onyx/context/search/pipeline.py:207:                        chunk_to_section[(chunk.document_id, chunk.chunk_id)] = section
HEAD:backend/onyx/context/search/pipeline.py:210:                current_section_chunks = [curr_chunk]
HEAD:backend/onyx/context/search/pipeline.py:213:        if current_section_chunks:
HEAD:backend/onyx/context/search/pipeline.py:214:            # Find the chunk that appears first in the original list
HEAD:backend/onyx/context/search/pipeline.py:215:            center_chunk = min(
HEAD:backend/onyx/context/search/pipeline.py:216:                current_section_chunks,
HEAD:backend/onyx/context/search/pipeline.py:217:                key=lambda c: chunk_to_original_index.get(
HEAD:backend/onyx/context/search/pipeline.py:218:                    (c.document_id, c.chunk_id), float("inf")
HEAD:backend/onyx/context/search/pipeline.py:221:            section = inference_section_from_chunks(
HEAD:backend/onyx/context/search/pipeline.py:222:                center_chunk=center_chunk,
HEAD:backend/onyx/context/search/pipeline.py:223:                chunks=current_section_chunks.copy(),
HEAD:backend/onyx/context/search/pipeline.py:226:                for chunk in current_section_chunks:
HEAD:backend/onyx/context/search/pipeline.py:227:                    chunk_to_section[(chunk.document_id, chunk.chunk_id)] = section
HEAD:backend/onyx/context/search/pipeline.py:230:    # Use (document_id, chunk_id) of center_chunk as unique identifier for sections
HEAD:backend/onyx/context/search/pipeline.py:234:    for chunk in chunks:
HEAD:backend/onyx/context/search/pipeline.py:235:        section = chunk_to_section.get((chunk.document_id, chunk.chunk_id))
HEAD:backend/onyx/context/search/pipeline.py:238:                section.center_chunk.document_id,
HEAD:backend/onyx/context/search/pipeline.py:239:                section.center_chunk.chunk_id,
HEAD:backend/onyx/context/search/pipeline.py:245:            # Chunk wasn't part of any merged section, create a single-chunk section
HEAD:backend/onyx/context/search/pipeline.py:246:            single_section = inference_section_from_chunks(
HEAD:backend/onyx/context/search/pipeline.py:247:                center_chunk=chunk,
HEAD:backend/onyx/context/search/pipeline.py:248:                chunks=[chunk],
HEAD:backend/onyx/context/search/pipeline.py:252:                    single_section.center_chunk.document_id,
HEAD:backend/onyx/context/search/pipeline.py:253:                    single_section.center_chunk.chunk_id,
HEAD:backend/onyx/context/search/pipeline.py:265:    chunk_search_request: ChunkSearchRequest,
HEAD:backend/onyx/context/search/pipeline.py:268:    document_index: DocumentIndex,
HEAD:backend/onyx/context/search/pipeline.py:269:    # Used for ACLs and federated search, anonymous users only see public docs
HEAD:backend/onyx/context/search/pipeline.py:276:    # in the LLM context and need to be searched via vector DB.
HEAD:backend/onyx/context/search/pipeline.py:280:    acl_filters: list[str] | None = None,
HEAD:backend/onyx/context/search/pipeline.py:281:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/pipeline.py:284:    # (FORCED_DOCUMENT_SET_NAMES). Chat and other callers leave this False.
HEAD:backend/onyx/context/search/pipeline.py:285:    force_configured_document_set_scope: bool = False,
HEAD:backend/onyx/context/search/pipeline.py:286:) -> list[InferenceChunk]:
HEAD:backend/onyx/context/search/pipeline.py:287:    persona_document_sets: list[str] | None = (
HEAD:backend/onyx/context/search/pipeline.py:288:        persona_search_info.document_set_names if persona_search_info else None
HEAD:backend/onyx/context/search/pipeline.py:303:        user_provided_filters=chunk_search_request.user_selected_filters,
HEAD:backend/onyx/context/search/pipeline.py:307:        persona_document_sets=persona_document_sets,
HEAD:backend/onyx/context/search/pipeline.py:310:        bypass_acl=chunk_search_request.bypass_acl,
HEAD:backend/onyx/context/search/pipeline.py:313:        acl_filters=acl_filters,
HEAD:backend/onyx/context/search/pipeline.py:314:        force_configured_document_set_scope=force_configured_document_set_scope,
HEAD:backend/onyx/context/search/pipeline.py:317:    query_keywords = strip_stopwords(chunk_search_request.query)
HEAD:backend/onyx/context/search/pipeline.py:319:    query_request = ChunkIndexRequest(
HEAD:backend/onyx/context/search/pipeline.py:320:        query=chunk_search_request.query,
HEAD:backend/onyx/context/search/pipeline.py:321:        hybrid_alpha=chunk_search_request.hybrid_alpha,
HEAD:backend/onyx/context/search/pipeline.py:322:        recency_bias_multiplier=chunk_search_request.recency_bias_multiplier,
HEAD:backend/onyx/context/search/pipeline.py:325:        limit=chunk_search_request.limit,
HEAD:backend/onyx/context/search/pipeline.py:328:    retrieved_chunks = search_chunks(
HEAD:backend/onyx/context/search/pipeline.py:331:        document_index=document_index,
HEAD:backend/onyx/context/search/pipeline.py:333:        embedding_model=embedding_model,
HEAD:backend/onyx/context/search/pipeline.py:339:    censored_chunks: list[InferenceChunk] = fetch_ee_implementation_or_noop(
HEAD:backend/onyx/context/search/pipeline.py:341:        "_post_query_chunk_censoring",
HEAD:backend/onyx/context/search/pipeline.py:342:        retrieved_chunks,
HEAD:backend/onyx/context/search/pipeline.py:344:        chunks=retrieved_chunks,
HEAD:backend/onyx/context/search/pipeline.py:348:    return censored_chunks
HEAD:backend/onyx/context/search/preprocessing/access_filters.py:3:from onyx.access.access import get_acl_for_user
HEAD:backend/onyx/context/search/preprocessing/access_filters.py:9:    user_acl = get_acl_for_user(user, session)
HEAD:backend/onyx/context/search/preprocessing/access_filters.py:10:    return list(user_acl)
HEAD:backend/onyx/context/search/preprocessing/access_filters.py:14:    user_acl_filters = build_access_filters_for_user(user, db_session)
HEAD:backend/onyx/context/search/preprocessing/access_filters.py:17:        document_set=None,
```
Derived data such as chunks, embeddings, indexes and ACL representations are
security assets even when the source document remains authoritative.
## Tool, MCP and Execution Assets
Evidence lines: 650
```text
HEAD:backend/ee/onyx/db/mcp.py:5:from onyx.db.models import MCPServer__User, MCPServer__UserGroup
HEAD:backend/ee/onyx/db/mcp.py:17:        db_session.query(MCPServer__User).filter(
HEAD:backend/ee/onyx/db/mcp.py:18:            MCPServer__User.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:21:            db_session.add(MCPServer__User(mcp_server_id=server_id, user_id=user_id))
HEAD:backend/ee/onyx/db/mcp.py:25:        db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/mcp.py:26:            MCPServer__UserGroup.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:30:                MCPServer__UserGroup(mcp_server_id=server_id, user_group_id=group_id)
HEAD:backend/ee/onyx/db/user_group.py:46:    MCPServer__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:135:    db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:136:        MCPServer__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:250:    rendered as an active document. `sandbox` stays off: the logo is embedded
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:258:        sandbox=False,
HEAD:backend/ee/onyx/server/gateway/api.py:45:from onyx.llm.model_response import ChatCompletionMessageToolCall
HEAD:backend/ee/onyx/server/gateway/api.py:55:    ToolCall,
HEAD:backend/ee/onyx/server/gateway/api.py:505:    tool_call: ToolCall | ChatCompletionMessageToolCall,
HEAD:backend/ee/onyx/server/gateway/api.py:521:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/api.py:1056:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:69:_TOOL_TYPE_CODE_INTERPRETER = "code_interpreter"
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:144:        if tool_type == _TOOL_TYPE_CODE_INTERPRETER:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:146:            # A string container references an existing sandbox under our
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:154:                    "code_interpreter tools referencing an existing container "
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:16:    ChatCompletionDeltaToolCall,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:59:        self.tool_call_buffer: dict[int, ChatCompletionDeltaToolCall] = {}
HEAD:backend/onyx/auth/oauth_token_manager.py:10:from onyx.db.models import OAuthConfig, OAuthUserToken
HEAD:backend/onyx/auth/oauth_token_manager.py:73:    from any storage model so both `OAuthConfig`-backed tool OAuth and MCP
HEAD:backend/onyx/auth/oauth_token_manager.py:153:    def __init__(self, oauth_config: OAuthConfig, user_id: UUID, db_session: Session):
HEAD:backend/onyx/auth/oauth_token_manager.py:274:        oauth_config: OAuthConfig, redirect_uri: str, state: str
HEAD:backend/onyx/auth/oauth_token_manager.py:284:    def _flow_params(oauth_config: OAuthConfig) -> OAuthFlowParams:
HEAD:backend/onyx/auth/permission_projection.py:142:class MCPServerPermissions(TypedDict):
HEAD:backend/onyx/auth/permission_projection.py:149:MCP_SERVER_ACTIONS: frozenset[str] = frozenset(MCPServerPermissions.__annotations__)
HEAD:backend/onyx/auth/permission_projection.py:157:    result: MCPServerPermissions = {
HEAD:backend/onyx/auth/permissions.py:78:    Permission.CRAFT_SANDBOX.value: {
HEAD:backend/onyx/auth/permissions.py:95:        Permission.CRAFT_SANDBOX,
HEAD:backend/onyx/background/README.md:17:| Heavy                     | `apps/heavy.py`                | `connector_pruning`, `connector_doc_permissions_sync`, `connector_external_group_sync`, `csv_generation`, `sandbox`  |
HEAD:backend/onyx/background/README.md:83:Long running, resource intensive tasks, handles pruning and sandbox operations. Low concurrency - max concurrency of 4 with 1 prefetch.
HEAD:backend/onyx/background/README.md:89:Sandbox (new feature) for running Next.js, Python virtual env, OpenCode AI Agent, and access to knowledge files
HEAD:backend/onyx/background/celery/apps/heavy.py:134:            # Sandbox tasks (file sync, cleanup; build feature)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:23:from onyx.server.features.build.configs import SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:236:    # Sandbox sweep: background-snapshot changed sessions, sleep idle sandboxes.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:238:        "name": "cleanup-idle-sandboxes",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:239:        "task": OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:242:        # the effective interval is SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS * 8;
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:244:        "schedule": timedelta(seconds=SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS),
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:248:            "queue": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:1:"""Celery tasks for sandbox operations (cleanup, etc.)."""
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:12:from onyx.db.models import Sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:15:from onyx.server.features.build.configs import SANDBOX_IDLE_TIMEOUT_SECONDS
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:16:from onyx.server.features.build.db.sandbox import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:18:    get_running_sandboxes,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:21:from onyx.server.features.build.sandbox.factory import get_sandbox_manager
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:28:# so the data-loss bound scales with the pace of sandboxes going to sleep.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:33:    name=OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:38:def cleanup_idle_sandboxes_task(self: Task, *, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:39:    """Sweep RUNNING sandboxes: background-snapshot sessions, sleep idle ones.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:46:    The reap itself is ``sleep_sandbox`` (sandbox lifecycle), which stays
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:47:    fail-closed: snapshot failure on a reachable pod keeps the sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:51:    from onyx.server.features.build.session.sandbox_lifecycle import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:53:        is_sandbox_idle,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:55:        sleep_sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:58:    task_logger.info(f"cleanup_idle_sandboxes_task starting for tenant {tenant_id}")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:62:        OnyxRedisLocks.CLEANUP_IDLE_SANDBOXES_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:68:        task_logger.info("cleanup_idle_sandboxes_task - lock not acquired, skipping")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:72:        sandbox_manager = get_sandbox_manager()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:75:            running_sandboxes = get_running_sandboxes(db_session)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:76:            if not running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:77:                task_logger.debug("No running sandboxes found")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:82:            maybe_mark_tenant_active(tenant_id, caller="sandbox_cleanup")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:86:                seconds=SANDBOX_IDLE_TIMEOUT_SECONDS // SNAPSHOT_INTERVAL_DIVISOR
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:89:            # Partition so idle sandboxes are reaped first (reclaiming pods
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:91:            idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:92:            non_idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:93:            for sandbox in running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:95:                    idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:96:                    if is_sandbox_idle(sandbox, now)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:97:                    else non_idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:98:                ).append(sandbox)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:100:            for sandbox in idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:102:                    redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:105:                    sleep_sandbox(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:107:                        sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:108:                        sandbox=sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:114:                        f"Failed to sweep sandbox {sandbox.id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:119:            for sandbox in non_idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:120:                sandbox_id = sandbox.id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:127:                        db_session, sandbox.user_id, snapshot_cutoff
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:132:                        redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:136:                            "Skipping sandbox %s background snapshot while a "
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:138:                            sandbox.id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:142:                        # List session directories in the sandbox via the
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:146:                            sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:147:                            sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:167:                                sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:169:                                sandbox_id=sandbox_id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:191:                        and sandbox_manager.supports_opencode_history_persistence
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:194:                            sandbox_manager.create_opencode_history_snapshot(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:195:                                sandbox_id, tenant_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:200:                                f"for sandbox {sandbox_id}: {e}"
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:205:                        f"Failed to sweep sandbox {sandbox_id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:211:        task_logger.exception("Error in cleanup_idle_sandboxes_task")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:218:    task_logger.info("cleanup_idle_sandboxes_task completed")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:187:        "sandbox_queue_length": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:987:    n_sandbox = celery_get_queue_length(OnyxCeleryQueues.SANDBOX, r_celery)
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1024:        f"sandbox={n_sandbox} "
HEAD:backend/onyx/chat/chat_state.py:26:from onyx.tools.models import ChatFile, ToolCallInfo
HEAD:backend/onyx/chat/chat_state.py:48:        self.tool_calls: list[ToolCallInfo] = []
HEAD:backend/onyx/chat/chat_state.py:67:    def add_tool_call(self, tool_call: ToolCallInfo) -> None:
HEAD:backend/onyx/chat/chat_state.py:112:    def get_tool_calls(self) -> list[ToolCallInfo]:
HEAD:backend/onyx/chat/chat_utils.py:21:    ToolCallSimple,
HEAD:backend/onyx/chat/chat_utils.py:30:from onyx.context.search.utils import sandbox_filename_for_document
HEAD:backend/onyx/chat/chat_utils.py:68:from onyx.tools.models import ChatFile, ToolCallKickoff
HEAD:backend/onyx/chat/chat_utils.py:846:                    # Build ToolCallSimple list for this turn
HEAD:backend/onyx/chat/chat_utils.py:847:                    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:853:                            ToolCallSimple(
HEAD:backend/onyx/chat/chat_utils.py:967:    tool_calls: list[ToolCallKickoff], token_counter: Callable[[str], int]
HEAD:backend/onyx/chat/chat_utils.py:976:        tool_calls: List of ToolCallKickoff objects representing the failed tool calls
HEAD:backend/onyx/chat/chat_utils.py:986:    # Create ToolCallSimple for each failed tool call
HEAD:backend/onyx/chat/chat_utils.py:987:    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:991:            ToolCallSimple(
HEAD:backend/onyx/chat/chat_utils.py:1072:        filename = sandbox_filename_for_document(doc.semantic_identifier, doc.file_id)
HEAD:backend/onyx/chat/citation_utils.py:6:from onyx.tools.models import ToolResponse
HEAD:backend/onyx/chat/citation_utils.py:10:    tool_response: ToolResponse,
HEAD:backend/onyx/chat/llm_loop.py:30:    ToolCallSimple,
HEAD:backend/onyx/chat/llm_loop.py:63:    ToolCallDebug,
HEAD:backend/onyx/chat/llm_loop.py:70:    CustomToolCallSummary,
HEAD:backend/onyx/chat/llm_loop.py:72:    MemoryToolResponseSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:73:    PythonToolRichResponse,
HEAD:backend/onyx/chat/llm_loop.py:74:    ToolCallInfo,
HEAD:backend/onyx/chat/llm_loop.py:75:    ToolCallKickoff,
HEAD:backend/onyx/chat/llm_loop.py:76:    ToolResponse,
HEAD:backend/onyx/chat/llm_loop.py:79:from onyx.tools.tool_implementations.memory.models import MemoryToolResponse
HEAD:backend/onyx/chat/llm_loop.py:81:from onyx.tools.tool_implementations.python.python_tool import PythonTool
HEAD:backend/onyx/chat/llm_loop.py:262:    extracted_tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_loop.py:841:        code_interpreter_file_generated: bool = False
HEAD:backend/onyx/chat/llm_loop.py:1010:                include_file_reminder=code_interpreter_file_generated,
HEAD:backend/onyx/chat/llm_loop.py:1095:            tool_responses: list[ToolResponse] = []
HEAD:backend/onyx/chat/llm_loop.py:1103:                            obj=ToolCallDebug(
HEAD:backend/onyx/chat/llm_loop.py:1167:                    tool_call.tool_name == PythonTool.NAME
HEAD:backend/onyx/chat/llm_loop.py:1168:                    and not code_interpreter_file_generated
HEAD:backend/onyx/chat/llm_loop.py:1173:                            code_interpreter_file_generated = True
HEAD:backend/onyx/chat/llm_loop.py:1233:                if isinstance(tool_response.rich_response, PythonToolRichResponse):
HEAD:backend/onyx/chat/llm_loop.py:1241:                    tool_response.rich_response, CustomToolCallSummary
HEAD:backend/onyx/chat/llm_loop.py:1250:                memory_snapshot: MemoryToolResponseSnapshot | None = None
HEAD:backend/onyx/chat/llm_loop.py:1252:                if isinstance(tool_response.rich_response, MemoryToolResponse):
HEAD:backend/onyx/chat/llm_loop.py:1280:                        memory_snapshot = MemoryToolResponseSnapshot(
HEAD:backend/onyx/chat/llm_loop.py:1293:                elif isinstance(tool_response.rich_response, CustomToolCallSummary):
HEAD:backend/onyx/chat/llm_loop.py:1302:                tool_call_info = ToolCallInfo(
HEAD:backend/onyx/chat/llm_loop.py:1335:                # Build ToolCallSimple list for all tool calls in this turn
HEAD:backend/onyx/chat/llm_loop.py:1336:                tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:1347:                        ToolCallSimple(
HEAD:backend/onyx/chat/llm_step.py:41:    ToolCall,
HEAD:backend/onyx/chat/llm_step.py:64:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/chat/llm_step.py:89:class _XmlToolCallContentFilter:
HEAD:backend/onyx/chat/llm_step.py:388:) -> list[ToolCallKickoff]:
HEAD:backend/onyx/chat/llm_step.py:389:    """Extract ToolCallKickoff objects from the tool call map.
HEAD:backend/onyx/chat/llm_step.py:391:    Returns a list of ToolCallKickoff objects for valid tool calls (those with both id and name).
HEAD:backend/onyx/chat/llm_step.py:401:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:408:                ToolCallKickoff(
HEAD:backend/onyx/chat/llm_step.py:429:) -> list[ToolCallKickoff]:
HEAD:backend/onyx/chat/llm_step.py:443:        List of ToolCallKickoff objects for any matched tool calls
HEAD:backend/onyx/chat/llm_step.py:498:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:501:            ToolCallKickoff(
HEAD:backend/onyx/chat/llm_step.py:704:    tool_calls_list: list[ToolCall] | None = None
HEAD:backend/onyx/chat/llm_step.py:707:            ToolCall(
HEAD:backend/onyx/chat/llm_step.py:1135:            - ToolCallKickoff for tool calls (extracted at the end)
HEAD:backend/onyx/chat/llm_step.py:1182:    xml_tool_call_content_filter = _XmlToolCallContentFilter()
HEAD:backend/onyx/chat/llm_step.py:1502:            tool_calls_list: list[ToolCall] = [
HEAD:backend/onyx/chat/llm_step.py:1503:                ToolCall(
HEAD:backend/onyx/chat/models.py:19:from onyx.tools.models import SearchToolUsage, ToolCallKickoff
HEAD:backend/onyx/chat/models.py:33:class CustomToolResponse(BaseModel):
HEAD:backend/onyx/chat/models.py:56:class ToolCallResponse(BaseModel):
HEAD:backend/onyx/chat/models.py:90:    tool_calls: list[ToolCallResponse] = []
HEAD:backend/onyx/chat/models.py:146:class ToolCallSimple(BaseModel):
HEAD:backend/onyx/chat/models.py:172:    tool_calls: list[ToolCallSimple] | None = None
HEAD:backend/onyx/chat/models.py:244:    tool_calls: list[ToolCallKickoff] | None
HEAD:backend/onyx/chat/process_message.py:66:    ToolCallResponse,
HEAD:backend/onyx/chat/process_message.py:223:    """Convert ChatLoadedFile objects to ChatFile for tool usage (e.g., PythonTool).
HEAD:backend/onyx/chat/process_message.py:230:    receive zero-byte content for empty files, which PythonTool handles fine
HEAD:backend/onyx/chat/process_message.py:267:    pulls from the file store only when PythonTool actually accesses
HEAD:backend/onyx/chat/process_message.py:296:            # hand PythonTool an empty payload instead of letting the
HEAD:backend/onyx/chat/process_message.py:942:    # Convert loaded files to ChatFile format for tools like PythonTool
HEAD:backend/onyx/chat/process_message.py:2249:    # Convert ToolCallInfo list to ToolCallResponse list
HEAD:backend/onyx/chat/process_message.py:2251:        ToolCallResponse(
HEAD:backend/onyx/chat/prompt_utils.py:47:from onyx.tools.tool_implementations.python.python_tool import PythonTool
HEAD:backend/onyx/chat/prompt_utils.py:300:        has_python = any(isinstance(tool, PythonTool) for tool in tools)
HEAD:backend/onyx/chat/save_chat.py:15:from onyx.db.models import ChatMessage, ToolCall
HEAD:backend/onyx/chat/save_chat.py:20:from onyx.tools.models import ToolCallInfo
HEAD:backend/onyx/chat/save_chat.py:28:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:53:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:60:    Create ToolCall entries and link parent references and SearchDocs.
HEAD:backend/onyx/chat/save_chat.py:63:    1. Creating all ToolCall objects (with temporary parent references)
HEAD:backend/onyx/chat/save_chat.py:66:    4. Linking SearchDocs to ToolCalls
HEAD:backend/onyx/chat/save_chat.py:76:    # Create all ToolCall objects first (without parent_tool_call_id set)
HEAD:backend/onyx/chat/save_chat.py:78:    tool_call_objects: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:79:    tool_call_info_map: dict[str, ToolCallInfo] = {}
HEAD:backend/onyx/chat/save_chat.py:101:        # Create ToolCall DB entry (parent_tool_call_id will be set after flush)
HEAD:backend/onyx/chat/save_chat.py:137:    valid_tool_calls: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:158:    # Link SearchDocs only to valid ToolCalls
HEAD:backend/onyx/chat/save_chat.py:172:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:192:    6. Creates ToolCall entries and links SearchDocs to them
HEAD:backend/onyx/chat/save_chat.py:198:        tool_calls: List of tool call information to create ToolCall entries (may include search_docs)
HEAD:backend/onyx/chat/save_chat.py:340:    # 6. Create ToolCall entries and link SearchDocs to them
HEAD:backend/onyx/chat/tool_call_args_streaming.py:4:from onyx.llm.model_response import ChatCompletionDeltaToolCall
HEAD:backend/onyx/chat/tool_call_args_streaming.py:6:from onyx.server.query_and_chat.streaming_models import Packet, ToolCallArgumentDelta
HEAD:backend/onyx/chat/tool_call_args_streaming.py:14:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:25:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:70:        obj=ToolCallArgumentDelta(
HEAD:backend/onyx/coding_agent/mock_tools.py:21:            "repository. The agent clones the repo into an isolated sandbox and "
HEAD:backend/onyx/coding_agent/mock_tools.py:53:            "Run a bash command in the sandboxed session containing the "
HEAD:backend/onyx/coding_agent/models.py:3:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/coding_agent/models.py:6:class CodingAgentSpecialToolCalls(BaseModel):
HEAD:backend/onyx/coding_agent/models.py:7:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/coding_agent/models.py:8:    generate_answer_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/configs/app_configs.py:1171:# can be long-running (LLM + tool calls in a sandbox).
HEAD:backend/onyx/configs/app_configs.py:1656:CODE_INTERPRETER_BASE_URL = os.environ.get(
HEAD:backend/onyx/configs/app_configs.py:1657:    "CODE_INTERPRETER_BASE_URL", "http://localhost:8000"
HEAD:backend/onyx/configs/app_configs.py:1660:CODE_INTERPRETER_DEFAULT_TIMEOUT_MS = int(
HEAD:backend/onyx/configs/app_configs.py:1661:    os.environ.get("CODE_INTERPRETER_DEFAULT_TIMEOUT_MS") or 60_000
HEAD:backend/onyx/configs/app_configs.py:1664:CODE_INTERPRETER_MAX_OUTPUT_LENGTH = int(
HEAD:backend/onyx/configs/app_configs.py:1665:    os.environ.get("CODE_INTERPRETER_MAX_OUTPUT_LENGTH") or 50_000
HEAD:backend/onyx/configs/app_configs.py:1673:CODE_INTERPRETER_MAX_STAGED_FILES = int(
HEAD:backend/onyx/configs/app_configs.py:1674:    os.environ.get("CODE_INTERPRETER_MAX_STAGED_FILES") or 25
HEAD:backend/onyx/configs/app_configs.py:1677:CODE_INTERPRETER_MAX_STAGED_BYTES = int(
HEAD:backend/onyx/configs/app_configs.py:1678:    os.environ.get("CODE_INTERPRETER_MAX_STAGED_BYTES") or 100 * 1024 * 1024
HEAD:backend/onyx/configs/app_configs.py:1682:# store and uploading cache misses to the sandbox — so neither blocks the
HEAD:backend/onyx/configs/app_configs.py:1685:CODE_INTERPRETER_STAGING_CONCURRENCY = int(
HEAD:backend/onyx/configs/app_configs.py:1686:    os.environ.get("CODE_INTERPRETER_STAGING_CONCURRENCY") or 8
HEAD:backend/onyx/configs/app_configs.py:2138:AUTO_PROVISION_DEFAULT_EXTERNAL_APPS = (
HEAD:backend/onyx/configs/app_configs.py:2139:    os.environ.get("AUTO_PROVISION_DEFAULT_EXTERNAL_APPS", "false").lower() == "true"
HEAD:backend/onyx/configs/constants.py:312:    # Raw files for Craft sandbox access (xlsx, pptx, docx, etc.)
HEAD:backend/onyx/configs/constants.py:427:    SANDBOX_SNAPSHOT = "sandbox_snapshot"
HEAD:backend/onyx/configs/constants.py:498:    # Sandbox processing queue
HEAD:backend/onyx/configs/constants.py:499:    SANDBOX = "sandbox"
HEAD:backend/onyx/configs/constants.py:570:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:571:    CLEANUP_IDLE_SANDBOXES_BEAT_LOCK = "da_lock:cleanup_idle_sandboxes_beat"
HEAD:backend/onyx/configs/constants.py:722:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:723:    CLEANUP_IDLE_SANDBOXES = "cleanup_idle_sandboxes"
HEAD:backend/onyx/connectors/file/connector.py:190:    # code-interpreter sandbox" signal read by
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:80:For a sandbox, use its My Domain host, for example:
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:83:https://company--dev.sandbox.my.salesforce.com
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:116:- Sandbox selection
HEAD:backend/onyx/connectors/salesforce/auth.py:204:            domain="test" if credentials.is_sandbox else None,
HEAD:backend/onyx/connectors/salesforce/models.py:93:    is_sandbox: bool = False
HEAD:backend/onyx/context/search/utils.py:54:_SANDBOX_FILENAME_MAX_LENGTH = 200
HEAD:backend/onyx/context/search/utils.py:179:def sandbox_filename_for_document(title: str, file_id: str) -> str:
HEAD:backend/onyx/context/search/utils.py:181:    unique sandbox filename. Extensions on the title are preserved verbatim."""
HEAD:backend/onyx/context/search/utils.py:187:    max_base_len = max(1, _SANDBOX_FILENAME_MAX_LENGTH - len(suffix))
HEAD:backend/onyx/db/README.md:21:Tool calls are stored in the ToolCall table and can represent all of the following:
HEAD:backend/onyx/db/README.md:25:- Tool calls that are instead attached to other ToolCalls are tool calls that happen as part of an
HEAD:backend/onyx/db/chat.py:23:    ToolCall,
HEAD:backend/onyx/db/chat.py:577:    Link SearchDocs to a ToolCall by creating entries in the tool_call__search_doc junction table.
HEAD:backend/onyx/db/chat.py:584:    from onyx.db.models import ToolCall__SearchDoc
HEAD:backend/onyx/db/chat.py:587:        tool_call_search_doc = ToolCall__SearchDoc(
HEAD:backend/onyx/db/chat.py:625:                ToolCall.tool_call_children
HEAD:backend/onyx/db/code_interpreter.py:7:def fetch_code_interpreter_server(
HEAD:backend/onyx/db/code_interpreter.py:14:def update_code_interpreter_server_enabled(
HEAD:backend/onyx/db/enums.py:202:class MCPServerStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:371:    IDLE:         sandbox slept; workspace must be restored before use.
HEAD:backend/onyx/db/enums.py:372:    FAILED:       initialization failed after the sandbox came up; the
HEAD:backend/onyx/db/enums.py:457:    SANDBOX_WAKE_FAILED = "sandbox_wake_failed"
HEAD:backend/onyx/db/enums.py:471:class SandboxStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:479:        """Check if sandbox is in an active state (running)."""
HEAD:backend/onyx/db/enums.py:480:        return self == SandboxStatus.RUNNING
HEAD:backend/onyx/db/enums.py:483:        """Check if sandbox is in a terminal state."""
HEAD:backend/onyx/db/enums.py:484:        return self in (SandboxStatus.TERMINATED, SandboxStatus.FAILED)
HEAD:backend/onyx/db/enums.py:487:        """Check if sandbox is sleeping (pod terminated but can be restored)."""
HEAD:backend/onyx/db/enums.py:488:        return self == SandboxStatus.SLEEPING
HEAD:backend/onyx/db/enums.py:496:    `external_apps.providers`. `CUSTOM` is for admin-defined apps
HEAD:backend/onyx/db/enums.py:543:    whether the target id refers to an ``external_app`` or an ``mcp_server`` row,
HEAD:backend/onyx/db/enums.py:547:    EXTERNAL_APP = "EXTERNAL_APP"
HEAD:backend/onyx/db/enums.py:690:    CRAFT_SANDBOX = "craft_sandbox"
HEAD:backend/onyx/db/external_app.py:32:from onyx.skills.built_in import EXTERNAL_APP_BUILT_IN_SKILL_IDS
HEAD:backend/onyx/db/external_app.py:44:    external_app_id: int
HEAD:backend/onyx/db/external_app.py:141:def get_external_app_by_id(
HEAD:backend/onyx/db/external_app.py:143:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:148:        .where(ExternalApp.id == external_app_id)
HEAD:backend/onyx/db/external_app.py:153:def get_external_app_by_skill_id(
HEAD:backend/onyx/db/external_app.py:162:            ExternalApp__Skill.external_app_id == ExternalApp.id,
HEAD:backend/onyx/db/external_app.py:169:def get_skills_for_external_app(
HEAD:backend/onyx/db/external_app.py:171:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:181:            .where(ExternalApp__Skill.external_app_id == external_app_id)
HEAD:backend/onyx/db/external_app.py:199:        for app in get_external_apps(db_session, enabled_only=True)
HEAD:backend/onyx/db/external_app.py:204:def get_skill_external_app_dependencies(
HEAD:backend/onyx/db/external_app.py:214:            ExternalApp.id == ExternalApp__Skill.external_app_id,
HEAD:backend/onyx/db/external_app.py:219:                ExternalAppUserCredential.external_app_id == ExternalApp.id,
HEAD:backend/onyx/db/external_app.py:234:            external_app_id=app.id,
HEAD:backend/onyx/db/external_app.py:243:def get_external_apps(
HEAD:backend/onyx/db/external_app.py:258:def get_built_in_external_app(
HEAD:backend/onyx/db/external_app.py:271:            f"get_built_in_external_app requires a built-in app type, got "
HEAD:backend/onyx/db/external_app.py:286:    """Map external_app_id -> the user's credential row. Apps the user never
HEAD:backend/onyx/db/external_app.py:291:    return {row.external_app_id: row for row in db_session.scalars(stmt).all()}
HEAD:backend/onyx/db/external_app.py:294:def get_external_app_user_credential(
HEAD:backend/onyx/db/external_app.py:297:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:303:            ExternalAppUserCredential.external_app_id == external_app_id,
HEAD:backend/onyx/db/external_app.py:309:def create_external_app(
HEAD:backend/onyx/db/external_app.py:354:    built_in_skill_id = EXTERNAL_APP_BUILT_IN_SKILL_IDS.get(app.app_type)
HEAD:backend/onyx/db/external_app.py:380:    elif get_external_app_by_skill_id(db_session, skill.id) is not None:
HEAD:backend/onyx/db/external_app.py:392:def associate_custom_skill_with_external_app__no_commit(
HEAD:backend/onyx/db/external_app.py:395:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:404:        select(ExternalApp).where(ExternalApp.id == external_app_id).with_for_update()
HEAD:backend/onyx/db/external_app.py:409:            f"External app with id {external_app_id} not found.",
HEAD:backend/onyx/db/external_app.py:428:    existing_app = get_external_app_by_skill_id(db_session, skill.id)
HEAD:backend/onyx/db/external_app.py:445:            ExternalApp__Skill.external_app_id == app.id,
HEAD:backend/onyx/db/external_app.py:458:    db_session.add(ExternalApp__Skill(external_app_id=app.id, skill_id=skill.id))
HEAD:backend/onyx/db/external_app.py:466:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:484:        select(ExternalApp).where(ExternalApp.id == external_app_id).with_for_update()
HEAD:backend/onyx/db/external_app.py:489:            f"External app with id {external_app_id} not found.",
HEAD:backend/onyx/db/external_app.py:521:    associated_skills = get_skills_for_external_app(db_session, app.id)
HEAD:backend/onyx/db/external_app.py:544:        .join(ExternalApp, ExternalApp.id == ExternalApp__Skill.external_app_id)
HEAD:backend/onyx/db/external_app.py:547:            ExternalApp__Skill.external_app_id != app.id,
HEAD:backend/onyx/db/external_app.py:564:                ExternalApp__Skill.external_app_id == app.id,
HEAD:backend/onyx/db/external_app.py:573:                ExternalApp__Skill(external_app_id=app.id, skill_id=skill.id)
HEAD:backend/onyx/db/external_app.py:582:def update_external_app(
HEAD:backend/onyx/db/external_app.py:584:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:602:    app = get_external_app_by_id(db_session, external_app_id)
HEAD:backend/onyx/db/external_app.py:606:            f"External app with id {external_app_id} not found.",
HEAD:backend/onyx/db/external_app.py:641:def set_external_app_organization_credentials(
HEAD:backend/onyx/db/external_app.py:651:    # assignment shape as update_external_app's masked-credential restore).
HEAD:backend/onyx/db/external_app.py:666:        db_session, GatedAppKind.EXTERNAL_APP, app.id
HEAD:backend/onyx/db/external_app.py:671:def delete_external_app(
HEAD:backend/onyx/db/external_app.py:673:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:680:    app = get_external_app_by_id(db_session, external_app_id)
HEAD:backend/onyx/db/external_app.py:684:            f"External app with id {external_app_id} not found.",
HEAD:backend/onyx/db/external_app.py:687:    skills = get_skills_for_external_app(db_session, app.id)
HEAD:backend/onyx/db/external_app.py:703:def upsert_external_app_user_credential(
HEAD:backend/onyx/db/external_app.py:705:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:712:    Atomic via ON CONFLICT on (external_app_id, user_id). Raises
HEAD:backend/onyx/db/external_app.py:722:    app = get_external_app_by_id(db_session, external_app_id)
HEAD:backend/onyx/db/external_app.py:726:            f"External app with id {external_app_id} not found.",
HEAD:backend/onyx/db/external_app.py:730:        existing_credential = get_external_app_user_credential(
HEAD:backend/onyx/db/external_app.py:732:            external_app_id=external_app_id,
HEAD:backend/onyx/db/external_app.py:743:        external_app_id=external_app_id,
HEAD:backend/onyx/db/external_app.py:758:            ExternalAppUserCredential.external_app_id,
HEAD:backend/onyx/db/external_app.py:769:def disconnect_external_app_for_user(
HEAD:backend/onyx/db/external_app.py:772:    external_app_id: int,
HEAD:backend/onyx/db/external_app.py:777:    Flush only; the caller refreshes the user's sandbox and commits.
HEAD:backend/onyx/db/external_app.py:781:            ExternalAppUserCredential.external_app_id == external_app_id,
HEAD:backend/onyx/db/external_app.py:786:        ExternalApp__Skill.external_app_id == external_app_id
HEAD:backend/onyx/db/gated_app.py:21:        GatedApp.external_app_id
HEAD:backend/onyx/db/gated_app.py:22:        if kind is GatedAppKind.EXTERNAL_APP
HEAD:backend/onyx/db/llm.py:251:    onyx/db/external_app.py.
HEAD:backend/onyx/db/mcp.py:13:    MCPServerStatus,
HEAD:backend/onyx/db/mcp.py:16:    SandboxStatus,
HEAD:backend/onyx/db/mcp.py:20:    MCPConnectionConfig,
HEAD:backend/onyx/db/mcp.py:21:    MCPServer,
HEAD:backend/onyx/db/mcp.py:22:    MCPServer__User,
HEAD:backend/onyx/db/mcp.py:23:    MCPServer__UserGroup,
HEAD:backend/onyx/db/mcp.py:25:    Sandbox,
HEAD:backend/onyx/db/mcp.py:36:# MCPServer operations
HEAD:backend/onyx/db/mcp.py:37:def get_all_mcp_servers(db_session: Session) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:40:        db_session.scalars(select(MCPServer).order_by(MCPServer.created_at)).all()
HEAD:backend/onyx/db/mcp.py:44:def get_mcp_server_by_id(server_id: int, db_session: Session) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:46:    server = db_session.scalar(select(MCPServer).where(MCPServer.id == server_id))
HEAD:backend/onyx/db/mcp.py:52:def get_mcp_servers_by_owner(owner_email: str, db_session: Session) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:56:            select(MCPServer).where(MCPServer.owner == owner_email)
HEAD:backend/onyx/db/mcp.py:63:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:71:        select(MCPServer)
HEAD:backend/onyx/db/mcp.py:72:        .where(MCPServer.available_in_craft.is_(True))
HEAD:backend/onyx/db/mcp.py:73:        .options(selectinload(MCPServer.admin_connection_config))
HEAD:backend/onyx/db/mcp.py:84:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:104:        db_session.query(MCPServer).filter(MCPServer.id.in_(mcp_server_ids)).all()
HEAD:backend/onyx/db/mcp.py:118:    MCPServer__UG = aliased(MCPServer__UserGroup)
HEAD:backend/onyx/db/mcp.py:120:        stmt.outerjoin(MCPServer__UG, MCPServer__UG.mcp_server_id == MCPServer.id)
HEAD:backend/onyx/db/mcp.py:123:            User__UserGroup.user_group_id == MCPServer__UG.user_group_id,
HEAD:backend/onyx/db/mcp.py:125:        .outerjoin(MCPServer__User, MCPServer__User.mcp_server_id == MCPServer.id)
HEAD:backend/onyx/db/mcp.py:128:    where_clause = MCPServer.is_public == True  # noqa: E712
HEAD:backend/onyx/db/mcp.py:131:        where_clause |= MCPServer__User.user_id == user.id
HEAD:backend/onyx/db/mcp.py:133:        where_clause |= MCPServer.owner == user.email
HEAD:backend/onyx/db/mcp.py:139:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:142:        select(MCPServer).order_by(MCPServer.created_at), user
HEAD:backend/onyx/db/mcp.py:150:        select(MCPServer.id).where(MCPServer.id == server_id), user
HEAD:backend/onyx/db/mcp.py:156:    server: MCPServer, db_session: Session
HEAD:backend/onyx/db/mcp.py:158:    """User IDs with a RUNNING sandbox whose Craft session should be reloaded
HEAD:backend/onyx/db/mcp.py:160:    edited). Scoped to running sandboxes so the hot-reload push has somewhere to
HEAD:backend/onyx/db/mcp.py:165:    stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/mcp.py:172:            MCPServer__UserGroup,
HEAD:backend/onyx/db/mcp.py:173:            MCPServer__UserGroup.user_group_id == User__UserGroup.user_group_id,
HEAD:backend/onyx/db/mcp.py:175:        .where(MCPServer__UserGroup.mcp_server_id == server.id)
HEAD:backend/onyx/db/mcp.py:177:    direct_users = select(MCPServer__User.user_id).where(
HEAD:backend/onyx/db/mcp.py:178:        MCPServer__User.mcp_server_id == server.id
HEAD:backend/onyx/db/mcp.py:189:        Sandbox.user_id.in_(group_users)
HEAD:backend/onyx/db/mcp.py:190:        | Sandbox.user_id.in_(direct_users)
HEAD:backend/onyx/db/mcp.py:191:        | Sandbox.user_id.in_(owner_users)
HEAD:backend/onyx/db/mcp.py:192:        | Sandbox.user_id.in_(admin_users)
HEAD:backend/onyx/db/mcp.py:228:) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:230:    new_server = MCPServer(
HEAD:backend/onyx/db/mcp.py:266:    status: MCPServerStatus | None = None,
HEAD:backend/onyx/db/mcp.py:270:) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:373:# MCPConnectionConfig operations
HEAD:backend/onyx/db/mcp.py:376:) -> MCPConnectionConfig:
HEAD:backend/onyx/db/mcp.py:379:    stmt = select(MCPConnectionConfig).where(MCPConnectionConfig.id == config_id)
HEAD:backend/onyx/db/mcp.py:390:) -> MCPConnectionConfig | None:
HEAD:backend/onyx/db/mcp.py:393:        select(MCPConnectionConfig).where(
HEAD:backend/onyx/db/mcp.py:395:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/mcp.py:396:                MCPConnectionConfig.user_email == user_email,
HEAD:backend/onyx/db/mcp.py:404:) -> dict[int, MCPConnectionConfig]:
HEAD:backend/onyx/db/mcp.py:410:        select(MCPConnectionConfig).where(
HEAD:backend/onyx/db/mcp.py:412:                MCPConnectionConfig.mcp_server_id.in_(server_ids),
HEAD:backend/onyx/db/mcp.py:413:                MCPConnectionConfig.user_email == user_email,
HEAD:backend/onyx/db/mcp.py:422:) -> list[MCPConnectionConfig]:
HEAD:backend/onyx/db/mcp.py:426:            select(MCPConnectionConfig).where(
HEAD:backend/onyx/db/mcp.py:427:                MCPConnectionConfig.mcp_server_id == server_id
HEAD:backend/onyx/db/mcp.py:438:) -> MCPConnectionConfig:
HEAD:backend/onyx/db/mcp.py:440:    new_config = MCPConnectionConfig(
HEAD:backend/onyx/db/mcp.py:454:) -> MCPConnectionConfig:
HEAD:backend/onyx/db/mcp.py:465:) -> MCPConnectionConfig:
HEAD:backend/onyx/db/mcp.py:482:) -> MCPConnectionConfig:
HEAD:backend/onyx/db/mcp.py:511:        select(MCPConnectionConfig).where(
HEAD:backend/onyx/db/mcp.py:513:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/mcp.py:514:                MCPConnectionConfig.user_email == user_email,
HEAD:backend/onyx/db/mcp.py:530:        delete(MCPConnectionConfig).where(
HEAD:backend/onyx/db/mcp.py:532:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/mcp.py:533:                MCPConnectionConfig.user_email != "",
HEAD:backend/onyx/db/models.py:97:    MCPServerStatus,
HEAD:backend/onyx/db/models.py:109:    SandboxStatus,
HEAD:backend/onyx/db/models.py:128:from onyx.external_apps.url_glob import UrlGlob
HEAD:backend/onyx/db/models.py:495:    accessible_mcp_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:496:        "MCPServer", secondary="mcp_server__user", back_populates="users"
HEAD:backend/onyx/db/models.py:817:class ToolCall__SearchDoc(Base):
HEAD:backend/onyx/db/models.py:971:    # FILE_SYSTEM: Write to file system only (for CLI agent sandbox)
HEAD:backend/onyx/db/models.py:3402:    tool_calls: Mapped[list["ToolCall"] | None] = relationship(
HEAD:backend/onyx/db/models.py:3403:        "ToolCall",
HEAD:backend/onyx/db/models.py:3414:class ToolCall(Base):
HEAD:backend/onyx/db/models.py:3469:    parent_tool_call: Mapped["ToolCall | None"] = relationship(
HEAD:backend/onyx/db/models.py:3470:        "ToolCall",
HEAD:backend/onyx/db/models.py:3472:        remote_side="ToolCall.id",
HEAD:backend/onyx/db/models.py:3474:    tool_call_children: Mapped[list["ToolCall"]] = relationship(
HEAD:backend/onyx/db/models.py:3475:        "ToolCall",
HEAD:backend/onyx/db/models.py:3483:        secondary=ToolCall__SearchDoc.__table__,
HEAD:backend/onyx/db/models.py:3535:    tool_calls: Mapped[list["ToolCall"]] = relationship(
HEAD:backend/onyx/db/models.py:3536:        "ToolCall",
HEAD:backend/onyx/db/models.py:3537:        secondary=ToolCall__SearchDoc.__table__,
HEAD:backend/onyx/db/models.py:4055:    oauth_config: Mapped["OAuthConfig | None"] = relationship(
HEAD:backend/onyx/db/models.py:4056:        "OAuthConfig", back_populates="tools"
HEAD:backend/onyx/db/models.py:4065:    mcp_server: Mapped["MCPServer | None"] = relationship(
HEAD:backend/onyx/db/models.py:4066:        "MCPServer", back_populates="current_actions"
HEAD:backend/onyx/db/models.py:4070:class OAuthConfig(Base):
HEAD:backend/onyx/db/models.py:4151:    oauth_config: Mapped["OAuthConfig"] = relationship(
HEAD:backend/onyx/db/models.py:4152:        "OAuthConfig", back_populates="user_tokens"
HEAD:backend/onyx/db/models.py:4901:    # Immutable Agent Skills name and sandbox directory name.
HEAD:backend/onyx/db/models.py:4916:    # Existing custom rows are classified lazily before sandbox hydration.
HEAD:backend/onyx/db/models.py:5252:    accessible_mcp_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:5253:        "MCPServer", secondary="mcp_server__user_group", back_populates="user_groups"
HEAD:backend/onyx/db/models.py:5813:class MCPServer(Base):
HEAD:backend/onyx/db/models.py:5852:    status: Mapped[MCPServerStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:5853:        Enum(MCPServerStatus, native_enum=False),
HEAD:backend/onyx/db/models.py:5887:    admin_connection_config: Mapped["MCPConnectionConfig | None"] = relationship(
HEAD:backend/onyx/db/models.py:5888:        "MCPConnectionConfig",
HEAD:backend/onyx/db/models.py:5893:    user_connection_configs: Mapped[list["MCPConnectionConfig"]] = relationship(
HEAD:backend/onyx/db/models.py:5894:        "MCPConnectionConfig",
HEAD:backend/onyx/db/models.py:5895:        foreign_keys="MCPConnectionConfig.mcp_server_id",
HEAD:backend/onyx/db/models.py:5913:class MCPServer__User(Base):
HEAD:backend/onyx/db/models.py:5923:class MCPServer__UserGroup(Base):
HEAD:backend/onyx/db/models.py:5933:class MCPConnectionConfig(Base):
HEAD:backend/onyx/db/models.py:5971:    mcp_server: Mapped["MCPServer | None"] = relationship(
HEAD:backend/onyx/db/models.py:5972:        "MCPServer",
HEAD:backend/onyx/db/models.py:5976:    admin_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:5977:        "MCPServer",
HEAD:backend/onyx/db/models.py:5978:        foreign_keys="MCPServer.admin_connection_config_id",
HEAD:backend/onyx/db/models.py:6416:        # collide within one user's sandbox.
HEAD:backend/onyx/db/models.py:6427:class Sandbox(Base):
HEAD:backend/onyx/db/models.py:6428:    """Stores sandbox container metadata for users (one sandbox per user)."""
HEAD:backend/onyx/db/models.py:6430:    __tablename__ = "sandbox"
HEAD:backend/onyx/db/models.py:6442:    status: Mapped[SandboxStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:6443:        Enum(SandboxStatus, native_enum=False, name="sandboxstatus"),
HEAD:backend/onyx/db/models.py:6445:        default=SandboxStatus.PROVISIONING,
HEAD:backend/onyx/db/models.py:6472:    # be taken over. Failure diagnostics live in logs (keyed by sandbox ID +
HEAD:backend/onyx/db/models.py:6482:        Index("ix_sandbox_status", "status"),
HEAD:backend/onyx/db/models.py:6483:        Index("ix_sandbox_container_id", "container_id"),
HEAD:backend/onyx/db/models.py:6503:    # path of artifact in sandbox relative to outputs/
HEAD:backend/onyx/db/models.py:6510:    # Content hash from the sandbox manifest. Drives change detection: an
HEAD:backend/onyx/db/models.py:6520:    # Reserved for archived bytes served without the sandbox. NULL until an
HEAD:backend/onyx/db/models.py:6652:    All message data is stored in message_metadata as JSON (the raw sandbox event packet).
HEAD:backend/onyx/db/models.py:6809:    def pre_approved_external_app_ids(self) -> list[int]:
HEAD:backend/onyx/db/models.py:6813:            grant.gated_app.external_app_id
HEAD:backend/onyx/db/models.py:6815:            if grant.gated_app.external_app_id is not None
HEAD:backend/onyx/db/models.py:7067:    __tablename__ = "code_interpreter_server"
HEAD:backend/onyx/db/models.py:7189:    __tablename__ = "external_app__skill"
HEAD:backend/onyx/db/models.py:7191:        UniqueConstraint("skill_id", name="uq_external_app__skill_skill_id"),
HEAD:backend/onyx/db/models.py:7194:    external_app_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:7196:        ForeignKey("external_app.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:7207:    __tablename__ = "external_app"
HEAD:backend/onyx/db/models.py:7218:    # `external_apps.providers.PROVIDERS`.
HEAD:backend/onyx/db/models.py:7270:        back_populates="external_app",
HEAD:backend/onyx/db/models.py:7287:    __tablename__ = "external_app_user_credential"
HEAD:backend/onyx/db/models.py:7290:    external_app_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:7292:        ForeignKey("external_app.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:7326:    external_app: Mapped["ExternalApp"] = relationship(
HEAD:backend/onyx/db/models.py:7332:            "external_app_id",
HEAD:backend/onyx/db/models.py:7334:            name="uq_external_app_user_credential_app_user",
HEAD:backend/onyx/db/models.py:7351:    Exactly one of ``external_app_id`` / ``mcp_server_id`` is set; ``kind`` is
HEAD:backend/onyx/db/models.py:7359:    external_app_id: Mapped[int | None] = mapped_column(
HEAD:backend/onyx/db/models.py:7361:        ForeignKey("external_app.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:7372:        UniqueConstraint("external_app_id", name="uq_gated_app_external_app"),
HEAD:backend/onyx/db/models.py:7375:            "num_nonnulls(external_app_id, mcp_server_id) = 1",
HEAD:backend/onyx/db/models.py:7385:            GatedAppKind.EXTERNAL_APP
HEAD:backend/onyx/db/models.py:7386:            if self.external_app_id is not None
HEAD:backend/onyx/db/models.py:7394:            self.external_app_id
HEAD:backend/onyx/db/models.py:7395:            if self.external_app_id is not None
HEAD:backend/onyx/db/oauth_config.py:7:from onyx.db.models import OAuthConfig, OAuthUserToken, Tool
HEAD:backend/onyx/db/oauth_config.py:25:) -> OAuthConfig:
HEAD:backend/onyx/db/oauth_config.py:27:    oauth_config = OAuthConfig(
HEAD:backend/onyx/db/oauth_config.py:41:def get_oauth_config(oauth_config_id: int, db_session: Session) -> OAuthConfig | None:
HEAD:backend/onyx/db/oauth_config.py:44:        select(OAuthConfig).where(OAuthConfig.id == oauth_config_id)
HEAD:backend/onyx/db/oauth_config.py:48:def get_oauth_configs(db_session: Session) -> list[OAuthConfig]:
HEAD:backend/onyx/db/oauth_config.py:50:    return list(db_session.scalars(select(OAuthConfig)).all())
HEAD:backend/onyx/db/oauth_config.py:65:) -> OAuthConfig:
HEAD:backend/onyx/db/oauth_config.py:74:        select(OAuthConfig).where(OAuthConfig.id == oauth_config_id)
HEAD:backend/onyx/db/oauth_config.py:111:        select(OAuthConfig).where(OAuthConfig.id == oauth_config_id)
HEAD:backend/onyx/db/scheduled_task.py:62:    pre_approved_external_app_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:91:        external_app_ids=pre_approved_external_app_ids or [],
HEAD:backend/onyx/db/scheduled_task.py:103:    external_app_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:114:            (GatedAppKind.EXTERNAL_APP, external_app_ids),
HEAD:backend/onyx/db/scheduled_task.py:196:    pre_approved_external_app_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:226:        external_app_ids=pre_approved_external_app_ids,
HEAD:backend/onyx/db/skill.py:50:    SandboxStatus,
HEAD:backend/onyx/db/skill.py:53:from onyx.db.external_app import (
HEAD:backend/onyx/db/skill.py:55:    get_skill_external_app_dependencies,
HEAD:backend/onyx/db/skill.py:59:    Sandbox,
HEAD:backend/onyx/db/skill.py:94:    external_app_dependency: SkillExternalAppDependencyState | None
HEAD:backend/onyx/db/skill.py:256:    """Return user IDs with a running sandbox that should contain this skill.
HEAD:backend/onyx/db/skill.py:262:        stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:266:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:269:            User__UserGroup.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:276:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:281:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:284:            Skill__User.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:287:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:293:            select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:294:            .where(Sandbox.user_id == skill.author_user_id)
HEAD:backend/onyx/db/skill.py:295:            .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:322:    """Return the user's effective sandbox skills.
HEAD:backend/onyx/db/skill.py:327:    external_app_dependencies = get_skill_external_app_dependencies(db_session, user)
HEAD:backend/onyx/db/skill.py:328:    ready_external_app_skill_ids = [
HEAD:backend/onyx/db/skill.py:330:        for skill_id, dependency in external_app_dependencies.items()
HEAD:backend/onyx/db/skill.py:338:            Skill.id.in_(ready_external_app_skill_ids),
HEAD:backend/onyx/db/skill.py:468:    external_app_dependencies = get_skill_external_app_dependencies(
HEAD:backend/onyx/db/skill.py:491:                or skill_id not in external_app_dependencies
HEAD:backend/onyx/db/skill.py:492:                or external_app_dependencies[skill_id].ready
HEAD:backend/onyx/db/skill.py:494:            external_app_dependency=external_app_dependencies.get(skill_id),
HEAD:backend/onyx/db/tools.py:10:from onyx.db.enums import MCPServerStatus, Permission, PermissionAuthority
HEAD:backend/onyx/db/tools.py:12:    MCPServer,
HEAD:backend/onyx/db/tools.py:13:    OAuthConfig,
HEAD:backend/onyx/db/tools.py:18:    ToolCall,
HEAD:backend/onyx/db/tools.py:46:        query = query.outerjoin(MCPServer, Tool.mcp_server_id == MCPServer.id).where(
HEAD:backend/onyx/db/tools.py:49:                MCPServer.status == MCPServerStatus.CONNECTED,  # MCP tools connected
HEAD:backend/onyx/db/tools.py:111:def can_manage_mcp_server(user: User, server: MCPServer) -> bool:
HEAD:backend/onyx/db/tools.py:271:    # Clean up orphaned OAuthConfig if the oauth_config_id was changed
HEAD:backend/onyx/db/tools.py:281:            oauth_config = db_session.get(OAuthConfig, old_oauth_config_id)
HEAD:backend/onyx/db/tools.py:299:    # Clean up orphaned OAuthConfig if no other tools reference it
HEAD:backend/onyx/db/tools.py:305:            oauth_config = db_session.get(OAuthConfig, oauth_config_id)
HEAD:backend/onyx/db/tools.py:361:) -> ToolCall:
HEAD:backend/onyx/db/tools.py:363:    Create a ToolCall entry in the database.
HEAD:backend/onyx/db/tools.py:382:        The created ToolCall object
HEAD:backend/onyx/db/tools.py:384:    tool_call = ToolCall(
HEAD:backend/onyx/db/users.py:27:    MCPConnectionConfig,
HEAD:backend/onyx/db/users.py:28:    MCPServer,
HEAD:backend/onyx/db/users.py:661:        update(MCPServer)
HEAD:backend/onyx/db/users.py:662:        .where(MCPServer.owner == old_email)
HEAD:backend/onyx/db/users.py:666:        update(MCPConnectionConfig)
HEAD:backend/onyx/db/users.py:667:        .where(MCPConnectionConfig.user_email == old_email)
HEAD:backend/onyx/db/users.py:693:    sandbox/session reservation). Hold only for a short transaction."""
HEAD:backend/onyx/deep_research/dr_loop.py:19:    ToolCallSimple,
HEAD:backend/onyx/deep_research/dr_loop.py:71:from onyx.tools.models import ToolCallInfo, ToolCallKickoff
HEAD:backend/onyx/deep_research/dr_loop.py:499:                research_agent_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/deep_research/dr_loop.py:635:                        think_tool_simple = ToolCallSimple(
HEAD:backend/onyx/deep_research/dr_loop.py:738:                    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/deep_research/dr_loop.py:743:                            ToolCallSimple(
HEAD:backend/onyx/deep_research/dr_loop.py:793:                        tool_call_info = ToolCallInfo(
HEAD:backend/onyx/deep_research/models.py:4:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/deep_research/models.py:7:class SpecialToolCalls(BaseModel):
HEAD:backend/onyx/deep_research/models.py:8:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/models.py:9:    generate_report_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:7:from onyx.deep_research.models import SpecialToolCalls
HEAD:backend/onyx/deep_research/utils.py:8:from onyx.llm.model_response import ChatCompletionDeltaToolCall, Delta, FunctionCall
HEAD:backend/onyx/deep_research/utils.py:9:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/deep_research/utils.py:143:                complete_tool_call = ChatCompletionDeltaToolCall(
HEAD:backend/onyx/deep_research/utils.py:199:def check_special_tool_calls(tool_calls: list[ToolCallKickoff]) -> SpecialToolCalls:
HEAD:backend/onyx/deep_research/utils.py:200:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:201:    generate_report_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:209:    return SpecialToolCalls(
HEAD:backend/onyx/evals/README.md:109:    "expected_tools": ["PythonTool"],
HEAD:backend/onyx/evals/README.md:157:- `PythonTool`: Python code execution
HEAD:backend/onyx/external_apps/credentials.py:6:from onyx.db.external_app import (
HEAD:backend/onyx/external_apps/credentials.py:7:    get_external_app_by_id,
HEAD:backend/onyx/external_apps/credentials.py:8:    get_external_app_user_credential,
HEAD:backend/onyx/external_apps/credentials.py:40:    external_app_id: int,
HEAD:backend/onyx/external_apps/credentials.py:44:    ``external_app_id`` on behalf of ``user_id``.
HEAD:backend/onyx/external_apps/credentials.py:51:    app = get_external_app_by_id(db_session, external_app_id)
HEAD:backend/onyx/external_apps/credentials.py:58:    user_cred = get_external_app_user_credential(
HEAD:backend/onyx/external_apps/credentials.py:59:        db_session, external_app_id=external_app_id, user_id=user_id
HEAD:backend/onyx/external_apps/matching/engine.py:13:from onyx.external_apps.matching.request import MatchContext, ProxiedRequest
HEAD:backend/onyx/external_apps/matching/engine.py:14:from onyx.external_apps.matching.rules import rule_matches
HEAD:backend/onyx/external_apps/matching/engine.py:15:from onyx.external_apps.providers.registry import (
HEAD:backend/onyx/external_apps/matching/engine.py:40:    ``id`` indexes the table named by ``kind`` — ``external_app`` or
HEAD:backend/onyx/external_apps/matching/engine.py:154:    stored = get_action_policies(db_session, GatedAppKind.EXTERNAL_APP, app.id)
HEAD:backend/onyx/external_apps/matching/engine.py:171:            kind=GatedAppKind.EXTERNAL_APP, id=app.id, app_name=_app_name(app)
HEAD:backend/onyx/external_apps/matching/engine.py:211:            kind=GatedAppKind.EXTERNAL_APP, id=app.id, app_name=_app_name(app)
HEAD:backend/onyx/external_apps/matching/request.py:8:from onyx.external_apps.matching.graphql_parsing import parse_invocations
HEAD:backend/onyx/external_apps/matching/request.py:12:    """The normalised form of an outbound sandbox request, transport-agnostic.
HEAD:backend/onyx/external_apps/matching/request.py:14:    The proxy builds one of these from whatever the sandbox emitted (the Python
HEAD:backend/onyx/external_apps/matching/rules.py:10:from onyx.external_apps.matching.request import MatchContext
HEAD:backend/onyx/external_apps/matching/rules.py:11:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/matching/rules.py:68:            "add one in onyx.external_apps.matching.rules."
HEAD:backend/onyx/external_apps/presentation/decode.py:3:from onyx.external_apps.presentation.payload_decoders import PayloadDecoder
HEAD:backend/onyx/external_apps/presentation/decode.py:4:from onyx.external_apps.providers.registry import PROVIDERS
HEAD:backend/onyx/external_apps/providers/base.py:9:from onyx.external_apps.presentation.payload_decoders import PayloadDecoder
HEAD:backend/onyx/external_apps/providers/base.py:10:from onyx.external_apps.providers.actions import EndpointSpec
HEAD:backend/onyx/external_apps/providers/github.py:12:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/github.py:18:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/providers/gmail.py:8:from onyx.external_apps.presentation.payload_decoders import (
HEAD:backend/onyx/external_apps/providers/gmail.py:12:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/gmail.py:17:from onyx.external_apps.providers.base import OnyxManagedExtApp
HEAD:backend/onyx/external_apps/providers/gmail.py:18:from onyx.external_apps.providers.google_base import GoogleOAuthProvider
HEAD:backend/onyx/external_apps/providers/google_base.py:6:from onyx.external_apps.providers.actions import EndpointSpec
HEAD:backend/onyx/external_apps/providers/google_base.py:7:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/providers/google_calendar.py:6:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/google_calendar.py:11:from onyx.external_apps.providers.base import OnyxManagedExtApp
HEAD:backend/onyx/external_apps/providers/google_calendar.py:12:from onyx.external_apps.providers.google_base import GoogleOAuthProvider
HEAD:backend/onyx/external_apps/providers/google_drive.py:6:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/google_drive.py:11:from onyx.external_apps.providers.base import OnyxManagedExtApp
HEAD:backend/onyx/external_apps/providers/google_drive.py:12:from onyx.external_apps.providers.google_base import GoogleOAuthProvider
HEAD:backend/onyx/external_apps/providers/hubspot.py:13:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/hubspot.py:18:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/providers/linear.py:10:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/linear.py:15:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/providers/notion.py:11:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/notion.py:16:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/providers/notion.py:26:# Pinned across the provider and the sandbox skill so request-shaping stays
HEAD:backend/onyx/external_apps/providers/registry.py:5:from onyx.external_apps.models import (
HEAD:backend/onyx/external_apps/providers/registry.py:11:from onyx.external_apps.providers.actions import EndpointSpec
HEAD:backend/onyx/external_apps/providers/registry.py:12:from onyx.external_apps.providers.base import ExternalAppProvider, OnyxManagedExtApp
HEAD:backend/onyx/external_apps/providers/registry.py:13:from onyx.external_apps.providers.github import GitHubProvider
HEAD:backend/onyx/external_apps/providers/registry.py:14:from onyx.external_apps.providers.gmail import GmailProvider
HEAD:backend/onyx/external_apps/providers/registry.py:15:from onyx.external_apps.providers.google_calendar import GoogleCalendarProvider
HEAD:backend/onyx/external_apps/providers/registry.py:16:from onyx.external_apps.providers.google_drive import GoogleDriveProvider
HEAD:backend/onyx/external_apps/providers/registry.py:17:from onyx.external_apps.providers.hubspot import HubspotProvider
HEAD:backend/onyx/external_apps/providers/registry.py:18:from onyx.external_apps.providers.linear import LinearProvider
HEAD:backend/onyx/external_apps/providers/registry.py:19:from onyx.external_apps.providers.notion import NotionProvider
HEAD:backend/onyx/external_apps/providers/registry.py:20:from onyx.external_apps.providers.slack import SlackProvider
HEAD:backend/onyx/external_apps/providers/slack.py:10:from onyx.external_apps.providers.actions import (
HEAD:backend/onyx/external_apps/providers/slack.py:15:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/token_refresh.py:18:from onyx.db.external_app import (
HEAD:backend/onyx/external_apps/token_refresh.py:19:    disconnect_external_app_for_user,
HEAD:backend/onyx/external_apps/token_refresh.py:20:    get_external_app_by_id,
HEAD:backend/onyx/external_apps/token_refresh.py:21:    get_external_app_user_credential,
HEAD:backend/onyx/external_apps/token_refresh.py:22:    upsert_external_app_user_credential,
HEAD:backend/onyx/external_apps/token_refresh.py:25:from onyx.external_apps.providers.base import (
HEAD:backend/onyx/external_apps/token_refresh.py:30:from onyx.external_apps.providers.registry import get_provider_for_app
HEAD:backend/onyx/external_apps/token_refresh.py:31:from onyx.external_apps.token_utils import needs_refresh, stamp_expires_at
HEAD:backend/onyx/external_apps/token_refresh.py:49:    external_app_id: int,
```
## Credential and Secret Storage Mechanisms
Evidence lines: 600
```text
HEAD:backend/ee/onyx/auth/users.py:7:from ee.onyx.configs.app_configs import SUPER_CLOUD_API_KEY, SUPER_USERS
HEAD:backend/ee/onyx/auth/users.py:29:    if not SUPER_CLOUD_API_KEY:
HEAD:backend/ee/onyx/auth/users.py:30:        logger.warning("SUPER_CLOUD_API_KEY is not configured; rejecting request")
HEAD:backend/ee/onyx/auth/users.py:33:    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
HEAD:backend/ee/onyx/auth/users.py:34:    if not secrets.compare_digest(api_key, SUPER_CLOUD_API_KEY):
HEAD:backend/ee/onyx/configs/app_configs.py:145:SUPER_CLOUD_API_KEY: str | None = os.environ.get("SUPER_CLOUD_API_KEY")
HEAD:backend/ee/onyx/configs/app_configs.py:151:POSTHOG_API_KEY = os.environ.get("POSTHOG_API_KEY")
HEAD:backend/ee/onyx/configs/app_configs.py:157:MARKETING_POSTHOG_API_KEY = os.environ.get("MARKETING_POSTHOG_API_KEY")
HEAD:backend/ee/onyx/db/saml.py:28:        existing_saml_acc.encrypted_cookie = cookie
HEAD:backend/ee/onyx/db/saml.py:35:            encrypted_cookie=cookie,
HEAD:backend/ee/onyx/db/saml.py:55:                SamlAccount.encrypted_cookie == cookie,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:874:    users with emails like `__DANSWER_API_KEY_*` that should not count toward
HEAD:backend/ee/onyx/external_permissions/box/access.py:121:    if shared_link_access == "open" and not shared_link.is_password_enabled:
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:24:    box_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:6:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:58:    creds = credential_json(cc_pair)
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:24:    canvas_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:5:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:78:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:20:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:54:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:22:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:8:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:57:    gmail_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:17:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:390:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:16:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:510:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:29:    jira_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:9:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:166:        credentials=credential_json(cc_pair),
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:29:    sharepoint_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:27:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:30:    teams_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/utils.py:21:def credential_json(cc_pair: ConnectorCredentialPair) -> dict[str, Any]:
HEAD:backend/ee/onyx/external_permissions/utils.py:23:        cc_pair.credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/external_permissions/utils.py:24:        if cc_pair.credential.credential_json
HEAD:backend/ee/onyx/feature_flags/factory.py:13:    When the PostHog client isn't configured (no `POSTHOG_API_KEY` — the
HEAD:backend/ee/onyx/hooks/executor.py:179:        api_key=hook.api_key.get_value(apply_mask=False) if hook.api_key else None,
HEAD:backend/ee/onyx/main.py:42:from ee.onyx.utils.encryption import test_encryption
HEAD:backend/ee/onyx/main.py:48:    OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/main.py:86:    test_encryption()
HEAD:backend/ee/onyx/main.py:115:            OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:61:    access_token: str
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:62:    refresh_token: str
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:123:async def refresh_access_token(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:124:    refresh_token: RefreshTokenData,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:133:    account_id = str(refresh_token.userinfo["userId"])
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:134:    account_email = str(refresh_token.userinfo["email"])
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:145:        new_access_token = refresh_token.access_token
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:146:        new_refresh_token = refresh_token.refresh_token
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:149:            refresh_token.session["exp"] / 1000, tz=timezone.utc
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:157:            access_token=new_access_token,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:164:            refresh_token=new_refresh_token,
HEAD:backend/ee/onyx/server/features/hooks/api.py:85:        api_key_masked=(
HEAD:backend/ee/onyx/server/features/hooks/api.py:86:            hook.api_key.get_value(apply_mask=True) if hook.api_key else None
HEAD:backend/ee/onyx/server/features/hooks/api.py:134:    api_key: str | None,
HEAD:backend/ee/onyx/server/features/hooks/api.py:142:    (not reachable — indicates the api_key is invalid).
HEAD:backend/ee/onyx/server/features/hooks/api.py:151:    if api_key:
HEAD:backend/ee/onyx/server/features/hooks/api.py:152:        headers["Authorization"] = f"Bearer {api_key}"
HEAD:backend/ee/onyx/server/features/hooks/api.py:237:    the endpoint cannot be reached or the api_key is invalid. Hooks are created active.
HEAD:backend/ee/onyx/server/features/hooks/api.py:240:    api_key = req.api_key.get_secret_value() if req.api_key else None
HEAD:backend/ee/onyx/server/features/hooks/api.py:243:        api_key=api_key,
HEAD:backend/ee/onyx/server/features/hooks/api.py:254:        api_key=api_key,
HEAD:backend/ee/onyx/server/features/hooks/api.py:284:    """Update hook fields. If endpoint_url, api_key, or timeout_seconds changes, the
HEAD:backend/ee/onyx/server/features/hooks/api.py:292:    # api_key: UNSET = no change, None = clear, value = update
HEAD:backend/ee/onyx/server/features/hooks/api.py:293:    api_key: str | None | UnsetType
HEAD:backend/ee/onyx/server/features/hooks/api.py:294:    if "api_key" not in req.model_fields_set:
HEAD:backend/ee/onyx/server/features/hooks/api.py:295:        api_key = UNSET
HEAD:backend/ee/onyx/server/features/hooks/api.py:296:    elif req.api_key is None:
HEAD:backend/ee/onyx/server/features/hooks/api.py:297:        api_key = None
HEAD:backend/ee/onyx/server/features/hooks/api.py:299:        api_key = req.api_key.get_secret_value()
HEAD:backend/ee/onyx/server/features/hooks/api.py:302:    api_key_changing = not isinstance(api_key, UnsetType)
HEAD:backend/ee/onyx/server/features/hooks/api.py:306:    if endpoint_url_changing or api_key_changing or timeout_changing:
HEAD:backend/ee/onyx/server/features/hooks/api.py:313:        effective_api_key: str | None = (
HEAD:backend/ee/onyx/server/features/hooks/api.py:314:            (api_key if not isinstance(api_key, UnsetType) else None)
HEAD:backend/ee/onyx/server/features/hooks/api.py:315:            if api_key_changing
HEAD:backend/ee/onyx/server/features/hooks/api.py:317:                existing.api_key.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/features/hooks/api.py:318:                if existing.api_key
HEAD:backend/ee/onyx/server/features/hooks/api.py:329:            api_key=effective_api_key,
HEAD:backend/ee/onyx/server/features/hooks/api.py:341:        api_key=api_key,
HEAD:backend/ee/onyx/server/features/hooks/api.py:375:    api_key = hook.api_key.get_value(apply_mask=False) if hook.api_key else None
HEAD:backend/ee/onyx/server/features/hooks/api.py:378:        api_key=api_key,
HEAD:backend/ee/onyx/server/features/hooks/api.py:417:    api_key = hook.api_key.get_value(apply_mask=False) if hook.api_key else None
HEAD:backend/ee/onyx/server/features/hooks/api.py:420:        api_key=api_key,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:146:    if not provider.api_key:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:157:            "x-api-key": provider.api_key,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:200:    if not provider.api_key:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:210:            "Authorization": f"Bearer {provider.api_key}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:17:    OAUTH_CONFLUENCE_CLOUD_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:25:    update_credential_json,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:48:        access_token: str
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:51:        refresh_token: str
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:62:    CLIENT_SECRET = OAUTH_CONFLUENCE_CLOUD_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:156:    if not ConfluenceCloudOAuth.CLIENT_ID or not ConfluenceCloudOAuth.CLIENT_SECRET:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:200:                "client_secret": ConfluenceCloudOAuth.CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:222:            credential_json={
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:223:                "confluence_access_token": token_response.access_token,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:224:                "confluence_refresh_token": token_response.refresh_token,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:274:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:275:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:278:    access_token = credential_dict["confluence_access_token"]
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:285:                "Authorization": f"Bearer {access_token}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:344:    existing_credential_json = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:345:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:346:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:349:    new_credential_json: dict[str, Any] = dict(existing_credential_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:350:    new_credential_json["cloud_id"] = cloud_id
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:351:    new_credential_json["cloud_name"] = cloud_name
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:352:    new_credential_json["wiki_base"] = cloud_url
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:355:        update_credential_json(credential_id, new_credential_json, user, db_session)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:17:    OAUTH_GOOGLE_DRIVE_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:51:    CLIENT_SECRET = OAUTH_GOOGLE_DRIVE_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/google_drive.py:118:    if not GoogleDriveOAuth.CLIENT_ID or not GoogleDriveOAuth.CLIENT_SECRET:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:162:                "client_secret": GoogleDriveOAuth.CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:179:        authorized_user_info["client_secret"] = OAUTH_GOOGLE_DRIVE_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/google_drive.py:180:        authorized_user_info["refresh_token"] = authorization_response["refresh_token"]
HEAD:backend/ee/onyx/server/oauth/google_drive.py:200:            credential_json=credential_dict,
HEAD:backend/ee/onyx/server/oauth/slack.py:16:    OAUTH_SLACK_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/slack.py:40:    CLIENT_SECRET = OAUTH_SLACK_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/slack.py:107:    if not SlackOAuth.CLIENT_ID or not SlackOAuth.CLIENT_SECRET:
HEAD:backend/ee/onyx/server/oauth/slack.py:151:                "client_secret": SlackOAuth.CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/slack.py:166:        access_token: str = response_data.get("access_token")
HEAD:backend/ee/onyx/server/oauth/slack.py:171:            credential_json={"slack_bot_token": access_token},
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:77:        llm_provider_api_key=llm.config.api_key,
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:7:from onyx.db.api_key import is_api_key_email_address
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:40:    elif is_api_key_email_address(user.email):
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:11:from onyx.db.api_key import is_api_key_email_address
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:147:        if row.email != DELETED_USER_EXPORT_EMAIL and not is_api_key_email_address(
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:182:    users = get_all_users(db_session, include_api_key_users=False)
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:39:from onyx.configs.constants import DANSWER_API_KEY_PREFIX, UNNAMED_KEY_PLACEHOLDER
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:40:from onyx.db.api_key import is_api_key_email_address
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:68:    `API_KEY__<key name>@<uuid>onyxapikey.ai`, so per-key spend already
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:72:    if not is_api_key_email_address(name):
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:79:    if local_part.lower().startswith(DANSWER_API_KEY_PREFIX.lower()):
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:80:        local_part = local_part[len(DANSWER_API_KEY_PREFIX) :]
HEAD:backend/ee/onyx/server/scim/api.py:20:from fastapi_users.password import PasswordHelper
HEAD:backend/ee/onyx/server/scim/api.py:90:    return AuditActor(api_key_id=f"scim_token:{token.id}", auth_type="scim")
HEAD:backend/ee/onyx/server/scim/api.py:155:_pw_helper = PasswordHelper()
HEAD:backend/ee/onyx/server/scim/api.py:865:    # Create user with a random password (SCIM users authenticate via IdP)
HEAD:backend/ee/onyx/server/scim/api.py:869:        hashed_password=_pw_helper.hash(_pw_helper.generate()),
HEAD:backend/ee/onyx/server/scim/auth.py:59:    (``generate_api_key``). An IdP presents only this bearer token, so the
HEAD:backend/ee/onyx/server/scim/models.py:290:    changePassword: ScimSupported = ScimSupported(supported=False)
HEAD:backend/ee/onyx/server/tenants/access.py:6:from onyx.configs.app_configs import DATA_PLANE_SECRET, EXPECTED_API_KEY, JWT_ALGORITHM
HEAD:backend/ee/onyx/server/tenants/access.py:28:    api_key = request.headers.get("X-API-KEY")
HEAD:backend/ee/onyx/server/tenants/access.py:29:    if api_key != EXPECTED_API_KEY:
HEAD:backend/ee/onyx/server/tenants/billing.py:24:stripe.api_key = STRIPE_SECRET_KEY
HEAD:backend/ee/onyx/server/tenants/provisioning.py:29:    ANTHROPIC_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:31:    COHERE_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:34:    OPENAI_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:35:    OPENROUTER_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:44:from onyx.db.image_generation import create_default_image_gen_config_from_api_key
HEAD:backend/ee/onyx/server/tenants/provisioning.py:375:def configure_default_api_keys(db_session: Session) -> None:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:405:    if OPENAI_DEFAULT_API_KEY and AUTO_PROVISION_DEFAULT_LLM_PROVIDERS:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:416:            api_key=OPENAI_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:420:            api_key_changed=True,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:427:            create_default_image_gen_config_from_api_key(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:428:                db_session, OPENAI_DEFAULT_API_KEY
HEAD:backend/ee/onyx/server/tenants/provisioning.py:435:            "(OPENAI_DEFAULT_API_KEY unset or AUTO_PROVISION_DEFAULT_LLM_PROVIDERS=false)"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:439:    if ANTHROPIC_DEFAULT_API_KEY and AUTO_PROVISION_DEFAULT_LLM_PROVIDERS:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:453:            api_key=ANTHROPIC_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:457:            api_key_changed=True,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:464:            "(ANTHROPIC_DEFAULT_API_KEY unset or AUTO_PROVISION_DEFAULT_LLM_PROVIDERS=false)"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:490:            api_key_changed=True,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:500:    if OPENROUTER_DEFAULT_API_KEY and AUTO_PROVISION_DEFAULT_LLM_PROVIDERS:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:525:            api_key=OPENROUTER_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:527:            api_key_changed=True,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:534:            "(OPENROUTER_DEFAULT_API_KEY unset or AUTO_PROVISION_DEFAULT_LLM_PROVIDERS=false)"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:538:    if COHERE_DEFAULT_API_KEY:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:541:            api_key=COHERE_DEFAULT_API_KEY,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:589:            "COHERE_DEFAULT_API_KEY not set, skipping Cohere embedding provider configuration"
HEAD:backend/ee/onyx/server/tenants/provisioning.py:749:            configure_default_api_keys(db_session)
HEAD:backend/ee/onyx/server/tenants/schema_management.py:31:        password=spec.password,
HEAD:backend/ee/onyx/utils/encryption.py:8:from onyx.configs.app_configs import ENCRYPTION_KEY_SECRET
HEAD:backend/ee/onyx/utils/encryption.py:20:        raise RuntimeError("Invalid ENCRYPTION_KEY_SECRET - too short")
HEAD:backend/ee/onyx/utils/encryption.py:31:def _encrypt_string(input_str: str, key: str | None = None) -> bytes:
HEAD:backend/ee/onyx/utils/encryption.py:32:    effective_key = key if key is not None else ENCRYPTION_KEY_SECRET
HEAD:backend/ee/onyx/utils/encryption.py:42:    encryptor = cipher.encryptor()
HEAD:backend/ee/onyx/utils/encryption.py:43:    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
HEAD:backend/ee/onyx/utils/encryption.py:45:    return iv + encrypted_data
HEAD:backend/ee/onyx/utils/encryption.py:48:def _decrypt_bytes(input_bytes: bytes, key: str | None = None) -> str:
HEAD:backend/ee/onyx/utils/encryption.py:49:    effective_key = key if key is not None else ENCRYPTION_KEY_SECRET
HEAD:backend/ee/onyx/utils/encryption.py:56:        encrypted_data = input_bytes[16:]
HEAD:backend/ee/onyx/utils/encryption.py:61:        decryptor = cipher.decryptor()
HEAD:backend/ee/onyx/utils/encryption.py:62:        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
HEAD:backend/ee/onyx/utils/encryption.py:65:        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
HEAD:backend/ee/onyx/utils/encryption.py:67:        return decrypted_data.decode()
HEAD:backend/ee/onyx/utils/encryption.py:73:        # Does NOT handle data encrypted with a different key — that
HEAD:backend/ee/onyx/utils/encryption.py:76:            "AES decryption failed — falling back to raw decode. Run the re-encrypt secrets script to rotate to the current key."
HEAD:backend/ee/onyx/utils/encryption.py:82:                "Data is not valid UTF-8 — likely encrypted with a different key. "
HEAD:backend/ee/onyx/utils/encryption.py:83:                "Run the re-encrypt secrets script to rotate to the current key."
HEAD:backend/ee/onyx/utils/encryption.py:87:def encrypt_string_to_bytes(input_str: str, key: str | None = None) -> bytes:
HEAD:backend/ee/onyx/utils/encryption.py:88:    versioned_encryption_fn = fetch_versioned_implementation(
HEAD:backend/ee/onyx/utils/encryption.py:89:        "onyx.utils.encryption", "_encrypt_string"
HEAD:backend/ee/onyx/utils/encryption.py:91:    return versioned_encryption_fn(input_str, key=key)
HEAD:backend/ee/onyx/utils/encryption.py:94:def decrypt_bytes_to_string(input_bytes: bytes, key: str | None = None) -> str:
HEAD:backend/ee/onyx/utils/encryption.py:95:    versioned_decryption_fn = fetch_versioned_implementation(
HEAD:backend/ee/onyx/utils/encryption.py:96:        "onyx.utils.encryption", "_decrypt_bytes"
HEAD:backend/ee/onyx/utils/encryption.py:98:    return versioned_decryption_fn(input_bytes, key=key)
HEAD:backend/ee/onyx/utils/encryption.py:101:def test_encryption() -> None:
HEAD:backend/ee/onyx/utils/encryption.py:103:    encrypted_bytes = encrypt_string_to_bytes(test_string)
HEAD:backend/ee/onyx/utils/encryption.py:104:    decrypted_string = decrypt_bytes_to_string(encrypted_bytes)
HEAD:backend/ee/onyx/utils/encryption.py:105:    if test_string != decrypted_string:
HEAD:backend/ee/onyx/utils/encryption.py:106:        raise RuntimeError("Encryption decryption test failed")
HEAD:backend/ee/onyx/utils/posthog_client.py:8:    MARKETING_POSTHOG_API_KEY,
HEAD:backend/ee/onyx/utils/posthog_client.py:9:    POSTHOG_API_KEY,
HEAD:backend/ee/onyx/utils/posthog_client.py:25:if POSTHOG_API_KEY:
HEAD:backend/ee/onyx/utils/posthog_client.py:27:        project_api_key=POSTHOG_API_KEY,
HEAD:backend/ee/onyx/utils/posthog_client.py:34:        "POSTHOG_API_KEY is not set but MULTI_TENANT is enabled — "
HEAD:backend/ee/onyx/utils/posthog_client.py:43:if MARKETING_POSTHOG_API_KEY:
HEAD:backend/ee/onyx/utils/posthog_client.py:45:        project_api_key=MARKETING_POSTHOG_API_KEY,
HEAD:backend/ee/onyx/utils/posthog_client.py:103:    if not POSTHOG_API_KEY:
HEAD:backend/ee/onyx/utils/posthog_client.py:106:    cookie_name = f"ph_{POSTHOG_API_KEY}_posthog"
HEAD:backend/ee/onyx/utils/posthog_client.py:116:    if not MARKETING_POSTHOG_API_KEY:
HEAD:backend/ee/onyx/utils/posthog_client.py:118:    return f"onyx_custom_ph_{MARKETING_POSTHOG_API_KEY}_posthog"
HEAD:backend/onyx/auth/anonymous_user.py:60:        password_configured=False,
HEAD:backend/onyx/auth/api_key.py:11:    API_KEY_LENGTH,
HEAD:backend/onyx/auth/api_key.py:12:    API_KEY_PREFIX,
HEAD:backend/onyx/auth/api_key.py:13:    DEPRECATED_API_KEY_PREFIX,
HEAD:backend/onyx/auth/api_key.py:16:from onyx.configs.app_configs import API_KEY_HASH_ROUNDS
HEAD:backend/onyx/auth/api_key.py:22:    api_key_id: int
HEAD:backend/onyx/auth/api_key.py:23:    api_key_display: str
HEAD:backend/onyx/auth/api_key.py:24:    api_key: str | None = None  # only present on initial creation
HEAD:backend/onyx/auth/api_key.py:25:    api_key_name: str | None = None
HEAD:backend/onyx/auth/api_key.py:31:def generate_api_key(tenant_id: str | None = None) -> str:
HEAD:backend/onyx/auth/api_key.py:33:        return API_KEY_PREFIX + secrets.token_urlsafe(API_KEY_LENGTH)
HEAD:backend/onyx/auth/api_key.py:36:    return f"{API_KEY_PREFIX}{encoded_tenant}.{secrets.token_urlsafe(API_KEY_LENGTH)}"
HEAD:backend/onyx/auth/api_key.py:39:def _deprecated_hash_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:40:    return sha256_crypt.hash(api_key, salt="", rounds=API_KEY_HASH_ROUNDS)
HEAD:backend/onyx/auth/api_key.py:43:def hash_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:46:    if api_key.startswith(API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:47:        return hashlib.sha256(api_key.encode("utf-8")).hexdigest()
HEAD:backend/onyx/auth/api_key.py:49:    if api_key.startswith(DEPRECATED_API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:50:        return _deprecated_hash_api_key(api_key)
HEAD:backend/onyx/auth/api_key.py:52:    raise ValueError(f"Invalid API key prefix: {api_key[:3]}")
HEAD:backend/onyx/auth/api_key.py:55:def build_displayable_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:56:    if api_key.startswith(API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:57:        api_key = api_key[len(API_KEY_PREFIX) :]
HEAD:backend/onyx/auth/api_key.py:59:    return API_KEY_PREFIX + api_key[:4] + "********" + api_key[-4:]
HEAD:backend/onyx/auth/api_key.py:62:def get_hashed_api_key_from_request(request: Request) -> str | None:
HEAD:backend/onyx/auth/api_key.py:69:        valid_prefixes=[API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX],
HEAD:backend/onyx/auth/api_key.py:70:        hash_fn=hash_api_key,
HEAD:backend/onyx/auth/captcha.py:5:1. Email/password signup — ``UserManager.create`` verifies the token
HEAD:backend/onyx/auth/captcha.py:29:    RECAPTCHA_ENTERPRISE_API_KEY,
HEAD:backend/onyx/auth/captcha.py:105:        and bool(RECAPTCHA_ENTERPRISE_API_KEY)
HEAD:backend/onyx/auth/captcha.py:241:                params={"key": RECAPTCHA_ENTERPRISE_API_KEY},
HEAD:backend/onyx/auth/constants.py:4:API_KEY_PREFIX = "on_"
HEAD:backend/onyx/auth/constants.py:5:DEPRECATED_API_KEY_PREFIX = "dn_"
HEAD:backend/onyx/auth/constants.py:6:API_KEY_LENGTH = 192
HEAD:backend/onyx/auth/constants.py:18:API_KEY_HEADER_NAME = "Authorization"
HEAD:backend/onyx/auth/constants.py:19:API_KEY_HEADER_ALTERNATIVE_NAME = "X-Onyx-Authorization"
HEAD:backend/onyx/auth/email_utils.py:27:    SENDGRID_API_KEY,
HEAD:backend/onyx/auth/email_utils.py:197:    if SENDGRID_API_KEY:
HEAD:backend/onyx/auth/email_utils.py:264:    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
HEAD:backend/onyx/auth/email_utils.py:373:    # Cloud offers Google login alongside password signup.
HEAD:backend/onyx/auth/email_utils.py:376:            "<p>To join the organization, please click the button below to set a password "
HEAD:backend/onyx/auth/email_utils.py:380:        message += "<p>To join the organization, please click the button below to set a password and complete your registration.</p>"
HEAD:backend/onyx/auth/email_utils.py:400:        text_content += "You'll be asked to set a password or login with Google to complete your registration."
HEAD:backend/onyx/auth/email_utils.py:432:def send_forgot_password_email(
HEAD:backend/onyx/auth/email_utils.py:438:    # Builds a forgot password email with or without fancy HTML
HEAD:backend/onyx/auth/email_utils.py:450:    subject = f"Reset Your {application_name} Password"
HEAD:backend/onyx/auth/email_utils.py:451:    heading = "Reset Your Password"
HEAD:backend/onyx/auth/email_utils.py:453:    message = "<p>Please click the button below to reset your password. This link will expire in 24 hours.</p>"
HEAD:backend/onyx/auth/email_utils.py:454:    cta_text = "Reset Password"
HEAD:backend/onyx/auth/email_utils.py:455:    cta_link = f"{WEB_DOMAIN}/auth/reset-password?token={token}{tenant_param}"
HEAD:backend/onyx/auth/email_utils.py:464:        f"Please click the following link to reset your password. This link will expire in 24 hours.\n"
HEAD:backend/onyx/auth/email_utils.py:465:        f"{WEB_DOMAIN}/auth/reset-password?token={token}{tenant_param}"
HEAD:backend/onyx/auth/login_claims_capture.py:231:    userinfo_endpoint: str, access_token: str
HEAD:backend/onyx/auth/login_claims_capture.py:236:            headers={"Authorization": f"Bearer {access_token}"},
HEAD:backend/onyx/auth/login_claims_capture.py:248:async def _fetch_ms_graph_profile(access_token: str) -> dict[str, Any]:
HEAD:backend/onyx/auth/login_claims_capture.py:257:            headers={"Authorization": f"Bearer {access_token}"},
HEAD:backend/onyx/auth/login_claims_capture.py:332:        access_token = token.get("access_token")
HEAD:backend/onyx/auth/login_claims_capture.py:333:        if userinfo_endpoint and access_token:
HEAD:backend/onyx/auth/login_claims_capture.py:335:                userinfo = await _fetch_userinfo(userinfo_endpoint, access_token)
HEAD:backend/onyx/auth/login_claims_capture.py:345:        if access_token and userinfo_endpoint and _MS_GRAPH_HOST in userinfo_endpoint:
HEAD:backend/onyx/auth/login_claims_capture.py:347:                directory_profile = await _fetch_ms_graph_profile(access_token)
HEAD:backend/onyx/auth/login_claims_capture.py:368:                "has_refresh_token": bool(token.get("refresh_token")),
HEAD:backend/onyx/auth/oauth_refresher.py:17:    OAUTH_CLIENT_SECRET,
HEAD:backend/onyx/auth/oauth_refresher.py:194:    client_secret: str = field(repr=False)
HEAD:backend/onyx/auth/oauth_refresher.py:226:                "Could not read SSO provider %s config (re-encryption needed after "
HEAD:backend/onyx/auth/oauth_refresher.py:232:        client_secret = config.get("client_secret") or ""
HEAD:backend/onyx/auth/oauth_refresher.py:238:        if endpoint and client_id and client_secret:
HEAD:backend/onyx/auth/oauth_refresher.py:239:            return _RefreshContext(endpoint, client_id, client_secret)
HEAD:backend/onyx/auth/oauth_refresher.py:242:            "has_client_id=%s has_client_secret=%s",
HEAD:backend/onyx/auth/oauth_refresher.py:246:            bool(client_secret),
HEAD:backend/onyx/auth/oauth_refresher.py:254:    if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_SECRET:
HEAD:backend/onyx/auth/oauth_refresher.py:259:    return _RefreshContext(endpoint, OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET)
HEAD:backend/onyx/auth/oauth_refresher.py:305:    if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:326:                    "client_secret": context.client_secret,
HEAD:backend/onyx/auth/oauth_refresher.py:327:                    "refresh_token": oauth_account.refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:328:                    "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_refresher.py:341:            new_access_token = token_data.get("access_token")
HEAD:backend/onyx/auth/oauth_refresher.py:342:            new_refresh_token = token_data.get(
HEAD:backend/onyx/auth/oauth_refresher.py:343:                "refresh_token", oauth_account.refresh_token
HEAD:backend/onyx/auth/oauth_refresher.py:356:                "access_token": new_access_token,
HEAD:backend/onyx/auth/oauth_refresher.py:357:                "refresh_token": new_refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:405:        if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:415:            # refreshed `expires_at` (and `refresh_token` for IdPs that
HEAD:backend/onyx/auth/oauth_refresher.py:460:async def check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:468:    return bool(oauth_account.refresh_token)
HEAD:backend/onyx/auth/oauth_refresher.py:471:async def get_oauth_accounts_requiring_refresh_token(user: User) -> List[OAuthAccount]:
HEAD:backend/onyx/auth/oauth_refresher.py:481:        has_refresh_token = await check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:484:        if not has_refresh_token:
HEAD:backend/onyx/auth/oauth_token_manager.py:10:from onyx.db.models import OAuthConfig, OAuthUserToken
HEAD:backend/onyx/auth/oauth_token_manager.py:79:    client_secret: str | None = None
HEAD:backend/onyx/auth/oauth_token_manager.py:133:    if params.client_secret:
HEAD:backend/onyx/auth/oauth_token_manager.py:134:        data["client_secret"] = params.client_secret
HEAD:backend/onyx/auth/oauth_token_manager.py:158:    def get_valid_access_token(self) -> str | None:
HEAD:backend/onyx/auth/oauth_token_manager.py:175:            if "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:177:                    return self.refresh_token(user_token)
HEAD:backend/onyx/auth/oauth_token_manager.py:184:        return token_data.get("access_token")
HEAD:backend/onyx/auth/oauth_token_manager.py:186:    def refresh_token(self, user_token: OAuthUserToken) -> str:
HEAD:backend/onyx/auth/oauth_token_manager.py:193:            or self.oauth_config.client_secret is None
HEAD:backend/onyx/auth/oauth_token_manager.py:196:                "OAuth client_id and client_secret are required for token refresh"
HEAD:backend/onyx/auth/oauth_token_manager.py:202:            "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_token_manager.py:203:            "refresh_token": token_data["refresh_token"],
HEAD:backend/onyx/auth/oauth_token_manager.py:205:            "client_secret": self._unwrap_sensitive_str(
HEAD:backend/onyx/auth/oauth_token_manager.py:206:                self.oauth_config.client_secret
HEAD:backend/onyx/auth/oauth_token_manager.py:225:        # Preserve refresh_token if not returned (some providers don't return it)
HEAD:backend/onyx/auth/oauth_token_manager.py:226:        if "refresh_token" not in new_token_data and "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:227:            new_token_data["refresh_token"] = token_data["refresh_token"]
HEAD:backend/onyx/auth/oauth_token_manager.py:237:        return new_token_data["access_token"]
HEAD:backend/onyx/auth/oauth_token_manager.py:262:            or self.oauth_config.client_secret is None
HEAD:backend/onyx/auth/oauth_token_manager.py:265:                "OAuth client_id and client_secret are required for code exchange"
HEAD:backend/onyx/auth/oauth_token_manager.py:287:        client_secret = (
HEAD:backend/onyx/auth/oauth_token_manager.py:288:            OAuthTokenManager._unwrap_sensitive_str(oauth_config.client_secret)
HEAD:backend/onyx/auth/oauth_token_manager.py:289:            if oauth_config.client_secret is not None
HEAD:backend/onyx/auth/oauth_token_manager.py:296:            client_secret=client_secret,
HEAD:backend/onyx/auth/oidc_client.py:119:        client_secret: str,
HEAD:backend/onyx/auth/oidc_client.py:127:            client_secret,
HEAD:backend/onyx/auth/permissions.py:61:    Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS.value: {
HEAD:backend/onyx/auth/permissions.py:196:        permissions=[Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:237:        id="create_user_access_token",
HEAD:backend/onyx/auth/permissions.py:240:        permissions=[Permission.CREATE_USER_API_KEYS],
HEAD:backend/onyx/auth/schemas.py:61:        # Email changes must go through the verification flow, password changes
HEAD:backend/onyx/auth/schemas.py:62:        # through /password/change-password, which requires the old password.
HEAD:backend/onyx/auth/schemas.py:64:        d.pop("password", None)
HEAD:backend/onyx/auth/session_tokens.py:24:from onyx.auth.constants import API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX
HEAD:backend/onyx/auth/session_tokens.py:138:    if token.startswith((API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX)):
HEAD:backend/onyx/auth/signup_rate_limit.py:1:"""Per-IP rate limit on email/password signup."""
HEAD:backend/onyx/auth/sso_url_guard.py:27:    if parts.username or parts.password:
HEAD:backend/onyx/auth/users.py:29:from fastapi.security import OAuth2PasswordRequestForm
HEAD:backend/onyx/auth/users.py:65:from onyx.auth.api_key import get_hashed_api_key_from_request
HEAD:backend/onyx/auth/users.py:68:    send_forgot_password_email,
HEAD:backend/onyx/auth/users.py:113:    DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN,
HEAD:backend/onyx/auth/users.py:114:    DANSWER_API_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:116:    PASSWORD_SPECIAL_CHARS,
HEAD:backend/onyx/auth/users.py:121:from onyx.db.api_key import fetch_api_key_auth_result
HEAD:backend/onyx/auth/users.py:123:    get_access_token_db,
HEAD:backend/onyx/auth/users.py:219:    The secret signs password-reset and email-verification tokens, OAuth login
HEAD:backend/onyx/auth/users.py:230:        "USER_AUTH_SECRET is empty. It signs password-reset and email-"
HEAD:backend/onyx/auth/users.py:245:    if email and email.endswith(DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN):
HEAD:backend/onyx/auth/users.py:247:        if name == DANSWER_API_KEY_PREFIX + UNNAMED_KEY_PLACEHOLDER:
HEAD:backend/onyx/auth/users.py:253:        return name.replace("API_KEY__", "API Key: ")
HEAD:backend/onyx/auth/users.py:258:def generate_password() -> str:
HEAD:backend/onyx/auth/users.py:265:    password = [
HEAD:backend/onyx/auth/users.py:272:    remaining_length = 12 - len(password)
HEAD:backend/onyx/auth/users.py:274:    password.extend(secrets.choice(all_characters) for _ in range(remaining_length))
HEAD:backend/onyx/auth/users.py:276:    # Shuffle the password to randomize the position of the required characters
HEAD:backend/onyx/auth/users.py:277:    random.shuffle(password)
HEAD:backend/onyx/auth/users.py:279:    return "".join(password)
HEAD:backend/onyx/auth/users.py:284:    # password signups.
HEAD:backend/onyx/auth/users.py:587:    reset_password_token_secret = USER_AUTH_SECRET
HEAD:backend/onyx/auth/users.py:700:        if safe and not MULTI_TENANT and not security_settings.password_auth_enabled:
HEAD:backend/onyx/auth/users.py:703:                "Password signup is disabled. Sign in through your SSO provider.",
HEAD:backend/onyx/auth/users.py:755:        # We verify the password here to make sure it's valid before we proceed
HEAD:backend/onyx/auth/users.py:756:        await self.validate_password(
HEAD:backend/onyx/auth/users.py:757:            user_create.password, cast(schemas.UC, user_create)
HEAD:backend/onyx/auth/users.py:927:                sync_user.hashed_password = self.password_helper.hash(
HEAD:backend/onyx/auth/users.py:928:                    user_create.password
HEAD:backend/onyx/auth/users.py:949:    async def validate_password(  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/auth/users.py:950:        self, password: str, _: schemas.UC | models.UP
HEAD:backend/onyx/auth/users.py:953:        if len(password) < settings.password_min_length:
HEAD:backend/onyx/auth/users.py:954:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:955:                reason=f"Password must be at least {settings.password_min_length} characters long."
HEAD:backend/onyx/auth/users.py:957:        if len(password) > settings.password_max_length:
HEAD:backend/onyx/auth/users.py:958:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:959:                reason=f"Password must not exceed {settings.password_max_length} characters."
HEAD:backend/onyx/auth/users.py:961:        if settings.password_require_uppercase and not any(
HEAD:backend/onyx/auth/users.py:962:            char.isupper() for char in password
HEAD:backend/onyx/auth/users.py:964:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:965:                reason="Password must contain at least one uppercase letter."
HEAD:backend/onyx/auth/users.py:967:        if settings.password_require_lowercase and not any(
HEAD:backend/onyx/auth/users.py:968:            char.islower() for char in password
HEAD:backend/onyx/auth/users.py:970:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:971:                reason="Password must contain at least one lowercase letter."
HEAD:backend/onyx/auth/users.py:973:        if settings.password_require_digit and not any(
HEAD:backend/onyx/auth/users.py:974:            char.isdigit() for char in password
HEAD:backend/onyx/auth/users.py:976:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:977:                reason="Password must contain at least one number."
HEAD:backend/onyx/auth/users.py:979:        if settings.password_require_special_char and not any(
HEAD:backend/onyx/auth/users.py:980:            char in PASSWORD_SPECIAL_CHARS for char in password
HEAD:backend/onyx/auth/users.py:982:            raise exceptions.InvalidPasswordException(
HEAD:backend/onyx/auth/users.py:983:                reason=f"Password must contain at least one special character from the following set: {PASSWORD_SPECIAL_CHARS}."
HEAD:backend/onyx/auth/users.py:1002:        access_token: str,
HEAD:backend/onyx/auth/users.py:1006:        refresh_token: Optional[str] = None,
HEAD:backend/onyx/auth/users.py:1068:                "access_token": access_token,
HEAD:backend/onyx/auth/users.py:1072:                "refresh_token": refresh_token,
HEAD:backend/onyx/auth/users.py:1110:                        # is claimable, password signups included. The same provider
HEAD:backend/onyx/auth/users.py:1156:                    password = self.password_helper.generate()
HEAD:backend/onyx/auth/users.py:1159:                        "hashed_password": self.password_helper.hash(password),
HEAD:backend/onyx/auth/users.py:1419:    async def on_after_forgot_password(
HEAD:backend/onyx/auth/users.py:1440:            send_forgot_password_email(user.email, tenant_id=tenant_id, token=token)
HEAD:backend/onyx/auth/users.py:1442:            logger.error("Failed to send password reset email to %s: %s", user.email, e)
HEAD:backend/onyx/auth/users.py:1445:                "Failed to send the password reset email.",
HEAD:backend/onyx/auth/users.py:1449:            AuditAction.PASSWORD_FORGOT,
HEAD:backend/onyx/auth/users.py:1454:    async def on_after_reset_password(
HEAD:backend/onyx/auth/users.py:1460:            AuditAction.PASSWORD_RESET,
HEAD:backend/onyx/auth/users.py:1525:        self, credentials: OAuth2PasswordRequestForm
HEAD:backend/onyx/auth/users.py:1538:        if not MULTI_TENANT and not get_security_settings().password_auth_enabled:
HEAD:backend/onyx/auth/users.py:1540:            raise BasicAuthenticationError(detail="PASSWORD_LOGIN_DISABLED")
HEAD:backend/onyx/auth/users.py:1562:            self.password_helper.hash(credentials.password)
HEAD:backend/onyx/auth/users.py:1578:                self.password_helper.hash(credentials.password)
HEAD:backend/onyx/auth/users.py:1585:                    detail="NO_WEB_LOGIN_AND_HAS_NO_PASSWORD",
HEAD:backend/onyx/auth/users.py:1588:            verified, updated_password_hash = self.password_helper.verify_and_update(
HEAD:backend/onyx/auth/users.py:1589:                credentials.password, user.hashed_password
HEAD:backend/onyx/auth/users.py:1595:            if updated_password_hash is not None:
HEAD:backend/onyx/auth/users.py:1597:                    user, {"hashed_password": updated_password_hash}
HEAD:backend/onyx/auth/users.py:1602:    async def reset_password_as_admin(self, user_id: uuid.UUID) -> str:
HEAD:backend/onyx/auth/users.py:1603:        """Admin-only. Generate a random password for a user and return it."""
HEAD:backend/onyx/auth/users.py:1605:        new_password = generate_password()
HEAD:backend/onyx/auth/users.py:1606:        await self._update(user, {"password": new_password})
HEAD:backend/onyx/auth/users.py:1607:        return new_password
HEAD:backend/onyx/auth/users.py:1609:    async def change_password_if_old_matches(
HEAD:backend/onyx/auth/users.py:1610:        self, user: User, old_password: str, new_password: str
HEAD:backend/onyx/auth/users.py:1613:        For normal users to change password if they know the old one.
HEAD:backend/onyx/auth/users.py:1614:        Raises 400 if old password doesn't match.
HEAD:backend/onyx/auth/users.py:1616:        verified, updated_password_hash = self.password_helper.verify_and_update(
HEAD:backend/onyx/auth/users.py:1617:            old_password, user.hashed_password
HEAD:backend/onyx/auth/users.py:1620:            # Raise some HTTPException (or your custom exception) if old password is invalid:
HEAD:backend/onyx/auth/users.py:1625:                detail="Invalid current password",
HEAD:backend/onyx/auth/users.py:1628:        # If the hash was upgraded behind the scenes, we can keep it before setting the new password:
HEAD:backend/onyx/auth/users.py:1629:        if updated_password_hash:
HEAD:backend/onyx/auth/users.py:1630:            user.hashed_password = updated_password_hash
HEAD:backend/onyx/auth/users.py:1632:        # Now apply and validate the new password
HEAD:backend/onyx/auth/users.py:1633:        await self._update(user, {"password": new_password})
HEAD:backend/onyx/auth/users.py:1671:    async def refresh_token(self, token: Optional[str], user: Any) -> str:
HEAD:backend/onyx/auth/users.py:1758:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1794:        access_token_db: AccessTokenDatabase[AccessToken],
HEAD:backend/onyx/auth/users.py:1797:        super().__init__(access_token_db, lifetime_seconds)
HEAD:backend/onyx/auth/users.py:1798:        self._access_token_db = access_token_db
HEAD:backend/onyx/auth/users.py:1800:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1806:        access_token = await self._access_token_db.get_by_token(token)
HEAD:backend/onyx/auth/users.py:1808:        if access_token is None:
HEAD:backend/onyx/auth/users.py:1816:        await self._access_token_db.update(access_token, {"expires": new_expires})
HEAD:backend/onyx/auth/users.py:1869:    async def refresh_token(
HEAD:backend/onyx/auth/users.py:1883:    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
HEAD:backend/onyx/auth/users.py:1886:        access_token_db, lifetime_seconds=SESSION_EXPIRE_TIME_SECONDS
HEAD:backend/onyx/auth/users.py:1980:                supports_refresh = hasattr(strategy, "refresh_token") and callable(
HEAD:backend/onyx/auth/users.py:1981:                    getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:1986:                        refresh_method = getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:2107:                    password=generate_password(),
HEAD:backend/onyx/auth/users.py:2162:    `user.oauth_accounts[0].access_token` directly to the upstream service. The
HEAD:backend/onyx/auth/users.py:2165:    hook the stored access_token could rot at the IdP's lifetime (~1 h on
HEAD:backend/onyx/auth/users.py:2249:        elif hashed_api_key := get_hashed_api_key_from_request(request):
HEAD:backend/onyx/auth/users.py:2250:            api_key = await fetch_api_key_auth_result(hashed_api_key, async_db_session)
HEAD:backend/onyx/auth/users.py:2251:            if api_key is not None:
HEAD:backend/onyx/auth/users.py:2252:                user = api_key.user
HEAD:backend/onyx/auth/users.py:2254:                    UsageCredentialType.API_KEY,
HEAD:backend/onyx/auth/users.py:2255:                    str(api_key.api_key_id),
HEAD:backend/onyx/auth/users.py:2256:                    api_key.api_key_name,
HEAD:backend/onyx/auth/users.py:2257:                    api_key.api_key_display,
HEAD:backend/onyx/auth/users.py:2307:        hashed_password="",
HEAD:backend/onyx/auth/users.py:2580:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_DECODE_ERROR
HEAD:backend/onyx/auth/users.py:2584:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_ALREADY_EXPIRED
HEAD:backend/onyx/auth/users.py:2588:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_DECODE_ERROR
HEAD:backend/onyx/auth/users.py:2636:            token["access_token"]
HEAD:backend/onyx/auth/users.py:2673:            token["access_token"],
HEAD:backend/onyx/auth/users.py:2677:            token.get("refresh_token"),
HEAD:backend/onyx/auth/users.py:2783:    async def null_access_token_state() -> tuple[OAuth2Token, Optional[str]] | None:
HEAD:backend/onyx/auth/users.py:2786:    access_token_state_dependency = (
HEAD:backend/onyx/auth/users.py:2787:        oauth2_authorize_callback if not enable_pkce else null_access_token_state
HEAD:backend/onyx/auth/users.py:2927:        access_token_state: Tuple[OAuth2Token, Optional[str]] | None = Depends(
HEAD:backend/onyx/auth/users.py:2928:            access_token_state_dependency
HEAD:backend/onyx/auth/users.py:3017:                token = await oauth_client.get_access_token(
HEAD:backend/onyx/auth/users.py:3029:            if access_token_state is None:
HEAD:backend/onyx/auth/users.py:3033:            token, callback_state = access_token_state
HEAD:backend/onyx/auth/utils.py:9:    API_KEY_HEADER_ALTERNATIVE_NAME,
HEAD:backend/onyx/auth/utils.py:10:    API_KEY_HEADER_NAME,
HEAD:backend/onyx/auth/utils.py:11:    API_KEY_PREFIX,
HEAD:backend/onyx/auth/utils.py:13:    DEPRECATED_API_KEY_PREFIX,
HEAD:backend/onyx/auth/utils.py:30:        hash_fn: Function to hash the token (e.g., hash_api_key or hash_pat)
HEAD:backend/onyx/auth/utils.py:37:        API_KEY_HEADER_ALTERNATIVE_NAME
HEAD:backend/onyx/auth/utils.py:38:    ) or request.headers.get(API_KEY_HEADER_NAME)
HEAD:backend/onyx/auth/utils.py:73:        API_KEY_HEADER_ALTERNATIVE_NAME
HEAD:backend/onyx/auth/utils.py:74:    ) or request.headers.get(API_KEY_HEADER_NAME)
HEAD:backend/onyx/auth/utils.py:111:        [API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX, SCIM_TOKEN_PREFIX],
HEAD:backend/onyx/db/api_key.py:4:from fastapi_users.password import PasswordHelper
HEAD:backend/onyx/db/api_key.py:9:from onyx.auth.api_key import (
HEAD:backend/onyx/db/api_key.py:11:    build_displayable_api_key,
HEAD:backend/onyx/db/api_key.py:12:    generate_api_key,
HEAD:backend/onyx/db/api_key.py:13:    hash_api_key,
HEAD:backend/onyx/db/api_key.py:16:    DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN,
HEAD:backend/onyx/db/api_key.py:17:    DANSWER_API_KEY_PREFIX,
HEAD:backend/onyx/db/api_key.py:31:from onyx.server.api_key.models import APIKeyArgs
HEAD:backend/onyx/db/api_key.py:41:    api_key_id: int
HEAD:backend/onyx/db/api_key.py:42:    api_key_name: str | None
HEAD:backend/onyx/db/api_key.py:43:    api_key_display: str
HEAD:backend/onyx/db/api_key.py:46:def get_api_key_email_pattern() -> str:
HEAD:backend/onyx/db/api_key.py:47:    return DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN
HEAD:backend/onyx/db/api_key.py:50:def is_api_key_email_address(email: str) -> bool:
HEAD:backend/onyx/db/api_key.py:51:    return email.endswith(get_api_key_email_pattern())
HEAD:backend/onyx/db/api_key.py:54:def fetch_api_keys(db_session: Session) -> list[ApiKeyDescriptor]:
HEAD:backend/onyx/db/api_key.py:55:    api_keys = (
HEAD:backend/onyx/db/api_key.py:62:        [api_key.user_id for api_key in api_keys],
HEAD:backend/onyx/db/api_key.py:67:            api_key_id=api_key.id,
HEAD:backend/onyx/db/api_key.py:68:            api_key_display=api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:69:            api_key_name=api_key.name,
HEAD:backend/onyx/db/api_key.py:70:            user_id=api_key.user_id,
HEAD:backend/onyx/db/api_key.py:73:                for gid, gname in groups_by_user.get(api_key.user_id, [])
HEAD:backend/onyx/db/api_key.py:76:        for api_key in api_keys
HEAD:backend/onyx/db/api_key.py:80:def fetch_api_key(db_session: Session, api_key_id: int) -> ApiKeyDescriptor | None:
HEAD:backend/onyx/db/api_key.py:81:    api_key = db_session.scalar(
HEAD:backend/onyx/db/api_key.py:82:        select(ApiKey).options(joinedload(ApiKey.user)).where(ApiKey.id == api_key_id)
HEAD:backend/onyx/db/api_key.py:84:    if api_key is None:
HEAD:backend/onyx/db/api_key.py:88:        db_session, [api_key.user_id], include_default=True
HEAD:backend/onyx/db/api_key.py:91:        api_key_id=api_key.id,
HEAD:backend/onyx/db/api_key.py:92:        api_key_display=api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:93:        api_key_name=api_key.name,
HEAD:backend/onyx/db/api_key.py:94:        user_id=api_key.user_id,
HEAD:backend/onyx/db/api_key.py:97:            for gid, gname in groups_by_user.get(api_key.user_id, [])
HEAD:backend/onyx/db/api_key.py:102:async def fetch_user_for_api_key(
HEAD:backend/onyx/db/api_key.py:103:    hashed_api_key: str, async_db_session: AsyncSession
HEAD:backend/onyx/db/api_key.py:110:        .where(ApiKey.hashed_api_key == hashed_api_key)
HEAD:backend/onyx/db/api_key.py:114:async def fetch_api_key_auth_result(
HEAD:backend/onyx/db/api_key.py:115:    hashed_api_key: str, async_db_session: AsyncSession
HEAD:backend/onyx/db/api_key.py:124:                .where(ApiKey.hashed_api_key == hashed_api_key)
HEAD:backend/onyx/db/api_key.py:135:        api_key_id=row.id,
HEAD:backend/onyx/db/api_key.py:136:        api_key_name=row.name,
HEAD:backend/onyx/db/api_key.py:137:        api_key_display=row.api_key_display,
HEAD:backend/onyx/db/api_key.py:141:def get_api_key_fake_email(
HEAD:backend/onyx/db/api_key.py:145:    return f"{DANSWER_API_KEY_PREFIX}{name}@{unique_id}{DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN}"
HEAD:backend/onyx/db/api_key.py:148:def insert_api_key(
HEAD:backend/onyx/db/api_key.py:149:    db_session: Session, api_key_args: APIKeyArgs, user_id: uuid.UUID | None
HEAD:backend/onyx/db/api_key.py:151:    std_password_helper = PasswordHelper()
HEAD:backend/onyx/db/api_key.py:156:    api_key = generate_api_key(tenant_id)
HEAD:backend/onyx/db/api_key.py:157:    api_key_user_id = uuid.uuid4()
HEAD:backend/onyx/db/api_key.py:159:    display_name = api_key_args.name or UNNAMED_KEY_PLACEHOLDER
HEAD:backend/onyx/db/api_key.py:160:    api_key_user_row = User(
HEAD:backend/onyx/db/api_key.py:161:        id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:162:        email=get_api_key_fake_email(display_name, str(api_key_user_id)),
HEAD:backend/onyx/db/api_key.py:163:        # a random password for the "user"
HEAD:backend/onyx/db/api_key.py:164:        hashed_password=std_password_helper.hash(std_password_helper.generate()),
HEAD:backend/onyx/db/api_key.py:170:    db_session.add(api_key_user_row)
HEAD:backend/onyx/db/api_key.py:172:    api_key_row = ApiKey(
HEAD:backend/onyx/db/api_key.py:173:        name=api_key_args.name,
HEAD:backend/onyx/db/api_key.py:174:        hashed_api_key=hash_api_key(api_key),
HEAD:backend/onyx/db/api_key.py:175:        api_key_display=build_displayable_api_key(api_key),
HEAD:backend/onyx/db/api_key.py:176:        user_id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:179:    db_session.add(api_key_row)
HEAD:backend/onyx/db/api_key.py:182:    set_user_groups__no_commit(db_session, api_key_user_id, api_key_args.group_ids)
HEAD:backend/onyx/db/api_key.py:187:        api_key_id=api_key_row.id,
HEAD:backend/onyx/db/api_key.py:188:        api_key_display=api_key_row.api_key_display,
HEAD:backend/onyx/db/api_key.py:189:        api_key=api_key,
HEAD:backend/onyx/db/api_key.py:190:        api_key_name=api_key_args.name,
HEAD:backend/onyx/db/api_key.py:191:        user_id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:192:        groups=get_user_groups(db_session, api_key_user_id, include_default=True),
HEAD:backend/onyx/db/api_key.py:196:def update_api_key(
HEAD:backend/onyx/db/api_key.py:197:    db_session: Session, api_key_id: int, api_key_args: APIKeyArgs
HEAD:backend/onyx/db/api_key.py:199:    existing_api_key = db_session.scalar(select(ApiKey).where(ApiKey.id == api_key_id))
HEAD:backend/onyx/db/api_key.py:200:    if existing_api_key is None:
HEAD:backend/onyx/db/api_key.py:202:            OnyxErrorCode.NOT_FOUND, f"API key with id {api_key_id} does not exist"
HEAD:backend/onyx/db/api_key.py:205:    existing_api_key.name = api_key_args.name
HEAD:backend/onyx/db/api_key.py:206:    api_key_user = db_session.scalar(
HEAD:backend/onyx/db/api_key.py:208:            User.id == existing_api_key.user_id  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/db/api_key.py:211:    if api_key_user is None:
HEAD:backend/onyx/db/api_key.py:214:    email_name = api_key_args.name or UNNAMED_KEY_PLACEHOLDER
HEAD:backend/onyx/db/api_key.py:215:    api_key_user.email = get_api_key_fake_email(email_name, str(api_key_user.id))
HEAD:backend/onyx/db/api_key.py:219:    set_user_groups__no_commit(db_session, api_key_user.id, api_key_args.group_ids)
HEAD:backend/onyx/db/api_key.py:224:        api_key_id=existing_api_key.id,
HEAD:backend/onyx/db/api_key.py:225:        api_key_display=existing_api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:226:        api_key_name=api_key_args.name,
HEAD:backend/onyx/db/api_key.py:227:        user_id=existing_api_key.user_id,
HEAD:backend/onyx/db/api_key.py:229:            db_session, existing_api_key.user_id, include_default=True
HEAD:backend/onyx/db/api_key.py:234:def regenerate_api_key(db_session: Session, api_key_id: int) -> ApiKeyDescriptor:
HEAD:backend/onyx/db/api_key.py:236:    existing_api_key = db_session.scalar(select(ApiKey).where(ApiKey.id == api_key_id))
HEAD:backend/onyx/db/api_key.py:237:    if existing_api_key is None:
HEAD:backend/onyx/db/api_key.py:238:        raise ValueError(f"API key with id {api_key_id} does not exist")
HEAD:backend/onyx/db/api_key.py:240:    api_key_user = db_session.scalar(
HEAD:backend/onyx/db/api_key.py:242:            User.id == existing_api_key.user_id  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/db/api_key.py:245:    if api_key_user is None:
HEAD:backend/onyx/db/api_key.py:251:    new_api_key = generate_api_key(tenant_id)
HEAD:backend/onyx/db/api_key.py:252:    existing_api_key.hashed_api_key = hash_api_key(new_api_key)
HEAD:backend/onyx/db/api_key.py:253:    existing_api_key.api_key_display = build_displayable_api_key(new_api_key)
HEAD:backend/onyx/db/api_key.py:256:    recompute_user_permissions__no_commit(api_key_user.id, db_session)
HEAD:backend/onyx/db/api_key.py:261:        api_key_id=existing_api_key.id,
HEAD:backend/onyx/db/api_key.py:262:        api_key_display=existing_api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:263:        api_key=new_api_key,
HEAD:backend/onyx/db/api_key.py:264:        api_key_name=existing_api_key.name,
HEAD:backend/onyx/db/api_key.py:265:        user_id=existing_api_key.user_id,
HEAD:backend/onyx/db/api_key.py:267:            db_session, existing_api_key.user_id, include_default=True
HEAD:backend/onyx/db/api_key.py:272:def remove_api_key(db_session: Session, api_key_id: int) -> None:
HEAD:backend/onyx/db/api_key.py:273:    existing_api_key = db_session.scalar(select(ApiKey).where(ApiKey.id == api_key_id))
```
## Sensitive Configuration Names
Captured names: 262
Only configuration identifiers were captured.
Values were intentionally excluded.
```text
AGENT_ANSWER_GENERATION_BY_FAST_LLM
AGENT_DEFAULT_MAX_TOKENS_ANSWER_GENERATION
AGENT_DEFAULT_MAX_TOKENS_ENTITY_TERM_EXTRACTION
AGENT_DEFAULT_MAX_TOKENS_HISTORY_SUMMARY
AGENT_DEFAULT_MAX_TOKENS_SUBANSWER_GENERATION
AGENT_DEFAULT_MAX_TOKENS_SUBQUERY_GENERATION
AGENT_DEFAULT_MAX_TOKENS_SUBQUESTION_GENERATION
AGENT_DEFAULT_MAX_TOKENS_VALIDATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_COMPARE_ANSWERS
AGENT_DEFAULT_TIMEOUT_LLM_DOCUMENT_VERIFICATION
AGENT_DEFAULT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION
AGENT_DEFAULT_TIMEOUT_LLM_GENERAL_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION
AGENT_DEFAULT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_CHECK
AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_GENERATION
AGENT_DEFAULT_TIMEOUT_LLM_SUBQUESTION_GENERATION
AGENT_MAX_TOKENS_ANSWER_GENERATION
AGENT_MAX_TOKENS_ENTITY_TERM_EXTRACTION
AGENT_MAX_TOKENS_HISTORY_SUMMARY
AGENT_MAX_TOKENS_SUBANSWER_GENERATION
AGENT_MAX_TOKENS_SUBQUERY_GENERATION
AGENT_MAX_TOKENS_SUBQUESTION_GENERATION
AGENT_MAX_TOKENS_VALIDATION
AGENT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS
AGENT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION
AGENT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION
AGENT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION
AGENT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK
AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION
AGENT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION
AGENT_TIMEOUT_LLM_COMPARE_ANSWERS
AGENT_TIMEOUT_LLM_DOCUMENT_VERIFICATION
AGENT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION
AGENT_TIMEOUT_LLM_GENERAL_GENERATION
AGENT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION
AGENT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION
AGENT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION
AGENT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION
AGENT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION
AGENT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION
AGENT_TIMEOUT_LLM_SUBANSWER_CHECK
AGENT_TIMEOUT_LLM_SUBANSWER_GENERATION
AGENT_TIMEOUT_LLM_SUBQUESTION_GENERATION
ANTHROPIC_DEFAULT_API_KEY
API_KEY_HASH_ROUNDS
AUTO_LLM_CONFIG_URL
AUTO_LLM_UPDATE_INTERVAL_SECONDS
AUTO_PROVISION_DEFAULT_LLM_PROVIDERS
AWS_REGION_NAME
AZURE_FILE_STORE_CONTAINER_NAME
AZURE_FILE_STORE_PREFIX
AZURE_IMAGE_API_BASE
AZURE_IMAGE_API_KEY
AZURE_IMAGE_API_VERSION
AZURE_IMAGE_DEPLOYMENT_NAME
AZURE_STORAGE_ACCOUNT_KEY
AZURE_STORAGE_ACCOUNT_NAME
AZURE_STORAGE_ACCOUNT_URL
AZURE_STORAGE_CONNECTION_STRING
BRAINTRUST_API_KEY
COHERE_DEFAULT_API_KEY
CONTEXTUAL_RAG_LLM_TIMEOUT
DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN
DANSWER_API_KEY_PREFIX
DANSWER_REDIS_FUNCTION_LOCK_PREFIX
DATA_PLANE_SECRET
DEFAULT_LLM_INPUT_COST_PER_MTOK
DEFAULT_LLM_OUTPUT_COST_PER_MTOK
DEFAULT_OBJECT_STORAGE_CREDENTIAL
DISABLE_LITELLM_STREAMING
DISCORD_BOT_TOKEN
DISCORD_SERVICE_API_KEY_NAME
DOCUMENT_PUSH_API_KEY
DR_REPORT_LLM_TIMEOUT_S
EGNYTE_CLIENT_SECRET
ENABLE_AZURE_IMAGE_CAP
ENCRYPTION_KEY_SECRET
EXPECTED_API_KEY
EXT_APP_GITHUB_CLIENT_SECRET
EXT_APP_GMAIL_CLIENT_SECRET
EXT_APP_GOOGLE_CALENDAR_CLIENT_ID
EXT_APP_GOOGLE_CALENDAR_CLIENT_SECRET
EXT_APP_GOOGLE_DRIVE_CLIENT_ID
EXT_APP_GOOGLE_DRIVE_CLIENT_SECRET
EXT_APP_HUBSPOT_CLIENT_SECRET
EXT_APP_LINEAR_CLIENT_SECRET
EXT_APP_NOTION_CLIENT_SECRET
EXT_APP_SLACK_CLIENT_SECRET
GATED_TENANTS_KEY
GCS_SERVICE_ACCOUNT_KEY_JSON
GCS_SERVICE_ACCOUNT_KEY_PATH
GEN_AI_API_KEY
GEN_AI_INPUT_TOKEN_SAFETY_MARGIN
GEN_AI_MAX_TOKENS
GEN_AI_MODEL_FALLBACK_MAX_TOKENS
GEN_AI_NUM_RESERVED_OUTPUT_TOKENS
GOOGLE_DRIVE_ADVANCED_PARSE_MAX_BYTES
GOOGLE_DRIVE_CONNECTOR_SIZE_THRESHOLD
GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY
GOOGLE_LOGIN_BASE_SCOPES
HEALTH_CHECK_BYPASS_TOKEN
KV_ALLOW_SAME_PROVIDER_SUBJECT_RELINK_KEY
KV_ANONYMOUS_USER_PERSONALIZATION_KEY
KV_ANONYMOUS_USER_PREFERENCES_KEY
KV_CRED_KEY
KV_CUSTOMER_UUID_KEY
KV_CUSTOM_ANALYTICS_SCRIPT_KEY
KV_ENTERPRISE_SETTINGS_KEY
KV_GEN_AI_KEY_CHECK_TIME
KV_INSTANCE_DOMAIN_KEY
KV_KG_CONFIG_KEY
KV_PASSWORD_AUTH_ENABLED_KEY
KV_PENDING_USERS_KEY
KV_REINDEX_KEY
KV_SETTINGS_KEY
KV_UNSTRUCTURED_API_KEY
KV_USER_STORE_KEY
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LINEAR_CLIENT_SECRET
LLM_FIRST_CHUNK_MAX_RETRIES
LLM_SOCKET_READ_TIMEOUT
LOG_POSTGRES_CONN_COUNTS
LOG_POSTGRES_LATENCY
MARKETING_POSTHOG_API_KEY
MASK_CREDENTIAL_CHAR
MASK_CREDENTIAL_LONG_RE
MASK_CREDENTIAL_PREFIX
MAX_TOKENS_FOR_FULL_INCLUSION
MCP_SERVER_ALLOW_LOOPBACK
MCP_SERVER_ALLOW_PRIVATE_NETWORK
MCP_SERVER_CORS_ORIGINS
MCP_SERVER_ENABLED
MCP_SERVER_HOST
MCP_SERVER_PORT
MCP_TOOL_CALL_TIMEOUT_SECONDS
METRICS_AUTH_TOKEN
MOCK_LLM_RESPONSE
OAUTH_CLIENT_ID
OAUTH_CLIENT_SECRET
OAUTH_CONFLUENCE_CLOUD_CLIENT_ID
OAUTH_CONFLUENCE_CLOUD_CLIENT_SECRET
OAUTH_ENABLED
OAUTH_GOOGLE_DRIVE_CLIENT_ID
OAUTH_GOOGLE_DRIVE_CLIENT_SECRET
OAUTH_SLACK_CLIENT_ID
OAUTH_SLACK_CLIENT_SECRET
ONYX_CELERY_BEAT_HEARTBEAT_KEY
ONYX_CLOUD_REDIS_RUNTIME
ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH
OPENAI_DEFAULT_API_KEY
OPENROUTER_DEFAULT_API_KEY
OPENSEARCH_ADMIN_PASSWORD
OPENSEARCH_AWS_SERVICE
PASSWORD_MAX_LENGTH
PASSWORD_MIN_LENGTH
PASSWORD_REQUIRE_DIGIT
PASSWORD_REQUIRE_LOWERCASE
PASSWORD_REQUIRE_SPECIAL_CHAR
PASSWORD_REQUIRE_UPPERCASE
PASSWORD_SPECIAL_CHARS
POSTGRES_API_SERVER_POOL_OVERFLOW
POSTGRES_API_SERVER_POOL_SIZE
POSTGRES_API_SERVER_READ_ONLY_POOL_OVERFLOW
POSTGRES_API_SERVER_READ_ONLY_POOL_SIZE
POSTGRES_CELERY_BEAT_APP_NAME
POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
POSTGRES_CELERY_WORKER_HEAVY_APP_NAME
POSTGRES_CELERY_WORKER_INDEXING_CHILD_APP_NAME
POSTGRES_CELERY_WORKER_LIGHT_APP_NAME
POSTGRES_CELERY_WORKER_MONITORING_APP_NAME
POSTGRES_CELERY_WORKER_PRIMARY_APP_NAME
POSTGRES_CELERY_WORKER_SCHEDULED_TASKS_APP_NAME
POSTGRES_CELERY_WORKER_USER_FILE_PROCESSING_APP_NAME
POSTGRES_DB
POSTGRES_HOST
POSTGRES_PASSWORD
POSTGRES_POOL_PRE_PING
POSTGRES_POOL_RECYCLE_DEFAULT
POSTGRES_PORT
POSTGRES_TCP_KEEPALIVES
POSTGRES_TCP_KEEPALIVES_COUNT
POSTGRES_TCP_KEEPALIVES_IDLE
POSTGRES_TCP_KEEPALIVES_INTERVAL
POSTGRES_UNKNOWN_APP_NAME
POSTGRES_USER
POSTGRES_USE_NULL_POOL
POSTGRES_WEB_APP_NAME
POSTHOG_API_KEY
PROMPT_CACHE_REDIS_TTL_MULTIPLIER
RECAPTCHA_ENTERPRISE_API_KEY
RECAPTCHA_SITE_KEY
REDIS_AUTH_KEY_PREFIX
REDIS_DB_NUMBER
REDIS_DB_NUMBER_CELERY
REDIS_DB_NUMBER_CELERY_RESULT_BACKEND
REDIS_HEALTH_CHECK_INTERVAL
REDIS_HOST
REDIS_PASSWORD
REDIS_POOL_MAX_CONNECTIONS
REDIS_PORT
REDIS_REPLICA_HOST
REDIS_SENTINEL_MASTER_NAME
REDIS_SENTINEL_PASSWORD
REDIS_SOCKET_CONNECT_TIMEOUT
REDIS_SOCKET_KEEPALIVE_OPTIONS
REDIS_SOCKET_TIMEOUT
REDIS_SSL
REDIS_SSL_CA_CERTS
REDIS_SSL_CERT_REQS
REDIS_SSL_CHECK_HOSTNAME
S3_AWS_ACCESS_KEY_ID
S3_AWS_SECRET_ACCESS_KEY
S3_ENDPOINT_URL
S3_FILE_STORE_BUCKET_NAME
S3_FILE_STORE_PREFIX
S3_GENERATE_LOCAL_CHECKSUM
S3_VERIFY_SSL
SALESFORCE_CLIENT_SECRET
SECONDARY_LLM_FLOW_TIMEOUT_S
SENDGRID_API_KEY
SEND_USER_METADATA_TO_LLM_PROVIDER
SLACK_USER_TOKEN_PREFIX
STRIPE_PUBLISHABLE_KEY_OVERRIDE
STRIPE_PUBLISHABLE_KEY_URL
STRIPE_SECRET_KEY
TESTRAIL_API_KEY
UNNAMED_KEY_PLACEHOLDER
USER_AUTH_SECRET
USE_REDIS_IAM_AUTH
USE_SEMANTIC_KEYWORD_EXPANSIONS_BASIC_SEARCH
USING_AWS_MANAGED_OPENSEARCH
VERTEXAI_DEFAULT_CREDENTIALS
VESPA_CLOUD_KEY_PATH
WEB_CONNECTOR_OAUTH_CLIENT_ID
WEB_CONNECTOR_OAUTH_CLIENT_SECRET
WEB_CONNECTOR_OAUTH_TOKEN_URL
```
## External Connector Families
Connector directories: 57
```text
airtable
asana
axero
bitbucket
blob
bookstack
box
braintrust
canvas
capability_checks
clickup
coda
confluence
cross_connector_utils
discord
discourse
document360
dropbox
drupal_wiki
egnyte
file
fireflies
freshdesk
gitbook
github
gitlab
gmail
gong
google_drive
google_site
google_utils
guru
highspot
hubspot
imap
jira
linear
loopio
lumapps
mediawiki
microsoft_utils
mock_connector
notion
outline
productboard
salesforce
sharepoint
slab
slack
teams
testrail
web
wikipedia
xenforo
zendesk
zoom
zulip
```
## Network and External-Call Mechanisms
Evidence lines: 600
```text
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:93:    except (requests.RequestException, ValueError) as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:128:        except (requests.RequestException, ValueError) as e:
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:83:    GATEWAY_PATH_PREFIX: LLM_GATEWAY_MIN_TIER,  # external LLM gateway API
HEAD:backend/ee/onyx/db/external_perm.py:77:    # external API calls (e.g. Google Drive folder iteration). Without this,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:123:                (e.g. externally-owned files where the API returns no permissions
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:187:    # For externally-owned files, the Drive API may return no permissions
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:4:from urllib.parse import urlparse
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:621:    external_user_groups.extend(enumerate_entra_groups(graph_api, already_resolved))
HEAD:backend/ee/onyx/hooks/executor.py:102:    if not hook.endpoint_url:
HEAD:backend/ee/onyx/hooks/executor.py:167:    endpoint_url = hook.endpoint_url
HEAD:backend/ee/onyx/hooks/executor.py:171:    if not endpoint_url:
HEAD:backend/ee/onyx/hooks/executor.py:173:            f"hook_id={hook_id} is active but has no endpoint_url — "
HEAD:backend/ee/onyx/hooks/executor.py:174:            "active hooks without an endpoint_url must be rejected by _lookup_hook"
HEAD:backend/ee/onyx/hooks/executor.py:178:        endpoint_url=endpoint_url,
HEAD:backend/ee/onyx/main.py:5:from httpx_oauth.clients.google import GoogleOAuth2
HEAD:backend/ee/onyx/server/billing/api.py:26:import httpx
HEAD:backend/ee/onyx/server/billing/api.py:476:            async with httpx.AsyncClient() as client:
HEAD:backend/ee/onyx/server/billing/api.py:490:        except httpx.HTTPError:
HEAD:backend/ee/onyx/server/billing/service.py:15:import httpx
HEAD:backend/ee/onyx/server/billing/service.py:109:        async with httpx.AsyncClient(
HEAD:backend/ee/onyx/server/billing/service.py:120:    except httpx.HTTPStatusError as e:
HEAD:backend/ee/onyx/server/billing/service.py:134:    except httpx.RequestError:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:4:import httpx
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:170:    except httpx.HTTPStatusError as e:
HEAD:backend/ee/onyx/server/enterprise_settings/models.py:3:from urllib.parse import urlparse
HEAD:backend/ee/onyx/server/features/hooks/api.py:1:import httpx
HEAD:backend/ee/onyx/server/features/hooks/api.py:44:def _check_ssrf_safety(endpoint_url: str) -> None:
HEAD:backend/ee/onyx/server/features/hooks/api.py:45:    """Raise OnyxError if endpoint_url could be used for SSRF.
HEAD:backend/ee/onyx/server/features/hooks/api.py:64:            endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:84:        endpoint_url=hook.endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:133:    endpoint_url: str,
HEAD:backend/ee/onyx/server/features/hooks/api.py:137:    """Check whether endpoint_url is reachable by sending an empty POST request.
HEAD:backend/ee/onyx/server/features/hooks/api.py:139:    We use POST since hook endpoints expect POST requests. The server will typically
HEAD:backend/ee/onyx/server/features/hooks/api.py:145:    - Any httpx.TimeoutException (ConnectTimeout, ReadTimeout, WriteTimeout, PoolTimeout) →
HEAD:backend/ee/onyx/server/features/hooks/api.py:149:    _check_ssrf_safety(endpoint_url)
HEAD:backend/ee/onyx/server/features/hooks/api.py:154:        with httpx.Client(timeout=timeout_seconds, follow_redirects=False) as client:
HEAD:backend/ee/onyx/server/features/hooks/api.py:155:            response = client.post(endpoint_url, headers=headers)
HEAD:backend/ee/onyx/server/features/hooks/api.py:162:    except httpx.TimeoutException as exc:
HEAD:backend/ee/onyx/server/features/hooks/api.py:168:            endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:178:            endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:242:        endpoint_url=req.endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:253:        endpoint_url=req.endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:284:    """Update hook fields. If endpoint_url, api_key, or timeout_seconds changes, the
HEAD:backend/ee/onyx/server/features/hooks/api.py:301:    endpoint_url_changing = "endpoint_url" in req.model_fields_set
HEAD:backend/ee/onyx/server/features/hooks/api.py:306:    if endpoint_url_changing or api_key_changing or timeout_changing:
HEAD:backend/ee/onyx/server/features/hooks/api.py:309:            req.endpoint_url
HEAD:backend/ee/onyx/server/features/hooks/api.py:310:            if endpoint_url_changing
HEAD:backend/ee/onyx/server/features/hooks/api.py:311:            else existing.endpoint_url  # endpoint_url is required on create and cannot be cleared on update
HEAD:backend/ee/onyx/server/features/hooks/api.py:328:            endpoint_url=effective_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:340:        endpoint_url=(req.endpoint_url if endpoint_url_changing else UNSET),
HEAD:backend/ee/onyx/server/features/hooks/api.py:370:    if not hook.endpoint_url:
HEAD:backend/ee/onyx/server/features/hooks/api.py:377:        endpoint_url=hook.endpoint_url,
HEAD:backend/ee/onyx/server/features/hooks/api.py:412:    if not hook.endpoint_url:
HEAD:backend/ee/onyx/server/features/hooks/api.py:419:        endpoint_url=hook.endpoint_url,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:6:nearly verbatim to Anthropic over httpx instead of going through LiteLLM's
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:17:from urllib.parse import urlsplit, urlunsplit
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:19:import httpx
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:104:def _timeout() -> httpx.Timeout:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:105:    return httpx.Timeout(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:210:def _non_streaming_error_response(response: httpx.Response) -> JSONResponse:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:255:    # actual call goes straight over httpx, never through llm.invoke/stream.
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:280:            with httpx.Client(timeout=_timeout()) as client:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:282:        except httpx.TimeoutException as e:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:289:        except httpx.HTTPError as e:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:390:            client = stack.enter_context(httpx.Client(timeout=_timeout()))
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:493:        with httpx.Client(timeout=_timeout()) as client:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:495:    except httpx.HTTPError as e:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:1:"""Proxies ``/v1/responses`` to OpenAI over httpx rather than LiteLLM's
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:15:import httpx
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:95:def _timeout() -> httpx.Timeout:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:96:    return httpx.Timeout(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:251:def _non_streaming_error_response(response: httpx.Response) -> JSONResponse:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:282:    # actual call goes straight over httpx, never through llm.invoke/stream.
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:307:            with httpx.Client(timeout=_timeout()) as client:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:309:        except httpx.TimeoutException as e:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:316:        except httpx.HTTPError as e:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:447:            client = stack.enter_context(httpx.Client(timeout=_timeout()))
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:61:        # Anthropic passthrough, which must close both the httpx response and
HEAD:backend/ee/onyx/server/license/api.py:121:            response = requests.post(
HEAD:backend/ee/onyx/server/license/api.py:155:    except requests.HTTPError as e:
HEAD:backend/ee/onyx/server/license/api.py:175:    except requests.RequestException:
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:82:        # is not held while serving other requests.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:195:        response = requests.post(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:282:        response = requests.get(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:157:        response = requests.post(
HEAD:backend/ee/onyx/server/oauth/slack.py:146:        response = requests.post(
HEAD:backend/ee/onyx/server/scim/api.py:179:    Currently returns OktaProvider for all requests. When multi-provider
HEAD:backend/ee/onyx/server/scim/auth.py:22:from urllib.parse import quote
HEAD:backend/ee/onyx/server/scim/auth.py:98:    """FastAPI dependency that authenticates SCIM requests.
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:38:        response = requests.get(url, headers=headers, timeout=30)
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:60:    except requests.exceptions.RequestException as e:
HEAD:backend/ee/onyx/server/tenants/billing.py:55:    response = requests.post(
HEAD:backend/ee/onyx/server/tenants/billing.py:65:        except (ValueError, requests.exceptions.JSONDecodeError):
HEAD:backend/ee/onyx/server/tenants/billing.py:92:    response = requests.get(
HEAD:backend/ee/onyx/server/tenants/billing.py:109:    response = requests.get(
HEAD:backend/ee/onyx/server/tenants/billing.py:143:    response = requests.post(
HEAD:backend/ee/onyx/server/tenants/billing_api.py:21:import httpx
HEAD:backend/ee/onyx/server/tenants/billing_api.py:280:            async with httpx.AsyncClient() as client:
HEAD:backend/ee/onyx/server/tenants/billing_api.py:294:        except httpx.HTTPError:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:4:import aiohttp  # Async HTTP client
HEAD:backend/ee/onyx/server/tenants/provisioning.py:5:import httpx
HEAD:backend/ee/onyx/server/tenants/provisioning.py:250:    async with aiohttp.ClientSession() as session:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:619:    async with httpx.AsyncClient() as client:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:634:    async with aiohttp.ClientSession() as session:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:668:        response = requests.get(
HEAD:backend/ee/onyx/server/tenants/proxy.py:24:import httpx
HEAD:backend/ee/onyx/server/tenants/proxy.py:195:        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
HEAD:backend/ee/onyx/server/tenants/proxy.py:206:    except httpx.HTTPStatusError as e:
HEAD:backend/ee/onyx/server/tenants/proxy.py:216:    except httpx.RequestError:
HEAD:backend/ee/onyx/utils/license.py:115:def license_from_control_plane_response(response: requests.Response) -> str:
HEAD:backend/ee/onyx/utils/license.py:387:def _rejection_detail(response: requests.Response) -> str | None:
HEAD:backend/ee/onyx/utils/license.py:437:    response = requests.get(
HEAD:backend/ee/onyx/utils/posthog_client.py:3:from urllib.parse import unquote
HEAD:backend/ee/onyx/utils/tier.py:122:    except (requests.RequestException, ValueError) as e:
HEAD:backend/onyx/auth/api_key.py:4:from urllib.parse import quote
HEAD:backend/onyx/auth/captcha.py:23:import httpx
HEAD:backend/onyx/auth/captcha.py:236:        async with httpx.AsyncClient() as client:
HEAD:backend/onyx/auth/disposable_email_validator.py:13:import httpx
HEAD:backend/onyx/auth/disposable_email_validator.py:116:            with httpx.Client(timeout=10.0) as client:
HEAD:backend/onyx/auth/disposable_email_validator.py:148:        except httpx.HTTPError as e:
HEAD:backend/onyx/auth/jwt.py:54:            response = requests.get(public_key_url)
HEAD:backend/onyx/auth/jwt.py:68:    except (requests.RequestException, SSRFException, ValueError) as exc:
HEAD:backend/onyx/auth/login_claims_capture.py:34:import httpx
HEAD:backend/onyx/auth/login_claims_capture.py:233:    async with httpx.AsyncClient(timeout=10) as client:
HEAD:backend/onyx/auth/login_claims_capture.py:253:    async with httpx.AsyncClient(timeout=10) as client:
HEAD:backend/onyx/auth/login_claims_capture.py:286:    ``oauth_client`` is the httpx_oauth client used for the login (its
HEAD:backend/onyx/auth/oauth_refresher.py:9:import httpx
HEAD:backend/onyx/auth/oauth_refresher.py:159:            async with httpx.AsyncClient() as client:
HEAD:backend/onyx/auth/oauth_refresher.py:169:        except (httpx.HTTPError, ValueError) as e:
HEAD:backend/onyx/auth/oauth_refresher.py:321:        async with httpx.AsyncClient() as client:
HEAD:backend/onyx/auth/oauth_token_manager.py:3:from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
HEAD:backend/onyx/auth/oauth_token_manager.py:19:def validate_oauth_endpoint_url(url: str, *, resolve_dns: bool = True) -> None:
HEAD:backend/onyx/auth/oauth_token_manager.py:126:    a computed `expires_at`; raises `requests.HTTPError` on a non-2xx response."""
HEAD:backend/onyx/auth/oauth_token_manager.py:138:    validate_oauth_endpoint_url(params.token_url)
HEAD:backend/onyx/auth/oauth_token_manager.py:139:    response = requests.post(
HEAD:backend/onyx/auth/oauth_token_manager.py:209:        validate_oauth_endpoint_url(self.oauth_config.token_url)
HEAD:backend/onyx/auth/oauth_token_manager.py:210:        response = requests.post(
HEAD:backend/onyx/auth/oidc_client.py:7:from urllib.parse import unquote, urlsplit
HEAD:backend/onyx/auth/oidc_client.py:9:import httpx
HEAD:backend/onyx/auth/oidc_client.py:10:from httpx_oauth.clients.openid import BASE_SCOPES, OpenID
HEAD:backend/onyx/auth/oidc_client.py:11:from httpx_oauth.exceptions import GetIdEmailError
HEAD:backend/onyx/auth/oidc_client.py:12:from httpx_oauth.oauth2 import GetAccessTokenError
HEAD:backend/onyx/auth/oidc_client.py:24:def _error_body_summary(response: httpx.Response) -> str:
HEAD:backend/onyx/auth/oidc_client.py:144:        async with self.get_httpx_client() as client:
HEAD:backend/onyx/auth/pat.py:6:from urllib.parse import quote
HEAD:backend/onyx/auth/sso_url_guard.py:4:from urllib.parse import urlsplit
HEAD:backend/onyx/auth/sso_web_error.py:15:from urllib.parse import quote
HEAD:backend/onyx/auth/users.py:13:from urllib.parse import urlparse
HEAD:backend/onyx/auth/users.py:56:from httpx_oauth.exceptions import GetIdEmailError
HEAD:backend/onyx/auth/users.py:57:from httpx_oauth.integrations.fastapi import OAuth2AuthorizeCallback
HEAD:backend/onyx/auth/users.py:58:from httpx_oauth.oauth2 import BaseOAuth2, GetAccessTokenError, OAuth2Token
HEAD:backend/onyx/auth/utils.py:4:from urllib.parse import unquote
HEAD:backend/onyx/background/README.md:85:Does not interact with the Document Index, it handles the syncs with external systems. Large volume API calls to handle pruning and fetching permissions, etc.
HEAD:backend/onyx/background/README.md:95:- Docfetching runs connectors to pull documents from external APIs (Google Drive, Confluence, etc.), stores batches to file storage, and dispatches docprocessing tasks
HEAD:backend/onyx/background/celery/apps/app_base.py:45:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/apps/app_base.py:454:    HttpxPool.close_all()
HEAD:backend/onyx/background/celery/apps/light.py:8:from onyx.background.celery.celery_utils import httpx_init_vespa_pool
HEAD:backend/onyx/background/celery/apps/light.py:114:        httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/apps/light.py:120:        httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/celery_utils.py:7:import httpx
HEAD:backend/onyx/background/celery/celery_utils.py:35:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/celery_utils.py:281:def httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/celery_utils.py:287:    httpx_cert = None
HEAD:backend/onyx/background/celery/celery_utils.py:288:    httpx_verify = False
HEAD:backend/onyx/background/celery/celery_utils.py:290:        httpx_cert = cast(tuple[str, str], (ssl_cert, ssl_key))
HEAD:backend/onyx/background/celery/celery_utils.py:291:        httpx_verify = True
HEAD:backend/onyx/background/celery/celery_utils.py:293:    HttpxPool.init_client(
HEAD:backend/onyx/background/celery/celery_utils.py:295:        cert=httpx_cert,
HEAD:backend/onyx/background/celery/celery_utils.py:296:        verify=httpx_verify,
HEAD:backend/onyx/background/celery/celery_utils.py:299:        limits=httpx.Limits(max_keepalive_connections=max_keepalive_connections),
HEAD:backend/onyx/background/celery/configs/base.py:2:import urllib.parse
HEAD:backend/onyx/background/celery/configs/base.py:30:    CELERY_PASSWORD_PART = ":" + urllib.parse.quote(REDIS_PASSWORD, safe="") + "@"
HEAD:backend/onyx/background/celery/configs/base.py:50:            f"&ssl_certfile={urllib.parse.quote(REDIS_SSL_CERTFILE, safe='')}"
HEAD:backend/onyx/background/celery/configs/base.py:51:            f"&ssl_keyfile={urllib.parse.quote(REDIS_SSL_KEYFILE, safe='')}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:23:from onyx.background.celery.celery_utils import httpx_init_vespa_pool
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:118:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1692:    # 20 is the documented default for httpx max_keepalive_connections
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1694:        httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1698:        httpx_init_vespa_pool(20)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1804:                httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:216:                httpx_client=vespa_client,
HEAD:backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py:1:import httpx
HEAD:backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py:28:        retry=retry_if_exception_type(httpx.ReadTimeout),
HEAD:backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py:40:        retry=retry_if_exception_type(httpx.ReadTimeout),
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:6:import httpx
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:37:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:207:            httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:291:            if isinstance(e, httpx.HTTPStatusError):
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:17:from onyx.background.celery.celery_utils import httpx_init_vespa_pool
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:76:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:396:    # 20 is the documented default for httpx max_keepalive_connections
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:398:        httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:402:        httpx_init_vespa_pool(20)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:427:            httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:511:            httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:893:                httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:897:                httpx_init_vespa_pool(20)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:916:                    httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1114:                httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1118:                httpx_init_vespa_pool(20)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1146:                    httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:7:import httpx
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:64:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:541:                httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:607:            if isinstance(e, httpx.HTTPStatusError):
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:48:from onyx.httpx.httpx_pool import HttpxPool
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:137:        httpx_client=HttpxPool.get("vespa"),
HEAD:backend/onyx/chat/process_message.py:1664:    - ``handle_stream_message_objects`` for single-model (N=1) requests.
HEAD:backend/onyx/configs/app_configs.py:4:import urllib.parse
HEAD:backend/onyx/configs/app_configs.py:614:POSTGRES_PASSWORD = urllib.parse.quote_plus(
HEAD:backend/onyx/configs/app_configs.py:1559:DOCUMENT_PUSH_ENDPOINT_URL = os.environ.get("DOCUMENT_PUSH_ENDPOINT_URL") or None
HEAD:backend/onyx/configs/app_configs.py:2032:DB_READONLY_PASSWORD: str = urllib.parse.quote_plus(
HEAD:backend/onyx/configs/app_configs.py:2044:# S3_ENDPOINT_URL is for MinIO and other S3-compatible storage. Leave blank for AWS S3.
HEAD:backend/onyx/configs/app_configs.py:2045:S3_ENDPOINT_URL = os.environ.get("S3_ENDPOINT_URL")
HEAD:backend/onyx/configs/app_configs.py:2057:    s3_endpoint_url: str | None,
HEAD:backend/onyx/configs/app_configs.py:2062:    if not s3_endpoint_url:
HEAD:backend/onyx/configs/app_configs.py:2068:    S3_ENDPOINT_URL, S3_AWS_ACCESS_KEY_ID, S3_AWS_SECRET_ACCESS_KEY
HEAD:backend/onyx/connectors/airtable/airtable_connector.py:255:                        attachment_response = requests.get(
HEAD:backend/onyx/connectors/airtable/airtable_connector.py:260:                    except requests.exceptions.HTTPError as e:
HEAD:backend/onyx/connectors/airtable/airtable_connector.py:273:                                        attachment_response = requests.get(
HEAD:backend/onyx/connectors/axero/connector.py:45:    return requests.get(
HEAD:backend/onyx/connectors/bitbucket/connector.py:44:    import httpx
HEAD:backend/onyx/connectors/bitbucket/connector.py:67:    """Connector for indexing Bitbucket Cloud pull requests.
HEAD:backend/onyx/connectors/bitbucket/connector.py:107:    def _client(self) -> httpx.Client:
HEAD:backend/onyx/connectors/bitbucket/connector.py:115:        client: httpx.Client,
HEAD:backend/onyx/connectors/bitbucket/connector.py:163:    def _iter_target_repositories(self, client: httpx.Client) -> Iterator[str]:
HEAD:backend/onyx/connectors/bitbucket/connector.py:281:        """Return only document IDs for all existing pull requests."""
HEAD:backend/onyx/connectors/bitbucket/utils.py:8:import httpx
HEAD:backend/onyx/connectors/bitbucket/utils.py:101:    exceptions=(BitbucketRetriableError, httpx.RequestError),
HEAD:backend/onyx/connectors/bitbucket/utils.py:105:    client: httpx.Client, url: str, params: dict[str, Any] | None = None
HEAD:backend/onyx/connectors/bitbucket/utils.py:106:) -> httpx.Response:
HEAD:backend/onyx/connectors/bitbucket/utils.py:114:    except httpx.RequestError:
HEAD:backend/onyx/connectors/bitbucket/utils.py:120:    except httpx.HTTPStatusError as e:
HEAD:backend/onyx/connectors/bitbucket/utils.py:141:def build_auth_client(email: str, api_token: str) -> httpx.Client:
HEAD:backend/onyx/connectors/bitbucket/utils.py:142:    """Create an authenticated httpx client for Bitbucket Cloud API."""
HEAD:backend/onyx/connectors/bitbucket/utils.py:143:    return httpx.Client(auth=(email, api_token), http2=True)
HEAD:backend/onyx/connectors/bitbucket/utils.py:147:    client: httpx.Client,
HEAD:backend/onyx/connectors/bitbucket/utils.py:180:    client: httpx.Client, workspace: str, project_key: str | None = None
HEAD:backend/onyx/connectors/blob/connector.py:9:from urllib.parse import quote
HEAD:backend/onyx/connectors/blob/connector.py:11:import boto3
HEAD:backend/onyx/connectors/blob/connector.py:52:    from mypy_boto3_s3 import S3Client
HEAD:backend/onyx/connectors/blob/connector.py:81:        # non-default partitions (e.g. GovCloud's us-gov-west-1) — without it boto3
HEAD:backend/onyx/connectors/blob/connector.py:117:        """Checks for boto3 credentials based on the bucket type.
HEAD:backend/onyx/connectors/blob/connector.py:125:        - S3: Creates a standard boto3 S3 client
HEAD:backend/onyx/connectors/blob/connector.py:146:            endpoint_url = f"https://{credentials['account_id']}.{subdomain}r2.cloudflarestorage.com"
HEAD:backend/onyx/connectors/blob/connector.py:148:            self.s3_client = boto3.client(
HEAD:backend/onyx/connectors/blob/connector.py:150:                endpoint_url=endpoint_url,
HEAD:backend/onyx/connectors/blob/connector.py:173:                session = boto3.Session(
HEAD:backend/onyx/connectors/blob/connector.py:179:                # If using IAM roles, we assume the role and let boto3 handle the credentials.
HEAD:backend/onyx/connectors/blob/connector.py:191:                    sts_client = boto3.client("sts", region_name=self.region_name)
HEAD:backend/onyx/connectors/blob/connector.py:213:                session = boto3.Session(botocore_session=botocore_session)
HEAD:backend/onyx/connectors/blob/connector.py:218:                self.s3_client = boto3.client("s3", region_name=self.region_name)
HEAD:backend/onyx/connectors/blob/connector.py:232:            self.s3_client = boto3.client(
HEAD:backend/onyx/connectors/blob/connector.py:234:                endpoint_url="https://storage.googleapis.com",
HEAD:backend/onyx/connectors/blob/connector.py:247:            self.s3_client = boto3.client(
HEAD:backend/onyx/connectors/blob/connector.py:249:                endpoint_url=f"https://{credentials['namespace']}.compat.objectstorage.{credentials['region']}.oraclecloud.com",
HEAD:backend/onyx/connectors/blob/connector.py:325:            account_id = self.s3_client.meta.endpoint_url.split("//")[1].split(".")[0]
HEAD:backend/onyx/connectors/blob/connector.py:341:            namespace = self.s3_client.meta.endpoint_url.split("//")[1].split(".")[0]
HEAD:backend/onyx/connectors/blob/connector.py:630:                "No valid blob storage credentials found or provided to boto3."
HEAD:backend/onyx/connectors/blob/connector.py:634:                "Partial or incomplete blob storage credentials provided to boto3."
HEAD:backend/onyx/connectors/bookstack/client.py:33:        response = requests.get(
HEAD:backend/onyx/connectors/box/connector.py:7:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/braintrust/connector.py:140:        self._rate_limited_request: Callable[..., requests.Response] | None = None
HEAD:backend/onyx/connectors/braintrust/connector.py:154:            requests.ConnectionError,
HEAD:backend/onyx/connectors/braintrust/connector.py:155:            requests.Timeout,
HEAD:backend/onyx/connectors/braintrust/connector.py:166:    ) -> requests.Response:
HEAD:backend/onyx/connectors/braintrust/connector.py:167:        response = requests.request(
HEAD:backend/onyx/connectors/braintrust/connector.py:611:        except requests.HTTPError as e:
HEAD:backend/onyx/connectors/canvas/client.py:7:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/canvas/client.py:90:        response = rl_requests.get(
HEAD:backend/onyx/connectors/clickup/connector.py:57:        response = requests.get(
HEAD:backend/onyx/connectors/coda/connector.py:104:        response = rl_requests.get(
HEAD:backend/onyx/connectors/confluence/connector.py:6:from urllib.parse import quote
HEAD:backend/onyx/connectors/confluence/connector.py:9:from requests.exceptions import HTTPError
HEAD:backend/onyx/connectors/confluence/connector.py:148:    # NOTE: requests.Response is falsy for error statuses, so compare to None.
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:20:from urllib.parse import quote
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:145:def _is_confcloud_77618_response(response: requests.Response) -> bool:
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:420:                    r = requests.get(
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:856:        response: requests.Response = self.get(path, advanced_mode=True)
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1064:        requests.Response back. Without it, the library's _response_handler
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1079:        response: requests.Response = self.post(url, data=data, advanced_mode=True)
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1205:        response: requests.Response = self.get(path, advanced_mode=True)
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1258:        response: requests.Response = self.get(path, advanced_mode=True)
HEAD:backend/onyx/connectors/confluence/utils.py:8:from urllib.parse import parse_qs, quote, urljoin, urlparse
HEAD:backend/onyx/connectors/confluence/utils.py:161:        resp: requests.Response = confluence_client._session.get(attachment_link)
HEAD:backend/onyx/connectors/confluence/utils.py:309:    response = requests.post(
HEAD:backend/onyx/connectors/confluence/utils.py:363:            except requests.HTTPError as e:
HEAD:backend/onyx/connectors/confluence/utils.py:386:def _handle_http_error(e: requests.HTTPError, attempt: int, max_retries: int) -> int:
HEAD:backend/onyx/connectors/cross_connector_utils/miscellaneous_utils.py:6:from urllib.parse import urljoin, urlparse
HEAD:backend/onyx/connectors/cross_connector_utils/miscellaneous_utils.py:204:    response = requests.get(tenant_info_url, timeout=10)
HEAD:backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py:22:    """Builds a generic wrapper/decorator for calls to external APIs that
HEAD:backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py:94:R = TypeVar("R", bound=Callable[..., requests.Response])
HEAD:backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py:103:    def wrapped_request(*args: list, **kwargs: dict[str, Any]) -> requests.Response:
HEAD:backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py:122:_rate_limited_get = wrap_request_to_handle_ratelimiting(requests.get)
HEAD:backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py:123:_rate_limited_post = wrap_request_to_handle_ratelimiting(requests.post)
HEAD:backend/onyx/connectors/discourse/connector.py:2:import urllib.parse
HEAD:backend/onyx/connectors/discourse/connector.py:45:    response = requests.get(
HEAD:backend/onyx/connectors/discourse/connector.py:60:        parsed_url = urllib.parse.urlparse(base_url)
HEAD:backend/onyx/connectors/discourse/connector.py:82:        categories_endpoint = urllib.parse.urljoin(self.base_url, "categories.json")
HEAD:backend/onyx/connectors/discourse/connector.py:97:        topic_endpoint = urllib.parse.urljoin(self.base_url, f"t/{topic_id}.json")
HEAD:backend/onyx/connectors/discourse/connector.py:101:        topic_url = urllib.parse.urljoin(self.base_url, f"t/{topic['slug']}")
HEAD:backend/onyx/connectors/discourse/connector.py:156:            latest_endpoint = urllib.parse.urljoin(
HEAD:backend/onyx/connectors/discourse/connector.py:167:                category_endpoint = urllib.parse.urljoin(
HEAD:backend/onyx/connectors/document360/connector.py:66:        response = requests.get(
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:67:    rate_limit_builder(max_calls=10, period=1)(rl_requests.get)
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:962:        except requests.exceptions.RequestException as e:
HEAD:backend/onyx/connectors/egnyte/connector.py:6:from urllib.parse import quote
HEAD:backend/onyx/connectors/fireflies/connector.py:189:            response: requests.Response | None = None
HEAD:backend/onyx/connectors/fireflies/connector.py:191:                response = requests.post(
HEAD:backend/onyx/connectors/freshdesk/connector.py:89:) -> requests.Response:
HEAD:backend/onyx/connectors/freshdesk/connector.py:90:    return rl_requests.get(url, auth=auth, params=params)
HEAD:backend/onyx/connectors/gitbook/connector.py:4:from urllib.parse import urljoin
HEAD:backend/onyx/connectors/gitbook/connector.py:46:        response = rl_requests.get(
HEAD:backend/onyx/connectors/gitbook/connector.py:505:                except requests.HTTPError as e:
HEAD:backend/onyx/connectors/gitbook/connector.py:526:        except requests.RequestException as e:
HEAD:backend/onyx/connectors/github/utils.py:3:from urllib.parse import ParseResult, urlparse
HEAD:backend/onyx/connectors/gitlab/connector.py:218:            merge_requests = project.mergerequests.list(
HEAD:backend/onyx/connectors/gong/connector.py:7:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/gong/connector.py:11:from requests.adapters import HTTPAdapter
HEAD:backend/onyx/connectors/gong/connector.py:12:from urllib3.util import Retry
HEAD:backend/onyx/connectors/gong/connector.py:109:        # urllib3 Retry already respects the Retry-After header by default
HEAD:backend/onyx/connectors/gong/connector.py:118:        self._session = requests.Session()
HEAD:backend/onyx/connectors/gong/connector.py:133:    ) -> requests.Response:
HEAD:backend/onyx/connectors/google_drive/connector.py:10:from urllib.parse import ParseResult, parse_qs, urlparse
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:5:from urllib.parse import urlparse, urlunparse
HEAD:backend/onyx/connectors/google_drive/file_retrieval.py:5:from urllib.parse import parse_qs, urlparse
HEAD:backend/onyx/connectors/google_utils/google_kv.py:4:from urllib.parse import ParseResult, parse_qs, urlparse
HEAD:backend/onyx/connectors/guru/connector.py:66:        session = requests.Session()
HEAD:backend/onyx/connectors/highspot/client.py:3:from urllib.parse import urljoin
HEAD:backend/onyx/connectors/highspot/client.py:6:from requests.adapters import HTTPAdapter
HEAD:backend/onyx/connectors/highspot/client.py:7:from requests.exceptions import HTTPError, RequestException, Timeout
HEAD:backend/onyx/connectors/highspot/client.py:8:from urllib3.util.retry import Retry
HEAD:backend/onyx/connectors/highspot/client.py:78:        self.session = requests.Session()
HEAD:backend/onyx/connectors/highspot/client.py:131:            requests.exceptions.RequestException: On request failures
HEAD:backend/onyx/connectors/highspot/utils.py:2:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/hubspot/connector.py:358:        response = requests.get(
HEAD:backend/onyx/connectors/hubspot/rate_limit.py:19:# with a maximum of 190 requests, and a per-second limit of 19 requests.
HEAD:backend/onyx/connectors/jira/connector.py:276:    except requests.exceptions.JSONDecodeError:
HEAD:backend/onyx/connectors/jira/utils.py:5:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/linear/connector.py:6:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/linear/connector.py:50:def _make_query(request_body: dict[str, Any], api_key: str) -> requests.Response:
HEAD:backend/onyx/connectors/linear/connector.py:58:            response = requests.post(
HEAD:backend/onyx/connectors/lumapps/client.py:27:def _backoff_seconds(response: requests.Response, attempt: int) -> float:
HEAD:backend/onyx/connectors/lumapps/client.py:61:        self._session = requests.Session()
HEAD:backend/onyx/connectors/lumapps/client.py:122:        last_network_error: requests.RequestException | None = None
HEAD:backend/onyx/connectors/lumapps/client.py:141:            except requests.RequestException as e:
HEAD:backend/onyx/connectors/mediawiki/family.py:9:from urllib.parse import urlparse, urlunparse
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:18:from urllib.parse import quote, unquote, urlsplit
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:310:    Transport errors from requests/urllib3 quote the request target, so a
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:321:        head_resp = requests.head(url, timeout=timeout, allow_redirects=True)
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:326:    except requests.RequestException:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:331:        with requests.get(
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:343:    except requests.RequestException:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:350:    request_factory: Callable[[], requests.Response],
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:361:    avoids reusing a stale socket from urllib3's connection pool.
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:365:            returns the ``requests.Response``. Called once per attempt.
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:372:        requests.RequestException: when retries are exhausted. HTTPError from
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:445:    def _factory() -> requests.Response:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:446:        return requests.get(url, stream=True, timeout=timeout)
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:468:    def _factory() -> requests.Response:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:469:        return requests.get(
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:535:        except requests.RequestException as e:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:743:        except requests.HTTPError as e:
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:817:    except requests.HTTPError as e:
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:39:    requests.exceptions.ConnectionError,
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:40:    requests.exceptions.Timeout,
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:41:    requests.exceptions.ChunkedEncodingError,
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:42:    requests.exceptions.ContentDecodingError,
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:66:def graph_error_code(response: requests.Response | None) -> str:
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:78:def log_and_raise_for_status(response: requests.Response) -> None:
HEAD:backend/onyx/connectors/microsoft_utils/graph_client.py:176:            response = requests.get(
HEAD:backend/onyx/connectors/mock_connector/connector.py:3:import httpx
HEAD:backend/onyx/connectors/mock_connector/connector.py:42:        self.client = httpx.Client(timeout=30.0)
HEAD:backend/onyx/connectors/notion/connector.py:5:from urllib.parse import parse_qs, urlparse
HEAD:backend/onyx/connectors/notion/connector.py:231:        res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:284:        res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:311:        res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:337:        res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:373:        res = rl_requests.post(
HEAD:backend/onyx/connectors/notion/connector.py:398:        res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:1055:        res = rl_requests.post(
HEAD:backend/onyx/connectors/notion/connector.py:1115:                except requests.exceptions.RequestException as e:
HEAD:backend/onyx/connectors/notion/connector.py:1316:                res = rl_requests.get(
HEAD:backend/onyx/connectors/notion/connector.py:1327:                res = rl_requests.post(
HEAD:backend/onyx/connectors/notion/connector.py:1335:        except requests.exceptions.HTTPError as http_err:
HEAD:backend/onyx/connectors/outline/client.py:4:from requests.exceptions import ConnectionError as RequestsConnectionError
HEAD:backend/onyx/connectors/outline/client.py:5:from requests.exceptions import RequestException, Timeout
HEAD:backend/onyx/connectors/outline/client.py:20:    """Client for interacting with the Outline API. Handles authentication and making HTTP requests."""
HEAD:backend/onyx/connectors/outline/client.py:37:            response = requests.post(
HEAD:backend/onyx/connectors/productboard/connector.py:68:            response = requests.get(
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:164:- [External Client App metadata](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_externalclientapplication.htm)
HEAD:backend/onyx/connectors/salesforce/auth.py:3:from urllib.parse import urlsplit
HEAD:backend/onyx/connectors/salesforce/auth.py:6:from requests.exceptions import HTTPError
HEAD:backend/onyx/connectors/salesforce/connector.py:12:from urllib.parse import urlencode
HEAD:backend/onyx/connectors/salesforce/onyx_salesforce.py:4:from urllib.parse import urlsplit, urlunsplit
HEAD:backend/onyx/connectors/salesforce/onyx_salesforce.py:7:from requests.adapters import HTTPAdapter
HEAD:backend/onyx/connectors/salesforce/onyx_salesforce.py:12:from urllib3.util.retry import Retry
HEAD:backend/onyx/connectors/salesforce/onyx_salesforce.py:168:            # urllib3 defaults to idempotent methods; let the SDK raise final errors.
HEAD:backend/onyx/connectors/salesforce/salesforce_calls.py:11:from urllib.parse import quote_plus
HEAD:backend/onyx/connectors/sharepoint/connector.py:11:from urllib.parse import unquote, urlsplit
HEAD:backend/onyx/connectors/sharepoint/connector.py:22:from requests.exceptions import HTTPError
HEAD:backend/onyx/connectors/sharepoint/connector.py:244:def _is_graph_invalid_request(response: requests.Response) -> bool:
HEAD:backend/onyx/connectors/sharepoint/connector.py:284:        resp = requests.get(probe_url, headers=headers, timeout=10)
HEAD:backend/onyx/connectors/sharepoint/connector.py:813:            resp = requests.get(
HEAD:backend/onyx/connectors/slab/connector.py:5:from urllib.parse import urljoin
HEAD:backend/onyx/connectors/slab/connector.py:59:            response = requests.post(
HEAD:backend/onyx/connectors/slab/connector.py:69:        except (requests.exceptions.Timeout, ValueError) as e:
HEAD:backend/onyx/connectors/slab/connector.py:74:            if isinstance(e, requests.exceptions.Timeout):
HEAD:backend/onyx/connectors/slack/connector.py:11:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/slack/source_operations.py:22:from urllib.error import URLError
HEAD:backend/onyx/connectors/slack/source_operations.py:23:from urllib.request import Request
HEAD:backend/onyx/connectors/slack/source_operations.py:88:    via an override of _perform_urllib_http_request in OnyxSlackWebClient.
HEAD:backend/onyx/connectors/slack/source_operations.py:241:    def _perform_urllib_http_request(
HEAD:backend/onyx/connectors/slack/source_operations.py:269:                    f"OnyxSlackWebClient._perform_urllib_http_request - "
HEAD:backend/onyx/connectors/slack/source_operations.py:274:            result = super()._perform_urllib_http_request(url=url, args=args)
HEAD:backend/onyx/connectors/slack/source_operations.py:280:                    "OnyxSlackWebClient._perform_urllib_http_request lock not owned on release"
HEAD:backend/onyx/connectors/slack/source_operations.py:285:    def _perform_urllib_http_request_internal(
HEAD:backend/onyx/connectors/slack/source_operations.py:292:        urllib/urlopen ... so this is a good place to perform our delay.
HEAD:backend/onyx/connectors/slack/source_operations.py:302:                "OnyxSlackWebClient._perform_urllib_http_request_internal delay: delay_ms=%r self.num_requests=%r",
HEAD:backend/onyx/connectors/slack/source_operations.py:309:        result = super()._perform_urllib_http_request_internal(url, req)
HEAD:backend/onyx/connectors/slack/source_operations.py:503:    urllib may surface a header value as a list; tolerate both shapes, like the
HEAD:backend/onyx/connectors/testrail/connector.py:156:            response = requests.get(
HEAD:backend/onyx/connectors/testrail/connector.py:163:        except requests.exceptions.HTTPError as e:
HEAD:backend/onyx/connectors/testrail/connector.py:180:        except requests.exceptions.RequestException as e:
HEAD:backend/onyx/connectors/web/connector.py:7:from urllib.parse import urljoin, urlparse
HEAD:backend/onyx/connectors/web/connector.py:14:from urllib3.exceptions import MaxRetryError
HEAD:backend/onyx/connectors/web/connector.py:196:        session = requests.Session()
HEAD:backend/onyx/connectors/web/connector.py:202:    except requests.exceptions.HTTPError as e:
HEAD:backend/onyx/connectors/web/connector.py:226:    except requests.exceptions.SSLError as e:
HEAD:backend/onyx/connectors/web/connector.py:233:    except (requests.RequestException, ValueError) as e:
HEAD:backend/onyx/connectors/web/connector.py:298:        response = requests.get(
HEAD:backend/onyx/connectors/web/connector.py:318:    except requests.RequestException as e:
HEAD:backend/onyx/connectors/web/connector.py:476:        head_response = requests.head(
HEAD:backend/onyx/connectors/web/connector.py:496:            response = requests.get(
HEAD:backend/onyx/connectors/xenforo/connector.py:17:from urllib.parse import urlparse
HEAD:backend/onyx/connectors/xenforo/connector.py:221:            response = requests.get(
HEAD:backend/onyx/connectors/zendesk/connector.py:8:from requests.exceptions import HTTPError
HEAD:backend/onyx/connectors/zendesk/connector.py:82:        response = requests.get(
HEAD:backend/onyx/connectors/zendesk/connector.py:225:    except requests.exceptions.HTTPError:
HEAD:backend/onyx/connectors/zoom/client.py:5:from urllib.parse import quote, urljoin, urlparse
HEAD:backend/onyx/connectors/zoom/client.py:8:from requests.adapters import HTTPAdapter
HEAD:backend/onyx/connectors/zoom/client.py:9:from urllib3.util import Retry
HEAD:backend/onyx/connectors/zoom/client.py:90:def _not_entitled_message(response: requests.Response) -> str | None:
HEAD:backend/onyx/connectors/zoom/client.py:104:def _raise_for_zoom_error(response: requests.Response, description: str) -> None:
HEAD:backend/onyx/connectors/zoom/client.py:120:    raise requests.HTTPError(
HEAD:backend/onyx/connectors/zoom/client.py:134:        self._session = requests.Session()
HEAD:backend/onyx/connectors/zoom/client.py:183:        self, description: str, send: Callable[[str], requests.Response]
HEAD:backend/onyx/connectors/zoom/client.py:184:    ) -> requests.Response:
HEAD:backend/onyx/connectors/zoom/client.py:205:    def _request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
HEAD:backend/onyx/connectors/zoom/client.py:209:        def send(token: str) -> requests.Response:
HEAD:backend/onyx/connectors/zoom/client.py:220:    def _request_webinar(self, endpoint: str) -> requests.Response:
HEAD:backend/onyx/connectors/zoom/client.py:393:        def send(token: str) -> requests.Response:
HEAD:backend/onyx/connectors/zoom/recordings/models.py:52:    if isinstance(error, requests.HTTPError):
HEAD:backend/onyx/connectors/zoom/recordings/models.py:61:    return isinstance(error, requests.RequestException)
HEAD:backend/onyx/connectors/zulip/connector.py:3:import urllib.parse
HEAD:backend/onyx/connectors/zulip/connector.py:57:            parsed = urllib.parse.urlparse(realm_url)
HEAD:backend/onyx/connectors/zulip/utils.py:4:from urllib.parse import quote
HEAD:backend/onyx/db/auth.py:84:    from external connectors, or API keys.
HEAD:backend/onyx/db/dal.py:6:  1. **External session** (FastAPI endpoints) — the caller provides a session
HEAD:backend/onyx/db/discord_bot.py:82:    Onyx API pods when sending chat requests.
HEAD:backend/onyx/db/engine/iam_auth.py:19:    Generate an IAM authentication token using boto3.
HEAD:backend/onyx/db/engine/iam_auth.py:21:    import boto3
HEAD:backend/onyx/db/engine/iam_auth.py:23:    client = boto3.client("rds", region_name=region)
HEAD:backend/onyx/db/engine/shard_registry.py:23:import urllib.parse
HEAD:backend/onyx/db/engine/shard_registry.py:150:            urllib.parse.quote_plus(str(raw_password))
HEAD:backend/onyx/db/hook.py:67:    endpoint_url: str | None = None,
HEAD:backend/onyx/db/hook.py:93:        endpoint_url=endpoint_url,
HEAD:backend/onyx/db/hook.py:123:    endpoint_url: str | None | UnsetType = UNSET,
HEAD:backend/onyx/db/hook.py:134:    - endpoint_url, api_key: pass UNSET to leave unchanged; pass None to clear.
HEAD:backend/onyx/db/hook.py:145:    if not isinstance(endpoint_url, UnsetType):
HEAD:backend/onyx/db/hook.py:146:        hook.endpoint_url = endpoint_url
HEAD:backend/onyx/db/models.py:7109:    endpoint_url: Mapped[str | None] = mapped_column(Text, nullable=True)
HEAD:backend/onyx/db/release_notes.py:3:from urllib.parse import urlencode
HEAD:backend/onyx/document_index/factory.py:1:import httpx
HEAD:backend/onyx/document_index/factory.py:76:    httpx_client: httpx.Client | None,
HEAD:backend/onyx/document_index/factory.py:83:        httpx_client=httpx_client,
HEAD:backend/onyx/document_index/factory.py:100:        httpx_client=httpx_client,
HEAD:backend/onyx/document_index/factory.py:115:    httpx_client: httpx.Client | None = None,
HEAD:backend/onyx/document_index/factory.py:134:    return _build_vespa_pair(search_settings, secondary_search_settings, httpx_client)
HEAD:backend/onyx/document_index/factory.py:140:    httpx_client: httpx.Client | None = None,
HEAD:backend/onyx/document_index/factory.py:164:            _build_vespa_pair(search_settings, secondary_search_settings, httpx_client)
HEAD:backend/onyx/document_index/interfaces_new.py:315:        The document and fields to update are specified in the update requests.
HEAD:backend/onyx/document_index/opensearch/client.py:14:    Urllib3AWSV4SignerAuth,
HEAD:backend/onyx/document_index/opensearch/client.py:287:        http_auth: tuple[str, str] | Urllib3AWSV4SignerAuth
HEAD:backend/onyx/document_index/opensearch/client.py:294:            # IAM ARN. Credentials come from the default boto3 chain (env, IRSA,
HEAD:backend/onyx/document_index/opensearch/client.py:296:            import boto3
HEAD:backend/onyx/document_index/opensearch/client.py:298:            credentials = boto3.Session().get_credentials()
HEAD:backend/onyx/document_index/opensearch/client.py:304:            http_auth = Urllib3AWSV4SignerAuth(credentials, aws_region, aws_service)
HEAD:backend/onyx/document_index/opensearch/client.py:997:        Retries on 429 too many requests.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:726:                # processing the remaining requests.
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:8:import httpx
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:238:        except httpx.HTTPError as e:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:252:            raise httpx.HTTPError(error_base) from e
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:356:        response: httpx.Response | None = None
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:367:        except httpx.HTTPError as e:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:382:            raise httpx.HTTPError(error_base) from e
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:528:    except httpx.HTTPError as e:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:530:            e.response.text if isinstance(e, httpx.HTTPStatusError) else None
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:533:            e.response.status_code if isinstance(e, httpx.HTTPStatusError) else None
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:551:        raise httpx.HTTPError(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:616:    chunk_requests.pop(0)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:649:            uncapped_requests.append(request)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:666:        capped_requests.append(request)
HEAD:backend/onyx/document_index/vespa/deletion.py:4:import httpx
HEAD:backend/onyx/document_index/vespa/deletion.py:17:def _retryable_http_delete(http_client: httpx.Client, url: str) -> None:
HEAD:backend/onyx/document_index/vespa/deletion.py:23:    doc_chunk_id: UUID, index_name: str, http_client: httpx.Client
HEAD:backend/onyx/document_index/vespa/deletion.py:30:    except httpx.HTTPStatusError as e:
HEAD:backend/onyx/document_index/vespa/deletion.py:38:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:11:import httpx
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:77:    doc_chunk_id: uuid.UUID, index_name: str, http_client: httpx.Client
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:108:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:144:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:242:        except httpx.HTTPStatusError as e:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:333:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:387:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:401:class BaseHTTPXClientContext(ABC):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:402:    """Abstract base class for an HTTPX client context manager."""
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:405:    def __enter__(self) -> httpx.Client:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:413:class GlobalHTTPXClientContext(BaseHTTPXClientContext):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:414:    """Context manager for a global HTTPX client that does not close it."""
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:416:    def __init__(self, client: httpx.Client):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:419:    def __enter__(self) -> httpx.Client:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:426:class TemporaryHTTPXClientContext(BaseHTTPXClientContext):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:427:    """Context manager for a temporary HTTPX client that closes it after use."""
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:429:    def __init__(self, client_factory: Callable[[], httpx.Client]):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:431:        self._client: httpx.Client | None = None  # Client will be created in __enter__
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:433:    def __enter__(self) -> httpx.Client:
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:27:        httpx_client=None,
HEAD:backend/onyx/document_index/vespa/shared_utils/utils.py:4:import httpx
HEAD:backend/onyx/document_index/vespa/shared_utils/utils.py:59:) -> httpx.Client:
HEAD:backend/onyx/document_index/vespa/shared_utils/utils.py:64:    return httpx.Client(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:8:import urllib.parse
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:15:import httpx
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:57:    BaseHTTPXClientContext,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:58:    GlobalHTTPXClientContext,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:59:    TemporaryHTTPXClientContext,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:99:# Set the logging level to WARNING to ignore INFO and DEBUG logs from httpx. By
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:101:httpx_logger = logging.getLogger("httpx")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:102:httpx_logger.setLevel(logging.WARNING)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:288:    response = requests.post(deploy_url, headers=headers, data=zip_file)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:377:    response = requests.post(deploy_url, headers=headers, data=zip_file)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:387:        encoded_doc_id = urllib.parse.quote_plus(self.document_id)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:393:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:457:    exceptions=httpx.HTTPError,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:463:    http_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:579:    except httpx.HTTPStatusError as e:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:610:        httpx_client: httpx.Client | None = None,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:615:        # NOTE: using `httpx` here since `requests` doesn't support HTTP2. This
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:617:        # large volume of requests.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:618:        self._httpx_client_context: BaseHTTPXClientContext
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:619:        if httpx_client:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:622:            self._httpx_client_context = GlobalHTTPXClientContext(httpx_client)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:626:            self._httpx_client_context = TemporaryHTTPXClientContext(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:706:            self._httpx_client_context as http_client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:789:            self._httpx_client_context as http_client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:828:        with self._httpx_client_context as httpx_client:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:829:            # Each invocation of this method can contain multiple update requests.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:838:                        http_client=httpx_client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:856:                            httpx_client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1085:        with self._httpx_client_context as http_client:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1132:    def httpx_client_context(self) -> BaseHTTPXClientContext:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1133:        return self._httpx_client_context
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1139:        httpx_client: httpx.Client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1147:            update: KGVespaChunkUpdateRequest, http_client: httpx.Client
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1148:        ) -> httpx.Response:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1161:                        httpx_client,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1169:                    except httpx.HTTPStatusError:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1170:                        # http_client is httpx.Client, so raise_for_status raises
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1171:                        # httpx.HTTPStatusError; logging here is the only way to
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1207:            processed_updates_requests.append(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1216:        with self._httpx_client_context as httpx_client:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1218:                processed_updates_requests, httpx_client
HEAD:backend/onyx/evals/eval_cli.py:154:        requests.RequestException: If the request fails
HEAD:backend/onyx/evals/eval_cli.py:167:    response = requests.post(url, headers=headers, json=payload)
HEAD:backend/onyx/evals/eval_cli.py:276:        except requests.RequestException as e:
HEAD:backend/onyx/external_apps/matching/engine.py:106:    mismatched grant semantics between current and persisted requests.
HEAD:backend/onyx/external_apps/providers/base.py:31:def token_response_error(http_response: requests.Response, body: Any) -> str | None:
HEAD:backend/onyx/external_apps/providers/base.py:154:    # How ``body`` is encoded on the wire: JSON (``requests.post(json=...)``)
HEAD:backend/onyx/external_apps/providers/base.py:336:            response = requests.post(
HEAD:backend/onyx/external_apps/providers/base.py:349:        except requests.RequestException as exc:
HEAD:backend/onyx/external_apps/providers/base.py:394:        self, response: requests.Response, body: dict[str, Any]
HEAD:backend/onyx/external_apps/providers/github.py:102:        description="Search repositories, issues, and pull requests.",
HEAD:backend/onyx/external_apps/providers/github.py:281:        self, response: requests.Response, body: dict[str, Any]
HEAD:backend/onyx/external_apps/providers/hubspot.py:2:from urllib.parse import quote
HEAD:backend/onyx/external_apps/providers/hubspot.py:217:        self, response: requests.Response, body: dict[str, Any]
HEAD:backend/onyx/external_apps/providers/hubspot.py:259:            response = requests.get(
HEAD:backend/onyx/external_apps/providers/hubspot.py:265:        except (requests.RequestException, ValueError) as exc:
HEAD:backend/onyx/federated_connectors/slack/federated_connector.py:3:from urllib.parse import urlencode
HEAD:backend/onyx/federated_connectors/slack/federated_connector.py:252:        response = requests.post(
HEAD:backend/onyx/file_store/README.md:58:S3_ENDPOINT_URL=http://localhost:9000  # MinIO endpoint
HEAD:backend/onyx/file_store/README.md:70:S3_ENDPOINT_URL=https://nyc3.digitaloceanspaces.com
HEAD:backend/onyx/file_store/README.md:146:- `S3_ENDPOINT_URL`: The service endpoint URL
HEAD:backend/onyx/file_store/file_store.py:16:    S3_ENDPOINT_URL,
HEAD:backend/onyx/file_store/file_store.py:42:    from mypy_boto3_s3 import S3Client
HEAD:backend/onyx/file_store/file_store.py:206:        s3_endpoint_url: str | None = None,
HEAD:backend/onyx/file_store/file_store.py:215:        self._s3_endpoint_url = s3_endpoint_url
HEAD:backend/onyx/file_store/file_store.py:223:                # Imported here: boto3 costs ~16 MB and most workers never build an S3 client.
HEAD:backend/onyx/file_store/file_store.py:224:                import boto3
HEAD:backend/onyx/file_store/file_store.py:233:                if self._s3_endpoint_url:
HEAD:backend/onyx/file_store/file_store.py:234:                    client_kwargs["endpoint_url"] = self._s3_endpoint_url
```
## Queue and Cache Dependencies
Evidence lines: 550
```text
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:2:from onyx.background.celery.apps.docfetching import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:2:from onyx.background.celery.apps.docprocessing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:2:from onyx.background.celery.apps.heavy import celery_app
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:8:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:9:            "ee.onyx.background.celery.tasks.cleanup",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:10:            "ee.onyx.background.celery.tasks.query_history",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:11:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/light.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/light.py:2:from onyx.background.celery.apps.light import celery_app
HEAD:backend/ee/onyx/background/celery/apps/light.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:8:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:9:            "ee.onyx.background.celery.tasks.ttl_management",
HEAD:backend/ee/onyx/background/celery/apps/light.py:10:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:2:from onyx.background.celery.apps.monitoring import celery_app
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:7:            "ee.onyx.background.celery.tasks.tenant_provisioning",
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:8:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/primary.py:2:from onyx.background.celery.apps.primary import celery_app
HEAD:backend/ee/onyx/background/celery/apps/primary.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/primary.py:7:            "ee.onyx.background.celery.tasks.hooks",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:9:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:10:            "ee.onyx.background.celery.tasks.cloud",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:11:            "ee.onyx.background.celery.tasks.ttl_management",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:12:            "ee.onyx.background.celery.tasks.usage_reporting",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:13:            "ee.onyx.background.celery.tasks.license_notifications",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:14:            "ee.onyx.background.celery.tasks.license_reclaim",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:15:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:16:            "ee.onyx.background.celery.tasks.sso_domain_revalidation",
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:2:from onyx.background.celery.apps.scheduled_tasks import celery_app
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:1:from onyx.background.celery.apps import app_base
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:2:from onyx.background.celery.apps.user_file_processing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:5:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:9:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:12:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:15:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:18:from onyx.configs.constants import OnyxCeleryPriority, OnyxCeleryQueues, OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:26:        "task": OnyxCeleryTask.GENERATE_USAGE_REPORT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:29:            "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:35:        "task": OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:38:            "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:44:        "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:47:            "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:49:            "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:54:        "task": OnyxCeleryTask.REVALIDATE_SSO_DOMAINS_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:57:            "priority": OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:72:            "task": OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:75:                "priority": OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:81:            "task": OnyxCeleryTask.CHECK_LICENSE_EXPIRY_NOTIFICATIONS,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:84:                "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:90:            "task": OnyxCeleryTask.GENERATE_USAGE_REPORT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:93:                "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:99:            "task": OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:102:                "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:108:            "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:111:                "priority": OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:113:                "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:120:            "task": OnyxCeleryTask.EXPORT_LOGS_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:123:                "priority": OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:128:                "queue": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:3:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:7:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:17:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:4:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:5:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:8:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:9:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:11:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:13:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:14:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:15:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:18:from onyx.redis.redis_pool import get_redis_client, redis_lock_dump
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:19:from onyx.redis.redis_tenant_work_gating import (
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:26:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:34:    redis_client: TenantRedisClient, task_name: str, interval_seconds: int
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:44:        raw = redis_client.get(key)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:48:        # tenant during a Redis hiccup.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:63:            redis_client.set(key, str(now_ms))
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:72:    name=OnyxCeleryTask.CLOUD_BEAT_TASK_GENERATOR,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:80:    queue: str = OnyxCeleryTask.DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:81:    priority: int = OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:89:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:91:    lock_beat: RedisLock = redis_client.lock(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:92:        f"{OnyxRedisLocks.CLOUD_BEAT_TASK_GENERATOR_LOCK}:{task_name}",
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:93:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:125:                redis_failed = False
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:130:                    redis_client, task_name, interval_s
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:147:                        redis_failed = True
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:149:                # Only refresh the gauge when Redis is known-reachable —
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:150:                # skip the ZCARD if we just failed open due to a Redis error.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:151:                if not redis_failed:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:169:            if current_time - last_lock_time >= (CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:192:            self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:215:            redis_lock_dump(lock_beat, redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:8:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:9:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:11:from redis import Redis
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:12:from redis.exceptions import LockError
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:13:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:26:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:27:from onyx.background.celery.celery_redis import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:28:    celery_find_task,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:29:    celery_get_broker_client,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:30:    celery_get_queue_length,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:31:    celery_get_queued_task_ids,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:32:    celery_get_unacked_task_ids,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:34:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:37:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:39:    CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:40:    DANSWER_REDIS_FUNCTION_LOCK_PREFIX,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:42:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:43:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:44:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:45:    OnyxRedisConstants,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:46:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:47:    OnyxRedisSignals,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:82:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:83:from onyx.redis.redis_connector_doc_perm_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:87:from onyx.redis.redis_pool import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:88:    get_redis_client,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:89:    get_redis_replica_client,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:90:    redis_lock_dump,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:92:from onyx.redis.redis_tenant_work_gating import maybe_mark_tenant_active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:93:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:215:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:217:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:218:    r_replica = get_redis_replica_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:220:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:222:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:261:            # clear any permission fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:262:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:265:                r_celery = celery_get_broker_client(self.app)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:283:        keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:288:                r.srem(OnyxRedisConstants.ACTIVE_FENCES, key_bytes)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:318:    app: Celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:320:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:331:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:347:        if redis_connector.prune.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:350:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:351:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:368:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:373:            celery_task_id=None,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:377:        result = app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:385:            priority=OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:388:        # fill in the celery task id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:389:        payload.celery_task_id = result.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:447:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:454:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:467:        payload = redis_connector.permissions.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:475:        if payload.celery_task_id is None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:492:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:494:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:571:            payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:579:                celery_task_id=payload.celery_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:584:                redis_connector, lock, r, timeout_seconds=JOB_TIMEOUT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:635:            result = redis_connector.permissions.update_db(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:666:        redis_connector.permissions.generator_complete = tasks_generated
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:687:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:688:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:792:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:793:    r_replica: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:794:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:795:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:801:    queue_len = celery_get_queue_length(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:807:    queued_upsert_tasks = celery_get_queued_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:810:    reserved_generator_tasks = celery_get_unacked_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:816:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:829:            r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:842:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:843:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:852:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:862:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:865:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:892:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:901:        redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:907:    if not payload.celery_task_id:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:913:    found = celery_find_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:914:        payload.celery_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:916:        r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:919:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:920:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:923:    if payload.celery_task_id in reserved_tasks:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:924:        # the celery task was prefetched and is reserved within a worker
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:925:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:928:    # look up every task in the current taskset in the celery queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:929:    # every entry in the taskset should have an associated entry in the celery task queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:930:    # because we get the celery tasks first, the entries in our own permissions taskset
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:931:    # should be roughly a subset of the tasks in celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:936:    # TODO: if the number of tasks in celery is much lower than than the taskset length
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:938:    # must not exist in celery.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:941:    tasks_not_in_celery = 0  # a non-zero number after completing our check is bad
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:943:    for member in r.sscan_iter(redis_connector.permissions.taskset_key):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:953:        tasks_not_in_celery += 1
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:959:    # we're active if there are still tasks to run and those tasks all exist in celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:960:    if tasks_scanned > 0 and tasks_not_in_celery == 0:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:961:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:965:    # if redis_connector_index.generator_locked():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:966:    #     logger.info(f"{payload.celery_task_id} is currently executing.")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:968:    # if we get here, we didn't find any direct indication that the associated celery tasks exist,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:972:    if redis_connector.permissions.active():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:975:    # celery tasks don't exist and the active signal has expired, possibly due to a crash. Clean it up.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:978:        "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:984:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:993:        redis_connector: RedisConnector,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:994:        redis_lock: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:995:        redis_client: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:999:        self.redis_connector: RedisConnector = redis_connector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1000:        self.redis_lock: RedisLock = redis_lock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1001:        self.redis_client = redis_client
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1004:        self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1013:        if self.redis_connector.stop.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1017:        # NOTE: Celery's soft_time_limit does not work with thread pools,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1026:                    self.redis_connector.cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1034:            self.redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1038:                CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1040:                self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1048:                self.redis_lock.timeout,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1055:            redis_lock_dump(self.redis_lock, self.redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1065:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1082:    initial = redis_connector.permissions.generator_complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1087:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1097:    remaining = redis_connector.permissions.get_remaining()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1136:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:7:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:8:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:10:from redis import Redis
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:11:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:13:from ee.onyx.background.celery.tasks.external_group_syncing.group_sync_utils import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:30:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:31:from onyx.background.celery.celery_redis import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:32:    celery_find_task,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:33:    celery_get_broker_client,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:34:    celery_get_unacked_task_ids,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:36:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:40:    CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:41:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:42:    CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:43:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:44:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:45:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:46:    OnyxRedisConstants,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:47:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:48:    OnyxRedisSignals,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:66:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:67:from onyx.redis.redis_connector_ext_group_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:68:    RedisConnectorExternalGroupSync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:69:    RedisConnectorExternalGroupSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:71:from onyx.redis.redis_pool import get_redis_client, get_redis_replica_client
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:72:from onyx.redis.redis_tenant_work_gating import maybe_mark_tenant_active
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:73:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:164:    name=OnyxCeleryTask.CHECK_FOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:170:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:172:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:173:    r_replica = get_redis_replica_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:175:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:177:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:234:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:235:            # clear fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:236:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:239:                r_celery = celery_get_broker_client(self.app)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:249:                OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:272:    app: Celery,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:274:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:285:        if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:292:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:293:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:308:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:310:        payload = RedisConnectorExternalGroupSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:314:            celery_task_id=None,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:316:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:318:        custom_task_id = f"{redis_connector.external_group_sync.taskset_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:320:        result = app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:321:            OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:326:            queue=OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:328:            priority=OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:331:        payload.celery_task_id = result.id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:332:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:352:    name=OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:371:    r = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:378:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:381:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:386:        if not redis_connector.external_group_sync.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:389:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:394:        payload = redis_connector.external_group_sync.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:400:        if payload.celery_task_id is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:403:                redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:410:            redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:415:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:416:        OnyxRedisLocks.CONNECTOR_EXTERNAL_GROUP_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:417:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:418:        timeout=CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:430:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:465:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:466:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:470:        redis_connector.external_group_sync.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:578:                # NOTE: Celery's soft_time_limit does not work with thread pools,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:681:    celery_app: Celery,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:682:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:683:    r_replica: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:684:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:685:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:687:    reserved_tasks = celery_get_unacked_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:688:        OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:693:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:704:            r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:715:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:717:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:724:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:734:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:737:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:761:        payload = redis_connector.external_group_sync.payload
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:772:        redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:778:    if not payload.celery_task_id:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:782:    found = celery_find_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:786:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:787:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:790:    if payload.celery_task_id in reserved_tasks:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:792:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:795:    # if we get here, we didn't find any direct indication that the associated celery tasks exist,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:799:    if redis_connector.external_group_sync.active():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:802:    # celery tasks don't exist and the active signal has expired, possibly due to a crash. Clean it up.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:806:            "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:814:    redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:1:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:4:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:15:    name=OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:2:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:16:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:25:    name=OnyxCeleryTask.CHECK_LICENSE_EXPIRY_NOTIFICATIONS,
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:4:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:19:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:21:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:39:        raw = get_redis_client().get(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:56:        return bool(get_redis_client().set(key, "1", nx=True, ex=interval))
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:68:        redis_client = get_redis_client()
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:70:            redis_client.delete(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:74:        pipe = redis_client.pipeline()
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:83:    name=OnyxCeleryTask.RECLAIM_LICENSE,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:3:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:11:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:24:# TODO(andrei): Kubernetes coverage is partial by design as of now. A celery
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:33:    name=OnyxCeleryTask.EXPORT_LOGS_COLLECT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:63:    name=OnyxCeleryTask.EXPORT_LOGS_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:5:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:13:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:31:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:8:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:12:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:19:    name=OnyxCeleryTask.REVALIDATE_SSO_DOMAINS_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:9:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:10:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:12:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:16:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:17:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:18:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:24:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:38:    name=OnyxCeleryTask.CLOUD_CHECK_AVAILABLE_TENANTS,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:39:    queue=OnyxCeleryQueues.MONITORING,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:58:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:59:    lock_check: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:60:        OnyxRedisLocks.CHECK_AVAILABLE_TENANTS_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:188:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:189:    lock_provision: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:190:        OnyxRedisLocks.CLOUD_PRE_PROVISION_TENANT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:5:from ee.onyx.background.celery_utils import should_perform_chat_ttl_check
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:8:    CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:10:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:11:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:12:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:13:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:17:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:18:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:28:if redis.call('get', KEYS[1]) == ARGV[1] then
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:29:    return redis.call('expire', KEYS[1], ARGV[2])
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:37:if redis.call('get', KEYS[1]) == ARGV[1] then
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:38:    return redis.call('del', KEYS[1])
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:45:def _release_chain_if_owned(redis_client: TenantRedisClient, chain_token: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:47:    redis_client.eval(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:49:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:55:    name=OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:92:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:95:    owns_chain = redis_client.eval(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:97:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:98:        [chain_token, str(CELERY_CHAT_TTL_DELETE_TASK_EXPIRES)],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:129:            self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:130:                OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:136:                queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:137:                priority=OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:138:                expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:141:            _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:144:        _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:148:    name=OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:170:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:174:    if not redis_client.set(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:175:        OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:178:        ex=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:183:        self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:184:            OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:190:            queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:191:            priority=OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:192:            expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:196:        _release_chain_if_owned(redis_client, chain_token)
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:4:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:7:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:15:    name=OnyxCeleryTask.GENERATE_USAGE_REPORT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:9:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:12:from onyx.redis.redis_usergroup import RedisUserGroup
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:13:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:20:    tenant_id: str, key_bytes: bytes, r: TenantRedisClient, db_session: Session
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:24:    usergroup_id_str = RedisUserGroup.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:35:    rug = RedisUserGroup(tenant_id, usergroup_id)
HEAD:backend/ee/onyx/background/task_name_builders.py:3:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/task_name_builders.py:5:QUERY_HISTORY_TASK_NAME_PREFIX = OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK
HEAD:backend/onyx/background/README.md:15:| Primary                   | `apps/primary.py`              | `celery`                                                                                                             |
HEAD:backend/onyx/background/README.md:22:| Background (consolidated) | `apps/background.py`           | All queues above except `celery`                                                                                     |
HEAD:backend/onyx/background/README.md:28:| **Beat**   | `beat.py`   | Celery beat scheduler with `DynamicTenantScheduler` that generates per-tenant periodic task schedules |
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
HEAD:backend/onyx/background/README.md:48:- waits for redis, postgres, document index to all be healthy
HEAD:backend/onyx/background/README.md:50:- cleans all the redis states associated with background jobs
HEAD:backend/onyx/background/README.md:53:Then it cycles through its tasks as scheduled by Celery Beat:
HEAD:backend/onyx/background/README.md:64:| `celery_beat_heartbeat`           | 1m        | Heartbeat for Beat watchdog                                                                |
HEAD:backend/onyx/background/README.md:66:Watchdog is a separate Python process managed by supervisord which runs alongside celery workers. It checks the ONYX_CELERY_BEAT_HEARTBEAT_KEY in
HEAD:backend/onyx/background/README.md:67:Redis to ensure Celery Beat is not dead. Beat schedules the celery_beat_heartbeat for Primary to touch the key and share that it's still alive.
HEAD:backend/onyx/background/README.md:111:For the full metric reference, integration guide, and PromQL examples, see [`docs/METRICS.md`](../../../docs/METRICS.md#celery-worker-metrics).
HEAD:backend/onyx/background/celery/apps/app_base.py:8:from celery import (
HEAD:backend/onyx/background/celery/apps/app_base.py:12:from celery.app import trace
HEAD:backend/onyx/background/celery/apps/app_base.py:13:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/app_base.py:14:from celery.signals import before_task_publish, task_postrun, task_prerun
HEAD:backend/onyx/background/celery/apps/app_base.py:15:from celery.states import READY_STATES
HEAD:backend/onyx/background/celery/apps/app_base.py:16:from celery.utils.log import get_task_logger
HEAD:backend/onyx/background/celery/apps/app_base.py:17:from celery.worker import strategy
HEAD:backend/onyx/background/celery/apps/app_base.py:18:from celery.worker.control import control_command
HEAD:backend/onyx/background/celery/apps/app_base.py:19:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/apps/app_base.py:20:from sentry_sdk.integrations.celery import CeleryIntegration
HEAD:backend/onyx/background/celery/apps/app_base.py:24:from onyx.background.celery.apps.task_formatters import (
HEAD:backend/onyx/background/celery/apps/app_base.py:25:    CeleryTaskColoredFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:26:    CeleryTaskJsonFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:27:    CeleryTaskPlainFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:29:from onyx.background.celery.celery_utils import (
HEAD:backend/onyx/background/celery/apps/app_base.py:30:    celery_is_worker_primary,
HEAD:backend/onyx/background/celery/apps/app_base.py:33:from onyx.background.celery.tasks.vespa.document_sync import (
HEAD:backend/onyx/background/celery/apps/app_base.py:42:from onyx.configs.constants import ONYX_CLOUD_CELERY_TASK_PREFIX, OnyxRedisLocks
HEAD:backend/onyx/background/celery/apps/app_base.py:46:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/onyx/background/celery/apps/app_base.py:47:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/app_base.py:48:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/app_base.py:49:from onyx.redis.redis_connector_ext_group_sync import RedisConnectorExternalGroupSync
HEAD:backend/onyx/background/celery/apps/app_base.py:50:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/app_base.py:51:from onyx.redis.redis_document_set import RedisDocumentSet
HEAD:backend/onyx/background/celery/apps/app_base.py:52:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/onyx/background/celery/apps/app_base.py:53:from onyx.redis.redis_usergroup import RedisUserGroup
HEAD:backend/onyx/background/celery/apps/app_base.py:69:    SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:83:        traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:84:        integrations=[CeleryIntegration()],
HEAD:backend/onyx/background/celery/apps/app_base.py:99:    Intentionally ungated, like Celery's built-in shutdown/terminate/revoke control
HEAD:backend/onyx/background/celery/apps/app_base.py:102:    from celery.worker import state as worker_state
HEAD:backend/onyx/background/celery/apps/app_base.py:113:    abstract = True  # So Celery knows not to register this as a real task.
HEAD:backend/onyx/background/celery/apps/app_base.py:194:    if task.name.startswith(ONYX_CLOUD_CELERY_TASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:198:    # Get tenant_id directly from kwargs- each celery task has a tenant_id kwarg
HEAD:backend/onyx/background/celery/apps/app_base.py:213:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:215:    # NOTE: we want to remove the `Redis*` classes, prefer to just have functions to
HEAD:backend/onyx/background/celery/apps/app_base.py:222:    if task_id.startswith(RedisDocumentSet.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:223:        document_set_id = RedisDocumentSet.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:225:            rds = RedisDocumentSet(tenant_id, int(document_set_id))
HEAD:backend/onyx/background/celery/apps/app_base.py:229:    if task_id.startswith(RedisUserGroup.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:230:        usergroup_id = RedisUserGroup.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:232:            rug = RedisUserGroup(tenant_id, int(usergroup_id))
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:237:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:242:    if task_id.startswith(RedisConnectorPrune.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:243:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:245:            RedisConnectorPrune.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:248:    if task_id.startswith(RedisConnectorPermissionSync.SUBTASK_PREFIX):
```
## Dependency Manifests and Lockfiles
Count: 30
```text
backend/onyx/server/features/build/sandbox/image/templates/outputs/web/bun.lock
backend/onyx/server/features/build/sandbox/image/templates/outputs/web/package.json
backend/uv.lock
bun.lock
cli/go.mod
cli/go.sum
cli/pyproject.toml
desktop/package.json
desktop/src-tauri/Cargo.lock
desktop/src-tauri/Cargo.toml
examples/widget/package.json
mobile/bun.lock
mobile/package.json
package.json
pyproject.toml
terraform-provider-onyx/go.mod
terraform-provider-onyx/go.sum
tools/ods-audit/pyproject.toml
tools/ods/go.mod
tools/ods/go.sum
tools/ods/pyproject.toml
uv.lock
web/bun.lock
web/lib/opal/package.json
web/lib/shared/package.json
web/package.json
web/tools/oxlint/anti-slop/package.json
web/tools/oxlint/i18n/package.json
web/tools/type-check/package.json
widget/package.json
```
## Container and Deployment Manifests
Count: 38
```text
.devcontainer/Dockerfile
backend/Dockerfile
backend/Dockerfile.model_server
backend/onyx/server/features/build/sandbox/image/Dockerfile
backend/tests/integration/mock_services/docker-compose.mock-it-services.yml
backend/tests/integration/mock_services/mock_connector_server/Dockerfile
cli/Dockerfile
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml
deployment/docker_compose/docker-compose.airgap-test.yml
deployment/docker_compose/docker-compose.airgap-tls-test.yml
deployment/docker_compose/docker-compose.craft.yml
deployment/docker_compose/docker-compose.dev.yml
deployment/docker_compose/docker-compose.mcp-api-key-test.yml
deployment/docker_compose/docker-compose.mcp-oauth-test.yml
deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml
deployment/docker_compose/docker-compose.multitenant.yml
deployment/docker_compose/docker-compose.onyx-lite.yml
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml
deployment/docker_compose/docker-compose.prod.yml
deployment/docker_compose/docker-compose.resources.yml
deployment/docker_compose/docker-compose.search-testing.yml
deployment/docker_compose/docker-compose.template.yml
deployment/docker_compose/docker-compose.yml
deployment/helm/charts/onyx-cnpg-crds/Chart.yaml
deployment/helm/charts/onyx-cnpg-crds/values.yaml
deployment/helm/charts/onyx/Chart.yaml
deployment/helm/charts/onyx/values-ci.yaml
deployment/helm/charts/onyx/values-lite.yaml
deployment/helm/charts/onyx/values.yaml
deployment/helm/dev/values-localdev.yaml
tools/loadtest/Dockerfile
tools/loadtest/mock_llm/Dockerfile
tools/profiling/docker-compose.yml
web/Dockerfile
```
## Container Image References
Count: 110
```text
HEAD:deployment/docker_compose/docker-compose.airgap-tls-test.yml:3:    image: ${ONYX_BACKEND_IMAGE:?ONYX_BACKEND_IMAGE must be set}
HEAD:deployment/docker_compose/docker-compose.craft.yml:69:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.craft.yml:141:    image: ${SANDBOX_CONTAINER_IMAGE:-onyxdotapp/sandbox:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:5:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:latest}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:12:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:43:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:5:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:latest}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:11:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:87:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:161:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:241:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:285:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:331:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:353:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:392:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:447:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:461:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:480:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
HEAD:deployment/docker_compose/docker-compose.prod.yml:11:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod.yml:87:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod.yml:161:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod.yml:241:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod.yml:285:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.prod.yml:331:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
HEAD:deployment/docker_compose/docker-compose.prod.yml:353:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
HEAD:deployment/docker_compose/docker-compose.prod.yml:392:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
HEAD:deployment/docker_compose/docker-compose.prod.yml:449:    image: certbot/certbot
HEAD:deployment/docker_compose/docker-compose.prod.yml:462:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
HEAD:deployment/docker_compose/docker-compose.prod.yml:476:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
HEAD:deployment/docker_compose/docker-compose.prod.yml:495:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:5:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:52:    image: onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:96:    image: onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:118:    image: onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:135:    image: onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:154:    image: postgres:15.2-alpine
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:169:    image: opensearchproject/opensearch:3.6.0
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:192:    image: nginx:1.25.5-alpine
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:219:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
HEAD:deployment/docker_compose/docker-compose.search-testing.yml:239:    image: redis:7.4-alpine
HEAD:deployment/docker_compose/docker-compose.template.yml:54:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.template.yml:155:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.template.yml:245:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.template.yml:325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.template.yml:376:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.template.yml:430:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
HEAD:deployment/docker_compose/docker-compose.template.yml:465:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
HEAD:deployment/docker_compose/docker-compose.template.yml:504:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
HEAD:deployment/docker_compose/docker-compose.template.yml:588:    image: certbot/certbot
HEAD:deployment/docker_compose/docker-compose.template.yml:602:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
HEAD:deployment/docker_compose/docker-compose.template.yml:628:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
HEAD:deployment/docker_compose/docker-compose.template.yml:664:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
HEAD:deployment/docker_compose/docker-compose.yml:48:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.yml:130:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.yml:202:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.yml:282:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.yml:325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
HEAD:deployment/docker_compose/docker-compose.yml:370:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
HEAD:deployment/docker_compose/docker-compose.yml:400:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
HEAD:deployment/docker_compose/docker-compose.yml:439:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
HEAD:deployment/docker_compose/docker-compose.yml:499:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
HEAD:deployment/docker_compose/docker-compose.yml:521:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
HEAD:deployment/docker_compose/docker-compose.yml:551:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:500:                    image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:4563:                        image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:6720:              image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:6847:                  image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:7603:                    image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:9555:                            image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:11075:                            image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:12588:                            image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:15525:                            image:
HEAD:deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml:16133:                                image:
HEAD:deployment/helm/charts/onyx/Chart.yaml:19:      image: docker.io/onyxdotapp/onyx-web-server:latest
HEAD:deployment/helm/charts/onyx/Chart.yaml:21:      image: docker.io/onyxdotapp/onyx-backend:latest
HEAD:deployment/helm/charts/onyx/templates/api-deployment.yaml:64:          image: "{{ .Values.api.image.repository }}:{{ .Values.api.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-beat.yaml:71:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-docfetching.yaml:62:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-docprocessing.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-heavy.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-light.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-monitoring.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-primary.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/celery-worker-user-file-processing.yaml:60:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/discordbot.yaml:63:          image: "{{ .Values.discordbot.image.repository }}:{{ .Values.discordbot.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/indexing-model-deployment.yaml:57:        image: "{{ .Values.indexCapability.image.repository }}:{{ .Values.indexCapability.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/inference-model-deployment.yaml:48:        image: "{{ .Values.inferenceCapability.image.repository }}:{{ .Values.inferenceCapability.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:58:          image: "{{ .Values.mcpServer.image.repository }}:{{ .Values.mcpServer.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml:82:          image: bitnami/kubectl:latest
HEAD:deployment/helm/charts/onyx/templates/sandbox-image-prepuller.yaml:71:          image: {{ $image }}
HEAD:deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml:68:        image: {{ $image }}
HEAD:deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml:93:        image: {{ $image }}
HEAD:deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml:133:        image: {{ $image }}
HEAD:deployment/helm/charts/onyx/templates/sandbox-proxy/deployment.yaml:70:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/sandbox-proxy/deployment.yaml:101:          image: "{{ .Values.celery_shared.image.repository }}:{{ .Values.celery_shared.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/slackbot.yaml:57:          image: "{{ .Values.slackbot.image.repository }}:{{ .Values.slackbot.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/tests/test-connection.yaml:14:      image: curlimages/curl:8.10.1
HEAD:deployment/helm/charts/onyx/templates/webserver-deployment.yaml:60:          image: "{{ .Values.webserver.image.repository }}:{{ .Values.webserver.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates_disabled/background-deployment.yaml:40:          image: "{{ .Values.background.image.repository }}:{{ .Values.background.image.tag | default .Chart.AppVersion }}"
HEAD:deployment/helm/charts/onyx/values.yaml:149:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:211:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:291:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:445:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:533:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:678:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:1036:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:1065:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:1094:  image:
HEAD:deployment/helm/charts/onyx/values.yaml:1194:    image: quay.io/opstree/redis
```
## File and Blob Assets
Evidence lines: 550
```text
HEAD:backend/onyx/chat/chat_utils.py:38:    UserFileStatus,
HEAD:backend/onyx/chat/chat_utils.py:41:from onyx.db.file_record import FileRecordNotFoundError
HEAD:backend/onyx/chat/chat_utils.py:46:from onyx.db.models import ChatMessage, ChatSession, Persona, User, UserFile
HEAD:backend/onyx/chat/chat_utils.py:54:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/onyx/chat/chat_utils.py:55:from onyx.file_store.models import ChatFileType, FileDescriptor
HEAD:backend/onyx/chat/chat_utils.py:56:from onyx.file_store.utils import plaintext_file_name_for_id, store_plaintext
HEAD:backend/onyx/chat/chat_utils.py:110:    — the ID that FileReaderTool accepts (``UserFile.id`` for user files).
HEAD:backend/onyx/chat/chat_utils.py:459:    file_store = get_default_file_store()
HEAD:backend/onyx/chat/chat_utils.py:464:        plaintext_io = file_store.read_file(plaintext_key, mode="b")
HEAD:backend/onyx/chat/chat_utils.py:508:    # Look up the UserFile row first (when one exists) — it supplies the token
HEAD:backend/onyx/chat/chat_utils.py:511:    user_file: UserFile | None = None
HEAD:backend/onyx/chat/chat_utils.py:519:        UserFileStatus.PROCESSING,
HEAD:backend/onyx/chat/chat_utils.py:520:        UserFileStatus.INDEXING,
HEAD:backend/onyx/chat/chat_utils.py:531:            file_io = get_default_file_store().read_file(file_id, mode="b")
HEAD:backend/onyx/chat/chat_utils.py:567:            return get_default_file_store().read_file(file_id, mode="b").read()
HEAD:backend/onyx/chat/chat_utils.py:568:        except FileRecordNotFoundError:
HEAD:backend/onyx/chat/chat_utils.py:1036:    file_store = get_default_file_store()
HEAD:backend/onyx/chat/chat_utils.py:1046:            record = file_store.read_file_record(doc.file_id)
HEAD:backend/onyx/chat/chat_utils.py:1065:            content = file_store.read_file(doc.file_id, mode="b").read()
HEAD:backend/onyx/chat/incognito.py:43:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/onyx/chat/incognito.py:44:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/chat/incognito.py:135:def sweep_incognito_generated_files(db_session: Session) -> None:
HEAD:backend/onyx/chat/incognito.py:136:    """Retry deletion of tool-generated blobs a teardown pass failed to remove.
HEAD:backend/onyx/chat/incognito.py:138:    A blob's record carries the session that produced it and deleting the blob
HEAD:backend/onyx/chat/incognito.py:158:            delete_incognito_generated_files(session_id, db_session)
HEAD:backend/onyx/chat/incognito.py:160:            # One unreachable blob must not strand every session behind it.
HEAD:backend/onyx/chat/incognito.py:243:def delete_incognito_generated_files(
HEAD:backend/onyx/chat/incognito.py:246:    """Delete the blobs the session's tools saved. True when none remain.
HEAD:backend/onyx/chat/incognito.py:248:    The file record carries the session stamp, so deleting the blob deletes the
HEAD:backend/onyx/chat/incognito.py:249:    handle with it. A blob the store refuses keeps both, which is what the
HEAD:backend/onyx/chat/incognito.py:251:    file_store = get_default_file_store()
HEAD:backend/onyx/chat/incognito.py:255:            file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/chat/llm_loop.py:46:from onyx.file_store.models import ChatFileType
HEAD:backend/onyx/chat/llm_loop.py:71:    CustomToolUserFileSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:72:    MemoryToolResponseSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:1172:                        if parsed.get("generated_files"):
HEAD:backend/onyx/chat/llm_loop.py:1231:                # Extract generated_files if this is a code interpreter response
HEAD:backend/onyx/chat/llm_loop.py:1232:                generated_files = None
HEAD:backend/onyx/chat/llm_loop.py:1234:                    generated_files = (
HEAD:backend/onyx/chat/llm_loop.py:1235:                        tool_response.rich_response.generated_files or None
HEAD:backend/onyx/chat/llm_loop.py:1238:                # Custom tools save image/CSV blobs and return their ids.
HEAD:backend/onyx/chat/llm_loop.py:1243:                    tool_response.rich_response.tool_result, CustomToolUserFileSnapshot
HEAD:backend/onyx/chat/llm_loop.py:1250:                memory_snapshot: MemoryToolResponseSnapshot | None = None
HEAD:backend/onyx/chat/llm_loop.py:1280:                        memory_snapshot = MemoryToolResponseSnapshot(
HEAD:backend/onyx/chat/llm_loop.py:1291:                elif memory_snapshot:
HEAD:backend/onyx/chat/llm_loop.py:1292:                    saved_response = json.dumps(memory_snapshot.model_dump())
HEAD:backend/onyx/chat/llm_loop.py:1314:                    generated_files=generated_files,
HEAD:backend/onyx/chat/llm_step.py:22:from onyx.file_store.models import ChatFileType
HEAD:backend/onyx/chat/models.py:9:from onyx.file_store.models import ChatFileType, InMemoryChatFile
HEAD:backend/onyx/chat/models.py:131:        from onyx.file_store.models import install_lazy_content_loader
HEAD:backend/onyx/chat/process_message.py:93:from onyx.db.models import ChatMessage, ChatSession, Persona, User, UserFile
HEAD:backend/onyx/chat/process_message.py:100:from onyx.file_store.models import ChatFileType, InMemoryChatFile
HEAD:backend/onyx/chat/process_message.py:101:from onyx.file_store.utils import (
HEAD:backend/onyx/chat/process_message.py:102:    get_default_file_store,
HEAD:backend/onyx/chat/process_message.py:260:    user_files: list[UserFile],
HEAD:backend/onyx/chat/process_message.py:299:                return get_default_file_store().read_file(file_id, mode="b").read()
HEAD:backend/onyx/chat/process_message.py:318:) -> list[UserFile]:
HEAD:backend/onyx/chat/process_message.py:377:    user_files: list[UserFile],
HEAD:backend/onyx/chat/process_message.py:514:def _build_tool_metadata(user_file: UserFile) -> FileToolMetadata:
HEAD:backend/onyx/chat/process_message.py:515:    """Build lightweight FileToolMetadata from a UserFile record.
HEAD:backend/onyx/chat/process_message.py:1241:        when the stop-button path snapshots a still-running model mid-loop —
HEAD:backend/onyx/chat/process_message.py:1516:                            # Snapshot every model now: finished loops save
HEAD:backend/onyx/chat/process_message.py:1771:            # Set for the whole turn so a blob any tool saves carries the
HEAD:backend/onyx/chat/process_message.py:1987:    # Snapshot all state under the container's lock before any DB write.
HEAD:backend/onyx/chat/prompt_utils.py:10:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/chat/save_chat.py:17:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/chat/save_chat.py:34:        if not tool_call_info.generated_files:
HEAD:backend/onyx/chat/save_chat.py:36:        for gen_file in tool_call_info.generated_files:
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:11:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE, STANDARD_CHUNK_SIZE
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:25:    """Create a PostgreSQL large object from *content* and return its OID.
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:67:            raise RuntimeError("Failed to create large object")
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:77:    """Read a PostgreSQL large object identified by *lobj_oid*.
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:80:    to ``lo_get`` which returns the large object's contents as *bytea*.
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:116:            raise RuntimeError("Failed to read large object")
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:130:    """Remove a large object by OID, regardless of driver implementation."""
HEAD:backend/onyx/db/chat.py:28:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/onyx/db/chat.py:29:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/db/chat.py:225:    file_store = get_default_file_store()
HEAD:backend/onyx/db/chat.py:231:            file_store.delete_file(file_id=file_info["id"], error_on_missing=False)
HEAD:backend/onyx/db/connector.py:45:    from onyx.db.enums import UserFileStatus
HEAD:backend/onyx/db/connector.py:46:    from onyx.db.models import UserFile
HEAD:backend/onyx/db/connector.py:48:    stmt = select(exists(UserFile).where(UserFile.status == UserFileStatus.COMPLETED))
HEAD:backend/onyx/db/connector_credential_pair.py:96:class ConnectorStateSnapshot(BaseModel):
HEAD:backend/onyx/db/connector_credential_pair.py:113:def get_connector_state_snapshots(
HEAD:backend/onyx/db/connector_credential_pair.py:115:) -> list[ConnectorStateSnapshot]:
HEAD:backend/onyx/db/connector_credential_pair.py:144:        ConnectorStateSnapshot(
HEAD:backend/onyx/db/connector_credential_pair.py:262:            to avoid fetching large JSONB blobs when they aren't needed.
HEAD:backend/onyx/db/document.py:58:from onyx.file_store.staging import delete_files_best_effort
HEAD:backend/onyx/db/document.py:309:    has none. The reindex port snapshots this at start as its upper bound so it
HEAD:backend/onyx/db/engine/tenant_utils.py:62:        conn.execute(text("DROP TABLE IF EXISTS _alembic_version_snapshot"))
HEAD:backend/onyx/db/engine/tenant_utils.py:73:                "CREATE TEMP TABLE _alembic_version_snapshot (schema_name text, version_num text)"
HEAD:backend/onyx/db/engine/tenant_utils.py:95:                                'INSERT INTO _alembic_version_snapshot
HEAD:backend/onyx/db/engine/tenant_utils.py:116:            text("SELECT schema_name, version_num FROM _alembic_version_snapshot")
HEAD:backend/onyx/db/engine/tenant_utils.py:120:        conn.execute(text("DROP TABLE IF EXISTS _alembic_version_snapshot"))
HEAD:backend/onyx/db/engine/tenant_utils.py:123:    # Schemas missing from the snapshot have no alembic_version table yet and
HEAD:backend/onyx/db/enums.py:294:class UserFileStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:474:    SLEEPING = "sleeping"  # Pod terminated, snapshots saved to FileStore
HEAD:backend/onyx/db/file_content.py:4:from onyx.db.file_record import FileRecordNotFoundError
HEAD:backend/onyx/db/file_content.py:5:from onyx.db.models import FileContent
HEAD:backend/onyx/db/file_content.py:11:) -> FileContent:
HEAD:backend/onyx/db/file_content.py:12:    record = db_session.query(FileContent).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_content.py:14:        raise FileRecordNotFoundError(
HEAD:backend/onyx/db/file_content.py:23:) -> FileContent | None:
HEAD:backend/onyx/db/file_content.py:24:    return db_session.query(FileContent).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_content.py:32:) -> FileContent:
HEAD:backend/onyx/db/file_content.py:35:    stmt = insert(FileContent).values(
HEAD:backend/onyx/db/file_content.py:41:        index_elements=[FileContent.file_id],
HEAD:backend/onyx/db/file_content.py:50:    return db_session.get(FileContent, file_id)  # ty: ignore[invalid-return-type]
HEAD:backend/onyx/db/file_content.py:60:    This avoids creating a duplicate row that shares the same Large Object OID,
HEAD:backend/onyx/db/file_content.py:64:        db_session.query(FileContent)
HEAD:backend/onyx/db/file_content.py:78:    db_session.query(FileContent).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:8:from onyx.db.models import FileRecord, IndexAttempt
HEAD:backend/onyx/db/file_record.py:9:from onyx.file_store.constants import INCOGNITO_SESSION_METADATA_KEY
HEAD:backend/onyx/db/file_record.py:15:) -> list[FileRecord]:
HEAD:backend/onyx/db/file_record.py:18:            select(FileRecord).where(
HEAD:backend/onyx/db/file_record.py:20:                    FileRecord.file_id.like(f"{QUERY_REPORT_NAME_PREFIX}-%"),
HEAD:backend/onyx/db/file_record.py:21:                    FileRecord.file_type == FileType.CSV,
HEAD:backend/onyx/db/file_record.py:22:                    FileRecord.file_origin == FileOrigin.QUERY_HISTORY_CSV,
HEAD:backend/onyx/db/file_record.py:29:def get_filerecord_by_file_id_optional(
HEAD:backend/onyx/db/file_record.py:32:) -> FileRecord | None:
HEAD:backend/onyx/db/file_record.py:33:    return db_session.query(FileRecord).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_record.py:36:class FileRecordNotFoundError(RuntimeError):
HEAD:backend/onyx/db/file_record.py:45:def get_filerecord_by_file_id(
HEAD:backend/onyx/db/file_record.py:48:) -> FileRecord:
HEAD:backend/onyx/db/file_record.py:49:    filestore = db_session.query(FileRecord).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_record.py:52:        raise FileRecordNotFoundError(
HEAD:backend/onyx/db/file_record.py:59:def get_filerecords_by_file_ids(
HEAD:backend/onyx/db/file_record.py:62:) -> list[FileRecord]:
HEAD:backend/onyx/db/file_record.py:68:        db_session.scalars(select(FileRecord).where(FileRecord.file_id.in_(file_ids)))
HEAD:backend/onyx/db/file_record.py:72:def update_filerecord_file_sizes(
HEAD:backend/onyx/db/file_record.py:81:        update(FileRecord)
HEAD:backend/onyx/db/file_record.py:82:        .where(FileRecord.file_id.in_(file_sizes.keys()))
HEAD:backend/onyx/db/file_record.py:85:        .where(FileRecord.file_size.is_(None))
HEAD:backend/onyx/db/file_record.py:86:        .values(file_size=case(file_sizes, value=FileRecord.file_id))
HEAD:backend/onyx/db/file_record.py:90:def get_filerecord_by_prefix(
HEAD:backend/onyx/db/file_record.py:93:) -> list[FileRecord]:
HEAD:backend/onyx/db/file_record.py:95:        return db_session.query(FileRecord).all()
HEAD:backend/onyx/db/file_record.py:97:        db_session.query(FileRecord).filter(FileRecord.file_id.like(f"{prefix}%")).all()
HEAD:backend/onyx/db/file_record.py:101:def delete_filerecord_by_file_id(
HEAD:backend/onyx/db/file_record.py:105:    db_session.query(FileRecord).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:108:def update_filerecord_origin(
HEAD:backend/onyx/db/file_record.py:117:    db_session.query(FileRecord).filter(
HEAD:backend/onyx/db/file_record.py:118:        FileRecord.file_id == file_id,
HEAD:backend/onyx/db/file_record.py:119:        FileRecord.file_origin == from_origin,
HEAD:backend/onyx/db/file_record.py:120:    ).update({FileRecord.file_origin: to_origin})
HEAD:backend/onyx/db/file_record.py:130:            select(FileRecord.file_id)
HEAD:backend/onyx/db/file_record.py:131:            .where(FileRecord.file_origin == FileOrigin.INDEXING_STAGING)
HEAD:backend/onyx/db/file_record.py:133:                FileRecord.file_metadata["index_attempt_id"].as_string()
HEAD:backend/onyx/db/file_record.py:164:            select(FileRecord.file_id)
HEAD:backend/onyx/db/file_record.py:165:            .where(FileRecord.file_origin == FileOrigin.INDEXING_STAGING)
HEAD:backend/onyx/db/file_record.py:167:                FileRecord.file_metadata["cc_pair_id"].as_string() == str(cc_pair_id)
HEAD:backend/onyx/db/file_record.py:169:            .where(FileRecord.file_metadata["tenant_id"].as_string() == tenant_id)
HEAD:backend/onyx/db/file_record.py:171:                FileRecord.file_metadata["index_attempt_id"].as_string()
HEAD:backend/onyx/db/file_record.py:175:                FileRecord.file_metadata["index_attempt_id"]
HEAD:backend/onyx/db/file_record.py:183:def upsert_filerecord(
HEAD:backend/onyx/db/file_record.py:193:) -> FileRecord:
HEAD:backend/onyx/db/file_record.py:197:    Every backend writes its record here, so this is also where a blob saved
HEAD:backend/onyx/db/file_record.py:207:    stmt = insert(FileRecord).values(
HEAD:backend/onyx/db/file_record.py:218:        index_elements=[FileRecord.file_id],
HEAD:backend/onyx/db/file_record.py:231:    return db_session.get(FileRecord, file_id)  # ty: ignore[invalid-return-type]
HEAD:backend/onyx/db/file_record.py:235:    """Ids of blobs a content-free session produced and has not deleted yet."""
HEAD:backend/onyx/db/file_record.py:238:            select(FileRecord.file_id).where(
HEAD:backend/onyx/db/file_record.py:239:                FileRecord.file_metadata[INCOGNITO_SESSION_METADATA_KEY].astext
HEAD:backend/onyx/db/file_record.py:249:    """Sessions still holding blobs. Empty in steady state, since teardown
HEAD:backend/onyx/db/file_record.py:256:        select(FileRecord.file_metadata[INCOGNITO_SESSION_METADATA_KEY].astext)
HEAD:backend/onyx/db/file_record.py:258:        .where(FileRecord.file_metadata.has_key(INCOGNITO_SESSION_METADATA_KEY))
HEAD:backend/onyx/db/incognito.py:17:from onyx.db.enums import IncognitoRecordMode, UserFileStatus
HEAD:backend/onyx/db/incognito.py:18:from onyx.db.models import ChatSession, User__UserGroup, UserFile, UserGroup
HEAD:backend/onyx/db/incognito.py:64:        update(UserFile)
HEAD:backend/onyx/db/incognito.py:65:        .where(UserFile.id.in_(file_ids))
HEAD:backend/onyx/db/incognito.py:66:        .values(status=UserFileStatus.DELETING)
HEAD:backend/onyx/db/incognito.py:80:        UserFile.incognito_session_id == chat_session_id,
HEAD:backend/onyx/db/incognito.py:81:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:84:        conditions.append(UserFile.user_id == user_id)
HEAD:backend/onyx/db/incognito.py:85:    file_ids = list(db_session.scalars(select(UserFile.id).where(*conditions)).all())
HEAD:backend/onyx/db/incognito.py:95:        UserFile.incognito.is_(True),
HEAD:backend/onyx/db/incognito.py:96:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:97:        UserFile.last_accessed_at < cutoff,
HEAD:backend/onyx/db/incognito.py:109:            select(UserFile.id)
HEAD:backend/onyx/db/incognito.py:110:            .where(*_stale_upload_conditions(), UserFile.incognito_session_id.is_(None))
HEAD:backend/onyx/db/incognito.py:111:            .order_by(UserFile.last_accessed_at)
HEAD:backend/onyx/db/incognito.py:131:        select(UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:132:        .outerjoin(ChatSession, ChatSession.id == UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:135:            UserFile.incognito_session_id.is_not(None),
HEAD:backend/onyx/db/incognito.py:138:        .group_by(UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:139:        .order_by(func.min(UserFile.last_accessed_at))
HEAD:backend/onyx/db/incognito.py:159:        update(UserFile)
HEAD:backend/onyx/db/incognito.py:161:            UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/incognito.py:162:            UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:176:            select(UserFile.id).where(
HEAD:backend/onyx/db/incognito.py:178:                UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/index_attempt_metrics.py:331:        # Snapshot before reset so a re-entrant ``record()`` during the DB
HEAD:backend/onyx/db/llm.py:1358:    # Both statements test the default in SQL rather than from a snapshot read
HEAD:backend/onyx/db/mcp.py:378:    read-compare-write over its JSON blob is atomic against concurrent writers."""
HEAD:backend/onyx/db/memory.py:22:    # Directory profile from the IdP login snapshot (country, department, ...)
HEAD:backend/onyx/db/models.py:124:    UserFileStatus,
HEAD:backend/onyx/db/models.py:129:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/db/models.py:493:    files: Mapped[list["UserFile"]] = relationship("UserFile", back_populates="user")
HEAD:backend/onyx/db/models.py:2475:    # Snapshot of resolved error rows captured at completion. Outlives later
HEAD:backend/onyx/db/models.py:4304:    # Relationship to UserFile
HEAD:backend/onyx/db/models.py:4305:    user_files: Mapped[list["UserFile"]] = relationship(
HEAD:backend/onyx/db/models.py:4306:        "UserFile",
HEAD:backend/onyx/db/models.py:4343:class Persona__UserFile(Base):
HEAD:backend/onyx/db/models.py:4841:class FileRecord(Base):
HEAD:backend/onyx/db/models.py:4852:    # External storage support (S3, MinIO, Azure Blob, etc.)
HEAD:backend/onyx/db/models.py:4871:class FileContent(Base):
HEAD:backend/onyx/db/models.py:4872:    """Stores file content in PostgreSQL using Large Objects.
HEAD:backend/onyx/db/models.py:4873:    Used when FILE_STORE_BACKEND=postgres to avoid needing S3/MinIO."""
HEAD:backend/onyx/db/models.py:4882:    # PostgreSQL Large Object OID referencing pg_largeobject
HEAD:backend/onyx/db/models.py:5446:    using the FileRecord
HEAD:backend/onyx/db/models.py:5467:    file = relationship("FileRecord")
HEAD:backend/onyx/db/models.py:5508:class Project__UserFile(Base):
HEAD:backend/onyx/db/models.py:5541:    user_files: Mapped[list["UserFile"]] = relationship(
HEAD:backend/onyx/db/models.py:5542:        "UserFile",
HEAD:backend/onyx/db/models.py:5543:        secondary=Project__UserFile.__table__,
HEAD:backend/onyx/db/models.py:5558:class UserFile(Base):
HEAD:backend/onyx/db/models.py:5564:        secondary=Persona__UserFile.__table__,
HEAD:backend/onyx/db/models.py:5577:    status: Mapped[UserFileStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:5578:        Enum(UserFileStatus, native_enum=False, name="userfilestatus"),
HEAD:backend/onyx/db/models.py:5580:        default=UserFileStatus.PROCESSING,
HEAD:backend/onyx/db/models.py:5618:        secondary=Project__UserFile.__table__,
HEAD:backend/onyx/db/models.py:6130:    """Stores the signed license blob (singleton pattern - only one row)."""
HEAD:backend/onyx/db/models.py:6399:    snapshots: Mapped[list["Snapshot"]] = relationship(
HEAD:backend/onyx/db/models.py:6400:        "Snapshot", back_populates="session", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:6620:class Snapshot(Base):
HEAD:backend/onyx/db/models.py:6621:    """Stores metadata about session output snapshots."""
HEAD:backend/onyx/db/models.py:6623:    __tablename__ = "snapshot"
HEAD:backend/onyx/db/models.py:6641:        "BuildSession", back_populates="snapshots"
HEAD:backend/onyx/db/models.py:6645:        Index("ix_snapshot_session_created", "session_id", desc("created_at")),
HEAD:backend/onyx/db/models.py:7456:    protocol-specific settings live in the encrypted `config` blob, validated
HEAD:backend/onyx/db/persona.py:40:    UserFile,
HEAD:backend/onyx/db/persona.py:55:    FullPersonaSnapshot,
HEAD:backend/onyx/db/persona.py:56:    MinimalPersonaSnapshot,
HEAD:backend/onyx/db/persona.py:58:    PersonaSnapshot,
HEAD:backend/onyx/db/persona.py:560:    snapshots: Sequence[MinimalPersonaSnapshot | PersonaSnapshot],
HEAD:backend/onyx/db/persona.py:566:    """Stamp each list snapshot with the same affordance map the single-agent GET does,
HEAD:backend/onyx/db/persona.py:569:    not one per persona. ``snapshots`` and ``personas`` must be in the same order."""
HEAD:backend/onyx/db/persona.py:586:    for snapshot, persona in zip(snapshots, personas, strict=True):
HEAD:backend/onyx/db/persona.py:588:        snapshot.permissions = persona_permissions(
HEAD:backend/onyx/db/persona.py:616:) -> FullPersonaSnapshot:
HEAD:backend/onyx/db/persona.py:697:    # Eager-load the share relations the snapshot reads so from_model doesn't
HEAD:backend/onyx/db/persona.py:711:    return FullPersonaSnapshot.from_model(persona)
HEAD:backend/onyx/db/persona.py:1032:def get_minimal_persona_snapshots_for_user(
HEAD:backend/onyx/db/persona.py:1039:) -> list[MinimalPersonaSnapshot]:
HEAD:backend/onyx/db/persona.py:1072:    snapshots = [
HEAD:backend/onyx/db/persona.py:1073:        MinimalPersonaSnapshot.from_model(
HEAD:backend/onyx/db/persona.py:1080:    stamp_persona_permissions(snapshots, results, user, db_session, user_group_ids)
HEAD:backend/onyx/db/persona.py:1081:    return snapshots
HEAD:backend/onyx/db/persona.py:1084:def get_persona_snapshots_for_user(
HEAD:backend/onyx/db/persona.py:1091:) -> list[PersonaSnapshot]:
HEAD:backend/onyx/db/persona.py:1124:    snapshots = [PersonaSnapshot.from_model(persona) for persona in results]
HEAD:backend/onyx/db/persona.py:1126:    stamp_persona_permissions(snapshots, results, user, db_session, user_group_ids)
HEAD:backend/onyx/db/persona.py:1127:    return snapshots
HEAD:backend/onyx/db/persona.py:1167:def get_minimal_persona_snapshots_paginated(
HEAD:backend/onyx/db/persona.py:1176:) -> list[MinimalPersonaSnapshot]:
HEAD:backend/onyx/db/persona.py:1177:    """Gets a single page of minimal persona snapshots with ordering.
HEAD:backend/onyx/db/persona.py:1195:        List of MinimalPersonaSnapshot objects for the requested page, ordered
HEAD:backend/onyx/db/persona.py:1207:    # Do eager loading of columns we know MinimalPersonaSnapshot.from_model will
HEAD:backend/onyx/db/persona.py:1237:    snapshots = [
HEAD:backend/onyx/db/persona.py:1238:        MinimalPersonaSnapshot.from_model(
HEAD:backend/onyx/db/persona.py:1245:    stamp_persona_permissions(snapshots, results, user, db_session, user_group_ids)
HEAD:backend/onyx/db/persona.py:1246:    return snapshots
HEAD:backend/onyx/db/persona.py:1249:def get_persona_snapshots_paginated(
HEAD:backend/onyx/db/persona.py:1258:) -> list[PersonaSnapshot]:
HEAD:backend/onyx/db/persona.py:1259:    """Gets a single page of persona snapshots (admin view) with ordering.
HEAD:backend/onyx/db/persona.py:1264:    This function returns PersonaSnapshot objects which contain more detailed
HEAD:backend/onyx/db/persona.py:1265:    information than MinimalPersonaSnapshot, used for admin views.
HEAD:backend/onyx/db/persona.py:1280:        List of PersonaSnapshot objects for the requested page, ordered by
HEAD:backend/onyx/db/persona.py:1292:    # Do eager loading of columns we know PersonaSnapshot.from_model will need.
HEAD:backend/onyx/db/persona.py:1320:    snapshots = [PersonaSnapshot.from_model(persona) for persona in results]
HEAD:backend/onyx/db/persona.py:1322:    stamp_persona_permissions(snapshots, results, user, db_session, user_group_ids)
HEAD:backend/onyx/db/persona.py:1323:    return snapshots
HEAD:backend/onyx/db/persona.py:1544:    """Flag the given UserFile rows so the background sync task picks them up
HEAD:backend/onyx/db/persona.py:1548:    db_session.query(UserFile).filter(UserFile.id.in_(user_file_ids)).update(
HEAD:backend/onyx/db/persona.py:1549:        {UserFile.needs_persona_sync: True},
HEAD:backend/onyx/db/persona.py:1689:            db_session.query(UserFile).filter(UserFile.id.in_(user_file_ids)).all()
HEAD:backend/onyx/db/persona.py:1997:    # set (the share-snapshot path already fetched it) to avoid a second query.
HEAD:backend/onyx/db/persona_sharing.py:2:the persona db layer and the API snapshot models can use them without cycles."""
HEAD:backend/onyx/db/port_attempt.py:85:    `up_to_doc_id` is the snapshot upper bound, carried across resumes.
HEAD:backend/onyx/db/port_attempt.py:392:    reconciler (which writes the promoted index from blob/DB, never the source), so it
HEAD:backend/onyx/db/projects.py:20:from onyx.db.enums import UserFileStatus
HEAD:backend/onyx/db/projects.py:21:from onyx.db.models import Project__UserFile, User, UserFile, UserProject
HEAD:backend/onyx/db/projects.py:34:    user_files: list[UserFile]
HEAD:backend/onyx/db/projects.py:43:    def indexable_files(self) -> list[UserFile]:
HEAD:backend/onyx/db/projects.py:84:        new_file = UserFile(
HEAD:backend/onyx/db/projects.py:95:            status=UserFileStatus.SKIPPED if should_skip else UserFileStatus.PROCESSING,
HEAD:backend/onyx/db/projects.py:100:        # Persist the UserFile first to satisfy FK constraints for association table
HEAD:backend/onyx/db/projects.py:105:            project_to_user_file = Project__UserFile(
HEAD:backend/onyx/db/projects.py:206:) -> list[UserFile]:
HEAD:backend/onyx/db/projects.py:212:        db_session.query(UserFile)
HEAD:backend/onyx/db/projects.py:213:        .join(Project__UserFile)
HEAD:backend/onyx/db/projects.py:214:        .filter(Project__UserFile.project_id == project_id)
HEAD:backend/onyx/db/projects.py:253:        db_session.query(func.coalesce(func.sum(UserFile.token_count), 0))
HEAD:backend/onyx/db/projects.py:255:            UserFile.user_id == user_id,
HEAD:backend/onyx/db/projects.py:256:            UserFile.projects.any(id=project_id),
HEAD:backend/onyx/db/skill.py:15:`bundle_file_id` so the caller can drop the blob from the file store
HEAD:backend/onyx/db/skill.py:16:immediately (skills sync via S3-backed bundles, so blob retention isn't
HEAD:backend/onyx/db/skill.py:406:    """Swap a skill's bundle blob and refresh its description.
HEAD:backend/onyx/db/skill.py:408:    Returns the old bundle file id so the caller can delete the old blob from
HEAD:backend/onyx/db/sso_provider.py:69:    # or decrypts assertions. Held in the encrypted config blob.
HEAD:backend/onyx/db/targeted_reindex.py:307:    `summary` is a snapshot of the cleared error rows captured before
HEAD:backend/onyx/db/user_file.py:7:from onyx.db.enums import UserFileStatus
HEAD:backend/onyx/db/user_file.py:8:from onyx.db.models import Persona, Project__UserFile, User, UserFile
HEAD:backend/onyx/db/user_file.py:19:    stmt = select(UserFile.id, UserFile.chunk_count).where(
HEAD:backend/onyx/db/user_file.py:20:        UserFile.id.in_(user_file_ids)
HEAD:backend/onyx/db/user_file.py:44:            db_session.query(func.sum(UserFile.token_count))
HEAD:backend/onyx/db/user_file.py:45:            .filter(UserFile.id.in_(file_ids))
HEAD:backend/onyx/db/user_file.py:60:    stmt = select(Project__UserFile.user_file_id, Project__UserFile.project_id).where(
HEAD:backend/onyx/db/user_file.py:61:        Project__UserFile.user_file_id.in_(user_file_uuid_ids)
HEAD:backend/onyx/db/user_file.py:80:        select(UserFile)
HEAD:backend/onyx/db/user_file.py:81:        .where(UserFile.id.in_(user_file_ids))
HEAD:backend/onyx/db/user_file.py:82:        .options(selectinload(UserFile.assistants))
HEAD:backend/onyx/db/user_file.py:100:        db_session.query(UserFile)
HEAD:backend/onyx/db/user_file.py:101:        .filter(UserFile.id.in_(user_file_ids))
HEAD:backend/onyx/db/user_file.py:102:        .update({UserFile.last_accessed_at: now}, synchronize_session=False)
HEAD:backend/onyx/db/user_file.py:109:) -> UserFile | None:
HEAD:backend/onyx/db/user_file.py:110:    """Fetch a UserFile row by id. Accepts str for callers whose input may not
HEAD:backend/onyx/db/user_file.py:111:    even be a UserFile id (e.g. a storage file_id) — those resolve to None."""
HEAD:backend/onyx/db/user_file.py:112:    return db_session.query(UserFile).filter(UserFile.id == user_file_id).first()
HEAD:backend/onyx/db/user_file.py:116:    """Resolve a `UserFile.id` to its underlying `FileRecord.file_id`.
HEAD:backend/onyx/db/user_file.py:118:    Returns None when the input is not a known `UserFile.id` (e.g. when the
HEAD:backend/onyx/db/user_file.py:131:    user_files = db_session.query(UserFile).filter(UserFile.id.in_(user_file_ids)).all()
HEAD:backend/onyx/db/user_file.py:139:) -> list[UserFile]:
HEAD:backend/onyx/db/user_file.py:153:        db_session.query(UserFile)
HEAD:backend/onyx/db/user_file.py:155:            joinedload(UserFile.user),
HEAD:backend/onyx/db/user_file.py:156:            selectinload(UserFile.assistants).options(*persona_sub_options),
HEAD:backend/onyx/db/user_file.py:158:        .filter(UserFile.id.in_(user_file_ids))
HEAD:backend/onyx/db/user_file.py:164:# `str(UserFile.id)`), so these accept/return `str` and convert to UUID for the query;
HEAD:backend/onyx/db/user_file.py:174:            select(UserFile.user_id)
HEAD:backend/onyx/db/user_file.py:175:            .where(UserFile.status == UserFileStatus.COMPLETED)
HEAD:backend/onyx/db/user_file.py:190:    `up_to_id` (the snapshot max id at attempt creation) bounds the scan so the attempt
HEAD:backend/onyx/db/user_file.py:195:    stmt = select(UserFile.id).where(
HEAD:backend/onyx/db/user_file.py:196:        UserFile.user_id == user_id,
HEAD:backend/onyx/db/user_file.py:197:        UserFile.status == UserFileStatus.COMPLETED,
HEAD:backend/onyx/db/user_file.py:198:        UserFile.incognito.is_(False),
HEAD:backend/onyx/db/user_file.py:201:        stmt = stmt.where(UserFile.id > UUID(after_id))
HEAD:backend/onyx/db/user_file.py:203:        stmt = stmt.where(UserFile.id <= UUID(up_to_id))
HEAD:backend/onyx/db/user_file.py:204:    stmt = stmt.order_by(UserFile.id).limit(limit)
HEAD:backend/onyx/db/user_file.py:209:    """The greatest COMPLETED file id for a user — the attempt's snapshot upper bound."""
HEAD:backend/onyx/db/user_file.py:211:        select(UserFile.id)
HEAD:backend/onyx/db/user_file.py:213:            UserFile.user_id == user_id,
HEAD:backend/onyx/db/user_file.py:214:            UserFile.status == UserFileStatus.COMPLETED,
HEAD:backend/onyx/db/user_file.py:216:        .order_by(UserFile.id.desc())
HEAD:backend/onyx/db/user_file.py:230:        select(UserFile.id).where(
HEAD:backend/onyx/db/user_file.py:231:            UserFile.user_id == user_id,
HEAD:backend/onyx/db/user_file.py:232:            UserFile.status == UserFileStatus.COMPLETED,
HEAD:backend/onyx/db/user_file.py:233:            UserFile.id.in_([UUID(i) for i in ids]),
HEAD:backend/onyx/db/user_file.py:250:        update(UserFile)
HEAD:backend/onyx/db/user_file.py:251:        .where(UserFile.id == user_file_id)
HEAD:backend/onyx/db/user_file.py:260:        update(UserFile)
HEAD:backend/onyx/db/user_file.py:261:        .where(UserFile.id == user_file_id)
HEAD:backend/onyx/db/user_file.py:270:        select(func.count()).where(UserFile.secondary_reconcile_pending.is_(True))
HEAD:backend/onyx/db/user_file.py:286:                    UserFile.user_id.in_(user_ids),
HEAD:backend/onyx/db/user_file.py:287:                    UserFile.status == UserFileStatus.COMPLETED,
HEAD:backend/onyx/db/user_file.py:288:                    UserFile.secondary_reconcile_pending.is_(True),
HEAD:backend/onyx/file_store/README.md:3:The Onyx file store provides a unified interface for storing files and large binary objects. It supports four storage backends: S3-compatible storage (AWS S3, MinIO, Digital Ocean Spaces, etc.), Google Cloud Storage (GCS), Azure Blob Storage, and PostgreSQL Large Objects.
HEAD:backend/onyx/file_store/README.md:25:The backend is selected via the `FILE_STORE_BACKEND` environment variable:
HEAD:backend/onyx/file_store/README.md:31:| `azure` | Azure Blob Storage | Native Azure with Workload Identity / managed identity support |
HEAD:backend/onyx/file_store/README.md:32:| `postgres` | PostgreSQL Large Objects | No external storage service required |
HEAD:backend/onyx/file_store/README.md:39:FILE_STORE_BACKEND=s3
HEAD:backend/onyx/file_store/README.md:40:S3_FILE_STORE_BUCKET_NAME=your-bucket-name  # Defaults to 'onyx-file-store-bucket'
HEAD:backend/onyx/file_store/README.md:41:S3_FILE_STORE_PREFIX=onyx-files  # Optional, defaults to 'onyx-files'
HEAD:backend/onyx/file_store/README.md:56:FILE_STORE_BACKEND=s3
HEAD:backend/onyx/file_store/README.md:57:S3_FILE_STORE_BUCKET_NAME=your-bucket-name
HEAD:backend/onyx/file_store/README.md:68:FILE_STORE_BACKEND=s3
HEAD:backend/onyx/file_store/README.md:69:S3_FILE_STORE_BUCKET_NAME=your-space-name
HEAD:backend/onyx/file_store/README.md:79:FILE_STORE_BACKEND=gcs
HEAD:backend/onyx/file_store/README.md:80:GCS_FILE_STORE_BUCKET_NAME=your-bucket-name    # Required
HEAD:backend/onyx/file_store/README.md:81:GCS_FILE_STORE_PREFIX=onyx-files               # Optional, defaults to 'onyx-files'
HEAD:backend/onyx/file_store/README.md:109:### Azure Blob Storage
HEAD:backend/onyx/file_store/README.md:112:FILE_STORE_BACKEND=azure
HEAD:backend/onyx/file_store/README.md:113:AZURE_FILE_STORE_CONTAINER_NAME=your-container-name  # Required
HEAD:backend/onyx/file_store/README.md:114:AZURE_FILE_STORE_PREFIX=onyx-files                   # Optional, defaults to 'onyx-files'
HEAD:backend/onyx/file_store/README.md:117:# Set explicitly for Azurite or sovereign clouds (e.g. *.blob.core.usgovcloudapi.net):
HEAD:backend/onyx/file_store/README.md:118:AZURE_STORAGE_ACCOUNT_URL=https://yourstorageaccount.blob.core.windows.net
HEAD:backend/onyx/file_store/README.md:134:**Required RBAC role:** `Storage Blob Data Contributor` on the storage account (or container)
HEAD:backend/onyx/file_store/README.md:139:(`mcr.microsoft.com/azure-storage/azurite`) emulates Azure Blob Storage, playing the role MinIO
HEAD:backend/onyx/file_store/README.md:145:- `S3_FILE_STORE_BUCKET_NAME`: Your bucket/container name
HEAD:backend/onyx/file_store/README.md:150:### PostgreSQL Large Objects
HEAD:backend/onyx/file_store/README.md:153:FILE_STORE_BACKEND=postgres
HEAD:backend/onyx/file_store/README.md:161:- `S3BackedFileStore` (`file_store.py`): For S3-compatible storage (AWS S3, MinIO, etc.)
HEAD:backend/onyx/file_store/README.md:162:- `GCSBackedFileStore` (`gcs_file_store.py`): For Google Cloud Storage with native ADC support
HEAD:backend/onyx/file_store/README.md:163:- `AzureBlobBackedFileStore` (`azure_blob_file_store.py`): For Azure Blob Storage with DefaultAzureCredential support
HEAD:backend/onyx/file_store/README.md:164:- `PostgresBackedFileStore` (`postgres_file_store.py`): For PostgreSQL Large Objects
HEAD:backend/onyx/file_store/README.md:166:The factory function `get_default_file_store()` returns the appropriate implementation based on `FILE_STORE_BACKEND`. The database uses generic column names (`bucket_name`, `object_key`) to maintain compatibility across all backends.
HEAD:backend/onyx/file_store/README.md:186:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/onyx/file_store/README.md:190:file_store = get_default_file_store()
HEAD:backend/onyx/file_store/README.md:193:file_store.initialize()
HEAD:backend/onyx/file_store/README.md:197:    file_id = file_store.save_file(
HEAD:backend/onyx/file_store/README.md:206:exists = file_store.has_file(
HEAD:backend/onyx/file_store/README.md:211:file_content = file_store.read_file(file_id)
HEAD:backend/onyx/file_store/README.md:214:file_content = file_store.read_file(file_id, use_tempfile=True)
HEAD:backend/onyx/file_store/README.md:217:file_record = file_store.read_file_record(file_id)
HEAD:backend/onyx/file_store/README.md:220:file_with_mime = file_store.get_file_with_mime_type(file_id)
HEAD:backend/onyx/file_store/README.md:223:file_store.delete_file(file_id)
HEAD:backend/onyx/file_store/README.md:226:## Blob Connector: GCS Authentication
HEAD:backend/onyx/file_store/README.md:228:The blob storage connector (`backend/onyx/connectors/blob/connector.py`) also supports native GCS authentication via the admin UI. When creating a Google Cloud Storage connector, three auth methods are available:
HEAD:backend/onyx/file_store/README.md:234:**Security note:** When using ADC/Workload Identity in the blob connector, the connector inherits the permissions of the pod's service account. If the SA has access to buckets beyond the intended connector target (e.g., the internal file store bucket), an admin could point a connector at those buckets. This mirrors the existing S3 "Assume Role" auth method. Mitigation is IAM scoping at the infrastructure level: scope the pod's service account to only the buckets it should access.
HEAD:backend/onyx/file_store/README.md:243:4. Call `file_store.initialize()` during application startup to ensure the bucket exists
HEAD:backend/onyx/file_store/azure_blob_file_store.py:12:    from azure.storage.blob import BlobServiceClient
HEAD:backend/onyx/file_store/azure_blob_file_store.py:20:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:21:    get_filerecord_by_file_id,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:22:    get_filerecord_by_file_id_optional,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:23:    get_filerecord_by_prefix,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:24:    upsert_filerecord,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:26:from onyx.db.models import FileRecord
HEAD:backend/onyx/file_store/azure_blob_file_store.py:27:from onyx.file_store.file_store import FileStore, content_byte_size
HEAD:backend/onyx/file_store/azure_blob_file_store.py:28:from onyx.file_store.s3_key_utils import generate_s3_key
HEAD:backend/onyx/file_store/azure_blob_file_store.py:36:class AzureBlobBackedFileStore(FileStore):
HEAD:backend/onyx/file_store/azure_blob_file_store.py:37:    """Azure Blob Storage backed file store with Workload Identity support.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:51:        self._blob_service_client: BlobServiceClient | None = None
HEAD:backend/onyx/file_store/azure_blob_file_store.py:65:                self._account_url = f"https://{account_name}.blob.core.windows.net"
HEAD:backend/onyx/file_store/azure_blob_file_store.py:83:    def _get_blob_service_client(self) -> BlobServiceClient:
HEAD:backend/onyx/file_store/azure_blob_file_store.py:84:        """Initialize the Azure Blob service client if not already done.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:92:        if self._blob_service_client is None:
HEAD:backend/onyx/file_store/azure_blob_file_store.py:94:                from azure.storage.blob import BlobServiceClient
HEAD:backend/onyx/file_store/azure_blob_file_store.py:97:                    self._blob_service_client = (
HEAD:backend/onyx/file_store/azure_blob_file_store.py:98:                        BlobServiceClient.from_connection_string(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:107:                    self._blob_service_client = BlobServiceClient(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:114:                    self._blob_service_client = BlobServiceClient(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:120:                logger.error("Failed to import azure-storage-blob: %s", e)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:123:                logger.error("Failed to initialize Azure Blob client: %s", e)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:125:                    f"Failed to initialize Azure Blob client: {e}"
HEAD:backend/onyx/file_store/azure_blob_file_store.py:128:        return self._blob_service_client
HEAD:backend/onyx/file_store/azure_blob_file_store.py:131:        """Generate blob name from file name with tenant ID prefix.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:134:        Azure blob names (both allow `/` path segments and cap at 1024 chars).
HEAD:backend/onyx/file_store/azure_blob_file_store.py:151:        client = self._get_blob_service_client()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:190:            file_record = get_filerecord_by_file_id_optional(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:209:        from azure.storage.blob import ContentSettings
HEAD:backend/onyx/file_store/azure_blob_file_store.py:214:        client = self._get_blob_service_client()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:216:        blob_client = client.get_blob_client(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:217:            container=self._container_name, blob=object_key
HEAD:backend/onyx/file_store/azure_blob_file_store.py:228:        blob_client.upload_blob(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:236:                upsert_filerecord(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:249:            # Clean up the uploaded blob unless a committed record still
HEAD:backend/onyx/file_store/azure_blob_file_store.py:251:            # survives the rollback, so deleting the blob it points at would
HEAD:backend/onyx/file_store/azure_blob_file_store.py:254:            # blob is safe (and necessary) to remove.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:257:                    existing_record = get_filerecord_by_file_id_optional(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:266:                    blob_client.delete_blob()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:269:                    "Failed to clean up orphaned Azure blob %s/%s "
HEAD:backend/onyx/file_store/azure_blob_file_store.py:288:            file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:292:        client = self._get_blob_service_client()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:293:        blob_client = client.get_blob_client(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:294:            container=file_record.bucket_name, blob=file_record.object_key
HEAD:backend/onyx/file_store/azure_blob_file_store.py:299:            blob_client.download_blob().readinto(temp_file)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:303:            # No encoding is set on download_blob(), so readall() returns bytes.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:304:            content = blob_client.download_blob().readall()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:309:    ) -> FileRecord:
HEAD:backend/onyx/file_store/azure_blob_file_store.py:311:            file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:319:        """Get the size of a file in bytes by querying Azure blob properties."""
HEAD:backend/onyx/file_store/azure_blob_file_store.py:322:                file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:328:            client = self._get_blob_service_client()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:329:            blob_client = client.get_blob_client(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:330:                container=file_record.bucket_name, blob=file_record.object_key
HEAD:backend/onyx/file_store/azure_blob_file_store.py:333:                properties = blob_client.get_blob_properties()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:353:                file_record = get_filerecord_by_file_id_optional(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:369:                    delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:375:                client = self._get_blob_service_client()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:376:                blob_client = client.get_blob_client(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:377:                    container=file_record.bucket_name, blob=file_record.object_key
HEAD:backend/onyx/file_store/azure_blob_file_store.py:380:                    blob_client.delete_blob()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:382:                    # Tolerate only a missing blob. A missing container means
HEAD:backend/onyx/file_store/azure_blob_file_store.py:389:                        != "BlobNotFound"
HEAD:backend/onyx/file_store/azure_blob_file_store.py:393:                        "delete_file: File %s not found in Azure Blob Storage "
HEAD:backend/onyx/file_store/azure_blob_file_store.py:399:                delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:412:        """Rename a file by repointing its DB record at the existing blob.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:414:        The blob is not moved — only file_id changes — and reads resolve via
HEAD:backend/onyx/file_store/azure_blob_file_store.py:415:        the stored object_key, so they still find it. The blob keeps its
HEAD:backend/onyx/file_store/azure_blob_file_store.py:417:        it has been renamed (the new write would overwrite the renamed blob).
HEAD:backend/onyx/file_store/azure_blob_file_store.py:423:                old_file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:430:                # Reuse the old record's bucket/object_key — the blob stays put.
HEAD:backend/onyx/file_store/azure_blob_file_store.py:431:                upsert_filerecord(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:443:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=db_session)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:468:                "Failed to read file %s from Azure Blob Storage",
HEAD:backend/onyx/file_store/azure_blob_file_store.py:474:    def list_files_by_prefix(self, prefix: str) -> list[FileRecord]:
HEAD:backend/onyx/file_store/azure_blob_file_store.py:477:            file_records = get_filerecord_by_prefix(
HEAD:backend/onyx/file_store/constants.py:4:# Marks a blob a content-free chat turn produced, so cleanup can find it by the
HEAD:backend/onyx/file_store/document_batch_storage.py:11:from onyx.file_store.file_store import FileStore, get_default_file_store
HEAD:backend/onyx/file_store/document_batch_storage.py:159:    def __init__(self, cc_pair_id: int, index_attempt_id: int, file_store: FileStore):
HEAD:backend/onyx/file_store/document_batch_storage.py:161:        self.file_store = file_store
HEAD:backend/onyx/file_store/document_batch_storage.py:174:            self.file_store.save_file(
HEAD:backend/onyx/file_store/document_batch_storage.py:201:            if not self.file_store.has_file(
HEAD:backend/onyx/file_store/document_batch_storage.py:211:            content_io = self.file_store.read_file(file_name)
HEAD:backend/onyx/file_store/document_batch_storage.py:227:        self.file_store.delete_file(batch_file_name, error_on_missing=False)
HEAD:backend/onyx/file_store/document_batch_storage.py:251:            for file in self.file_store.list_files_by_prefix(
HEAD:backend/onyx/file_store/document_batch_storage.py:266:            self.file_store.change_file_id(batch_file_name, new_batch_file_name)
HEAD:backend/onyx/file_store/document_batch_storage.py:290:    # The get_default_file_store will now correctly use S3BackedFileStore
HEAD:backend/onyx/file_store/document_batch_storage.py:292:    file_store = get_default_file_store()
HEAD:backend/onyx/file_store/document_batch_storage.py:293:    return FileStoreDocumentBatchStorage(cc_pair_id, index_attempt_id, file_store)
HEAD:backend/onyx/file_store/file_store.py:17:    S3_FILE_STORE_BUCKET_NAME,
HEAD:backend/onyx/file_store/file_store.py:18:    S3_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:28:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/file_store.py:29:    get_filerecord_by_file_id,
HEAD:backend/onyx/file_store/file_store.py:30:    get_filerecord_by_file_id_optional,
HEAD:backend/onyx/file_store/file_store.py:31:    get_filerecord_by_prefix,
HEAD:backend/onyx/file_store/file_store.py:32:    upsert_filerecord,
HEAD:backend/onyx/file_store/file_store.py:34:from onyx.db.models import FileRecord
HEAD:backend/onyx/file_store/file_store.py:35:from onyx.db.models import FileRecord as FileStoreModel
HEAD:backend/onyx/file_store/file_store.py:36:from onyx.file_store.s3_key_utils import generate_s3_key
HEAD:backend/onyx/file_store/file_store.py:44:    from onyx.file_store.azure_blob_file_store import AzureBlobBackedFileStore
HEAD:backend/onyx/file_store/file_store.py:45:    from onyx.file_store.gcs_file_store import GCSBackedFileStore
HEAD:backend/onyx/file_store/file_store.py:93:        the backing blob itself — content is assumed present when the record
HEAD:backend/onyx/file_store/file_store.py:114:        Save a file to the blob store
HEAD:backend/onyx/file_store/file_store.py:191:    def list_files_by_prefix(self, prefix: str) -> list[FileRecord]:
HEAD:backend/onyx/file_store/file_store.py:344:            file_record = get_filerecord_by_file_id_optional(
HEAD:backend/onyx/file_store/file_store.py:404:            upsert_filerecord(
HEAD:backend/onyx/file_store/file_store.py:427:            file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/file_store.py:460:            file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/file_store.py:473:                file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/file_store.py:505:                file_record = get_filerecord_by_file_id_optional(
HEAD:backend/onyx/file_store/file_store.py:520:                    delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:543:                delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:565:                old_file_record = get_filerecord_by_file_id(
HEAD:backend/onyx/file_store/file_store.py:573:                upsert_filerecord(
HEAD:backend/onyx/file_store/file_store.py:585:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:611:    def list_files_by_prefix(self, prefix: str) -> list[FileRecord]:
HEAD:backend/onyx/file_store/file_store.py:616:            file_records = get_filerecord_by_prefix(
HEAD:backend/onyx/file_store/file_store.py:622:def get_s3_file_store() -> S3BackedFileStore:
HEAD:backend/onyx/file_store/file_store.py:628:    bucket_name = S3_FILE_STORE_BUCKET_NAME
HEAD:backend/onyx/file_store/file_store.py:631:            "S3_FILE_STORE_BUCKET_NAME configuration is required for S3 file store"
HEAD:backend/onyx/file_store/file_store.py:640:        s3_prefix=S3_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:645:def get_gcs_file_store() -> "GCSBackedFileStore":
HEAD:backend/onyx/file_store/file_store.py:648:        GCS_FILE_STORE_BUCKET_NAME,
HEAD:backend/onyx/file_store/file_store.py:649:        GCS_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:654:    from onyx.file_store.gcs_file_store import GCSBackedFileStore
HEAD:backend/onyx/file_store/file_store.py:656:    bucket_name = GCS_FILE_STORE_BUCKET_NAME
HEAD:backend/onyx/file_store/file_store.py:658:        raise RuntimeError("GCS_FILE_STORE_BUCKET_NAME is required for GCS file store")
HEAD:backend/onyx/file_store/file_store.py:662:        gcs_prefix=GCS_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:669:def get_azure_file_store() -> "AzureBlobBackedFileStore":
HEAD:backend/onyx/file_store/file_store.py:670:    """Returns the Azure Blob Storage file store implementation."""
HEAD:backend/onyx/file_store/file_store.py:672:        AZURE_FILE_STORE_CONTAINER_NAME,
HEAD:backend/onyx/file_store/file_store.py:673:        AZURE_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:679:    from onyx.file_store.azure_blob_file_store import AzureBlobBackedFileStore
HEAD:backend/onyx/file_store/file_store.py:681:    container_name = AZURE_FILE_STORE_CONTAINER_NAME
HEAD:backend/onyx/file_store/file_store.py:684:            "AZURE_FILE_STORE_CONTAINER_NAME is required for Azure file store"
HEAD:backend/onyx/file_store/file_store.py:687:    return AzureBlobBackedFileStore(
HEAD:backend/onyx/file_store/file_store.py:689:        azure_prefix=AZURE_FILE_STORE_PREFIX,
HEAD:backend/onyx/file_store/file_store.py:697:def get_default_file_store() -> FileStore:
HEAD:backend/onyx/file_store/file_store.py:699:    Returns the configured file store implementation based on FILE_STORE_BACKEND.
HEAD:backend/onyx/file_store/file_store.py:701:    When FILE_STORE_BACKEND=postgres:
HEAD:backend/onyx/file_store/file_store.py:702:    - Files are stored in PostgreSQL using Large Objects.
HEAD:backend/onyx/file_store/file_store.py:705:    When FILE_STORE_BACKEND=s3 (default):
HEAD:backend/onyx/file_store/file_store.py:708:      - S3_FILE_STORE_BUCKET_NAME, S3_ENDPOINT_URL, S3_AWS_ACCESS_KEY_ID, etc.
HEAD:backend/onyx/file_store/file_store.py:710:    When FILE_STORE_BACKEND=gcs:
HEAD:backend/onyx/file_store/file_store.py:713:      - GCS_FILE_STORE_BUCKET_NAME, GCS_PROJECT_ID, GCS_SERVICE_ACCOUNT_KEY_PATH, etc.
HEAD:backend/onyx/file_store/file_store.py:715:    When FILE_STORE_BACKEND=azure:
HEAD:backend/onyx/file_store/file_store.py:716:    - Uses Azure Blob Storage with connection string, account key, or
HEAD:backend/onyx/file_store/file_store.py:719:      - AZURE_FILE_STORE_CONTAINER_NAME, AZURE_STORAGE_ACCOUNT_NAME,
HEAD:backend/onyx/file_store/file_store.py:722:    from onyx.configs.app_configs import FILE_STORE_BACKEND
HEAD:backend/onyx/file_store/file_store.py:725:    backend = FileStoreType(FILE_STORE_BACKEND)
```
## Logs, Audit and Telemetry Assets
Evidence lines: 550
```text
HEAD:backend/ee/onyx/access/access.py:78:            logger.error("Document %s has no source", document_id)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:126:            logger.info(
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:131:            logger.exception("Failed to re-validate SSO domain %s", record.domain)
HEAD:backend/ee/onyx/auth/users.py:30:        logger.warning("SUPER_CLOUD_API_KEY is not configured; rejecting request")
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:10:            "ee.onyx.background.celery.tasks.query_history",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:11:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/light.py:10:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:8:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:15:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:7:            "ee.onyx.background.celery.tasks.log_export",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:44:        "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:108:            "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:5:from ee.onyx.db.query_history import get_all_query_history_export_tasks
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:17:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:21:def export_query_history_cleanup_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:23:        tasks = get_all_query_history_export_tasks(db_session=db_session)
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:35:                logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:46:        task_logger.exception(f"full-fanout timestamp read failed: task={task_name}")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:65:            task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:121:                task_logger.exception("tenant work gating: runtime flag read failed")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:138:                        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:205:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:209:        task_logger.exception("Unexpected exception during cloud_beat_task_generator")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:212:            task_logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:220:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:94:from onyx.server.metrics.perm_sync_metrics import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:107:from onyx.utils.telemetry import RecordType, optional_telemetry
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:175:        logger.error("No sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:179:        logger.error("No doc sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:254:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:270:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:299:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:304:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:307:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:365:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:395:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:403:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:441:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:476:            logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:485:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:504:        task_logger.warning(error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:538:                    task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:542:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:553:                logger.error(error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:567:            logger.info("Syncing docs for %s with cc_pair=%s", source_type, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:623:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:646:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:662:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:672:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:675:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:696:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:774:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:778:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:783:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:875:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:894:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:955:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:966:    #     logger.info(f"{payload.celery_task_id} is currently executing.")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:976:    task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1022:                logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1046:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1071:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1089:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1098:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1103:    optional_telemetry(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1117:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1122:    optional_telemetry(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:74:from onyx.server.metrics.perm_sync_metrics import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:122:        task_logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:128:        task_logger.debug(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:135:        task_logger.debug(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:143:        task_logger.debug(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:182:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:228:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:244:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:254:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:259:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:262:        task_logger.exception(f"Unexpected exception: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:267:    task_logger.info(f"check_for_external_group_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:286:            logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:305:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:337:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:340:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:345:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:401:            logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:408:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:423:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:446:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:449:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:454:        task_logger.exception(msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:474:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:492:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:547:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:554:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:563:        logger.info("Marked external group sync attempt %s as in progress", attempt_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:565:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:598:                    logger.debug(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:612:                logger.debug("New external user groups: %s", external_user_group_batch)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:634:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:644:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:663:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:748:        task_logger.error(msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:769:        task_logger.exception(msg)
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:29:                logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:35:        logger.exception("Failed to clean up hook execution logs")
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:41:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:94:        logger.warning("License renewal check failed: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:42:        logger.debug("License reclaim backoff state unavailable: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:58:        logger.debug("License reclaim throttle unavailable: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:79:        logger.debug("License reclaim backoff update failed: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:97:            logger.error("Stored license does not verify, skipping reclaim")
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:117:            logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:131:            logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:143:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:5:from ee.onyx.server.log_export.collection import get_default_log_directories
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:6:from ee.onyx.server.log_export.storage import (
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:8:    delete_expired_log_exports,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:52:    logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:72:    delete_expired_log_exports()
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:7:from ee.onyx.server.query_history.models import QuestionAnswerPairSnapshot
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:8:from onyx.background.task_utils import construct_query_history_report_name
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:31:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:37:def export_query_history_task(
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:46:    from ee.onyx.server.query_history.api import (
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:75:            query_history_type = load_settings().query_history_type
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:77:                if query_history_type == QueryHistoryType.ANONYMIZED:
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:90:            logger.exception("Failed to export query history with task_id=%r", task_id)
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:98:    report_name = construct_query_history_report_name(task_id)
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:105:                file_origin=FileOrigin.QUERY_HISTORY_CSV,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:120:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:33:        logger.exception("Failed to re-project login domains for %s", tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:51:    task_logger.info("STARTING CHECK_AVAILABLE_TENANTS")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:53:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:66:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:85:        task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:93:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:99:            task_logger.info(f"Provisioning tenant {i + 1}/{batch_size}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:104:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:108:        task_logger.info(f"Provisioning complete: {provisioned}/{batch_size} succeeded")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:114:        task_logger.exception("Error in check_available_tenants task")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:120:            task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:144:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:159:                    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:165:            task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:196:        task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:206:        task_logger.info(f"Pre-provisioning tenant {tenant_id} on shard {shard_name}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:214:            task_logger.debug(f"Created schema for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:216:            task_logger.debug(f"Schema already exists for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:219:        task_logger.debug(f"Setting up tenant configuration: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:221:        task_logger.debug(f"Tenant configuration completed: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:225:        task_logger.debug(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:230:        task_logger.debug(f"Storing pre-provisioned tenant in database: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:243:                task_logger.info(f"Successfully pre-provisioned tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:247:                task_logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:254:        task_logger.error("Error in pre_provision_tenant task", exc_info=True)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:257:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:267:                task_logger.exception(f"Error during rollback for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:273:            task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:119:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:26:        task_logger.warning(f"Could not parse usergroup id from {fence_key}")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:32:        task_logger.exception(f"usergroup_id ({usergroup_id_str}) is not an integer!")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:44:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:76:                task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:90:                task_logger.info(
HEAD:backend/ee/onyx/background/celery_utils.py:23:        logger.debug("%s is already being performed. Skipping.", task_name)
HEAD:backend/ee/onyx/background/task_name_builders.py:5:QUERY_HISTORY_TASK_NAME_PREFIX = OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK
HEAD:backend/ee/onyx/background/task_name_builders.py:15:def query_history_task_name(start: datetime, end: datetime) -> str:
HEAD:backend/ee/onyx/background/task_name_builders.py:16:    return f"{QUERY_HISTORY_TASK_NAME_PREFIX}_{start}_{end}"
HEAD:backend/ee/onyx/db/external_perm.py:129:                logger.warning(
HEAD:backend/ee/onyx/db/license.py:132:        logger.info("License updated")
HEAD:backend/ee/onyx/db/license.py:136:        logger.info("License created")
HEAD:backend/ee/onyx/db/license.py:171:            logger.warning("License deleted but cache invalidation failed: %s", e)
HEAD:backend/ee/onyx/db/license.py:172:        logger.info("License deleted")
HEAD:backend/ee/onyx/db/license.py:254:        logger.warning("Failed to parse cached license metadata: %s", e)
HEAD:backend/ee/onyx/db/license.py:271:    logger.info("License cache invalidated")
HEAD:backend/ee/onyx/db/license.py:342:    logger.info(
HEAD:backend/ee/onyx/db/license.py:389:            logger.warning("License cache lease lost mid-publish, dropping entry")
HEAD:backend/ee/onyx/db/license.py:415:            logger.warning("License cache lock contended, serving uncached")
HEAD:backend/ee/onyx/db/license.py:417:        logger.warning("License cache lock errored (%s), serving uncached", e)
HEAD:backend/ee/onyx/db/license.py:448:        logger.error("Failed to verify license during cache refresh: %s", e)
HEAD:backend/ee/onyx/db/query_history.py:10:from ee.onyx.background.task_name_builders import QUERY_HISTORY_TASK_NAME_PREFIX
HEAD:backend/ee/onyx/db/query_history.py:192:def get_all_query_history_export_tasks(
HEAD:backend/ee/onyx/db/query_history.py:195:    return get_all_tasks_with_prefix(db_session, QUERY_HISTORY_TASK_NAME_PREFIX)
HEAD:backend/ee/onyx/db/scim.py:234:            logger.warning("SCIM user mapping %d not found during delete", mapping_id)
HEAD:backend/ee/onyx/db/scim.py:543:            logger.warning("SCIM group mapping %d not found during delete", mapping_id)
HEAD:backend/ee/onyx/db/standard_answer.py:23:        logger.error(
HEAD:backend/ee/onyx/db/usage_export.py:11:from ee.onyx.db.query_history import fetch_chat_sessions_eagerly_by_time
HEAD:backend/ee/onyx/db/user_group.py:70:    AuditAction,
HEAD:backend/ee/onyx/db/user_group.py:916:            AuditAction.USER_GROUP_CHANGE,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:86:                logger.warning(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:293:            logger.info("No mapping row to link in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:326:                logger.warning(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:372:        logger.warning("No linked OAuth identity to rekey in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:388:            logger.warning(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:405:            logger.warning("No mapping row to rekey in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:435:            logger.warning(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:581:            logger.info("Successfully added users %s to tenant %s", emails, tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:584:            logger.exception("Failed to add users to tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:607:            logger.exception(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:799:                logger.info(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:803:                logger.warning(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:809:            logger.exception(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:824:            logger.info("Removed %s from invited users list after acceptance", email)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:849:            logger.info("User %s denied invitation to tenant %s", email, tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:851:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/box/access.py:90:                logger.warning("Unrecognized Box collaboration role: %s", role_value)
HEAD:backend/ee/onyx/external_permissions/box/access.py:201:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:75:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:83:                logger.info("Box group %s has no members with logins", group.id)
HEAD:backend/ee/onyx/external_permissions/canvas/access.py:78:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:124:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:25:        logger.info("Processing groups for user: %s", user)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:38:                logger.error("user result missing username field: %s", user)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:44:                logger.warning(msg)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:47:                logger.error(msg)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:60:            logger.error(msg)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:62:            logger.debug(
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:69:        logger.error(msg)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:96:        logger.info("Processing groups for user with email: %s", email)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:102:                logger.error("User key not found for user with email %s", email)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:114:                logger.error(msg)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:116:                logger.info(
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:120:            logger.exception("Error getting user details for user with email %s", email)
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:45:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:50:                logger.warning("Cant find email for user %s", user.get("displayName"))
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:51:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:55:            logger.warning("no user email or username for %s", user)
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:126:            logger.debug(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:83:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:142:        logger.warning("Email for userKey %s not found in Confluence", user_key)
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:145:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:208:            logger.warning("Email for user %s not found in Confluence", user_name)
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:211:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:241:            logger.info(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:303:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:338:    logger.debug("Getting space permissions")
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:349:    logger.debug("Got %s spaces from confluence", len(all_space_keys))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:47:    logger.info("Starting GitHub document sync for CC pair ID: %s", cc_pair.id)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:55:    logger.info("GitHub connector credentials loaded successfully")
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:58:        logger.error("GitHub client initialization failed")
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:62:    logger.info("Fetching all repositories from GitHub API")
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:66:        logger.info("Found %s repositories to check", len(repos))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:68:        logger.error("Failed to fetch repositories: %s", e)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:76:    logger.info("Found %s documents to check", len(existing_docs))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:84:            logger.error("Failed to parse doc metadata: %s for doc %s", e, doc.id)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:86:    logger.info("Found %s documents to check", len(repo_to_doc_list_map))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:90:            logger.info("Processing repository: %s (name: %s)", repo.id, repo.name)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:95:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:109:                logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:120:                logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:136:                logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:140:            logger.error(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:144:    logger.info("GitHub document sync completed for CC pair ID: %s", cc_pair.id)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:155:    logger.info("Checking repository %s (%s) for changes", repo.id, repo.name)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:162:        logger.info("Repository %s (%s) has visibility changes", repo.id, repo.name)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:173:        logger.info("Repository %s (%s) has team changes", repo.id, repo.name)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:176:    logger.info("Repository %s (%s) has no changes", repo.id, repo.name)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:195:    logger.info("Current repository visibility: %s", current_repo_visibility.value)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:221:    logger.info("Inferred existing visibility: %s", existing_repo_visibility.value)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:225:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:246:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:281:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:290:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:26:    logger.info("Starting GitHub group sync...")
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:44:                logger.info("External group: %s", external_group)
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:47:            logger.error(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:47:    logger.debug("Starting operation '%s', attempt %s", description, retry_count + 1)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:50:        logger.debug("Operation '%s' completed successfully", description)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:55:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:66:            logger.exception(error_msg)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:69:        logger.warning("GitHub API error during %s: %s", description, e)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:72:        logger.exception("Unexpected error during %s: %s", description, e)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:99:    logger.info("Fetching organization members for %s", org_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:107:        logger.error("Failed to fetch organization %s", org_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:123:    logger.info("Fetched %s members for organization %s", len(org_members), org_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:134:    logger.info("Fetching teams for repository %s", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:146:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:169:        logger.info("Team %s has %s members", team.name, len(team_members))
HEAD:backend/ee/onyx/external_permissions/github/utils.py:171:    logger.info("Fetched %s teams for repository %s", len(teams_data), repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:181:    logger.info("Fetching team slugs for repository %s", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:194:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:207:    logger.info("Fetching collaborators for repository %s", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:246:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:258:        logger.exception("Repository ID is required to generate collaborators group ID")
HEAD:backend/ee/onyx/external_permissions/github/utils.py:267:        logger.exception(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:278:        logger.exception(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:293:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:299:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:306:    logger.info("Repository %s is private", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:330:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:337:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:346:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:374:        logger.info("ExternalAccess groups for %s: %s", repo.full_name, group_ids)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:382:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:392:        logger.info("ExternalAccess groups for %s: %s", repo.full_name, group_ids)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:408:    logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:415:        logger.info("Processing private repository %s", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:431:                logger.warning("Collaborator %s has no email", collab.login)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:439:            logger.info("Created collaborators group with %s emails", len(user_emails))
HEAD:backend/ee/onyx/external_permissions/github/utils.py:447:                logger.warning("Outside collaborator %s has no email", collab.login)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:455:            logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:466:                    logger.warning("Team member %s has no email", member.login)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:474:                logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:478:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:486:        logger.info("Processing internal repository %s", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:498:                logger.warning("Org member %s has no email", member.login)
HEAD:backend/ee/onyx/external_permissions/github/utils.py:504:        logger.info(
HEAD:backend/ee/onyx/external_permissions/github/utils.py:511:    logger.info("Repository %s is public - no user groups needed", repo.full_name)
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:81:                logger.warning("No permissions found for document %s", slim_doc.id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:50:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:58:        logger.debug(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:159:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:196:        logger.info(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:237:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:247:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:306:        logger.warning("Folder missing ID, returning empty permissions")
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:316:        logger.debug("No permissionIds found for folder %s", folder_id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:340:                logger.warning("User permission without email for folder %s", folder_id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:346:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:396:        logger.info("Drive perm sync: Processing %s documents", len(slim_doc_batch))
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:422:        logger.info("Drive perm sync: Processed %s total documents", total_processed)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:106:                    logger.debug(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:139:                    logger.debug(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:165:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:171:                logger.exception("Error getting folders for user %s", user_email)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:178:        logger.info(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:199:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:208:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:301:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:325:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:440:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:461:                    logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:470:                    logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:56:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:114:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:121:            logger.error("Error fetching members for group %s: %s", group_name, e)
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:136:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:175:    logger.info("Found %s groups in Jira", len(group_names))
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:186:            logger.debug("No members found for group %s", group_name)
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:189:        logger.debug("Found %s members for group %s", len(member_emails), group_name)
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:136:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:150:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:158:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:174:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:189:            logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:197:        logger.error(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:218:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:304:        logger.error(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:316:        logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:329:    logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:357:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:364:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:387:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:397:            logger.debug(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:413:                    logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:442:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:450:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:488:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:495:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:506:        logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:517:        logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:548:        logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:562:                logger.error(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:568:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:576:        logger.info(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:588:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:607:            logger.error(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:615:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:648:        logger.error("Project %s has no permissions attribute", jira_project)
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:652:        logger.error("Project %s permissions is not a list", jira_project)
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:656:    logger.info(
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:81:        logger.error("Failed to extract GUID from %s: %s", text, e)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:98:        logger.error("Failed to get Entra group id for name %s: %s", display_name, e)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:111:                logger.info("Extracted GUID %s from claims token %s", guid, identifier)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:117:        logger.error("Failed to resolve group id from %s: %s", identifier, e)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:134:        logger.error("Failed to get Entra group id for %s", identifier)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:148:            logger.debug("Member: %s", member_data)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:184:                logger.info("Added user: %s", user_principal_name or mail)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:187:                    logger.error("No display name for group: %s", member_data.get("id"))
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:192:                logger.info("Added group: %s", name)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:194:                logger.warning("Could not identify member type for: %s", member_data)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:225:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:248:    logger.info("Enumerated %s Entra groups via paginated Graph API", total_groups)
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:73:            logger.exception(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:57:    logger.info(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:61:        logger.warning("User '%s' not found in Salesforce", user_email)
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:69:    logger.debug("Object ID to access: %s", object_id_to_access)
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:41:    logger.info("Processing %s sites for group sync", len(site_descriptors))
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:48:        logger.debug("Processing site: %s", site_descriptor.url)
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:63:            logger.debug(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:114:        logger.error(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:139:        logger.error("Failed to check if item %s is public: %s", drive_item.id, e)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:153:            logger.info("Login name %s is public", login_name)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:180:            logger.debug("User: %s", user.to_json())
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:189:                    logger.warning(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:256:        logger.info(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:289:                    logger.warning("Group %s not found", group.login_name)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:336:        logger.warning("Group %s not found", group.login_name)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:396:            logger.debug("Assignment: %s", assignment.to_json())
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:400:                logger.info("Skipping Limited Access-only assignment")
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:459:    logger.info("User emails: %s", len(user_emails))
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:460:    logger.info("Group IDs: %s", len(group_ids))
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:482:            logger.info("Item %s is public", drive_item.id)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:575:                logger.info("Skipping Limited Access-only assignment")
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:615:        logger.info(
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:66:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:260:        logger.warning("Slack Grid detection during perm sync failed: %s", e)
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:269:            logger.warning("fetch_team_user_emails failed on Grid org: %s", e)
HEAD:backend/ee/onyx/external_permissions/utils.py:52:    logger.info("Starting %s doc sync for CC Pair ID: %s", doc_source, cc_pair.id)
HEAD:backend/ee/onyx/external_permissions/utils.py:62:    logger.info("Fetching all slim documents from %s", doc_source)
HEAD:backend/ee/onyx/external_permissions/utils.py:67:        logger.info("Got %s slim documents from %s", len(doc_batch), doc_source)
HEAD:backend/ee/onyx/external_permissions/utils.py:96:    logger.info(
HEAD:backend/ee/onyx/external_permissions/utils.py:106:    logger.warning(
HEAD:backend/ee/onyx/external_permissions/utils.py:112:        logger.warning("Removing access for missing_id=%r", missing_id)
HEAD:backend/ee/onyx/external_permissions/utils.py:118:    logger.info("Finished %s doc sync", doc_source)
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:54:            logger.error(
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:72:            logger.error(
HEAD:backend/ee/onyx/hooks/executor.py:130:            logger.exception(
HEAD:backend/ee/onyx/hooks/executor.py:148:            logger.warning("Failed to update is_reachable for hook_id=%s", hook_id)
HEAD:backend/ee/onyx/hooks/executor.py:203:        logger.warning(
HEAD:backend/ee/onyx/hooks/executor.py:242:            logger.exception(
HEAD:backend/ee/onyx/main.py:21:from ee.onyx.server.log_export.api import router as log_export_router
HEAD:backend/ee/onyx/main.py:33:from ee.onyx.server.query_history.api import router as query_history_router
HEAD:backend/ee/onyx/main.py:136:    include_router_with_global_prefix_prepended(application, query_history_router)
HEAD:backend/ee/onyx/main.py:159:    include_router_with_global_prefix_prepended(application, log_export_router)
HEAD:backend/ee/onyx/onyxbot/slack/handlers/handle_standard_answers.py:225:            logger.exception("Unable to send standard answer message: %s", e)
HEAD:backend/ee/onyx/search/process_search_query.py:99:                logger.debug(
HEAD:backend/ee/onyx/search/process_search_query.py:104:            logger.warning("Query expansion failed: %s; using original query only.", e)
HEAD:backend/ee/onyx/search/process_search_query.py:179:            logger.warning("All parallel searches returned empty results")
HEAD:backend/ee/onyx/search/process_search_query.py:224:            logger.debug(
HEAD:backend/ee/onyx/search/process_search_query.py:232:            logger.warning("LLM document selection failed: %s", e)
HEAD:backend/ee/onyx/secondary_llm_flows/query_expansion.py:61:            logger.warning("Keyword expansion returned empty response.")
HEAD:backend/ee/onyx/secondary_llm_flows/query_expansion.py:73:            logger.warning("Keyword expansion parsing returned no queries.")
HEAD:backend/ee/onyx/secondary_llm_flows/query_expansion.py:85:        logger.debug("Keyword expansion generated %s queries", len(expanded_queries))
HEAD:backend/ee/onyx/secondary_llm_flows/query_expansion.py:89:        logger.warning("Keyword expansion failed: %s", e)
HEAD:backend/ee/onyx/secondary_llm_flows/search_flow_classification.py:35:        logger.warning(
HEAD:backend/ee/onyx/secondary_llm_flows/search_flow_classification.py:46:    logger.warning(
HEAD:backend/ee/onyx/server/analytics/api.py:269:    # Merge both sets of metrics by date
HEAD:backend/ee/onyx/server/billing/api.py:106:        logger.debug(
HEAD:backend/ee/onyx/server/billing/api.py:113:        logger.error("Failed to check circuit breaker: %s", e)
HEAD:backend/ee/onyx/server/billing/api.py:130:        logger.warning(
HEAD:backend/ee/onyx/server/billing/api.py:136:        logger.error("Failed to open circuit breaker: %s", e)
HEAD:backend/ee/onyx/server/billing/api.py:146:        logger.info(
HEAD:backend/ee/onyx/server/billing/api.py:150:        logger.error("Failed to close circuit breaker: %s", e)
HEAD:backend/ee/onyx/server/billing/api.py:259:        logger.warning("Billing info cache client unavailable: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:276:            logger.warning("Billing info cache invalidation failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:316:            logger.warning("Billing info cache read failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:327:                    logger.warning("Billing info cache deserialize failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:352:            logger.warning("Billing info cache write failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:103:        logger.warning(
HEAD:backend/ee/onyx/server/billing/billing_cache.py:119:            logger.warning(
HEAD:backend/ee/onyx/server/billing/billing_cache.py:130:        logger.warning("billing cache write failed for tenant %s: %s", tenant_id, e)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:164:        logger.warning(
HEAD:backend/ee/onyx/server/billing/service.py:127:        logger.error("%s: %s - %s", error_message, e.response.status_code, detail)
HEAD:backend/ee/onyx/server/billing/service.py:135:        logger.exception("Failed to connect to billing service")
HEAD:backend/ee/onyx/server/billing/service.py:183:        logger.error("Control plane returned no checkout URL")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:87:    logger.info(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:103:    logger.info("Permissions sync queued: cc_pair=%s id=%s", cc_pair_id, payload_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:166:    logger.info(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:182:    logger.info("External group sync queued: cc_pair=%s id=%s", cc_pair_id, payload_id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:142:        logger.debug("Received response from Meechum auth URL for user %s", user.id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:153:        logger.debug("Access token has been refreshed for user %s", user.id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:168:        logger.info("Successfully refreshed tokens for user %s", user.id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:172:            logger.warning("Full authentication required for user %s", user.id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:177:        logger.error(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:187:        logger.error(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:274:        logger.exception("Faield to fetch logo file")
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:57:            logger.warning(
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:162:                logger.warning("Logo is %dx%d, over the pixel cap", width, height)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:169:        logger.warning("Logo has a %s header but does not decode", mime_type)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:177:        logger.notice("Uploading logo from local path %s", file)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:179:            logger.error(
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:189:        logger.notice("Uploading logo from uploaded file")
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:208:            logger.error("Logo at %s is not a valid PNG or JPEG image", file)
HEAD:backend/ee/onyx/server/features/hooks/api.py:166:        logger.warning(
HEAD:backend/ee/onyx/server/features/hooks/api.py:176:        logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:47:from onyx.tracing.flows import LLMFlow
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:48:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:49:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:50:from onyx.tracing.llm_utils import llm_generation_span, record_llm_span_output
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:170:            logger.debug(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:217:    logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:229:    logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:254:    # llm is built only for tracing config (model/provider metadata); the
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:285:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:294:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:410:                    logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:445:                    logger.warning(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:498:        logger.warning(
HEAD:backend/ee/onyx/server/gateway/api.py:62:from onyx.llm.tracing_wrap import _finalize_tool_calls
HEAD:backend/ee/onyx/server/gateway/api.py:114:from onyx.tracing.flows import LLMFlow
HEAD:backend/ee/onyx/server/gateway/api.py:115:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/api.py:116:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/api.py:117:from onyx.tracing.llm_utils import llm_generation_span, record_llm_response
HEAD:backend/ee/onyx/server/gateway/api.py:170:        logger.warning(
HEAD:backend/ee/onyx/server/gateway/api.py:240:        logger.warning(
HEAD:backend/ee/onyx/server/gateway/api.py:426:            logger.exception("LLM gateway invoke failed for model %s", request.model)
HEAD:backend/ee/onyx/server/gateway/api.py:804:            logger.exception(
HEAD:backend/ee/onyx/server/gateway/api.py:1353:            logger.exception(
HEAD:backend/ee/onyx/server/gateway/api.py:1512:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/api.py:1528:        logger.exception("LLM gateway token count failed for model %s", request.model)
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:45:from onyx.tracing.flows import LLMFlow
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:46:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:47:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:48:from onyx.tracing.llm_utils import llm_generation_span, record_llm_span_output
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:258:    logger.warning(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:281:    # llm is built only for tracing config (model/provider metadata); the
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:312:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:321:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:350:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:465:                    logger.warning(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:511:                    logger.warning(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:21:from onyx.llm.tracing_wrap import _finalize_tool_calls, _merge_tool_call_delta
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:22:from onyx.tracing.framework.span_data import GenerationSpanData
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:23:from onyx.tracing.framework.spans import Span
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:24:from onyx.tracing.llm_utils import record_llm_span_output
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:114:        logger.warning(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:127:            logger.warning(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:143:            logger.warning(
HEAD:backend/ee/onyx/server/license/api.py:148:        logger.info(
HEAD:backend/ee/onyx/server/log_export/api.py:11:from ee.onyx.server.log_export.collection import get_default_log_directories
HEAD:backend/ee/onyx/server/log_export/api.py:12:from ee.onyx.server.log_export.models import (
HEAD:backend/ee/onyx/server/log_export/api.py:18:from ee.onyx.server.log_export.storage import (
HEAD:backend/ee/onyx/server/log_export/api.py:19:    LOG_EXPORT_COLLECTION_DEADLINE,
HEAD:backend/ee/onyx/server/log_export/api.py:113:    ttl_seconds=LOG_EXPORT_COLLECTION_DEADLINE.total_seconds()
HEAD:backend/ee/onyx/server/log_export/api.py:135:def start_log_export(
HEAD:backend/ee/onyx/server/log_export/api.py:165:        deadline = now + LOG_EXPORT_COLLECTION_DEADLINE
HEAD:backend/ee/onyx/server/log_export/api.py:177:            logger.info(
HEAD:backend/ee/onyx/server/log_export/api.py:199:                    logger.warning(
HEAD:backend/ee/onyx/server/log_export/api.py:237:def get_log_export_status(
HEAD:backend/ee/onyx/server/log_export/api.py:266:def download_log_export(
HEAD:backend/ee/onyx/server/log_export/collection.py:57:    Mirrors the path selection in ``onyx.utils.logger._add_file_handlers``:
HEAD:backend/ee/onyx/server/log_export/storage.py:3:All state for one export lives under ``log_export/{export_id}/`` in the default
HEAD:backend/ee/onyx/server/log_export/storage.py:19:from ee.onyx.server.log_export.collection import (
HEAD:backend/ee/onyx/server/log_export/storage.py:24:from ee.onyx.server.log_export.models import (
HEAD:backend/ee/onyx/server/log_export/storage.py:39:LOG_EXPORT_FILE_ID_PREFIX = "log_export/"
HEAD:backend/ee/onyx/server/log_export/storage.py:43:LOG_EXPORT_RETENTION = timedelta(hours=12)
HEAD:backend/ee/onyx/server/log_export/storage.py:48:LOG_EXPORT_COLLECTION_DEADLINE = timedelta(seconds=90)
HEAD:backend/ee/onyx/server/log_export/storage.py:59:    return f"{LOG_EXPORT_FILE_ID_PREFIX}{export_id}/"
HEAD:backend/ee/onyx/server/log_export/storage.py:82:        file_origin=FileOrigin.LOG_EXPORT,
HEAD:backend/ee/onyx/server/log_export/storage.py:280:                        file_origin=FileOrigin.LOG_EXPORT,
HEAD:backend/ee/onyx/server/log_export/storage.py:288:        logger.exception(
```
Operational telemetry can itself contain sensitive identifiers, prompts,
document references, tool arguments or security events.
## Trust and Dependency Model
```text
Boundary | Security concern
---------|-----------------
Browser/client -> API | authentication, session integrity, request authorization
API -> PostgreSQL | authoritative identity, configuration and metadata
API/workers -> Redis | queues, locks, cached authorization/state
API/workers -> search index | derived searchable document/chunk/ACL state
API/workers -> file store | user files, generated files, indexed source artifacts
Application -> LLM provider | prompts, retrieved context, model credentials
Application -> embedding/reranker provider | document/query content and provider credentials
Application -> connector source | external data and connector credentials
Application -> MCP server | tool schemas, caller identity, credentials, tool results
LLM -> tool executor | untrusted model output becoming deterministic capability
Tool executor -> external app | side effects performed with application/user credentials
Application -> code sandbox | executable content, files and resource policy
Sandbox -> filesystem/network | blast-radius and egress boundary
Background queue -> workers | delayed security state and replay/retry behavior
Tenant context -> shared infrastructure | tenant isolation invariant
Logs/telemetry -> operators/storage | sensitive operational and user data exposure
```
## Current Asset-Class Model
```text
Asset class | Static evidence status
------------|-----------------------
Persistent/cache stores | OBSERVED
Application data models | OBSERVED
Identity/authorization assets | OBSERVED
AI/model assets | OBSERVED
RAG/derived-data assets | OBSERVED
Tool/MCP/execution assets | OBSERVED
Credential-storage mechanisms | OBSERVED
Sensitive config names | OBSERVED
External connector families | OBSERVED
Network-call mechanisms | OBSERVED
Queue/cache dependencies | OBSERVED
Dependency manifests/lockfiles | OBSERVED
Deployment/container manifests | OBSERVED
Container image references | OBSERVED
File/blob assets | OBSERVED
Logs/audit/telemetry assets | OBSERVED
Actual secret values | NOT COLLECTED
Runtime credential contents | NOT ACCESSED
Runtime data classification | NOT PROVEN
Actual external destinations | NOT EXECUTED
```
## Primary Security Asset Categories
The static architecture exposes security-relevant assets across:
- identity and authorization state;
- tenant identifiers and tenant-scoped state;
- documents and document metadata;
- chunks and embeddings;
- search indexes and ACL metadata;
- chat sessions and messages;
- personas/agents and their tool attachments;
- MCP server definitions and discovered tools;
- model/provider configuration;
- connector and provider credentials;
- OAuth/PAT/session/API-key material;
- user files and generated files;
- queues, locks and cached state;
- audit, telemetry and operational logs;
- dependency manifests and container images.
## Security Classification Principles
### Authoritative data
Examples include relational user, permission, connector and configuration
records.
### Derived data
Examples include chunks, embeddings, search-index documents, cached state and
tool-generated artifacts.
### Security control data
Examples include ACLs, tenant IDs, sessions, permissions and policy state.
### Credentials
Examples include connector credentials, OAuth tokens, API keys and provider
credentials.
### Executable capability
Examples include tools, MCP actions and sandbox/code execution.
### Operational evidence
Examples include logs, telemetry, queue state, audit actions and task status.
## Important Invariant
Protecting only the primary database is insufficient.
An AI application can expose equivalent sensitive information through:
source documents ->
chunks ->
embeddings ->
search results ->
LLM prompts ->
chat history ->
tool results ->
generated files ->
logs.
Each representation requires its own authorization, retention and deletion
analysis.
## Dependency/Supply-Chain Boundary
Dependency lockfiles, container images and deployment manifests are themselves
security assets because they determine what code and binaries execute.
This action inventories their locations but does not yet prove:
- dependency integrity;
- package provenance;
- image signature validity;
- absence of known vulnerabilities;
- absence of malicious dependencies;
- correct version pinning.
## Interpretation Boundary
This action proves the presence of asset classes and configuration mechanisms.
It does not prove:
- runtime contents;
- actual production secrets;
- runtime data sensitivity;
- effective encryption;
- credential rotation;
- credential least privilege;
- runtime egress behavior;
- dependency safety;
- container image trust;
- audit completeness.
## Safety Record
During Action 6.10:
- application execution: NO
- Docker execution: NO
- database access: NO
- Redis access: NO
- search-index access: NO
- file-store access: NO
- credential value read: NO
- environment-secret value read: NO
- external API call: NO
- model/provider call: NO
- dependency installation: NO
- vulnerability scanning: NO
- production/customer data: NO
- Onyx source modification: NO
## Result
Action 6.10 security asset, data, secret and dependency inventory: **PASS**.
