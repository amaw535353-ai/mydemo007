from types import SimpleNamespace
from typing import cast
from unittest.mock import MagicMock, patch
from uuid import UUID, uuid4

import pytest
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session

from onyx.access.access import (
    _user_can_access_generated_image,
    user_can_access_chat_file,
)
from onyx.db.models import FileRecord, User
from onyx.file_store.constants import (
    CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY,
    CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY,
)
from onyx.file_store.utils import save_file_from_base64
from onyx.utils.special_types import JSON_ro


def _user(user_id: UUID) -> User:
    return cast(User, SimpleNamespace(id=user_id))


def _db_session(
    metadata: JSON_ro,
    *,
    record_exists: bool = True,
    public_session: bool = False,
    legacy_session: bool = False,
) -> MagicMock:
    db_session = MagicMock(spec=Session)

    file_result = MagicMock()
    file_result.scalar_one_or_none.return_value = (
        FileRecord(file_metadata=metadata) if record_exists else None
    )

    public_result = MagicMock()
    is_legacy = metadata is None or metadata == {} or metadata == {"version": 1}
    public_result.first.return_value = (
        (uuid4(),) if (legacy_session if is_legacy else public_session) else None
    )

    db_session.execute.side_effect = [file_result, public_result]
    return db_session


def test_generated_image_owner_is_allowed() -> None:
    owner_id = uuid4()
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(owner_id),
            CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4()),
        }
    )

    assert _user_can_access_generated_image(
        "generated-image", _user(owner_id), db_session
    )
    assert db_session.execute.call_count == 1


def test_generated_image_non_owner_without_session_is_denied() -> None:
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(uuid4()),
        }
    )

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 1


def test_generated_image_non_owner_in_private_session_is_denied() -> None:
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(uuid4()),
            CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4()),
        },
        public_session=False,
    )

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 2


def test_generated_image_non_owner_in_public_session_is_allowed() -> None:
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(uuid4()),
            CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4()),
        },
        public_session=True,
    )

    assert _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 2


def test_generated_image_legacy_record_without_metadata_fails_closed() -> None:
    db_session = _db_session(None)

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 2


@pytest.mark.parametrize("metadata", [None, {}, {"version": 1}])
@pytest.mark.parametrize("authorized", [True, False])
def test_generated_image_legacy_requires_scoped_relationship(
    metadata: JSON_ro, authorized: bool
) -> None:
    user_id = uuid4()
    db_session = _db_session(metadata, legacy_session=authorized)

    assert (
        _user_can_access_generated_image("legacy-image", _user(user_id), db_session)
        is authorized
    )
    assert db_session.execute.call_count == 2
    statement = db_session.execute.call_args.args[0]
    compiled = statement.compile(dialect=postgresql.dialect())
    sql = str(compiled)
    assert "JOIN chat_session ON tool_call.chat_session_id = chat_session.id" in sql
    assert "tool_call.generated_images @>" in sql
    assert "chat_session.user_id =" in sql
    assert user_id in compiled.params.values()
    assert [{"file_id": "legacy-image"}] in compiled.params.values()
    tenant_sql = str(
        statement.compile(
            dialect=postgresql.dialect(),
            schema_translate_map={None: "synthetic_tenant"},
        )
    )
    assert "__[SCHEMA__none].tool_call" in tenant_sql
    assert "__[SCHEMA__none].chat_session" in tenant_sql


@pytest.mark.parametrize(
    "metadata",
    [[], ["owner"], "", "owner", 0, 1, 0.0, 1.5, False, True, None, {}],
    ids=[
        "empty-array",
        "array",
        "empty-string",
        "string",
        "zero",
        "integer",
        "zero-float",
        "float",
        "false",
        "true",
        "null",
        "empty-object",
    ],
)
def test_generated_image_invalid_metadata_is_denied(metadata: JSON_ro) -> None:
    db_session = _db_session(metadata, public_session=True)

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == (2 if metadata is None or metadata == {} else 1)


def test_generated_image_malformed_session_metadata_fails_closed() -> None:
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(uuid4()),
            CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: "not-a-uuid",
        }
    )

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 1


@pytest.mark.parametrize("owner", [None, [], {}, True, 42, "", "not-a-uuid"])
def test_generated_image_malformed_owner_cannot_use_public_session(owner: JSON_ro) -> None:
    db_session = _db_session(
        {
            CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: owner,
            CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4()),
        },
        public_session=True,
    )

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 1


def test_generated_image_missing_owner_cannot_use_public_session() -> None:
    db_session = _db_session(
        {CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4())},
        public_session=True,
    )

    assert not _user_can_access_generated_image(
        "generated-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 1


@pytest.mark.parametrize("allowed", [True, False])
def test_unrelated_connector_file_keeps_existing_authorization(allowed: bool) -> None:
    db_session = MagicMock(spec=Session)
    db_session.query.return_value.scalar.return_value = False
    db_session.execute.return_value.first.return_value = None
    db_session.execute.return_value.scalar_one_or_none.return_value = None
    user = _user(uuid4())

    with (
        patch(
            "onyx.access.access._user_can_access_persona_attached_file",
            return_value=False,
        ),
        patch(
            "onyx.access.access._user_can_access_connector_file",
            return_value=allowed,
        ) as connector,
    ):
        assert user_can_access_chat_file("connector-file", user, db_session) is allowed
        connector.assert_called_once_with("connector-file", user, db_session)


def test_unrelated_owned_user_file_keeps_existing_authorization() -> None:
    db_session = MagicMock(spec=Session)
    db_session.query.return_value.scalar.return_value = True

    assert user_can_access_chat_file("user-file", _user(uuid4()), db_session)
    db_session.execute.assert_not_called()


def test_non_generated_or_missing_file_record_is_denied() -> None:
    db_session = _db_session(None, record_exists=False)

    assert not _user_can_access_generated_image(
        "missing-image", _user(uuid4()), db_session
    )
    assert db_session.execute.call_count == 1


def test_generated_image_save_persists_access_metadata() -> None:
    metadata = {
        CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY: str(uuid4()),
        CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY: str(uuid4()),
    }
    file_store = MagicMock()
    file_store.save_file.return_value = "generated-image"

    with (
        patch(
            "onyx.file_store.utils.get_default_file_store",
            return_value=file_store,
        ),
        patch(
            "onyx.file_store.utils.get_image_type",
            return_value="image/png",
        ),
    ):
        result = save_file_from_base64("YQ==", metadata)

    assert result == "generated-image"
    assert file_store.save_file.call_args.kwargs["file_metadata"] == metadata
