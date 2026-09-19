"""Regression coverage for custom-action attachment authorization."""

from collections.abc import Generator
from uuid import uuid4

import pytest
from sqlalchemy.orm import Session

from onyx.db.engine.sql_engine import SqlEngine
from onyx.db.enums import Permission
from onyx.db.models import Persona, Tool, User
from onyx.db.persona import upsert_persona
from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError
from tests.external_dependency_unit.conftest import create_test_user


@pytest.fixture
def rollback_db_session() -> Generator[Session, None, None]:
    """Run each regression case inside an outer transaction."""
    SqlEngine.init_engine(pool_size=2, max_overflow=0)
    connection = SqlEngine.get_engine().connect()
    transaction = connection.begin()
    session = Session(
        bind=connection,
        expire_on_commit=False,
        join_transaction_mode="create_savepoint",
    )
    try:
        yield session
    finally:
        session.close()
        if transaction.is_active:
            transaction.rollback()
        connection.close()


def _create_custom_action(rollback_db_session: Session, owner: User) -> Tool:
    action = Tool(
        name=f"custom-action-guard-{uuid4().hex[:8]}",
        description="Synthetic custom-action attachment guard fixture",
        openapi_schema={
            "openapi": "3.0.0",
            "info": {"title": "Synthetic action", "version": "1.0.0"},
            "servers": [{"url": "http://127.0.0.1:9"}],
            "paths": {},
        },
        custom_headers=[{"key": "X-Phase9-Synthetic-Key", "value": "not-a-secret"}],
        user_id=owner.id,
        passthrough_auth=False,
        enabled=True,
    )
    rollback_db_session.add(action)
    rollback_db_session.commit()
    rollback_db_session.refresh(action)
    return action


def _upsert_persona_with_tools(
    rollback_db_session: Session,
    user: User,
    tool_ids: list[int],
    persona: Persona | None = None,
) -> Persona:
    return upsert_persona(
        user=user,
        persona_id=persona.id if persona else None,
        name=persona.name if persona else f"custom-action-agent-{uuid4().hex[:8]}",
        description="Synthetic custom-action attachment guard fixture",
        starter_messages=None,
        system_prompt=None,
        task_prompt=None,
        datetime_aware=None,
        is_public=False,
        tool_ids=tool_ids,
        db_session=rollback_db_session,
    )


def test_non_owner_cannot_attach_foreign_custom_action(
    rollback_db_session: Session,
) -> None:
    owner = create_test_user(rollback_db_session, "custom_action_owner")
    outsider = create_test_user(rollback_db_session, "custom_action_outsider")
    owner.effective_permissions = [Permission.MANAGE_ACTIONS.value]
    rollback_db_session.commit()
    action = _create_custom_action(rollback_db_session, owner)

    with pytest.raises(OnyxError, match="selected custom actions") as exc_info:
        _upsert_persona_with_tools(rollback_db_session, outsider, [action.id])
    assert exc_info.value.error_code is OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_owner_can_attach_own_custom_action(
    rollback_db_session: Session,
) -> None:
    owner = create_test_user(rollback_db_session, "custom_action_owner_allowed")
    owner.effective_permissions = []
    owner.is_group_manager = True
    rollback_db_session.commit()
    action = _create_custom_action(rollback_db_session, owner)

    persona = _upsert_persona_with_tools(rollback_db_session, owner, [action.id])

    assert {tool.id for tool in persona.tools} == {action.id}


def test_actions_admin_can_attach_foreign_custom_action(
    rollback_db_session: Session,
) -> None:
    owner = create_test_user(rollback_db_session, "custom_action_admin_owner")
    actions_admin = create_test_user(rollback_db_session, "custom_action_admin")
    actions_admin.effective_permissions = [Permission.MANAGE_ACTIONS.value]
    rollback_db_session.commit()
    action = _create_custom_action(rollback_db_session, owner)

    persona = _upsert_persona_with_tools(rollback_db_session, actions_admin, [action.id])

    assert {tool.id for tool in persona.tools} == {action.id}


def test_existing_foreign_custom_action_is_preserved(
    rollback_db_session: Session,
) -> None:
    owner = create_test_user(rollback_db_session, "custom_action_legacy_owner")
    persona_owner = create_test_user(rollback_db_session, "custom_action_legacy_agent_owner")
    action = _create_custom_action(rollback_db_session, owner)
    persona = _upsert_persona_with_tools(rollback_db_session, persona_owner, [])
    persona.tools = [action]
    rollback_db_session.commit()

    updated = _upsert_persona_with_tools(
        rollback_db_session, persona_owner, [action.id], persona
    )

    assert {tool.id for tool in updated.tools} == {action.id}


def test_removed_foreign_custom_action_cannot_be_readded(
    rollback_db_session: Session,
) -> None:
    owner = create_test_user(rollback_db_session, "custom_action_readd_owner")
    persona_owner = create_test_user(rollback_db_session, "custom_action_readd_agent_owner")
    action = _create_custom_action(rollback_db_session, owner)
    persona = _upsert_persona_with_tools(rollback_db_session, persona_owner, [])
    persona.tools = [action]
    rollback_db_session.commit()

    _upsert_persona_with_tools(rollback_db_session, persona_owner, [], persona)

    with pytest.raises(OnyxError, match="selected custom actions") as exc_info:
        _upsert_persona_with_tools(rollback_db_session, persona_owner, [action.id], persona)
    assert exc_info.value.error_code is OnyxErrorCode.INSUFFICIENT_PERMISSIONS
