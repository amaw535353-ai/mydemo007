#!/usr/bin/env bash
set -euo pipefail
set +H

# Phase 9 / Action 9.10 / Slice 4 — H9-12 runtime verification
# Authorized local lab only. Synthetic data only.
# Sequential requests only; hard ceiling below the engagement limit.

PROJECT="${PROJECT:-/workspaces/mydemo007}"
BRANCH="security/phase-9-identity-authorization-tenant-isolation"
REQUIRED_ANCESTOR="e3433c3ba21d344113f2e909b5e6144b4f620885"
ONYX_PIN="160f9b143605ca45a85bd387b5bd173840bab15d"
API="${API:-onyx-api_server-1}"
BASE_URL="${PHASE9_BASE_URL:-http://127.0.0.1:8080}"
MAX_REQUESTS=20
REQUESTS=0
OUT="${PHASE9_H12_EVIDENCE:-/tmp/phase9-action-9.10-slice4-h12-runtime.txt}"
TMP="$(mktemp -d)"
FILE_ID=""
ALICE_EMAIL=""
BOB_EMAIL=""
ALICE_HASH=""
BOB_HASH=""
LOGIN_READY=0

req() {
    REQUESTS=$((REQUESTS + 1))
    if [ "$REQUESTS" -gt "$MAX_REQUESTS" ]; then
        echo "STOP: request ceiling exceeded" >&2
        return 90
    fi
    curl --silent --show-error --max-time 5 --connect-timeout 3 --max-filesize 1048576 "$@"
}

cleanup() {
    rc=$?
    trap - EXIT
    set +e

    if [ "$LOGIN_READY" = "1" ]; then
        req -b "$TMP/alice.cookies" -X POST -o /dev/null "$BASE_URL/auth/logout" >/dev/null 2>&1 || true
        req -b "$TMP/bob.cookies"   -X POST -o /dev/null "$BASE_URL/auth/logout" >/dev/null 2>&1 || true
    fi

    if [ -n "$FILE_ID" ]; then
        docker exec -i "$API" python3 - "$FILE_ID" <<'PY' >/dev/null 2>&1 || true
import sys
from onyx.file_store.file_store import get_default_file_store
fid = sys.argv[1].strip()
if fid:
    get_default_file_store().delete_file(file_id=fid, error_on_missing=False)
PY
    fi

    if [ -n "$ALICE_EMAIL" ] && [ -n "$ALICE_HASH" ]; then
        docker exec -i "$DB" psql -X -q -v ON_ERROR_STOP=1 -U "$DB_USER" -d "$DB_NAME" \
          -v email="$ALICE_EMAIL" -v hash="$ALICE_HASH" >/dev/null 2>&1 <<'SQL' || true
UPDATE "user" SET hashed_password = :'hash' WHERE email = :'email';
SQL
    fi

    if [ -n "$BOB_EMAIL" ] && [ -n "$BOB_HASH" ]; then
        docker exec -i "$DB" psql -X -q -v ON_ERROR_STOP=1 -U "$DB_USER" -d "$DB_NAME" \
          -v email="$BOB_EMAIL" -v hash="$BOB_HASH" >/dev/null 2>&1 <<'SQL' || true
UPDATE "user" SET hashed_password = :'hash' WHERE email = :'email';
SQL
    fi

    rm -rf "$TMP"
    echo "CLEANUP: attempted logout, synthetic file deletion, password-hash restoration"
    exit "$rc"
}
trap cleanup EXIT

case "$BASE_URL" in
    http://127.0.0.1:*|http://localhost:*|http://[[]::1[]]:*|https://127.0.0.1:*|https://localhost:*|https://[[]::1[]]:*) ;;
    *) echo "REFUSED: PHASE9_BASE_URL must be loopback"; exit 2 ;;
esac

cd "$PROJECT"
test "$(git branch --show-current)" = "$BRANCH" || { echo "ERROR: wrong branch"; exit 2; }
git merge-base --is-ancestor "$REQUIRED_ANCESTOR" HEAD || { echo "ERROR: missing required Phase 9 ancestor"; exit 2; }
test -z "$(git status --porcelain)" || { echo "ERROR: worktree must be clean"; exit 2; }
docker inspect "$API" >/dev/null

DB="$(
    docker ps --format '{{.Names}}' |
    grep -E 'postgres|relational|db' |
    head -n 1 || true
)"
test -n "$DB" || { echo "ERROR: relational DB container not found"; exit 2; }

DB_USER="$(docker exec "$DB" sh -lc 'printf "%s" "${POSTGRES_USER:-postgres}"')"
DB_NAME="$(docker exec "$DB" sh -lc 'printf "%s" "${POSTGRES_DB:-postgres}"')"

exec > >(tee "$OUT") 2>&1

echo "===================================================="
echo "PHASE 9 - ACTION 9.10 - SLICE 4 - H9-12"
echo "CHAT_IMAGE_GEN CROSS-USER RUNTIME VERIFICATION"
echo "===================================================="
echo "Repo branch:     $(git branch --show-current)"
echo "Repo HEAD:       $(git rev-parse HEAD)"
echo "Recorded Onyx:   $ONYX_PIN"
echo "Base URL:        $BASE_URL"
echo "Request ceiling: $MAX_REQUESTS"
echo "Concurrency:     sequential"
echo "Data:            synthetic only"
echo

echo "[1/8] Verify live H9-12 code path"
LIVE_CHECK="$(
docker exec -i "$API" python3 - <<'PY'
import inspect
from onyx.access.access import user_can_access_chat_file
src = inspect.getsource(user_can_access_chat_file)
print("CHAT_IMAGE_GEN_BRANCH=" + ("YES" if "FileOrigin.CHAT_IMAGE_GEN" in src else "NO"))
print("UNCONDITIONAL_TRUE_BRANCH=" + ("YES" if "if is_chat_image_gen:" in src and "return True" in src else "NO"))
PY
)"
printf '%s\n' "$LIVE_CHECK"
grep -q 'CHAT_IMAGE_GEN_BRANCH=YES' <<<"$LIVE_CHECK"
grep -q 'UNCONDITIONAL_TRUE_BRANCH=YES' <<<"$LIVE_CHECK"

echo
echo "[2/8] Select reusable synthetic Alice/Bob pair"
ALICE_EMAIL="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT email
FROM \"user\"
WHERE email LIKE 'phase8-alice-%@example.com'
ORDER BY created_at DESC
LIMIT 1;
"
)"
test -n "$ALICE_EMAIL" || { echo "ERROR: no reusable synthetic Alice found"; exit 3; }
BOB_EMAIL="${ALICE_EMAIL/phase8-alice-/phase8-bob-}"
BOB_EXISTS="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT COUNT(*) FROM \"user\" WHERE email = '$BOB_EMAIL';
"
)"
test "$BOB_EXISTS" = "1" || { echo "ERROR: matching synthetic Bob not found"; exit 3; }

ALICE_ID="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT id::text FROM \"user\" WHERE email = '$ALICE_EMAIL';
"
)"
BOB_ID="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT id::text FROM \"user\" WHERE email = '$BOB_EMAIL';
"
)"
BOB_SUPER="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT COALESCE(is_superuser,false)::text FROM \"user\" WHERE email = '$BOB_EMAIL';
"
)"
test "$ALICE_ID" != "$BOB_ID"
test "$BOB_SUPER" = "false" || { echo "ERROR: Bob is superuser; unsuitable negative-test actor"; exit 3; }
echo "Alice: $ALICE_EMAIL"
echo "Bob:   $BOB_EMAIL"
echo "Bob superuser: $BOB_SUPER"

echo
echo "[3/8] Mint temporary synthetic login credential with rollback"
ALICE_HASH="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT hashed_password FROM \"user\" WHERE email = '$ALICE_EMAIL';
"
)"
BOB_HASH="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT hashed_password FROM \"user\" WHERE email = '$BOB_EMAIL';
"
)"
test -n "$ALICE_HASH"
test -n "$BOB_HASH"

TEMP_PASSWORD="Phase9-H12-Synthetic-$(date +%s)-Aa1!"
TEMP_HASH="$(
printf '%s' "$TEMP_PASSWORD" |
docker exec -i "$API" python3 -c '
import sys
from fastapi_users.password import PasswordHelper
pw = sys.stdin.read()
print(PasswordHelper().hash(pw))
'
)"
test -n "$TEMP_HASH"

docker exec -i "$DB" psql -X -q -v ON_ERROR_STOP=1 -U "$DB_USER" -d "$DB_NAME" \
  -v email="$ALICE_EMAIL" -v hash="$TEMP_HASH" >/dev/null <<'SQL'
UPDATE "user" SET hashed_password = :'hash' WHERE email = :'email';
SQL

docker exec -i "$DB" psql -X -q -v ON_ERROR_STOP=1 -U "$DB_USER" -d "$DB_NAME" \
  -v email="$BOB_EMAIL" -v hash="$TEMP_HASH" >/dev/null <<'SQL'
UPDATE "user" SET hashed_password = :'hash' WHERE email = :'email';
SQL

echo "Temporary hashes installed; originals retained only in shell memory."

echo
echo "[4/8] Authenticate Alice and Bob locally"
ALICE_LOGIN="$(
req -c "$TMP/alice.cookies" -o "$TMP/alice.login.body" -w '%{http_code}' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "username=$ALICE_EMAIL" \
  --data-urlencode "password=$TEMP_PASSWORD" \
  "$BASE_URL/auth/login"
)"
BOB_LOGIN="$(
req -c "$TMP/bob.cookies" -o "$TMP/bob.login.body" -w '%{http_code}' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "username=$BOB_EMAIL" \
  --data-urlencode "password=$TEMP_PASSWORD" \
  "$BASE_URL/auth/login"
)"
echo "Alice login HTTP: $ALICE_LOGIN"
echo "Bob login HTTP:   $BOB_LOGIN"
test "$ALICE_LOGIN" = "204" -o "$ALICE_LOGIN" = "200" || { echo "ERROR: Alice login failed"; exit 4; }
test "$BOB_LOGIN" = "204" -o "$BOB_LOGIN" = "200" || { echo "ERROR: Bob login failed"; exit 4; }
LOGIN_READY=1

echo
echo "[5/8] Create <=1 MB synthetic CHAT_IMAGE_GEN fixture"
FILE_ID="$(
docker exec -i "$API" python3 - "$ALICE_ID" <<'PY'
import sys
from io import BytesIO
from onyx.configs.constants import FileOrigin
from onyx.file_store.file_store import get_default_file_store

alice_id = sys.argv[1]
payload = b"PHASE9-H12-SYNTHETIC-ALICE-IMAGE-BYTES"
assert len(payload) <= 1024 * 1024
fid = get_default_file_store().save_file(
    content=BytesIO(payload),
    display_name="phase9-h12-alice-synthetic.png",
    file_origin=FileOrigin.CHAT_IMAGE_GEN,
    file_type="image/png",
    file_metadata={
        "phase9_test": True,
        "synthetic_owner_user_id": alice_id,
        "purpose": "H9-12 authorization verification",
    },
)
print(fid)
PY
)"
test -n "$FILE_ID"
echo "Synthetic file ID: $FILE_ID"

DB_RECORD="$(
docker exec "$DB" psql -X -U "$DB_USER" -d "$DB_NAME" -Atc "
SELECT
  file_origin || '|' ||
  COALESCE(file_metadata->>'synthetic_owner_user_id','') || '|' ||
  COALESCE(file_size::text,'')
FROM file_record
WHERE file_id = '$FILE_ID';
"
)"
echo "DB fixture: $DB_RECORD"
grep -q "^chat_image_gen|$ALICE_ID|" <<<"$DB_RECORD"

echo
echo "[6/8] Execute owner/control and cross-user requests"
ANON_HTTP="$(
req -o /dev/null -w '%{http_code}' "$BASE_URL/chat/file/$FILE_ID"
)"
ALICE_HTTP="$(
req -b "$TMP/alice.cookies" -o "$TMP/alice.file" -w '%{http_code}' "$BASE_URL/chat/file/$FILE_ID"
)"
BOB_HTTP="$(
req -b "$TMP/bob.cookies" -o "$TMP/bob.file" -w '%{http_code}' "$BASE_URL/chat/file/$FILE_ID"
)"
echo "Anonymous HTTP: $ANON_HTTP"
echo "Alice HTTP:     $ALICE_HTTP"
echo "Bob HTTP:       $BOB_HTTP"

if [ -f "$TMP/alice.file" ]; then
    echo "Alice response bytes: $(wc -c < "$TMP/alice.file")"
    echo "Alice response sha256: $(sha256sum "$TMP/alice.file" | awk '{print $1}')"
fi
if [ -f "$TMP/bob.file" ]; then
    echo "Bob response bytes:   $(wc -c < "$TMP/bob.file")"
    echo "Bob response sha256:  $(sha256sum "$TMP/bob.file" | awk '{print $1}')"
fi

echo
echo "[7/8] Direct runtime authorization predicate"
DIRECT="$(
docker exec -i "$API" python3 - "$FILE_ID" "$ALICE_ID" "$BOB_ID" <<'PY'
import sys
from uuid import UUID
from sqlalchemy import select

from onyx.access.access import user_can_access_chat_file
from onyx.db.engine.sql_engine import get_session_with_current_tenant
from onyx.db.models import User

fid, alice_id, bob_id = sys.argv[1:4]
with get_session_with_current_tenant() as db:
    alice = db.scalar(select(User).where(User.id == UUID(alice_id)))
    bob = db.scalar(select(User).where(User.id == UUID(bob_id)))
    print("ALICE_CAN_ACCESS=" + str(bool(user_can_access_chat_file(fid, alice, db))).upper())
    print("BOB_CAN_ACCESS=" + str(bool(user_can_access_chat_file(fid, bob, db))).upper())
PY
)"
printf '%s\n' "$DIRECT"

echo
echo "[8/8] Classification"
if { [ "$ANON_HTTP" = "401" ] || [ "$ANON_HTTP" = "403" ]; } \
   && [ "$ALICE_HTTP" = "200" ] \
   && [ "$BOB_HTTP" = "200" ] \
   && grep -q 'BOB_CAN_ACCESS=TRUE' <<<"$DIRECT"; then
    echo "RESULT=RUNTIME_CONFIRMED_CROSS_USER_ACCESS"
    echo "H9-12=FAIL_SECURITY_PROPERTY"
    echo "INTERPRETATION=Any authenticated synthetic Bob can fetch the Alice-marked CHAT_IMAGE_GEN fixture by ID."
    echo "NEXT=Promote to Action 9.11 for product-policy validation, impact, remediation and regression test."
elif [ "$ALICE_HTTP" = "200" ] && { [ "$BOB_HTTP" = "403" ] || [ "$BOB_HTTP" = "404" ]; }; then
    echo "RESULT=PASS"
    echo "H9-12=SECURITY_PROPERTY_ENFORCED"
else
    echo "RESULT=REVIEW"
    echo "H9-12=INCONCLUSIVE"
fi

echo "REQUESTS_USED=$REQUESTS"
echo "EVIDENCE=$OUT"
echo "ROLLBACK=automatic on exit"
echo "===================================================="
