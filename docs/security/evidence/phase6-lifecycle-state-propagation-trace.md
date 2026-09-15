# Phase 6 Action 6.9 - Lifecycle State Propagation Trace
## Purpose
Trace security-relevant state transitions through the exact pinned Onyx source.
Primary question:
When data, authorization, identity or capability state changes, what other
components must eventually converge on the new state?
Target lifecycle:
authoritative state change -> database -> asynchronous work -> search/index ->
cache -> file/object state -> observable result -> audit/logging.
This action performs static source analysis only.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.8 parent: `d1560fbcdeda8d12dd5252fec387baa40b48abd4`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Document and Connector Deletion
Evidence lines: 500
```text
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/document_set.py:127:        db_session.delete(existing[document_set.id])
HEAD:backend/ee/onyx/db/document_set.py:136:def delete_document_set_privacy__no_commit(
HEAD:backend/ee/onyx/db/hierarchy.py:41:            cc_pair.status != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/ee/onyx/db/user_group.py:202:        delete(DocumentSet__UserGroup).where(
HEAD:backend/ee/onyx/db/user_group.py:454:        # NOTE: CC pairs can never go from DELETING to any other state -> it's safe to ignore them
HEAD:backend/ee/onyx/db/user_group.py:455:        .where(ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING)
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1100:    Should be used very carefully (only for connectors that are being deleted)."""
HEAD:backend/ee/onyx/db/user_group.py:1108:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/db/user_group.py:1110:            f"Connector Credential Pair '{cc_pair_id}' is not in the DELETING state. status={cc_pair.status}"
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:357:    onto their new address, keeping one row and deleting the rest.
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:419:        # workspace, and deleting one cascades their membership away.
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:286:                # in sharepoint but it is removed from Azure AD. There is no actual documentation on this, but based on
HEAD:backend/ee/onyx/server/scim/api.py:304:_ENTRA_TOMBSTONE_PREFIX = re.compile(r"[0-9a-f]{32}", re.IGNORECASE)
HEAD:backend/ee/onyx/server/scim/api.py:307:def _is_entra_tombstone_rename(current_email: str, new_email: str) -> bool:
HEAD:backend/ee/onyx/server/scim/api.py:313:    match = _ENTRA_TOMBSTONE_PREFIX.match(new_email)
HEAD:backend/ee/onyx/server/scim/api.py:388:    - An Entra soft-delete tombstone value never overwrites the email.
HEAD:backend/ee/onyx/server/scim/api.py:400:    if _is_entra_tombstone_rename(user.email, requested_email):
HEAD:backend/ee/onyx/server/scim/api.py:402:            "SCIM email for %s is an Entra soft-delete tombstone; keeping email",
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:49:            "Last admin user is leaving the organization. Deleting tenant from control plane."
HEAD:backend/ee/onyx/server/user_group/api.py:548:    detach_ids = set(request.removed_document_set_ids)
HEAD:backend/ee/onyx/server/user_group/models.py:150:    removed_document_set_ids: list[int]
HEAD:backend/onyx/access/access.py:360:    TODO(delete-me): exists only because the File connector leaves
HEAD:backend/onyx/auth/permission_projection.py:34:    PUBLIC) is global-only. So is ``delete``, except for a private groupless connector
HEAD:backend/onyx/auth/permission_projection.py:38:        "delete": is_connectors_admin or owns_groupless,
HEAD:backend/onyx/auth/permission_projection.py:107:    MANAGE_DOCUMENT_SETS only. So is ``delete``, except for a private groupless set its
HEAD:backend/onyx/auth/permission_projection.py:108:    creator made — mirrors the GATE 2 carve-out in delete_document_set."""
HEAD:backend/onyx/auth/permission_projection.py:112:        "delete": is_document_sets_admin or owns_groupless,
HEAD:backend/onyx/auth/schemas.py:12:    """Legacy tombstone: kept only as the column type for ``User.role``, which is never
HEAD:backend/onyx/auth/session_tokens.py:4:and logout writes a tombstone instead of deleting, so a rejected token can be
HEAD:backend/onyx/auth/session_tokens.py:5:classified: EXPIRED (embedded expiry passed), TERMINATED (tombstone), NOT_FOUND
HEAD:backend/onyx/auth/session_tokens.py:31:# How long an entry outlives its logical expiry (and how long a tombstone
HEAD:backend/onyx/auth/session_tokens.py:39:    legacy values and tombstones parse too; ``AwareDatetime`` rejects naive
HEAD:backend/onyx/auth/session_tokens.py:99:def build_session_tombstone_value(
HEAD:backend/onyx/auth/session_tokens.py:103:    Builds the logout tombstone, preserving the original fields when the
HEAD:backend/onyx/auth/users.py:89:    build_session_tombstone_value,
HEAD:backend/onyx/auth/users.py:1289:            logger.exception("Error deleting anonymous user cookie")
HEAD:backend/onyx/auth/users.py:1744:        Overwrites the token with a tombstone so other tabs' rejections classify
HEAD:backend/onyx/auth/users.py:1752:            build_session_tombstone_value(
HEAD:backend/onyx/background/README.md:78:- Deletes documents that are marked for deletion in Postgres
HEAD:backend/onyx/background/celery/apps/app_base.py:47:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/app_base.py:50:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/primary.py:31:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/primary.py:34:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/primary.py:197:    RedisConnectorDelete.reset_all(r)
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:80:                        f"Skipping capability checks for deleted connector "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:30:    delete_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:35:    delete_all_documents_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:38:from onyx.db.document_set import delete_document_set_cc_pair_relationship__no_commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:61:from onyx.redis.redis_connector_delete import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:62:    RedisConnectorDelete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:63:    RedisConnectorDeletePayload,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:122:        prune_payload = redis_connector.prune.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:177:        # collect cc_pair_ids and note whether any are in DELETING status
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:179:        has_deleting_cc_pair = False
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:184:                if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:185:                    has_deleting_cc_pair = True
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:188:        # DELETING status. Marking on bare cc_pair existence would keep
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:191:        if has_deleting_cc_pair:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:203:                    # this means we wanted to start deleting but dependent tasks were running
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:245:            if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:281:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:294:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:305:    redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:306:    fence_payload = RedisConnectorDeletePayload(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:311:    redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:334:            # A running port could re-add docs we're deleting (create-only write).
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:364:        redis_connector.delete.taskset_clear()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:370:        tasks_generated = redis_connector.delete.generate_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:386:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:390:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:405:        redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:426:    fence_data = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:439:    if r.exists(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:456:        connector_id_to_delete: int | None = None
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:481:                redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:504:            delete_document_set_cc_pair_relationship__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:526:            connector_id_to_delete = cc_pair.connector_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:530:            # Explicitly delete document by connector credential pair records before deleting the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:531:            # This is needed because connector_id is a primary key in that table and cascading deletes won't work
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:532:            delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:534:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:542:            # related to the deleted DocumentByConnectorCredentialPair during commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:546:            delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:548:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:558:            # if there are no credentials left, delete the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:561:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:565:                    "Connector deletion - Connector already deleted, skipping connector cleanup"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:569:                    "Connector deletion - Found no credentials left for connector, deleting connector"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:571:                db_session.delete(connector)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:621:                f"cc_pair={cc_pair_id} connector={connector_id_to_delete} credential={credential_id_to_delete}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:633:        f"connector={connector_id_to_delete} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:638:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:666:        if not key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:727:    if not redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:734:        payload = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:743:        redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:766:    for member in r.sscan_iter(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:781:        redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:792:    if redis_connector.delete.active():
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:804:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:56:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:177:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:182:            f"fence={redis_connector.delete.fence_key}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:361:    7) pulls all document IDs from the source and compares those IDs to locally stored documents and deletes
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:376:    - non-checkpointed connectors/ new runs in general => delete the old document batches from the file store and do the new run
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:131:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:381:            if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:383:                    f"Skipping hierarchy fetching for deleting connector: cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:9:    SOAKING  -> (soak elapsed + new index can serve)                                -> DELETING
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:10:    DELETING -> (old index data gone, count-verified)                               -> RECLAIMED (row kept)
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:45:    mark_cc_pairs_deleting_if_still_wont_port__no_commit,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:55:    advance_to_deleting__no_commit,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:76:# Per-DELETING-row wall-clock budget. On a whale (multi-tenant delete_by_query is
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:90:    IndexReclaimStatus.DELETING,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:123:    move the still-not-recoverable consented connectors to DELETING and start the soak."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:129:    # connector re-activated after consent was captured can't be clobbered into DELETING.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:130:    deleted = mark_cc_pairs_deleting_if_still_wont_port__no_commit(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:137:        # Kick the connector-deletion pipeline (crash-resumable) now that DELETING is
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:156:    serve before deleting the old one."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:172:    if advance_to_deleting__no_commit(search_settings):
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:175:            "Old-index reclaim %s -> DELETING (index=%s).",
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:181:def _drive_deleting(db_session: Session, search_settings: SearchSettings) -> None:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:182:    """DELETING: delete the old index's data, looping bounded batches within a time
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:185:    INCOMPLETE leaves it DELETING for next tick."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:246:        elif status == IndexReclaimStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:247:            _drive_deleting(db_session, search_settings)
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:377:                    or cc_pair.status == ConnectorCredentialPairStatus.DELETING
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:382:                    log.info("cc_pair gone/deleting, stopping port")
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:387:            # stall watchdog fails it a full window later. After the cancel/deleting
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:200:        # if never pruned, use the connector creation time. We could also
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:204:        last_pruned = cc_pair.connector.time_created
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:206:    next_prune = last_pruned + timedelta(seconds=cc_pair.connector.prune_freq)
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:387:        # skip pruning if the cc_pair is deleting
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:388:        if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:390:                "try_creating_prune_generator_task: cc_pair=%s deleting", cc_pair.id
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:403:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:405:                "try_creating_prune_generator_task: cc_pair=%s deleting", cc_pair.id
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:489:    and compares those IDs to locally stored documents and deletes all locally stored IDs missing
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:520:                f"connector_prune_generator_task - fence not found: fence={redis_connector.prune.fence_key}"
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:842:    # Orphan tags can only appear when the prune actually removed documents.
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:18:    delete_document_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:19:    delete_documents_complete,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:33:from onyx.db.relationships import delete_document_references_from_kg
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:122:    To delete a connector / credential pair:
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:125:    (2) delete all documents from document stores
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:157:                action = DocumentCleanupAction.DELETE
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:214:        if action == DocumentCleanupAction.DELETE:
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:216:                _ = retry_document_index.delete(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:230:        if action == DocumentCleanupAction.DELETE:
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:232:                delete_document_references_from_kg(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:237:                delete_documents_complete(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:246:                delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:324:                    delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:78:    UserFileDeletingSkip,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:333:        if uf.status != UserFileStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:406:        if user_file is None or user_file.status == UserFileStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:444:        except UserFileDeletingSkip:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:445:            # File began deleting mid-pipeline — the delete owns removal; skip cleanly
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:446:            # rather than fail. (The early-out above catches the already-deleting case.)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:449:                "deleting mid-indexing; skipping"
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:467:            if uf is not None and uf.status != UserFileStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:497:        # (the adapter's DELETING skip re-checks under the row lock to close the race.)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:499:        if user_file is None or user_file.status == UserFileStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:530:        except UserFileDeletingSkip:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:531:            # File began deleting mid-pipeline — skip cleanly so the caller doesn't flag it
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:534:                f"_index_user_file_to_secondary - user file {user_file_id} began deleting "
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:714:                    and current_user_file.status != UserFileStatus.DELETING
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:729:                if uf.status != UserFileStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:766:    """Scan for user files with DELETING status and enqueue per-file tasks.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:777:       next beat cycle can re-enqueue if the file is still DELETING.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:810:            # DELETING pool here so the standard machinery below cleans them.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:823:                        UserFile.status == UserFileStatus.DELETING
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:862:    """Core implementation for deleting a single user file.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:873:        # and the file remains in DELETING status.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:948:                retry_document_index.delete(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:964:                f"delete_user_file_impl - Error deleting file id={user_file_id} - {e.__class__.__name__}"
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1233:    A blob's own record carries the session that produced it, and deleting the
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:60:        r.delete(DOCUMENT_SYNC_FENCE_KEY)
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:67:def delete_document_sync_taskset(r: TenantRedisClient) -> None:
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:69:    r.delete(DOCUMENT_SYNC_TASKSET_KEY)
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:75:    r.delete(DOCUMENT_SYNC_TASKSET_KEY)
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:76:    r.delete(DOCUMENT_SYNC_FENCE_KEY)
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:43:    delete_document_set,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:438:            # If there are no connectors of any kind, delete the document set.
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:439:            delete_document_set(document_set_row=document_set, db_session=db_session)
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:441:                f"Successfully deleted document set: document_set={document_set_id}"
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:571:            # Defer only if the doc can still be ported; an INVALID/DELETING-only
HEAD:backend/onyx/background/indexing/run_docfetching.py:305:    ) or cc_pair_loop.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/periodic_poller.py:7:   PROCESSING / DELETING / needs_sync states via the drain loops defined
HEAD:backend/onyx/background/task_utils.py:90:def _claim_next_deleting_file(
HEAD:backend/onyx/background/task_utils.py:94:    """Claim the next DELETING file.
HEAD:backend/onyx/background/task_utils.py:102:        .where(UserFile.status == UserFileStatus.DELETING)
HEAD:backend/onyx/background/task_utils.py:174:    """Delete all pending DELETING user files."""
HEAD:backend/onyx/background/task_utils.py:187:            file_id = _claim_next_deleting_file(session, exclude_ids=failed)
HEAD:backend/onyx/background/task_utils.py:263:    """Hand rows already marked DELETING to whatever drains them here.
HEAD:backend/onyx/chat/incognito.py:35:    mark_user_files_deleting,
HEAD:backend/onyx/chat/incognito.py:131:    mark_user_files_deleting(db_session, deletable)
HEAD:backend/onyx/chat/incognito.py:138:    A blob's record carries the session that produced it and deleting the blob
HEAD:backend/onyx/chat/incognito.py:248:    The file record carries the session stamp, so deleting the blob deletes the
HEAD:backend/onyx/chat/incognito_context.py:33:_TOMBSTONE_TTL_SECONDS = INCOGNITO_CONTEXT_TTL_SECONDS
HEAD:backend/onyx/chat/incognito_context.py:50:_TOMBSTONE = b"tombstone"
HEAD:backend/onyx/chat/incognito_context.py:53:if cur == 'tombstone' then
HEAD:backend/onyx/chat/incognito_context.py:96:    """The value's version and JSON body, or (0, None) for a tombstone or a
HEAD:backend/onyx/chat/incognito_context.py:193:    """Whether this session's teardown tombstone is still present.
HEAD:backend/onyx/chat/incognito_context.py:198:    return _stored_context(chat_session_id) == _TOMBSTONE
HEAD:backend/onyx/chat/incognito_context.py:215:        if raw is None or raw == _TOMBSTONE
HEAD:backend/onyx/chat/incognito_context.py:229:    """End the session now: tombstone the context so an in-flight turn cannot
HEAD:backend/onyx/chat/incognito_context.py:233:    client.set(_context_key(chat_session_id), _TOMBSTONE, ex=_TOMBSTONE_TTL_SECONDS)
HEAD:backend/onyx/configs/app_configs.py:1114:# Soak before deleting a PAST index, anchored to when it stopped being read.
HEAD:backend/onyx/configs/chat_configs.py:90:# As opposed to soft deleting them, which just hides them from non-admin users
HEAD:backend/onyx/configs/constants.py:222:# files are stuck in DELETING status and the beat keeps re-enqueuing them.
HEAD:backend/onyx/connectors/README.md:25:  - This is used by our pruning job which removes old documents from the index.
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:105:        # If attempting to update without deleting the connector:
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:112:                f"Please delete and recreate this connector, or contact Onyx support "
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:113:                f"for assistance with updating the configuration without deleting the connector."
HEAD:backend/onyx/connectors/interfaces.py:336:        Caller's responsibility is to delete the old ConnectorFailures and replace with the new ones.
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:631:    """Folders and tombstones carry no content, so only files in window index."""
HEAD:backend/onyx/connectors/salesforce/shelve_stuff/old_test_salesforce_shelves.py:118:    Clears the SF DB by deleting all files in the data directory.
HEAD:backend/onyx/connectors/salesforce/shelve_stuff/test_salesforce_shelves.py:118:    Clears the SF DB by deleting all files in the data directory.
HEAD:backend/onyx/db/chunk.py:56:def delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/chunk.py:60:    stmt = delete(ChunkStats).where(ChunkStats.document_id.in_(document_ids))
HEAD:backend/onyx/db/connector.py:116:        prune_freq=connector_data.prune_freq,
HEAD:backend/onyx/db/connector.py:155:def delete_connector(
HEAD:backend/onyx/db/connector.py:159:    """Only used in special cases (e.g. a connector is in a bad state and we need to delete it).
HEAD:backend/onyx/db/connector.py:165:            success=True, message="Connector was already deleted", data=connector_id
HEAD:backend/onyx/db/connector.py:168:    db_session.delete(connector)
HEAD:backend/onyx/db/connector.py:170:        success=True, message="Connector deleted successfully", data=connector_id
HEAD:backend/onyx/db/connector_alerts.py:18:    """Dedup key for connector alerts; cleanup deletes by exact match on it."""
HEAD:backend/onyx/db/connector_alerts.py:60:    """Delete every admin's alert for this connector so the next incident
HEAD:backend/onyx/db/connector_credential_pair.py:676:def delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/connector_credential_pair.py:681:    stmt = delete(ConnectorCredentialPair).where(
HEAD:backend/onyx/db/connector_credential_pair.py:903:        # For embedding swap checks, include PAUSED and exclude DELETING or INVALID
HEAD:backend/onyx/db/connector_credential_pair.py:923:    Works out to INVALID always + PAUSED under ACTIVE_ONLY. Excludes DELETING (already
HEAD:backend/onyx/db/connector_credential_pair.py:934:        ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/onyx/db/connector_credential_pair.py:939:def mark_cc_pairs_deleting_if_still_wont_port__no_commit(
HEAD:backend/onyx/db/connector_credential_pair.py:942:    """Atomically move the given cc_pairs to DELETING, but ONLY those still INVALID or
HEAD:backend/onyx/db/connector_credential_pair.py:945:    consent set was captured is skipped, never clobbered into DELETING (Postgres rechecks
HEAD:backend/onyx/db/connector_credential_pair.py:961:        .values(status=ConnectorCredentialPairStatus.DELETING)
HEAD:backend/onyx/db/credentials.py:340:                "Force deleting credential %s and its associated records", credential_id
HEAD:backend/onyx/db/credentials.py:343:            # Delete DocumentByConnectorCredentialPair records first
HEAD:backend/onyx/db/credentials.py:347:            # Then delete ConnectorCredentialPair records
HEAD:backend/onyx/db/credentials.py:349:                db_session.delete(connector)
HEAD:backend/onyx/db/credentials.py:351:            # Commit these deletions before deleting the credential
HEAD:backend/onyx/db/credentials.py:362:        logger.warning("Force deleting credential %s", credential_id)
HEAD:backend/onyx/db/credentials.py:364:        logger.notice("Deleting credential %s", credential_id)
HEAD:backend/onyx/db/document.py:30:from onyx.db.chunk import delete_chunk_stats_by_connector_credential_pair__no_commit
HEAD:backend/onyx/db/document.py:38:from onyx.db.feedback import delete_document_feedback_for_documents__no_commit
HEAD:backend/onyx/db/document.py:55:from onyx.db.tag import delete_document_tags_for_documents__no_commit
HEAD:backend/onyx/db/document.py:101:    *_for_cc_pairs variant — an INVALID/DELETING-only doc's flag never clears."""
HEAD:backend/onyx/db/document.py:110:    write — an INVALID/DELETING-only doc's deferred flag would never clear."""
HEAD:backend/onyx/db/document.py:141:    (ported) set so INVALID/DELETING-only deferred flags can't block the swap."""
HEAD:backend/onyx/db/document.py:825:        # NOTE: CC pairs can never go from DELETING to any other state -> it's safe to ignore them
HEAD:backend/onyx/db/document.py:826:        .where(ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING)
HEAD:backend/onyx/db/document.py:1132:def delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1139:    """Deletes a single document by cc pair relationship entry.
HEAD:backend/onyx/db/document.py:1144:    delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1151:def delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1158:    """This deletes just the document by cc pair entries for a particular cc pair.
HEAD:backend/onyx/db/document.py:1163:    stmt = delete(DocumentByConnectorCredentialPair).where(
HEAD:backend/onyx/db/document.py:1178:def delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1183:    """Deletes all document by connector credential pair entries for a specific connector and credential.
HEAD:backend/onyx/db/document.py:1185:    before deleting the connector itself. This is crucial because connector_id is part of the
HEAD:backend/onyx/db/document.py:1186:    primary key in DocumentByConnectorCredentialPair, and attempting to delete the Connector
HEAD:backend/onyx/db/document.py:1191:    stmt = delete(DocumentByConnectorCredentialPair).where(
HEAD:backend/onyx/db/document.py:1200:def delete_documents__no_commit(db_session: Session, document_ids: list[str]) -> None:
HEAD:backend/onyx/db/document.py:1201:    db_session.execute(delete(DbDocument).where(DbDocument.id.in_(document_ids)))
HEAD:backend/onyx/db/document.py:1236:def delete_documents_complete__no_commit(
HEAD:backend/onyx/db/document.py:1239:    """This completely deletes the documents from the db, including all foreign key relationships"""
HEAD:backend/onyx/db/document.py:1263:    # Continue with deleting the chunk stats for the documents
HEAD:backend/onyx/db/document.py:1264:    delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1269:    delete_documents_by_connector_credential_pair__no_commit(db_session, document_ids)
HEAD:backend/onyx/db/document.py:1270:    delete_document_feedback_for_documents__no_commit(
HEAD:backend/onyx/db/document.py:1273:    delete_document_tags_for_documents__no_commit(
HEAD:backend/onyx/db/document.py:1276:    delete_documents__no_commit(db_session, document_ids)
HEAD:backend/onyx/db/document.py:1279:def delete_documents_complete(
HEAD:backend/onyx/db/document.py:1283:    """Fully remove documents AND best-effort delete their attached files.
HEAD:backend/onyx/db/document.py:1288:    file_ids_to_delete = get_file_ids_for_document_ids(
HEAD:backend/onyx/db/document.py:1292:    delete_documents_complete__no_commit(
HEAD:backend/onyx/db/document.py:1300:def delete_all_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:1306:    """Delete all documents for a given connector credential pair.
HEAD:backend/onyx/db/document.py:1307:    This will delete all documents and their associated data (chunks, feedback, tags, etc.)
HEAD:backend/onyx/db/document.py:1331:        delete_documents_complete(
HEAD:backend/onyx/db/document.py:1336:            raise RuntimeError("Timeout reached while deleting documents")
HEAD:backend/onyx/db/document.py:1894:                != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/onyx/db/document.py:1961:def delete_document_by_id__no_commit(
HEAD:backend/onyx/db/document.py:1965:    """Delete a single document and its connector credential pair relationships.
HEAD:backend/onyx/db/document.py:1969:    This uses delete_documents_complete__no_commit which handles
HEAD:backend/onyx/db/document.py:1973:    delete_documents_complete__no_commit(db_session, [document_id])
HEAD:backend/onyx/db/document_access.py:40:        ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING
HEAD:backend/onyx/db/document_set.py:94:def _delete_document_set_cc_pairs__no_commit(
HEAD:backend/onyx/db/document_set.py:98:    stmt = delete(DocumentSet__ConnectorCredentialPair).where(
HEAD:backend/onyx/db/document_set.py:117:def delete_document_set_privacy__no_commit(
HEAD:backend/onyx/db/document_set.py:492:        # Delete existing federated connector mappings for this document set
HEAD:backend/onyx/db/document_set.py:493:        delete_stmt = delete(FederatedConnector__DocumentSet).where(
HEAD:backend/onyx/db/document_set.py:524:    _delete_document_set_cc_pairs__no_commit(
HEAD:backend/onyx/db/document_set.py:530:def delete_document_set(
HEAD:backend/onyx/db/document_set.py:534:    _delete_document_set_cc_pairs__no_commit(
HEAD:backend/onyx/db/document_set.py:537:    db_session.delete(document_set_row)
HEAD:backend/onyx/db/document_set.py:541:def mark_document_set_as_to_be_deleted(
HEAD:backend/onyx/db/document_set.py:547:    as needing an update. The actual document set row will be deleted by the background
HEAD:backend/onyx/db/document_set.py:564:                "Cannot delete document set while it is syncing. Please wait for it to finish syncing, and then try again."
HEAD:backend/onyx/db/document_set.py:568:        _delete_document_set_cc_pairs__no_commit(
HEAD:backend/onyx/db/document_set.py:572:        # delete all federated connector mappings so the cleanup task can fully
HEAD:backend/onyx/db/document_set.py:573:        # remove the document set once the Vespa sync completes
HEAD:backend/onyx/db/document_set.py:574:        delete_stmt = delete(FederatedConnector__DocumentSet).where(
HEAD:backend/onyx/db/document_set.py:579:        # delete all private document set information
HEAD:backend/onyx/db/document_set.py:581:            "onyx.db.document_set", "delete_document_set_privacy__no_commit"
HEAD:backend/onyx/db/document_set.py:596:def delete_document_set_cc_pair_relationship__no_commit(
HEAD:backend/onyx/db/document_set.py:599:    """Deletes all rows from DocumentSet__ConnectorCredentialPair where the
HEAD:backend/onyx/db/document_set.py:601:    delete_stmt = delete(DocumentSet__ConnectorCredentialPair).where(
HEAD:backend/onyx/db/document_set.py:815:    # NOTE: CC pairs can never go from DELETING to any other state -> it's safe to ignore them
HEAD:backend/onyx/db/document_set.py:820:        .where(ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING)  # noqa: E712
HEAD:backend/onyx/db/document_set.py:836:                func.array_remove(func.array_agg(DocumentSetDBModel.name), None), []
HEAD:backend/onyx/db/entities.py:293:    db_session.query(KGEntity).filter(KGEntity.document_id.in_(document_ids)).delete(
HEAD:backend/onyx/db/enums.py:235:    DELETING: deleting the old index's data (loops until count-verified empty).
HEAD:backend/onyx/db/enums.py:243:    DELETING = "DELETING"
HEAD:backend/onyx/db/enums.py:258:    DELETING = "DELETING"
HEAD:backend/onyx/db/enums.py:301:    DELETING = "DELETING"
HEAD:backend/onyx/db/federated.py:221:def delete_federated_connector_document_set_mapping(
HEAD:backend/onyx/db/federated.py:226:    """Delete a federated connector document set mapping."""
HEAD:backend/onyx/db/federated.py:319:def delete_federated_connector(
HEAD:backend/onyx/db/federated.py:323:    """Delete a federated connector and all its related data."""
HEAD:backend/onyx/db/federated.py:331:    # Delete related document set mappings (cascade should handle this)
HEAD:backend/onyx/db/federated.py:332:    db_session.delete(federated_connector)
HEAD:backend/onyx/db/feedback.py:205:def delete_document_feedback_for_documents__no_commit(
HEAD:backend/onyx/db/feedback.py:210:    stmt = delete(DocumentRetrievalFeedback).where(
HEAD:backend/onyx/db/hierarchy.py:878:    stmt = delete(HierarchyNodeByConnectorCredentialPair).where(
HEAD:backend/onyx/db/incognito.py:59:def mark_user_files_deleting(db_session: Session, file_ids: Sequence[UUID]) -> None:
HEAD:backend/onyx/db/incognito.py:60:    """Move these files to DELETING. Caller commits."""
HEAD:backend/onyx/db/incognito.py:66:        .values(status=UserFileStatus.DELETING)
HEAD:backend/onyx/db/incognito.py:70:def mark_incognito_user_files_deleting(
HEAD:backend/onyx/db/incognito.py:81:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:86:    mark_user_files_deleting(db_session, file_ids)
HEAD:backend/onyx/db/incognito.py:96:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:162:            UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/kg_temp_view.py:83:#         WHERE ccp.status != 'DELETING'
HEAD:backend/onyx/db/kg_temp_view.py:100:#         AND ccp.status != 'DELETING'
HEAD:backend/onyx/db/mcp.py:318:        "Deleting MCP server %s with %s associated tools", server_id, tools_count
HEAD:backend/onyx/db/models.py:336:    # Legacy tombstone column: no longer read or written by application code.
HEAD:backend/onyx/db/models.py:793:    # rows with `is_current=False` should be deleted when the document
HEAD:backend/onyx/db/models.py:1068:    # SET NULL when document is deleted - node can exist without its document
HEAD:backend/onyx/db/models.py:1070:        ForeignKey("document.id", ondelete="SET NULL"), nullable=True, index=True
HEAD:backend/onyx/db/models.py:1194:    # SET NULL when hierarchy node is deleted - document should not be blocked by node deletion
HEAD:backend/onyx/db/models.py:1271:        ForeignKey("document.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2123:        ForeignKey("connector.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:2205:        ForeignKey("federated_connector.id", ondelete="CASCADE"), nullable=False
HEAD:backend/onyx/db/models.py:2228:        ForeignKey("federated_connector.id", ondelete="CASCADE"), nullable=False
HEAD:backend/onyx/db/models.py:2231:        ForeignKey("document_set.id", ondelete="CASCADE"), nullable=False
HEAD:backend/onyx/db/models.py:2512:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2730:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2847:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2899:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:3126:        ForeignKey("connector.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:3139:        "Connector", back_populates="documents_by_connector", passive_deletes=True
HEAD:backend/onyx/db/models.py:3142:        "Credential", back_populates="documents_by_credential", passive_deletes=True
HEAD:backend/onyx/db/models.py:3440:    # Not a FK because we want to be able to delete the tool without deleting
HEAD:backend/onyx/db/models.py:4182:    # Owner user. SET NULL (not CASCADE) so deleting a user orphans shared
HEAD:backend/onyx/db/models.py:4385:        ForeignKey("document.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:5170:        ForeignKey("document_set.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:5369:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:5423:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:6922:    The target is a ``gated_app`` row (external app or MCP server). Deleting the
HEAD:backend/onyx/db/models.py:7352:    derived from which. Deleting the underlying target CASCADEs this row away,
HEAD:backend/onyx/db/permission_sync_attempt.py:552:    """Delete all doc permission sync attempts for a connector credential pair.
HEAD:backend/onyx/db/permission_sync_attempt.py:574:    """Delete all external group permission sync attempts for a connector credential pair.
HEAD:backend/onyx/db/persona.py:528:    or an owner-group member. A scoped manager is NOT included: deleting or publishing a
HEAD:backend/onyx/db/port_attempt.py:768:        cc_pair is DELETING, so a flag alone would wedge the waiter forever.
HEAD:backend/onyx/db/port_orphan_candidate.py:93:    The single choke point every index-delete entry point (connector cleanup, ingestion)
HEAD:backend/onyx/db/port_orphan_candidate.py:116:    """User-file analog of _for_document: record the deleted file under its user scope
HEAD:backend/onyx/db/port_orphan_candidate.py:139:    cc_pair or delete path recorded for the same document. Caller commits."""
HEAD:backend/onyx/db/relationships.py:577:def delete_document_references_from_kg(db_session: Session, document_id: str) -> None:
HEAD:backend/onyx/db/relationships.py:589:    db_session.query(KGEntity).filter(KGEntity.document_id == document_id).delete(
HEAD:backend/onyx/db/scheduled_task.py:108:    Reuse unchanged rows to avoid deleting and inserting the same unique key
HEAD:backend/onyx/db/search_settings.py:128:    # A promoted index may still be backfilling its port from this one; deleting it
HEAD:backend/onyx/db/search_settings.py:298:    IndexReclaimStatus.DELETING,
HEAD:backend/onyx/db/search_settings.py:343:    DELETING: the soak window + `_new_index_can_serve` gate exist for swapping out a *live*
HEAD:backend/onyx/db/search_settings.py:346:    abandoned_future.reclaim_status = IndexReclaimStatus.DELETING
HEAD:backend/onyx/db/search_settings.py:356:    """PAST indices still needing reclamation (PENDING/SOAKING/DELETING), oldest
HEAD:backend/onyx/db/search_settings.py:384:def advance_to_deleting__no_commit(search_settings: SearchSettings) -> bool:
HEAD:backend/onyx/db/search_settings.py:385:    """SOAKING -> DELETING: soak elapsed + new index healthy. No-op returning False
HEAD:backend/onyx/db/search_settings.py:389:    search_settings.reclaim_status = IndexReclaimStatus.DELETING
HEAD:backend/onyx/db/search_settings.py:396:    """DELETING -> RECLAIMED: the old index's data is gone. Terminal success — the PAST
HEAD:backend/onyx/db/search_settings.py:398:    No-op returning False unless currently DELETING. Caller commits."""
HEAD:backend/onyx/db/search_settings.py:399:    if search_settings.reclaim_status != IndexReclaimStatus.DELETING:
HEAD:backend/onyx/db/slack_channel_config.py:32:    # delete existing persona-document_set relationships
HEAD:backend/onyx/db/swap_index.py:15:    delete_all_documents_for_connector_credential_pair,
HEAD:backend/onyx/db/swap_index.py:88:                delete_all_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/swap_index.py:225:    required_cc_pairs: a global count would deadlock on un-portable INVALID/DELETING docs
HEAD:backend/onyx/db/tag.py:153:        delete_stmt = delete(Document__Tag).where(
HEAD:backend/onyx/db/tag.py:155:            Document__Tag.tag_id.in_(delete_tags),
HEAD:backend/onyx/db/tag.py:235:def delete_document_tags_for_documents__no_commit(
HEAD:backend/onyx/db/tag.py:238:    stmt = delete(Document__Tag).where(Document__Tag.document_id.in_(document_ids))
HEAD:backend/onyx/db/user_file.py:241:    DELETING liveness guard. A hard-deleted user CASCADE-drops its port attempts, so
HEAD:backend/onyx/db/users.py:955:        DocumentSet.user_id == user_to_delete.id
HEAD:backend/onyx/db/users.py:978:        DocumentSet__User.user_id == user_to_delete.id
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:89:        # remove document summary
HEAD:backend/onyx/document_index/document_metadata.py:3:Previously declared in the now-removed `onyx.document_index.interfaces` module.
HEAD:backend/onyx/document_index/interfaces_new.py:114:    allows us to only delete the extra "tail" chunks when the document has
HEAD:backend/onyx/document_index/interfaces_new.py:261:    Class must implement the ability to delete a document by a given unique
HEAD:backend/onyx/document_index/interfaces_new.py:275:        Hard deletes all of the chunks for the corresponding document in the
HEAD:backend/onyx/document_index/interfaces_new.py:496:    - Delete documents
HEAD:backend/onyx/document_index/opensearch/client.py:365:            Exception: There was an error deleting the search pipeline.
HEAD:backend/onyx/document_index/opensearch/client.py:648:            Exception: There was an error deleting the index.
HEAD:backend/onyx/document_index/opensearch/client.py:660:        logger.info("Deleting index %s.", self._index_name)
HEAD:backend/onyx/document_index/opensearch/client.py:1121:    def delete_document(self, document_chunk_id: str) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:1122:        """Deletes a document.
HEAD:backend/onyx/document_index/opensearch/client.py:1129:            Exception: There was an error deleting the document.
HEAD:backend/onyx/document_index/opensearch/client.py:1132:            True if the document was deleted, False if it was not found.
HEAD:backend/onyx/document_index/opensearch/client.py:1136:                "Trying to delete document chunk %s from index %s.",
HEAD:backend/onyx/document_index/opensearch/client.py:1140:            result = self._client.delete(index=self._index_name, id=document_chunk_id)
HEAD:backend/onyx/document_index/opensearch/client.py:1156:                    "Successfully deleted document chunk %s from index %s.",
HEAD:backend/onyx/document_index/opensearch/client.py:1180:        """Deletes documents by a query.
HEAD:backend/onyx/document_index/opensearch/client.py:1183:            query_body: The body of the query to delete documents by.
HEAD:backend/onyx/document_index/opensearch/client.py:1192:            Exception: There was an error deleting the documents.
HEAD:backend/onyx/document_index/opensearch/client.py:1195:            The number of documents deleted.
HEAD:backend/onyx/document_index/opensearch/client.py:1198:            "Trying to delete documents by query for index %s.",
HEAD:backend/onyx/document_index/opensearch/client.py:1213:                f"Failed to delete some or all of the documents for index {self._index_name}."
HEAD:backend/onyx/document_index/opensearch/client.py:1220:                f"Failed to delete some or all of the documents for index {self._index_name}. "
HEAD:backend/onyx/document_index/opensearch/client.py:1221:                f"{num_deleted} documents were deleted out of {num_processed} documents that were "
HEAD:backend/onyx/document_index/opensearch/client.py:1226:            "Successfully deleted %s documents by query for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:414:        Groups chunks by document ID and for each document, deletes existing
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:473:            if onyx_document.id not in deleted_doc_ids:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:477:                deleted_doc_ids.add(onyx_document.id)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:539:        """Deletes all chunks for a given document.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:543:        TODO(andrei): Consider implementing this method to delete on document
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:561:            "[OpenSearchDocumentIndex] Deleting document %s from index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:565:        query_body = DocumentQuery.delete_from_document_id_query(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:572:    def delete_port_written_chunks(self, document_ids: list[str]) -> int:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:586:            query_body = DocumentQuery.delete_port_written_chunks_query(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1068:    def delete(self, document_id: str, chunk_count: int | None = None) -> int:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1069:        total = self._primary.delete(document_id, chunk_count)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1071:            total += self._secondary.delete(document_id, chunk_count)
HEAD:backend/onyx/document_index/opensearch/port_copy.py:192:    def delete_port_written(self, document_ids: list[str]) -> int:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:196:        return self._future_index.delete_port_written_chunks(document_ids)
HEAD:backend/onyx/document_index/opensearch/search.py:259:    def delete_from_document_id_query(
HEAD:backend/onyx/document_index/opensearch/search.py:264:        Returns a final search query which deletes chunks from a given document
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:200:        SEMANTIC_IDENTIFIER: remove_invalid_unicode_chars(document.semantic_identifier),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:55:from onyx.document_index.vespa.deletion import delete_vespa_chunks
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:398:    """Determines which chunks need to be deleted during document reindexing.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:741:            chunks_to_delete = get_document_chunk_ids(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:747:            # Delete old Vespa documents.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:782:    def delete(self, document_id: str, chunk_count: int | None = None) -> int:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:798:            chunks_to_delete = get_document_chunk_ids(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1294:    def delete(self, document_id: str, chunk_count: int | None = None) -> int:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1295:        total = self._primary.delete(document_id, chunk_count)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1297:            total += self._secondary.delete(document_id, chunk_count)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:251:            # survives the rollback, so deleting the blob it points at would
HEAD:backend/onyx/file_store/gcs_file_store.py:208:            # survives the rollback, so deleting the blob it points at would
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:45:class UserFileDeletingSkip(ConnectorStopSignal):
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:46:    """A user file is DELETING at write time — skip the write, don't retry or fail. Subclasses
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:72:    if any(status == UserFileStatus.DELETING for _, status in rows):
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:73:        raise UserFileDeletingSkip("user file is being deleted; skipping index write")
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:278:            if user_file.status != UserFileStatus.DELETING:
HEAD:backend/onyx/indexing/indexing_pipeline.py:596:        # Blob deletes run only after Document.file_id is durable.
HEAD:backend/onyx/kg/clustering/clustering.py:451:        logger.error("Error deleting relationships: %s", e)
HEAD:backend/onyx/kg/clustering/clustering.py:460:        logger.error("Error deleting relationship types: %s", e)
HEAD:backend/onyx/kg/clustering/clustering.py:469:        logger.error("Error deleting entities: %s", e)
HEAD:backend/onyx/kg/clustering/clustering.py:470:    logger.info("Finished deleting all transferred staging entries")
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1172:        # Remove invalid Unicode characters (e.g., unpaired surrogates from malformed documents)
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:60:    logger.debug("Deleting potentially sensitive message %s", message.id)
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:68:        logger.exception("Unexpected error deleting message %s: %s", message.id, e)
HEAD:backend/onyx/redis/redis_connector.py:1:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/redis/redis_connector.py:4:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/redis/redis_connector.py:23:        self.prune = RedisConnectorPrune(tenant_id, cc_pair_id, self.redis)
HEAD:backend/onyx/redis/redis_connector.py:24:        self.delete = RedisConnectorDelete(tenant_id, cc_pair_id, self.redis)
HEAD:backend/onyx/redis/redis_connector_delete.py:24:class RedisConnectorDeletePayload(BaseModel):
HEAD:backend/onyx/redis/redis_connector_delete.py:29:class RedisConnectorDelete:
HEAD:backend/onyx/redis/redis_connector_delete.py:67:    def payload(self) -> RedisConnectorDeletePayload | None:
HEAD:backend/onyx/redis/redis_connector_delete.py:74:        payload = RedisConnectorDeletePayload.model_validate_json(fence_str)
HEAD:backend/onyx/redis/redis_connector_delete.py:78:    def set_fence(self, payload: RedisConnectorDeletePayload | None) -> None:
HEAD:backend/onyx/redis/redis_connector_delete.py:170:        taskset_key = f"{RedisConnectorDelete.TASKSET_PREFIX}_{id}"
HEAD:backend/onyx/redis/redis_connector_delete.py:176:        """Deletes all redis values for all connectors"""
HEAD:backend/onyx/redis/redis_connector_delete.py:177:        for key in r.scan_iter(RedisConnectorDelete.ACTIVE_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_delete.py:180:        for key in r.scan_iter(RedisConnectorDelete.TASKSET_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_delete.py:183:        for key in r.scan_iter(RedisConnectorDelete.FENCE_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:281:        """Deletes all redis values for all connectors"""
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:173:        """Deletes all redis values for all connectors"""
HEAD:backend/onyx/redis/redis_connector_prune.py:260:        """Deletes all redis values for all connectors"""
HEAD:backend/onyx/redis/redis_connector_utils.py:26:    if redis_connector.delete.fenced:
HEAD:backend/onyx/redis/redis_connector_utils.py:29:            task_name=redis_connector.delete.fence_key,
HEAD:backend/onyx/redis/redis_connector_utils.py:33:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/redis/redis_connector_utils.py:36:            task_name=redis_connector.delete.fence_key,
HEAD:backend/onyx/redis/redis_utils.py:1:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/redis/redis_utils.py:3:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/redis/redis_utils.py:14:    if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/server/documents/cc_pair.py:409:            # A group update tombstones the old row until the sync clears it, so
HEAD:backend/onyx/server/documents/cc_pair.py:499:    # Pause/resume only. Accepting DELETING here would let a scoped manager delete via
HEAD:backend/onyx/server/documents/cc_pair.py:900:        # this call, so a failed association rolls back rather than deleting it.
HEAD:backend/onyx/server/documents/connector.py:65:    delete_connector,
HEAD:backend/onyx/server/documents/connector.py:721:        prune_freq=connector.prune_freq,
HEAD:backend/onyx/server/documents/connector.py:975:    # NOTE: If the connector is deleting behind the scenes,
HEAD:backend/onyx/server/documents/connector.py:1624:        prune_freq=updated_connector.prune_freq,
```
Deletion is potentially multi-stage rather than a single storage operation.
## Search Index Deletion and Reindexing
Evidence lines: 279
```text
HEAD:backend/ee/onyx/db/document_set.py:136:def delete_document_set_privacy__no_commit(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:286:                # in sharepoint but it is removed from Azure AD. There is no actual documentation on this, but based on
HEAD:backend/ee/onyx/server/user_group/api.py:548:    detach_ids = set(request.removed_document_set_ids)
HEAD:backend/ee/onyx/server/user_group/models.py:150:    removed_document_set_ids: list[int]
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:100:            # expensive re-embed for non-paying tenants; it pauses and self-heals on un-gate.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:113:            # reclaim an index once its reindex has truly completed (a gated tenant's
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:114:            # deferred reindex never swaps / never drains, so it's never fetched).
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:38:from onyx.db.document_set import delete_document_set_cc_pair_relationship__no_commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:47:from onyx.db.index_attempt import delete_index_attempts, get_recent_attempts_for_cc_pair
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:504:            delete_document_set_cc_pair_relationship__no_commit(
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:25:    reindex: bool,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:69:            from_beginning=reindex,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:77:        # get processed before re-indexing of existing connectors
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:1:"""Celery task for executing a targeted reindex.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:7:`onyx.background.indexing.run_targeted_reindex`.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:19:from onyx.db.targeted_reindex import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:20:    get_index_attempts_for_targeted_reindex_job,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:21:    get_targeted_reindex_job,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:27:_TARGETED_REINDEX_SOFT_TIME_LIMIT = 60 * 30  # 30 minutes
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:28:_TARGETED_REINDEX_TIME_LIMIT = _TARGETED_REINDEX_SOFT_TIME_LIMIT + 60
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:31:def run_targeted_reindex(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:32:    targeted_reindex_job_id: int,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:35:    """Body of the targeted-reindex task. Lifted out of the @shared_task
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:38:    from onyx.background.indexing.run_targeted_reindex import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:46:            "targeted_reindex_job_id": targeted_reindex_job_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:52:        job = get_targeted_reindex_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:61:        attempts = get_index_attempts_for_targeted_reindex_job(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:62:            db_session, targeted_reindex_job_id
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:77:            target_rows = get_targets_for_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:81:                "Targeted reindex starting: %d cc_pair(s), %d target(s)",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:120:                        "cc_pair_id=%s connector does not support targeted reindex",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:129:                db_session, targeted_reindex_job_id, landed_keys
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:167:            log.exception("Targeted reindex task failed; marking job FAILED")
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:170:                job = get_targeted_reindex_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:172:                    attempts = get_index_attempts_for_targeted_reindex_job(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:173:                        db_session, targeted_reindex_job_id
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:191:        "Targeted reindex done: resolved=%d runtime_skipped=%d still_failing=%d",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:199:    name=OnyxCeleryTask.TARGETED_REINDEX_TASK,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:200:    soft_time_limit=_TARGETED_REINDEX_SOFT_TIME_LIMIT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:201:    time_limit=_TARGETED_REINDEX_TIME_LIMIT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:204:def targeted_reindex_task(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:207:    targeted_reindex_job_id: int,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:210:    run_targeted_reindex(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:211:        targeted_reindex_job_id=targeted_reindex_job_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:33:from onyx.background.celery.tasks.docprocessing.targeted_reindex_task import (  # noqa: F401  # registers @shared_task with celery
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:34:    targeted_reindex_task,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:204:                    # Synthetic attempts spawned by the targeted-reindex flow
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:207:                    IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:807:        reindex = False
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:810:            if cc_pair.indexing_trigger == IndexingMode.REINDEX:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:811:                reindex = True
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:828:            reindex,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1105:                        IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1165:                        IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1323:            # of index attempts since they were never deleted. After that, the number will be
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:225:    # Legacy FUTURE reindex indexes once, then stops so the swap can fire. A
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:1:"""Old-index reclamation: delete every reclaim-tracked PAST index after a reindex.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:76:# Per-DELETING-row wall-clock budget. On a whale (multi-tenant delete_by_query is
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:99:    """The new PRESENT index is healthy enough to serve before we delete the old one.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:147:            "Old-index reclaim %s -> SOAKING (index=%s, cc_pairs deleted=%d).",
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:197:            f"{search_settings.index_name}; refusing to delete it."
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:375:                    IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:1:"""Reindexing port machinery: the producer task plus the beat scheduler.
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:4:documents PRESENT -> FUTURE (re-embedded under the new model) and committing a
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:107:# bad/over-quota embed key, deleted model) so it doesn't recreate + re-embed every
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:307:        # the live PRESENT for a normal reindex.
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:569:    stuck failing at the same cursor isn't recreated (and re-embedded) every tick."""
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:605:    """The settings the port should populate. A normal reindex ports the FUTURE
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:616:        # source index can be reclaimed, and the reindex/vespa guards read "not
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:719:        # recreate + re-embed every tick. A progressing port (cursor advanced) has a
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:134:class PruneCallback(IndexingCallbackBase):
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:842:    # Orphan tags can only appear when the prune actually removed documents.
HEAD:backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py:37:        return self.index.delete(doc_id, chunk_count=chunk_count)
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:18:    delete_document_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:19:    delete_documents_complete,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:33:from onyx.db.relationships import delete_document_references_from_kg
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:93:    # chunks remain (the index delete failed), so the sweep still needs to clean them.
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:160:                # If a port is filling a target index, record this delete so the
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:162:                # create-only copy resurrects it. Commit before the index delete
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:216:                _ = retry_document_index.delete(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:232:                delete_document_references_from_kg(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:237:                delete_documents_complete(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:246:                delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:324:                    delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:409:                "being deleted; skipping indexing (the delete owns removal)"
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:482:    """Index one user file into the secondary (reindex-port target) index, re-embedding with
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:495:        # Don't resurrect a file already being deleted into the target index — the delete
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:551:    """During a reindex-port, also index a freshly-processed file into the secondary target so
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:923:                # Record the deletion before the index delete (below) so a racing port's
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:939:        # index resolves itself (Vespa fans out to find chunks, OpenSearch deletes
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:948:                retry_document_index.delete(
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:67:def delete_document_sync_taskset(r: TenantRedisClient) -> None:
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:43:    delete_document_set,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:439:            delete_document_set(document_set_row=document_set, db_session=db_session)
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:492:            # INSTANT reindex-port: the promoted primary is still backfilling. Flag it so
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:551:            # Reindex-port: doc missing from a still-populating index (FUTURE, or the
HEAD:backend/onyx/background/indexing/run_docfetching.py:514:        # get processed before re-indexing of existing connectors
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:1:"""Per-cc-pair fetch + index for the targeted-reindex flow.
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:3:The targeted-reindex celery task delegates the actual connector
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:8:`ConnectorFailure` inputs that the `Resolver.reindex` interface
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:11:FUTURE indexes both receive the reindex during a model swap).
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:15:reindex isn't supported yet for that source.
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:40:    TargetedReindexJobTarget,
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:42:from onyx.db.targeted_reindex import targets_to_connector_failures
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:66:class CCPairReindexResult:
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:107:    attempt's overall reindex run; it propagates into tracing /
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:193:    reindex flow. Without this, ancestor folders/spaces yielded by a
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:194:    Resolver during reindex would never land in Postgres or the redis
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:195:    cache, so KG ancestor lookups for newly-reindexed docs would fall
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:217:    targets: Sequence[TargetedReindexJobTarget],
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:221:) -> CCPairReindexResult:
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:226:    connector is instantiated once and its `reindex` output is fed
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:235:        # Shouldn't happen — create_targeted_reindex_job spawns one
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:241:        return CCPairReindexResult(set(), target_doc_ids, unsupported=False)
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:251:        return CCPairReindexResult(set(), target_doc_ids, unsupported=False)
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:266:        return CCPairReindexResult(set(), target_doc_ids, unsupported=True)
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:286:        for item in connector.reindex(
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:329:            context=f"targeted-reindex staging cleanup cc_pair={cc_pair_id}",
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:348:    return CCPairReindexResult(
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:356:    targets: Sequence[TargetedReindexJobTarget],
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:357:) -> dict[int, list[TargetedReindexJobTarget]]:
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:358:    by_cc_pair: dict[int, list[TargetedReindexJobTarget]] = defaultdict(list)
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:19:    Removes indexing-time content additions from chunks. Inverse of
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:89:        # remove document summary
HEAD:backend/onyx/document_index/disabled.py:20:from onyx.indexing.models import DocMetadataAwareIndexChunk
HEAD:backend/onyx/document_index/disabled.py:44:        chunks: Iterable[DocMetadataAwareIndexChunk],  # noqa: ARG002
HEAD:backend/onyx/document_index/document_index_utils.py:14:from onyx.indexing.models import DocMetadataAwareIndexChunk, MultipassConfig
HEAD:backend/onyx/document_index/document_index_utils.py:186:def get_uuid_from_chunk(chunk: DocMetadataAwareIndexChunk) -> uuid.UUID:
HEAD:backend/onyx/document_index/document_index_utils.py:196:    chunk: DocMetadataAwareIndexChunk,
HEAD:backend/onyx/document_index/document_metadata.py:3:Previously declared in the now-removed `onyx.document_index.interfaces` module.
HEAD:backend/onyx/document_index/factory.py:35:    The reindex port needs the lone index (to scan a PIT / call index_raw_chunks),
HEAD:backend/onyx/document_index/factory.py:151:    reindex-port target still backfilling (see OpenSearchIndexPair.update).
HEAD:backend/onyx/document_index/interfaces_new.py:14:from onyx.indexing.models import DocMetadataAwareIndexChunk
HEAD:backend/onyx/document_index/interfaces_new.py:113:    the chunks for a document and then re-index the document. This information
HEAD:backend/onyx/document_index/interfaces_new.py:152:    # Source creation time. Patched onto existing chunks without re-embedding when
HEAD:backend/onyx/document_index/interfaces_new.py:160:    secondary (FUTURE) index yet (e.g. mid reindex port). Carries the doc ids so
HEAD:backend/onyx/document_index/interfaces_new.py:228:        chunks: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/interfaces_new.py:236:        NOTE: When a document is reindexed/updated here and has gotten shorter,
HEAD:backend/onyx/document_index/opensearch/client.py:140:    surface this rather than fail (reindex port: doc not in FUTURE yet)."""
HEAD:backend/onyx/document_index/opensearch/client.py:162:# Rejection by an index/cluster block, e.g. the read_only_allow_delete block
HEAD:backend/onyx/document_index/opensearch/client.py:410:                docs_deleted=raw_index_info.get("docs.deleted", ""),
HEAD:backend/onyx/document_index/opensearch/client.py:651:            True if the index was deleted, False if it did not exist.
HEAD:backend/onyx/document_index/opensearch/client.py:664:        logger.info("Index %s deleted successfully.", self._index_name)
HEAD:backend/onyx/document_index/opensearch/client.py:686:          reindex).
HEAD:backend/onyx/document_index/opensearch/client.py:1009:                409 as benign. The reindex port uses this so a stale backlog
HEAD:backend/onyx/document_index/opensearch/client.py:1121:    def delete_document(self, document_chunk_id: str) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:1174:    def delete_by_query(
HEAD:backend/onyx/document_index/opensearch/client.py:1206:        result = self._client.delete_by_query(**params)
HEAD:backend/onyx/document_index/opensearch/client.py:1358:                OpenSearchUpdateError (FUTURE write during a reindex port).
HEAD:backend/onyx/document_index/opensearch/client.py:1427:                        # (FUTURE write during a reindex port)
HEAD:backend/onyx/document_index/opensearch/client.py:1810:        Vectors are excluded — the port re-embeds. If the PIT expired the scan
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:2:reindex. Deployment-mode-aware and idempotent — safe to re-run until it reports
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:8:from onyx.configs.app_configs import OLD_INDEX_RECLAIM_DELETE_BATCH_SIZE
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:30:    OLD_INDEX_RECLAIM_DELETE_BATCH_SIZE docs per call so a whale can't run past the
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:54:        deleted = client.delete_by_query(
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:55:            tenant_query, refresh=True, max_docs=OLD_INDEX_RECLAIM_DELETE_BATCH_SIZE
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:59:            "Reclaimed tenant %s from shared index %s: deleted=%s remaining=%s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:68:from onyx.indexing.models import DocMetadataAwareIndexChunk, Document
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:200:    chunk: DocMetadataAwareIndexChunk,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:265:        # DocMetadataAwareIndexChunk and instead using OpenSearchDocumentIndex's
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:401:                        "Failed to update mappings for index %s. This likely means a field type was changed which requires reindexing. Error: %s",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:409:        chunks: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:451:        current_chunks: list[DocMetadataAwareIndexChunk] = []
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:453:        def _flush_chunks(doc_chunks: list[DocMetadataAwareIndexChunk]) -> None:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:570:        return self._client.delete_by_query(query_body)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:590:            deleted += self._client.delete_by_query(query_body)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:975:        Used by the Vespa migration task and the reindex port. The reindex port
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1020:        # INSTANT reindex-port: primary is a promoted, still-backfilling index; see update().
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1063:        chunks: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/opensearch/port_copy.py:1:"""PRESENT -> FUTURE chunk copy for the reindex port.
HEAD:backend/onyx/document_index/opensearch/port_copy.py:4:scan, re-embeds them under the FUTURE model, and writes them to the FUTURE index
HEAD:backend/onyx/document_index/opensearch/port_copy.py:10:Contextual-RAG-ON AUGMENTATION re-embeds one document per page — its per-chunk LLM
HEAD:backend/onyx/document_index/opensearch/port_copy.py:28:from onyx.indexing.port_reembed import (
HEAD:backend/onyx/document_index/opensearch/port_copy.py:29:    AugmentationReembedContext,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:30:    ReembedStrategy,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:32:    select_reembed_strategy,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:44:) -> AugmentationReembedContext:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:54:        return AugmentationReembedContext(
HEAD:backend/onyx/document_index/opensearch/port_copy.py:69:    return AugmentationReembedContext(
HEAD:backend/onyx/document_index/opensearch/port_copy.py:85:    strategy: ReembedStrategy,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:88:    augmentation_ctx: AugmentationReembedContext | None = None,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:96:    should_abort brackets each re-embed and precedes each write — it aborts a cancelled
HEAD:backend/onyx/document_index/opensearch/port_copy.py:101:    # re-embed one doc per page so the unheartbeated per-chunk LLM re-enrichment is bounded
HEAD:backend/onyx/document_index/opensearch/port_copy.py:104:        strategy is ReembedStrategy.AUGMENTATION
HEAD:backend/onyx/document_index/opensearch/port_copy.py:123:        reembedded = re_embed_chunks(
HEAD:backend/onyx/document_index/opensearch/port_copy.py:130:        if not reembedded:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:136:        reembedded = [
HEAD:backend/onyx/document_index/opensearch/port_copy.py:137:            chunk.model_copy(update={"written_by_port": True}) for chunk in reembedded
HEAD:backend/onyx/document_index/opensearch/port_copy.py:143:        for i in range(0, len(reembedded), _PORT_WRITE_PAGE_SIZE):
HEAD:backend/onyx/document_index/opensearch/port_copy.py:146:            sub = reembedded[i : i + _PORT_WRITE_PAGE_SIZE]
HEAD:backend/onyx/document_index/opensearch/port_copy.py:161:    """Resolves the OpenSearch handles, reembed strategy, and embedder once so
HEAD:backend/onyx/document_index/opensearch/port_copy.py:172:        self._strategy = select_reembed_strategy(
HEAD:backend/onyx/document_index/opensearch/port_copy.py:188:        self._augmentation_ctx: AugmentationReembedContext | None = None
HEAD:backend/onyx/document_index/opensearch/port_copy.py:189:        if self._strategy is ReembedStrategy.AUGMENTATION:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:196:        return self._future_index.delete_port_written_chunks(document_ids)
HEAD:backend/onyx/document_index/opensearch/schema.py:178:    # lacks the field are never sent it). Only the reindex port sets it True, and only on
HEAD:backend/onyx/document_index/opensearch/schema.py:179:    # the freshly-created target index; the orphan sweep deletes by it.
HEAD:backend/onyx/document_index/opensearch/schema.py:420:                    # OPENSEARCH_TEXT_ANALYZER. Existing indices need reindexing
HEAD:backend/onyx/document_index/opensearch/search.py:269:        Intended to be supplied to the OpenSearch client's delete_by_query
HEAD:backend/onyx/document_index/vespa/deletion.py:45:        index_name: Name of the index to delete from.
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:62:from onyx.indexing.models import DocMetadataAwareIndexChunk
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:106:    chunks: list[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:142:    chunk: DocMetadataAwareIndexChunk,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:200:        SEMANTIC_IDENTIFIER: remove_invalid_unicode_chars(document.semantic_identifier),
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:331:    chunks: list[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:369:    chunk: DocMetadataAwareIndexChunk,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:370:) -> DocMetadataAwareIndexChunk:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:31:from onyx.configs.constants import KV_REINDEX_KEY
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:55:from onyx.document_index.vespa.deletion import delete_vespa_chunks
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:88:from onyx.indexing.models import DocMetadataAwareIndexChunk
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:241:    needs_reindexing = False
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:243:        needs_reindexing = cast(bool, kv_store.load(KV_REINDEX_KEY))
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:245:        logger.debug("Could not load the reindexing flag. Using ngrams")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:270:    schema = _add_ngrams_to_schema(schema) if needs_reindexing else schema
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:334:    needs_reindexing = False
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:336:        needs_reindexing = cast(bool, kv_store.load(KV_REINDEX_KEY))
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:338:        logger.debug("Could not load the reindexing flag. Using ngrams")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:372:        schema = _add_ngrams_to_schema(schema) if needs_reindexing else schema
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:398:    """Determines which chunks need to be deleted during document reindexing.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:400:    When a document is reindexed, it may have fewer chunks than before. This
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:411:        document_id: The Vespa-sanitized ID of the document being reindexed.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:413:            reindexing. None for documents using the legacy chunk ID system.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:415:            reindexing. This becomes the starting index for deletion since
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:616:        # is beneficial for indexing / updates / deletes since we have to make a
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:656:        chunks: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:681:            chunks_iter: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:684:        ) -> Generator[DocMetadataAwareIndexChunk, None, None]:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:726:                # previously existed and this is a reindex.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1288:        chunks: Iterable[DocMetadataAwareIndexChunk],
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:32:    DocMetadataAwareIndexChunk,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:294:    ) -> DocMetadataAwareIndexChunk:
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:295:        return DocMetadataAwareIndexChunk.from_index_chunk(
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:31:    DocMetadataAwareIndexChunk,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:136:        # Pre-seed every updatable_id with 0 so user files reindexing to zero
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:265:            # Secondary (reindex-port) write: chunks are written; the PRESENT pass owns the
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:330:    ) -> DocMetadataAwareIndexChunk:
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:331:        return DocMetadataAwareIndexChunk.from_index_chunk(
HEAD:backend/onyx/indexing/chunker.py:33:# Single source of truth — the reindex port reuses it to mirror indexing budgets.
HEAD:backend/onyx/indexing/indexing_pipeline.py:85:    DocMetadataAwareIndexChunk,
HEAD:backend/onyx/indexing/indexing_pipeline.py:363:    """Return the subset of documents that need to be re-indexed, plus their pre-computed hashes.
HEAD:backend/onyx/indexing/indexing_pipeline.py:414:        # check so we never suppress a legitimate re-index (see docstring).
HEAD:backend/onyx/indexing/indexing_pipeline.py:1557:                def _enriched_stream() -> Iterator[DocMetadataAwareIndexChunk]:
HEAD:backend/onyx/indexing/models.py:94:class DocMetadataAwareIndexChunk(IndexChunk):
HEAD:backend/onyx/indexing/models.py:132:    ) -> "DocMetadataAwareIndexChunk":
HEAD:backend/onyx/indexing/models.py:195:    switchover_type: SwitchoverType = SwitchoverType.REINDEX
HEAD:backend/onyx/indexing/models.py:252:    ) -> DocMetadataAwareIndexChunk: ...
HEAD:backend/onyx/indexing/port_reembed.py:1:"""Re-embed stored PRESENT chunks under FUTURE search settings without
HEAD:backend/onyx/indexing/port_reembed.py:7:  not): the embedding input is unchanged from indexing, so we re-embed the same
HEAD:backend/onyx/indexing/port_reembed.py:15:  text, re-glue under FUTURE settings, then re-embed. Two sub-cases keyed on the
HEAD:backend/onyx/indexing/port_reembed.py:18:      and re-embed the bare chunk (no LLM).
HEAD:backend/onyx/indexing/port_reembed.py:30:existing chunk is a benign 409) so we re-embed unconditionally rather than
HEAD:backend/onyx/indexing/port_reembed.py:70:CONTEXTUAL_RAG_REEMBED_TRACE_NAME = "contextual_rag_reembed"
HEAD:backend/onyx/indexing/port_reembed.py:73:class ReembedStrategy(enum.Enum):
HEAD:backend/onyx/indexing/port_reembed.py:74:    # Only the embedder changed; re-embed the same enriched text (tail swapped).
HEAD:backend/onyx/indexing/port_reembed.py:76:    # The contextual-RAG enrichment changed; rebuild the text, then re-embed.
HEAD:backend/onyx/indexing/port_reembed.py:81:class AugmentationReembedContext:
HEAD:backend/onyx/indexing/port_reembed.py:96:def select_reembed_strategy(
HEAD:backend/onyx/indexing/port_reembed.py:98:) -> ReembedStrategy:
HEAD:backend/onyx/indexing/port_reembed.py:117:        ReembedStrategy.AUGMENTATION
HEAD:backend/onyx/indexing/port_reembed.py:119:        else ReembedStrategy.MODEL_ONLY
HEAD:backend/onyx/indexing/port_reembed.py:253:            "Duplicate (document_id, chunk_index) identities among re-embedded "
HEAD:backend/onyx/indexing/port_reembed.py:270:    strategy: ReembedStrategy,
HEAD:backend/onyx/indexing/port_reembed.py:272:    augmentation_ctx: AugmentationReembedContext | None = None,
HEAD:backend/onyx/indexing/port_reembed.py:275:    """Re-embed stored chunks under a prebuilt strategy + embedder (no DB access).
HEAD:backend/onyx/indexing/port_reembed.py:283:    doc-text reconstruction needs it complete. FUTURE-RAG-off and MODEL_ONLY re-embed
HEAD:backend/onyx/indexing/port_reembed.py:289:    change it can count the tail differently and flip the threshold, re-embedding
HEAD:backend/onyx/indexing/port_reembed.py:294:    if strategy is ReembedStrategy.AUGMENTATION:
HEAD:backend/onyx/indexing/port_reembed.py:297:                "AUGMENTATION re-embed requires an AugmentationReembedContext"
HEAD:backend/onyx/indexing/port_reembed.py:299:        return _augmentation_reembed(stored_chunks, embedder, augmentation_ctx)
HEAD:backend/onyx/indexing/port_reembed.py:302:        raise ValueError("MODEL_ONLY re-embed requires the PRESENT tokenizer")
HEAD:backend/onyx/indexing/port_reembed.py:328:    # the AUGMENTATION path; keeps port_reembed's import surface light + cycle-free.
HEAD:backend/onyx/indexing/port_reembed.py:369:    MAX_METADATA_PERCENTAGE skip; see _semantic_tail_was_embedded), so the re-embedded
HEAD:backend/onyx/indexing/port_reembed.py:379:def _augmentation_reembed(
HEAD:backend/onyx/indexing/port_reembed.py:382:    ctx: AugmentationReembedContext,
HEAD:backend/onyx/indexing/port_reembed.py:432:                "contextual-RAG-on re-embed requires an LLM + tokenizer in the context"
HEAD:backend/onyx/indexing/port_reembed.py:439:            CONTEXTUAL_RAG_REEMBED_TRACE_NAME,
HEAD:backend/onyx/indexing/vector_db_insertion.py:15:from onyx.indexing.models import DocMetadataAwareIndexChunk
HEAD:backend/onyx/indexing/vector_db_insertion.py:33:    make_chunks: Callable[[], Iterable[DocMetadataAwareIndexChunk]],
HEAD:backend/onyx/indexing/vector_db_insertion.py:79:    def key(chunk: DocMetadataAwareIndexChunk) -> str:
```
Removing authoritative database state is not sufficient if searchable copies
remain in an index backend.
## Permission Revocation and Synchronization
Evidence lines: 600
```text
HEAD:backend/ee/onyx/access/access.py:11:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:24:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:141:"""Jobs / utils for kicking off doc permissions sync tasks."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:317:def try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:583:            callback = PermissionSyncCallback(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:630:                    f"Permission sync task timed out or stop signal detected: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:663:            f"Completed doc permission sync attempt {attempt_id}: {tasks_generated} docs, {docs_with_errors} errors"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:814:    # validate all existing permission sync jobs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1006:        self.last_tag: str = "PermissionSyncCallback.__init__"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:3:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:6:from onyx.db.connector import mark_cc_pair_as_external_group_synced
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:11:def _get_all_cc_pair_ids_to_mark_as_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:23:def mark_all_relevant_cc_pairs_as_external_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:28:    cc_pair_ids = _get_all_cc_pair_ids_to_mark_as_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:30:        mark_cc_pair_as_external_group_synced(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:14:    mark_all_relevant_cc_pairs_as_external_group_synced,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:26:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:59:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:62:    mark_external_group_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:63:    mark_external_group_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:93:    """Helper to mark an external group sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:95:        mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:218:            maybe_mark_tenant_active(tenant_id, caller="external_group_sync")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:562:        mark_external_group_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:563:        logger.info("Marked external group sync attempt %s as in progress", attempt_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:625:            mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:674:        mark_all_relevant_cc_pairs_as_external_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:6:    mark_user_group_as_synced,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:64:                mark_user_group_as_synced(db_session, user_group)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:80:                mark_user_group_as_synced(db_session=db_session, user_group=user_group)
HEAD:backend/ee/onyx/configs/app_configs.py:5:# Auto Permission Sync
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
HEAD:backend/ee/onyx/configs/app_configs.py:111:TEAMS_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:112:    os.environ.get("TEAMS_PERMISSION_DOC_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:119:SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:120:    os.environ.get("SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY") or 30 * 60
HEAD:backend/ee/onyx/configs/app_configs.py:124:SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY = int(
HEAD:backend/ee/onyx/configs/app_configs.py:125:    os.environ.get("SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY") or 5 * 60
HEAD:backend/ee/onyx/connectors/capability_applicability.py:10:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/connectors/capability_applicability.py:24:        applicable.add(CredentialCapability.DOC_PERMISSION_SYNC)
HEAD:backend/ee/onyx/connectors/capability_checks.py:20:    build_slack_doc_permission_sync_checks,
HEAD:backend/ee/onyx/connectors/capability_checks.py:26:_DOC_PERMISSION_SYNC_CHECKS_BY_SOURCE: dict[DocumentSource, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/connectors/capability_checks.py:27:    DocumentSource.SLACK: build_slack_doc_permission_sync_checks(),
HEAD:backend/ee/onyx/connectors/capability_checks.py:53:            display_name="Permission sync validation",
HEAD:backend/ee/onyx/connectors/capability_checks.py:81:        CredentialCapability.DOC_PERMISSION_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:82:            _DOC_PERMISSION_SYNC_CHECKS_BY_SOURCE.get(source, [])
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:21:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:35:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:56:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:58:    Two distinct permission surfaces are needed for SharePoint perm sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:86:    Override this if your connector needs to validate permissions syncing.
HEAD:backend/ee/onyx/db/document_set.py:21:def make_doc_set_private(
HEAD:backend/ee/onyx/db/mcp.py:9:def make_mcp_server_private(
HEAD:backend/ee/onyx/db/persona.py:13:    mark_persona_user_files_for_sync,
HEAD:backend/ee/onyx/db/persona.py:202:        mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/ee/onyx/db/scim.py:72:        Only one token is active at a time — this method automatically revokes
HEAD:backend/ee/onyx/db/scim.py:75:        # Revoke any currently active tokens
HEAD:backend/ee/onyx/db/scim.py:106:    def revoke_token(self, token_id: int) -> None:
HEAD:backend/ee/onyx/db/user_group.py:58:    recompute_permissions_for_group__no_commit,
HEAD:backend/ee/onyx/db/user_group.py:59:    recompute_user_permissions__no_commit,
HEAD:backend/ee/onyx/db/user_group.py:556:    recompute_user_permissions__no_commit(user_group.user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:848:    # effective_permissions is derived from group grants — so leaving can revoke the very
HEAD:backend/ee/onyx/db/user_group.py:901:    recompute_user_permissions__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:946:    recompute_user_permissions__no_commit([user_id], db_session)
HEAD:backend/ee/onyx/db/user_group.py:957:def revoke_group_manager(db_session: Session, user_id: UUID, group_id: int) -> None:
HEAD:backend/ee/onyx/db/user_group.py:1068:    # Recompute permissions for affected users now that their
HEAD:backend/ee/onyx/db/user_group.py:1070:    recompute_user_permissions__no_commit(affected_user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:1085:def mark_user_group_as_synced(db_session: Session, user_group: UserGroup) -> None:
HEAD:backend/ee/onyx/db/user_group.py:1119:class PermissionChange(NamedTuple):
HEAD:backend/ee/onyx/db/user_group.py:1135:) -> PermissionChange:
HEAD:backend/ee/onyx/db/user_group.py:1199:    recompute_permissions_for_group__no_commit(group_id, db_session)
HEAD:backend/ee/onyx/db/user_group.py:1212:    return PermissionChange(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:589:def remove_users_from_tenant(emails: list[str], tenant_id: str) -> None:
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:48:            # replace membership and revoke access for everyone omitted, so treat
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:73:                # instead of being replaced by a partial set (which would revoke
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:8:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:12:from ee.onyx.external_permissions.utils import generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:336:               When False (default), leave unprefixed (for permission sync path).
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:16:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:101:            # Check if repository has any permission changes
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:153:    Check if repository has any permission changes (visibility or team updates).
HEAD:backend/ee/onyx/external_permissions/github/utils.py:317:    add_prefix: When this method is called during the initial permission sync via the connector,
HEAD:backend/ee/onyx/external_permissions/github/utils.py:326:    # 2. Repo permissions can change without updating the repo's updated_at timestamp,
HEAD:backend/ee/onyx/external_permissions/github/utils.py:327:    #    forcing full permission syncs for all documents every time, which is inefficient.
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:4:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:13:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:120:                When invoked from doc_sync (permission sync), use the default (False)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:299:                   When False (default), leave unprefixed (for permission sync path).
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:33:Folder Permission Sync.
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:162:            # 401 indicates a customer-side credential issue (token revoked /
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:227:"""Individual Shared Drive / My Drive Permission Sync"""
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:262:        # Raise PermissionError so the caller marks the sync attempt as a
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:641:               When False (default), leave unprefixed (for permission sync path).
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:1:"""Entra ID group expansion for the Microsoft permission-sync paths.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:20:    from the database, typically used in permission synchronization workflows.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:37:    from the database, typically used in permission synchronization workflows.
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:2:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:48:    # Anonymous users can only access public (non-permission-synced) content
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:67:                "Skipping Slack permission sync for configured channels missing "
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:2:THIS IS NOT USEFUL OR USED FOR PERMISSION SYNCING
HEAD:backend/ee/onyx/external_permissions/sync_params.py:7:    BOX_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:8:    BOX_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:9:    CANVAS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:10:    CANVAS_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:11:    CONFLUENCE_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:12:    CONFLUENCE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:13:    DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:14:    GITHUB_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:15:    GITHUB_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:16:    GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:17:    JIRA_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:18:    JIRA_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:19:    SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:20:    SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:21:    SLACK_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:22:    TEAMS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:24:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/sync_params.py:73:    from ee.onyx.external_permissions.box.doc_sync import box_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:79:    from ee.onyx.external_permissions.box.group_sync import box_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:85:    from ee.onyx.external_permissions.canvas.doc_sync import canvas_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:91:    from ee.onyx.external_permissions.canvas.group_sync import canvas_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:97:    from ee.onyx.external_permissions.confluence.doc_sync import confluence_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:103:    from ee.onyx.external_permissions.confluence.group_sync import confluence_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:109:    from ee.onyx.external_permissions.github.doc_sync import github_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:115:    from ee.onyx.external_permissions.github.group_sync import github_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:121:    from ee.onyx.external_permissions.gmail.doc_sync import gmail_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:127:    from ee.onyx.external_permissions.google_drive.doc_sync import gdrive_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:133:    from ee.onyx.external_permissions.google_drive.group_sync import gdrive_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:139:    from ee.onyx.external_permissions.jira.doc_sync import jira_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:145:    from ee.onyx.external_permissions.jira.group_sync import jira_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:159:    from ee.onyx.external_permissions.sharepoint.doc_sync import sharepoint_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:165:    from ee.onyx.external_permissions.sharepoint.group_sync import sharepoint_group_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:171:    from ee.onyx.external_permissions.slack.doc_sync import slack_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:177:    from ee.onyx.external_permissions.teams.doc_sync import teams_doc_sync
HEAD:backend/ee/onyx/external_permissions/sync_params.py:221:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:226:            group_sync_frequency=GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:233:            doc_sync_frequency=CONFLUENCE_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:238:            group_sync_frequency=CONFLUENCE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:245:            doc_sync_frequency=JIRA_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:250:            group_sync_frequency=JIRA_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:257:            doc_sync_frequency=CANVAS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:262:            group_sync_frequency=CANVAS_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:269:            doc_sync_frequency=BOX_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:274:            group_sync_frequency=BOX_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:283:            doc_sync_frequency=SLACK_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:290:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:297:            doc_sync_frequency=GITHUB_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:302:            group_sync_frequency=GITHUB_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:314:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:323:            doc_sync_frequency=TEAMS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:330:            doc_sync_frequency=SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:335:            group_sync_frequency=SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:3:from ee.onyx.external_permissions.perm_sync_types import (
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/utils.py:4:from ee.onyx.external_permissions.perm_sync_types import FetchAllDocumentsIdsFunction
HEAD:backend/ee/onyx/server/documents/cc_pair.py:6:from ee.onyx.background.celery.tasks.doc_permission_syncing.tasks import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:7:    try_creating_permissions_sync_task,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:63:    """Triggers permissions sync on a particular cc_pair immediately"""
HEAD:backend/ee/onyx/server/documents/cc_pair.py:84:            "Permissions sync task already in progress.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:88:        "Permissions sync cc_pair=%s connector_id=%s credential_id=%s %s connector.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:94:    payload_id = try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:100:            "Permissions sync task creation failed.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:103:    logger.info("Permissions sync queued: cc_pair=%s id=%s", cc_pair_id, payload_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:107:        message="Successfully created the permissions sync task.",
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:386:    revokes all previous tokens. The raw token value is returned exactly once
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:84:        "read:content-details:confluence%20"  # for permission sync
HEAD:backend/ee/onyx/server/scim/api.py:70:    recompute_permissions_for_group__no_commit,
HEAD:backend/ee/onyx/server/scim/api.py:71:    recompute_user_permissions__no_commit,
HEAD:backend/ee/onyx/server/scim/api.py:295:    ``EXT_PERM_USER`` accounts are created by external permission sync and do
HEAD:backend/ee/onyx/server/scim/api.py:1365:    # Recompute permissions for initial members.
HEAD:backend/ee/onyx/server/scim/api.py:1366:    recompute_user_permissions__no_commit(member_uuids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1439:    # Recompute permissions for current members (batch) and removed members.
HEAD:backend/ee/onyx/server/scim/api.py:1440:    recompute_permissions_for_group__no_commit(group.id, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1442:    recompute_user_permissions__no_commit(removed_ids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1532:    # Recompute permissions for all users whose group membership changed.
HEAD:backend/ee/onyx/server/scim/api.py:1533:    recompute_user_permissions__no_commit(affected_uuids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1573:    # Capture member IDs before deletion so we can recompute their permissions.
HEAD:backend/ee/onyx/server/scim/api.py:1584:    # Recompute permissions for users who lost this group membership.
HEAD:backend/ee/onyx/server/scim/api.py:1585:    recompute_user_permissions__no_commit(affected_user_ids, db_session)
HEAD:backend/ee/onyx/server/scim/auth.py:121:        raise ScimAuthError(401, "SCIM token has been revoked")
HEAD:backend/ee/onyx/server/scim/models.py:363:# where admins create/revoke the bearer tokens that IdPs use to authenticate.
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:6:    remove_users_from_tenant,
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:71:        remove_users_from_tenant([user_to_delete.email], tenant_id)
HEAD:backend/ee/onyx/server/user_group/api.py:18:    revoke_group_manager,
HEAD:backend/ee/onyx/server/user_group/api.py:253:        AuditAction.USER_GROUP_PERMISSION_CHANGE,
HEAD:backend/ee/onyx/server/user_group/api.py:260:            "added": [permission.value for permission in change.added],
HEAD:backend/ee/onyx/server/user_group/api.py:261:            "removed": [permission.value for permission in change.removed],
HEAD:backend/ee/onyx/server/user_group/api.py:483:    # so a pre-lock read re-applies a share a concurrent save just revoked.
HEAD:backend/ee/onyx/server/user_group/api.py:639:            revoke_group_manager(db_session, request.user_id, user_group_id)
HEAD:backend/ee/onyx/utils/tier.py:173:    Auto-permission-sync requires connector-side permission tracking, which
HEAD:backend/onyx/access/access.py:127:    revoked as soon as the address belongs to somebody else.
HEAD:backend/onyx/access/access.py:149:            "onyx.external_permissions.sync_params",
HEAD:backend/onyx/access/models.py:56:        This effectively makes the document in question "private" or inaccessible to anyone else.
HEAD:backend/onyx/access/models.py:58:        This is especially helpful to use when you are performing permission-syncing, and some document's permissions aren't able
HEAD:backend/onyx/access/models.py:153:# Union type for elements that can have permissions synced
HEAD:backend/onyx/auth/invited_users.py:9:def remove_user_from_invited_users(email: str) -> int:
HEAD:backend/onyx/auth/users.py:71:from onyx.auth.invited_users import get_invited_users, remove_user_from_invited_users
HEAD:backend/onyx/auth/users.py:346:def remove_user_from_invited_users_after_login(
HEAD:backend/onyx/auth/users.py:352:        remove_user_from_invited_users(email)
HEAD:backend/onyx/auth/users.py:397:        # A permission-sync placeholder is not a member: appearing in a
HEAD:backend/onyx/auth/users.py:893:                remove_user_from_invited_users(user_create.email)
HEAD:backend/onyx/auth/users.py:1210:                remove_user_from_invited_users(replaced_email)
HEAD:backend/onyx/auth/users.py:1268:            remove_user_from_invited_users_after_login(user.email, user.id, tenant_id)
HEAD:backend/onyx/auth/users.py:1864:        # is incremented whenever the user logs out (or gets login revoked). Whenever
HEAD:backend/onyx/background/README.md:17:| Heavy                     | `apps/heavy.py`                | `connector_pruning`, `connector_doc_permissions_sync`, `connector_external_group_sync`, `csv_generation`, `sandbox`  |
HEAD:backend/onyx/background/celery/apps/app_base.py:48:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/app_base.py:91:def clear_revoked(state: Any, **kwargs: Any) -> dict[str, Any]:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:92:    """Remote command to wipe this worker's in-memory revoked-task set.
HEAD:backend/onyx/background/celery/apps/app_base.py:95:    cross-node entries don't expire — so after a mass-revoke it can pin at its 50k
HEAD:backend/onyx/background/celery/apps/app_base.py:97:    the fleet without restarting. Deliberate use only: revoked state is dropped.
HEAD:backend/onyx/background/celery/apps/app_base.py:99:    Intentionally ungated, like Celery's built-in shutdown/terminate/revoke control
HEAD:backend/onyx/background/celery/apps/app_base.py:104:    count = len(worker_state.revoked)
HEAD:backend/onyx/background/celery/apps/app_base.py:105:    worker_state.revoked.clear()
HEAD:backend/onyx/background/celery/apps/app_base.py:106:    task_logger.warning("clear_revoked: cleared %d revoked task ids", count)
HEAD:backend/onyx/background/celery/apps/app_base.py:107:    return {"ok": f"cleared {count} revoked task ids"}
HEAD:backend/onyx/background/celery/apps/app_base.py:248:    if task_id.startswith(RedisConnectorPermissionSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:251:            RedisConnectorPermissionSync.remove_from_taskset(
HEAD:backend/onyx/background/celery/apps/app_base.py:265:def on_task_revoked(
HEAD:backend/onyx/background/celery/apps/app_base.py:269:    """Drain the doc-sync taskset when a task is revoked/expired.
HEAD:backend/onyx/background/celery/apps/app_base.py:742:    "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:745:    "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/docfetching.py:24:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docfetching.py:83:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:84:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:86:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:25:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:86:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:87:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:89:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/heavy.py:15:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/heavy.py:66:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:67:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:69:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/light.py:21:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/light.py:72:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/light.py:73:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/light.py:75:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/light.py:76:    app_base.on_task_revoked(**kwargs)
HEAD:backend/onyx/background/celery/apps/light.py:164:            "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/primary.py:32:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/primary.py:44:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/primary.py:95:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/primary.py:96:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/primary.py:98:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/primary.py:200:    RedisConnectorPermissionSync.reset_all(r)
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:15:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:66:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:67:def on_task_revoked(sender: Any | None = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:69:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:39:CLOUD_DOC_PERMISSION_SYNC_MULTIPLIER_DEFAULT = 1.0
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:260:                "name": "check-for-doc-permissions-sync",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:261:                "task": OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:329:                # If the task was not dequeued in this time, revoke it.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:348:    "check-for-doc-permissions-sync",
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:48:from onyx.db.permission_sync_attempt import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:49:    delete_doc_permission_sync_attempts__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:50:    delete_external_group_permission_sync_attempts__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:87:def revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:104:                app.control.revoke(recent_index_attempts[0].celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:106:                    f"Revoked indexing task {recent_index_attempts[0].celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:112:        permissions_sync_payload = redis_connector.permissions.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:113:        if permissions_sync_payload and permissions_sync_payload.celery_task_id:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:114:            app.control.revoke(permissions_sync_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:116:                f"Revoked permissions sync task {permissions_sync_payload.celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:119:        task_logger.exception("Exception while revoking permissions sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:124:            app.control.revoke(prune_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:125:            task_logger.info(f"Revoked pruning task {prune_payload.celery_task_id}.")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:132:            app.control.revoke(external_group_sync_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:134:                f"Revoked external group sync task {external_group_sync_payload.celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:204:                    # on the first error, we set a stop signal and revoke the dependent tasks
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:210:                        # one time revoke of celery tasks
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:212:                        revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:493:            # permission sync attempts
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:494:            delete_doc_permission_sync_attempts__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:498:            delete_external_group_permission_sync_attempts__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:710:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:171:        "permissions_sync_queue_length": OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:958:    n_permissions_sync = celery_get_queue_length(
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:959:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1013:        f"permissions_sync={n_permissions_sync} "
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:394:        # skip pruning if doc permissions sync is running
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:397:                "try_creating_prune_generator_task: cc_pair=%s permissions sync running",
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:760:        # fanned out. If they were, reset would orphan them (it doesn't revoke
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:844:    # (mark_ccpair_as_pruned / update_sync_record_status commit internally),
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:859:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:862:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:908:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:24:    mark_document_as_synced,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:129:    (5) update document store entries to remove access associated with the
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:256:                mark_document_as_synced(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1180:        # Phase 3: short write session — mark sync as done
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:183:    maybe_mark_tenant_active(tenant_id, caller="vespa_sync")
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:39:    mark_document_as_synced,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:40:    mark_document_synced_secondary_pending,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:47:    mark_document_set_as_synced,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:444:            mark_document_set_as_synced(document_set_id, db_session)
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:572:            # doc's flag would never clear -> swap deadlock, so mark it synced.
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:578:                    mark_document_synced_secondary_pending(
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:582:                    mark_document_as_synced(
HEAD:backend/onyx/background/indexing/run_docfetching.py:964:                                "credentials or revoked access. Update its "
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:268:    include_permissions = cc_pair.access_type == AccessType.SYNC
HEAD:backend/onyx/chat/incognito.py:73:    authorize against a revoked setting for the cache TTL.
HEAD:backend/onyx/chat/process_message.py:1709:                    # will check for access before running. This instance should be removed
HEAD:backend/onyx/configs/constants.py:163:CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT = 3600  # 1 hour (in seconds)
HEAD:backend/onyx/configs/constants.py:468:    CONNECTOR_DOC_PERMISSIONS_SYNC = "connector_doc_permissions_sync"
HEAD:backend/onyx/configs/constants.py:519:    CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK = (
HEAD:backend/onyx/configs/constants.py:520:        "da_lock:check_connector_doc_permissions_sync_beat"
HEAD:backend/onyx/configs/constants.py:537:    CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX = (
HEAD:backend/onyx/configs/constants.py:538:        "da_lock:connector_doc_permissions_sync"
HEAD:backend/onyx/configs/constants.py:580:    BLOCK_VALIDATE_PERMISSION_SYNC_FENCES = (
HEAD:backend/onyx/configs/constants.py:581:        "signal:block_validate_permission_sync_fences"
HEAD:backend/onyx/configs/constants.py:634:    CHECK_FOR_DOC_PERMISSIONS_SYNC = "check_for_doc_permissions_sync"
HEAD:backend/onyx/configs/constants.py:673:    CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK = (
HEAD:backend/onyx/configs/constants.py:674:        "connector_permission_sync_generator_task"
HEAD:backend/onyx/connectors/README.md:91:  slim-doc pass (pruning / permission sync) if the connector has one. The slim pass must admit
HEAD:backend/onyx/connectors/bitbucket/connector.py:309:                                # Note: this is not actually used for permission sync yet, just pruning
HEAD:backend/onyx/connectors/box/connector.py:785:                    # Slim retrieval feeds permission sync and pruning; silently
HEAD:backend/onyx/connectors/box/connector.py:786:                    # dropping a subtree could revoke or leak access, so fail loudly.
HEAD:backend/onyx/connectors/box/connector.py:829:        """Verify the scopes required by Box permission group sync."""
HEAD:backend/onyx/connectors/box/connector.py:836:                    "The Box app cannot enumerate groups/users. Permission sync "
HEAD:backend/onyx/connectors/box/models.py:14:    # None outside permission-sync runs.
HEAD:backend/onyx/connectors/canvas/connector.py:967:            "Canvas permission sync requires course roster email visibility. "
HEAD:backend/onyx/connectors/capabilities.py:16:    DOC_PERMISSION_SYNC = "doc_permission_sync"
HEAD:backend/onyx/connectors/capability_checks/recorder.py:84:                display_name="Permission sync validation",
HEAD:backend/onyx/connectors/confluence/access.py:25:    permission-sync path, where upsert_document_external_perms adds the prefix.
HEAD:backend/onyx/connectors/confluence/access.py:101:    permission-sync path, where upsert_document_external_perms adds the prefix.
HEAD:backend/onyx/connectors/confluence/connector.py:1095:        """Yield slim docs for permission sync. Tries the fast path
HEAD:backend/onyx/connectors/confluence/connector.py:1112:                "(URL=%s); restarting Confluence permission sync with "
HEAD:backend/onyx/connectors/confluence/connector.py:1377:        (instead of 403) for non-admin callers, so a regular permission-sync
HEAD:backend/onyx/connectors/confluence/connector.py:1381:        connectors without permission sync don't have admin rights forced
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:222:        # failed", so we don't keep retrying every space-permissions sync.
HEAD:backend/onyx/connectors/connector_runner.py:162:                            "Connector does not support permission syncing"
HEAD:backend/onyx/connectors/gmail/connector.py:306:        # This is used to perform permission sync
HEAD:backend/onyx/connectors/google_drive/connector.py:34:    PermissionSyncContext,
HEAD:backend/onyx/connectors/google_drive/connector.py:559:        permission_sync_context: PermissionSyncContext | None = None,
HEAD:backend/onyx/connectors/google_drive/connector.py:594:            permission_sync_context: If provided, permissions will be fetched for hierarchy nodes.
HEAD:backend/onyx/connectors/google_drive/connector.py:595:                Contains google_domain and primary_admin_email needed for permission syncing.
HEAD:backend/onyx/connectors/google_drive/connector.py:597:                       When False (default), leave unprefixed (for permission sync path).
HEAD:backend/onyx/connectors/google_drive/connector.py:605:            if permission_sync_context
HEAD:backend/onyx/connectors/google_drive/connector.py:670:                if permission_sync_context:
HEAD:backend/onyx/connectors/google_drive/connector.py:673:                        permission_sync_context.google_domain,
HEAD:backend/onyx/connectors/google_drive/connector.py:1747:        permission_sync_context = (
HEAD:backend/onyx/connectors/google_drive/connector.py:1748:            PermissionSyncContext(
HEAD:backend/onyx/connectors/google_drive/connector.py:1797:                    permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:1806:                permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:1815:        permission_sync_context: PermissionSyncContext | None,
HEAD:backend/onyx/connectors/google_drive/connector.py:1831:                permission_sync_context=permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:1876:                    (retrieved_file, permission_sync_context),
HEAD:backend/onyx/connectors/google_drive/connector.py:1893:        permission_sync_context: PermissionSyncContext | None,
HEAD:backend/onyx/connectors/google_drive/connector.py:1903:                permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:2032:        permission_sync_context = (
HEAD:backend/onyx/connectors/google_drive/connector.py:2033:            PermissionSyncContext(
HEAD:backend/onyx/connectors/google_drive/connector.py:2054:            permission_sync_context=permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:2061:                (rf, permission_sync_context),
HEAD:backend/onyx/connectors/google_drive/connector.py:2089:            permission_sync_context = (
HEAD:backend/onyx/connectors/google_drive/connector.py:2090:                PermissionSyncContext(
HEAD:backend/onyx/connectors/google_drive/connector.py:2102:                permission_sync_context=permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:2113:                        permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/connector.py:2250:        Required for permission sync, which calls
HEAD:backend/onyx/connectors/google_drive/connector.py:2254:        steady stream of `PermissionError` log lines on every group-sync tick.
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:241:class PermissionSyncContext(BaseModel):
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:601:               When False (default), leave unprefixed (for permission sync path
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:620:            "onyx.external_permissions.google_drive.doc_sync",
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:642:    permission_sync_context: PermissionSyncContext | None,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:671:            permission_sync_context,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:719:    permission_sync_context: PermissionSyncContext | None,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:860:                company_domain=permission_sync_context.google_domain,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:864:                    creds, user_email=permission_sync_context.primary_admin_email
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:869:            if permission_sync_context
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:954:    permission_sync_context: PermissionSyncContext | None,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:964:            company_domain=permission_sync_context.google_domain,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:975:                user_email=permission_sync_context.primary_admin_email,
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:987:        if permission_sync_context
HEAD:backend/onyx/connectors/google_drive/file_retrieval.py:221:                   When False (default), leave unprefixed (for permission sync path
HEAD:backend/onyx/connectors/google_drive/file_retrieval.py:231:            "onyx.external_permissions.google_drive.doc_sync",
HEAD:backend/onyx/connectors/interfaces.py:84:        to do permission sync validation
HEAD:backend/onyx/connectors/interfaces.py:148:# permission syncing information for connected documents
HEAD:backend/onyx/connectors/interfaces.py:337:        If include_permissions is True, the documents will have permissions synced.
HEAD:backend/onyx/connectors/jira/access.py:30:                   When False (default), leave unprefixed (for permission sync path
HEAD:backend/onyx/connectors/jira/connector.py:574:                       When False (default), leave unprefixed (for permission sync path).
HEAD:backend/onyx/connectors/jira/connector.py:984:                        # Permission sync path - don't prefix, upsert_document_external_perms handles it
HEAD:backend/onyx/connectors/lumapps/connector.py:105:    ``CheckpointedConnectorWithPermSync`` and has no entry in the EE permission-sync
HEAD:backend/onyx/connectors/models.py:235:    # only filled in EE for connectors w/ permission sync enabled
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:152:grants and the ECA refresh token policy. Revoke the old grant, then authorize
HEAD:backend/onyx/connectors/sharepoint/connector.py:732:        Required for permission sync (RoleAssignments enumeration uses the
HEAD:backend/onyx/connectors/sharepoint/connector.py:748:                "Permission sync needs the SharePoint REST API, which only accepts "
HEAD:backend/onyx/connectors/sharepoint/connector.py:752:                "Certificate Authentication, or turn permission sync off."
HEAD:backend/onyx/connectors/sharepoint/connector.py:801:        Required for permission sync, which expands Azure AD groups attached to
HEAD:backend/onyx/connectors/slack/capability_checks.py:4:doc-permission-sync time by composing the same gateway operations production
HEAD:backend/onyx/connectors/slack/capability_checks.py:18:  DOC_PERMISSION_SYNC (channel enumeration for ACLs)
HEAD:backend/onyx/connectors/slack/capability_checks.py:19:- ``groups:read``      -> INDEXING (private channels), DOC_PERMISSION_SYNC
HEAD:backend/onyx/connectors/slack/capability_checks.py:24:- ``team:read``        -> INDEXING and DOC_PERMISSION_SYNC on Enterprise Grid
HEAD:backend/onyx/connectors/slack/capability_checks.py:27:  DOC_PERMISSION_SYNC (member-to-profile resolution)
HEAD:backend/onyx/connectors/slack/capability_checks.py:28:- ``users:read.email`` -> DOC_PERMISSION_SYNC (member-to-email resolution)
HEAD:backend/onyx/connectors/slack/capability_checks.py:117:    if error == "token_revoked":
HEAD:backend/onyx/connectors/slack/capability_checks.py:119:            f"Slack bot token has been revoked ({error})."
HEAD:backend/onyx/connectors/slack/capability_checks.py:635:    """Lists one channel under the permission-sync capability.
HEAD:backend/onyx/connectors/slack/capability_checks.py:645:            capability=CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/capability_checks.py:647:            display_name="Channels can be listed for permission sync",
HEAD:backend/onyx/connectors/slack/capability_checks.py:666:                "which permission sync requires to enumerate channels and "
HEAD:backend/onyx/connectors/slack/capability_checks.py:672:    """Lists one private channel under the permission-sync capability.
HEAD:backend/onyx/connectors/slack/capability_checks.py:681:            capability=CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/capability_checks.py:683:            display_name="Private channels can be listed for permission sync",
HEAD:backend/onyx/connectors/slack/capability_checks.py:702:                "The bot token cannot list private channels. Permission sync "
HEAD:backend/onyx/connectors/slack/capability_checks.py:706:                "access lists, so users removed from a private channel keep "
HEAD:backend/onyx/connectors/slack/capability_checks.py:716:            capability=CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/capability_checks.py:739:                "permission sync requires to map Slack members to Onyx users "
HEAD:backend/onyx/connectors/slack/capability_checks.py:757:                "permission sync cannot map Slack members to Onyx users. This "
HEAD:backend/onyx/connectors/slack/capability_checks.py:774:            capability=CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/capability_checks.py:798:                "(`conversations.members`), which permission sync requires to "
HEAD:backend/onyx/connectors/slack/capability_checks.py:810:                "profiles (`users.info`), which permission sync uses for "
HEAD:backend/onyx/connectors/slack/capability_checks.py:818:    Not required: without it, permission sync still runs but silently marks
HEAD:backend/onyx/connectors/slack/capability_checks.py:824:            capability=CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/capability_checks.py:850:                "Without it, permission sync silently marks every public "
HEAD:backend/onyx/connectors/slack/capability_checks.py:870:def build_slack_doc_permission_sync_checks() -> list[CapabilityCheck]:
HEAD:backend/onyx/connectors/slack/capability_checks.py:871:    """Returns the DOC_PERMISSION_SYNC capability checks for Slack.
HEAD:backend/onyx/connectors/slack/connector.py:1527:            elif slack_error == "token_revoked":
HEAD:backend/onyx/connectors/slack/connector.py:1529:                    f"Slack bot token has been revoked ({slack_error})."
HEAD:backend/onyx/connectors/slack/source_operations.py:602:            CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/source_operations.py:619:            CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/source_operations.py:656:            CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/source_operations.py:763:            CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/source_operations.py:780:            CredentialCapability.DOC_PERMISSION_SYNC,
HEAD:backend/onyx/connectors/slack/source_operations.py:802:        capabilities={CredentialCapability.DOC_PERMISSION_SYNC},
HEAD:backend/onyx/connectors/source_operations.py:254:                    "property is not allowed on a gateway; make it private or "
HEAD:backend/onyx/connectors/source_operations.py:265:                    "on a gateway; make it private or expose it as a stamped "
HEAD:backend/onyx/connectors/zoom/client.py:387:        make this connector fetch private addresses. The token goes only to the
HEAD:backend/onyx/db/api_key.py:22:from onyx.db.permissions import recompute_user_permissions__no_commit
HEAD:backend/onyx/db/api_key.py:218:    # (set_user_groups__no_commit recomputes permissions, so edits repair stale keys)
HEAD:backend/onyx/db/api_key.py:256:    recompute_user_permissions__no_commit(api_key_user.id, db_session)
HEAD:backend/onyx/db/connector.py:326:def mark_cc_pair_as_permissions_synced(
HEAD:backend/onyx/db/connector.py:340:def mark_cc_pair_as_external_group_synced(db_session: Session, cc_pair_id: int) -> None:
HEAD:backend/onyx/db/connector.py:348:    # The sync time can be marked after it ran because all group syncs
HEAD:backend/onyx/db/connector_credential_pair.py:218:        # pair — a permission-synced one has no group to sit in, which would lock its
HEAD:backend/onyx/db/connector_credential_pair.py:771:            "onyx.external_permissions.sync_params",
HEAD:backend/onyx/db/document.py:793:      automatic permission sync step)
HEAD:backend/onyx/db/document.py:907:        # from overwriting permissions set by permission sync jobs.
HEAD:backend/onyx/db/document.py:1088:def mark_document_as_synced(
HEAD:backend/onyx/db/document.py:1110:def mark_document_synced_secondary_pending(
HEAD:backend/onyx/db/document.py:1117:    mark_document_as_synced once a sync reaches FUTURE.
HEAD:backend/onyx/db/document.py:1119:    ``synced_as_of``: see mark_document_as_synced."""
HEAD:backend/onyx/db/document_set.py:273:def make_doc_set_private(
HEAD:backend/onyx/db/document_set.py:393:            "onyx.db.document_set", "make_doc_set_private"
HEAD:backend/onyx/db/document_set.py:464:            "onyx.db.document_set", "make_doc_set_private"
HEAD:backend/onyx/db/document_set.py:515:def mark_document_set_as_synced(document_set_id: int, db_session: Session) -> None:
HEAD:backend/onyx/db/document_set.py:587:        # mark the row as needing a sync, it will be deleted there since there
HEAD:backend/onyx/db/enums.py:86:class PermissionSyncStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:87:    """Status enum for permission sync attempts"""
HEAD:backend/onyx/db/enums.py:98:            PermissionSyncStatus.SUCCESS,
HEAD:backend/onyx/db/enums.py:99:            PermissionSyncStatus.COMPLETED_WITH_ERRORS,
HEAD:backend/onyx/db/enums.py:100:            PermissionSyncStatus.CANCELED,
HEAD:backend/onyx/db/enums.py:101:            PermissionSyncStatus.FAILED,
HEAD:backend/onyx/db/enums.py:107:            self == PermissionSyncStatus.SUCCESS
HEAD:backend/onyx/db/enums.py:108:            or self == PermissionSyncStatus.COMPLETED_WITH_ERRORS
HEAD:backend/onyx/db/enums.py:869:    # Recorded from the blocking validation at doc-permission-sync run start.
HEAD:backend/onyx/db/external_app.py:472:    skill to organization-wide viewer access; removed skills keep their current
HEAD:backend/onyx/db/hierarchy.py:754:    This is used during permission sync to update folder permissions
HEAD:backend/onyx/db/kg_temp_view.py:208:#             revoke_kg_relationships = text(
HEAD:backend/onyx/db/kg_temp_view.py:209:#                 f"REVOKE SELECT ON {kg_relationships_view_name} FROM {DB_READONLY_USER}"
HEAD:backend/onyx/db/kg_temp_view.py:211:#             db_drop_session.execute(revoke_kg_relationships)
HEAD:backend/onyx/db/kg_temp_view.py:218:#             revoke_kg_entities = text(
HEAD:backend/onyx/db/kg_temp_view.py:219:#                 f"REVOKE SELECT ON {kg_entity_view_name} FROM {DB_READONLY_USER}"
HEAD:backend/onyx/db/kg_temp_view.py:221:#             db_drop_session.execute(revoke_kg_entities)
HEAD:backend/onyx/db/mcp.py:197:def make_mcp_server_private(
HEAD:backend/onyx/db/mcp.py:204:    Raises if restriction is requested, mirroring `make_doc_set_private`."""
HEAD:backend/onyx/db/mcp.py:357:def remove_user_from_mcp_server(
HEAD:backend/onyx/db/mcp.py:360:    """Remove a user's access to an MCP server"""
HEAD:backend/onyx/db/models.py:104:    PermissionSyncStatus,
```
Permission revocation is security critical because stale indexed ACLs can
produce a temporary or persistent authorization gap.
## MCP and Tool Revocation
Evidence lines: 103
```text
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:108:    gate_enabled = False
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:122:                gate_enabled = False
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:82:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:993:        redis_connector: RedisConnector,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:999:        self.redis_connector: RedisConnector = redis_connector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:66:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:68:    RedisConnectorExternalGroupSync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:69:    RedisConnectorExternalGroupSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:310:        payload = RedisConnectorExternalGroupSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/db/scim.py:72:        Only one token is active at a time — this method automatically revokes
HEAD:backend/ee/onyx/db/scim.py:75:        # Revoke any currently active tokens
HEAD:backend/ee/onyx/db/scim.py:106:    def revoke_token(self, token_id: int) -> None:
HEAD:backend/ee/onyx/db/token_limit.py:57:    enabled_only: bool = False,
HEAD:backend/ee/onyx/db/user_group.py:848:    # effective_permissions is derived from group grants — so leaving can revoke the very
HEAD:backend/ee/onyx/db/user_group.py:957:def revoke_group_manager(db_session: Session, user_id: UUID, group_id: int) -> None:
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:48:            # replace membership and revoke access for everyone omitted, so treat
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:73:                # instead of being replaced by a partial set (which would revoke
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:162:            # 401 indicates a customer-side credential issue (token revoked /
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:53:    exclude_regex_enabled: bool = False,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:92:    include_regex_enabled: bool = False,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:94:    exclude_regex_enabled: bool = False,
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:35:            True if the feature is enabled for the user, False otherwise.
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:51:            return bool(is_enabled) if is_enabled is not None else False
HEAD:backend/ee/onyx/server/billing/models.py:60:    payment_method_enabled: bool = False
HEAD:backend/ee/onyx/server/documents/cc_pair.py:22:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/server/documents/cc_pair.py:80:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:159:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:386:    revokes all previous tokens. The raw token value is returned exactly once
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:394:            # A disconnected client only sets `cancelled`; a blocking
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:451:            # A disconnected client only sets `cancelled`; without this
HEAD:backend/ee/onyx/server/log_export/api.py:286:        # disconnects under ASGI >= 2.4), while a generator ``finally`` never
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:25:- LICENSE_ENFORCEMENT_ENABLED=false (default):
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:62:            db_session=db_session, enabled_only=True, ordered=False
HEAD:backend/ee/onyx/server/scim/auth.py:121:        raise ScimAuthError(401, "SCIM token has been revoked")
HEAD:backend/ee/onyx/server/scim/models.py:363:# where admins create/revoke the bearer tokens that IdPs use to authenticate.
HEAD:backend/ee/onyx/server/settings/api.py:28:    - LICENSE_ENFORCEMENT_ENABLED is False (legacy/rollout mode)
HEAD:backend/ee/onyx/server/settings/api.py:80:    If LICENSE_ENFORCEMENT_ENABLED is false, ee_features_enabled is set to True
HEAD:backend/ee/onyx/server/settings/api.py:117:                settings.ee_features_enabled = False
HEAD:backend/ee/onyx/server/settings/api.py:133:            settings.ee_features_enabled = False
HEAD:backend/ee/onyx/server/settings/api.py:138:        settings.ee_features_enabled = False
HEAD:backend/ee/onyx/server/tenants/proxy.py:370:    payment_method_enabled: bool = False
HEAD:backend/ee/onyx/server/user_group/api.py:18:    revoke_group_manager,
HEAD:backend/ee/onyx/server/user_group/api.py:483:    # so a pre-lock read re-applies a share a concurrent save just revoked.
HEAD:backend/ee/onyx/server/user_group/api.py:639:            revoke_group_manager(db_session, request.user_id, user_group_id)
HEAD:backend/ee/onyx/utils/tier.py:179:    LICENSE_ENFORCEMENT_ENABLED=False, treat the tenant as ENTERPRISE so
HEAD:backend/ee/onyx/utils/tier.py:196:    LICENSE_ENFORCEMENT_ENABLED=False passes, matching the sync-access
HEAD:backend/onyx/db/mcp.py:159:    after this server changes (enabled/disabled for craft, tools toggled, URL
HEAD:backend/onyx/db/mcp.py:311:def delete_mcp_server(server_id: int, db_session: Session) -> None:
HEAD:backend/onyx/db/mcp.py:312:    """Delete an MCP server and all associated tools (via CASCADE)"""
HEAD:backend/onyx/db/mcp.py:324:    logger.info("Successfully deleted MCP server %s and its tools", server_id)
HEAD:backend/onyx/db/mcp.py:357:def remove_user_from_mcp_server(
HEAD:backend/onyx/db/mcp.py:360:    """Remove a user's access to an MCP server"""
HEAD:backend/onyx/db/tools.py:36:    only_enabled: bool = False,
HEAD:backend/onyx/db/tools.py:73:    only_enabled: bool = False,
HEAD:backend/onyx/db/tools.py:124:    """The gate for every per-tool action (edit, delete, toggle, OAuth config). An MCP tool
HEAD:backend/onyx/db/tools.py:126:    there, a server's owner could delete it but not disable one of its tools."""
HEAD:backend/onyx/db/tools.py:289:def delete_tool__no_commit(tool_id: int, db_session: Session) -> None:
HEAD:backend/onyx/db/tools.py:296:    db_session.delete(tool)
HEAD:backend/onyx/server/features/mcp/api.py:51:    delete_mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:73:    delete_tool__no_commit,
HEAD:backend/onyx/server/features/mcp/api.py:1104:    """Disconnect the caller from an MCP server: remove their own connection
HEAD:backend/onyx/server/features/mcp/api.py:1114:    # Disconnecting revokes tool discovery for this user; reload their craft
HEAD:backend/onyx/server/features/mcp/api.py:1120:        message="Disconnected",
HEAD:backend/onyx/server/features/mcp/api.py:1549:            delete_tool__no_commit(db_tool.id, db)
HEAD:backend/onyx/server/features/mcp/api.py:1560:            delete_tool__no_commit(db_tool.id, db)
HEAD:backend/onyx/server/features/mcp/api.py:2161:    # Disable any existing tools that were not processed above
HEAD:backend/onyx/server/features/mcp/api.py:2210:    """Get all tools associated with MCP servers, including both enabled and disabled tools"""
HEAD:backend/onyx/server/features/mcp/api.py:2652:def delete_mcp_server_admin(
HEAD:backend/onyx/server/features/mcp/api.py:2659:    """Delete an MCP server and cascading related objects (tools, configs)."""
HEAD:backend/onyx/server/features/mcp/api.py:2675:        tools_to_delete = get_tools_by_mcp_server_id(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2683:            logger.debug("  - Tool to delete: %s (ID: %s)", tool.name, tool.id)
HEAD:backend/onyx/server/features/mcp/api.py:2686:        delete_mcp_server(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2701:                delete_tool__no_commit(tool.id, db_session)
HEAD:backend/onyx/server/features/mcp/oauth.py:934:            # revoked (RFC 6749) — discard the dead grant so the connection
HEAD:backend/onyx/server/features/tool/api.py:21:    delete_tool__no_commit,
HEAD:backend/onyx/server/features/tool/api.py:210:@admin_router.delete("/custom/{tool_id}", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/features/tool/api.py:211:def delete_custom_tool(
HEAD:backend/onyx/server/features/tool/api.py:220:        delete_tool__no_commit(tool_id, db_session)
HEAD:backend/onyx/server/features/tool/api.py:247:    """Enable or disable one or more tools.
HEAD:backend/onyx/server/features/tool/models.py:48:    default_enabled: bool = False
HEAD:backend/onyx/server/features/tool/models.py:77:            default_enabled=config.default_enabled if config else False,
HEAD:backend/onyx/server/features/tool/tool_visibility.py:19:    default_enabled: bool = False  # Whether tool is enabled by default
HEAD:backend/onyx/server/features/tool/tool_visibility.py:35:        default_enabled=False,
HEAD:backend/onyx/server/features/tool/tool_visibility.py:41:        default_enabled=False,
```
MCP/tool removal or disabling must converge across server records, discovered
tools, agent/persona configuration, credentials and active capability views.
## User and Group Lifecycle
Evidence lines: 213
```text
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/external_perm.py:29:def delete_user__ext_group_for_user__no_commit(
HEAD:backend/ee/onyx/db/external_perm.py:34:        delete(User__ExternalUserGroupId).where(
HEAD:backend/ee/onyx/db/external_perm.py:40:def delete_user__ext_group_for_cc_pair__no_commit(
HEAD:backend/ee/onyx/db/external_perm.py:45:        delete(User__ExternalUserGroupId).where(
HEAD:backend/ee/onyx/db/external_perm.py:56:        delete(PublicExternalUserGroup).where(
HEAD:backend/ee/onyx/db/external_perm.py:200:        delete(User__ExternalUserGroupId).where(
HEAD:backend/ee/onyx/db/external_perm.py:206:        delete(PublicExternalUserGroup).where(
HEAD:backend/ee/onyx/db/persona.py:50:    """Reconcile persona__user_group rows to ``desired_shares`` — delete missing, update
HEAD:backend/ee/onyx/db/persona.py:112:    owns_agent = can_delete_persona(acting_user, persona, db_session)
HEAD:backend/ee/onyx/db/scim.py:230:    def delete_user_mapping(self, mapping_id: int) -> None:
HEAD:backend/ee/onyx/db/scim.py:231:        """Delete a user mapping by ID. No-op if already deleted."""
HEAD:backend/ee/onyx/db/scim.py:289:    def deactivate_user(self, user: User) -> None:
HEAD:backend/ee/onyx/db/scim.py:594:    def delete_group(self, group: UserGroup) -> None:
HEAD:backend/ee/onyx/db/scim.py:735:            sa_delete(User__UserGroup).where(
HEAD:backend/ee/onyx/db/scim.py:741:    def delete_group_with_members(self, group: UserGroup) -> None:
HEAD:backend/ee/onyx/db/scim.py:744:            sa_delete(User__UserGroup).where(User__UserGroup.user_group_id == group.id)
HEAD:backend/ee/onyx/db/user_group.py:59:    recompute_user_permissions__no_commit,
HEAD:backend/ee/onyx/db/user_group.py:100:        db_session.delete(user__user_group_relationship)
HEAD:backend/ee/onyx/db/user_group.py:178:        db_session.delete(token_rate_limit__user_group_relationship)
HEAD:backend/ee/onyx/db/user_group.py:194:        db_session.delete(user_group__cc_pair_relationship)
HEAD:backend/ee/onyx/db/user_group.py:202:        delete(DocumentSet__UserGroup).where(
HEAD:backend/ee/onyx/db/user_group.py:556:    recompute_user_permissions__no_commit(user_group.user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:850:    if user.id in removed_user_ids and not _retains_group_admin_without(
HEAD:backend/ee/onyx/db/user_group.py:901:    recompute_user_permissions__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:946:    recompute_user_permissions__no_commit([user_id], db_session)
HEAD:backend/ee/onyx/db/user_group.py:1070:    recompute_user_permissions__no_commit(affected_user_ids, db_session)
HEAD:backend/ee/onyx/db/user_group.py:1077:def delete_user_group(db_session: Session, user_group: UserGroup) -> None:
HEAD:backend/ee/onyx/db/user_group.py:1081:    db_session.delete(user_group)
HEAD:backend/ee/onyx/db/user_group.py:1094:def delete_user_group_cc_pair_relationship__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:589:def remove_users_from_tenant(emails: list[str], tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:836:        # Delete the mapping for this user and tenant
HEAD:backend/ee/onyx/server/billing/api.py:86:# When set, billing requests to Stripe are disabled until user manually retries
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:17:from onyx.db.user_usage import DELETED_USER_EXPORT_EMAIL, UsageExportRow
HEAD:backend/ee/onyx/server/reporting/usage_report_data.py:147:        if row.email != DELETED_USER_EXPORT_EMAIL and not is_api_key_email_address(
HEAD:backend/ee/onyx/server/reporting/usage_report_pdf.py:630:            "System, deleted-user, and API-key spend is included in every total. "
HEAD:backend/ee/onyx/server/scim/api.py:71:    recompute_user_permissions__no_commit,
HEAD:backend/ee/onyx/server/scim/api.py:303:# Entra ID frees a soft-deleted user's UPN by prefixing the 32-hex objectId.
HEAD:backend/ee/onyx/server/scim/api.py:310:    Entra syncs objectId-prefixed values for soft-deleted users. Writing one
HEAD:backend/ee/onyx/server/scim/api.py:429:            dal.deactivate_user(user)
HEAD:backend/ee/onyx/server/scim/api.py:809:        # happens when we reactivate a deactivated user OR promote a shadow
HEAD:backend/ee/onyx/server/scim/api.py:1155:@scim_router.delete("/Users/{user_id}", status_code=204, response_model=None)
HEAD:backend/ee/onyx/server/scim/api.py:1156:def delete_user(
HEAD:backend/ee/onyx/server/scim/api.py:1161:    """Delete a user (RFC 7644 §3.6).
HEAD:backend/ee/onyx/server/scim/api.py:1163:    Deactivates the user and removes the SCIM mapping. Note that Okta
HEAD:backend/ee/onyx/server/scim/api.py:1181:    dal.deactivate_user(user)
HEAD:backend/ee/onyx/server/scim/api.py:1182:    dal.delete_user_mapping(mapping.id)
HEAD:backend/ee/onyx/server/scim/api.py:1366:    recompute_user_permissions__no_commit(member_uuids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1442:    recompute_user_permissions__no_commit(removed_ids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1533:    recompute_user_permissions__no_commit(affected_uuids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1585:    recompute_user_permissions__no_commit(affected_user_ids, db_session)
HEAD:backend/ee/onyx/server/scim/api.py:1590:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:87:    response.delete_cookie(FASTAPI_USERS_AUTH_COOKIE_NAME)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:626:async def delete_user_from_control_plane(tenant_id: str, email: str) -> None:
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:6:    remove_users_from_tenant,
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:8:from ee.onyx.server.tenants.provisioning import delete_user_from_control_plane
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:14:from onyx.db.users import delete_user_from_db, get_user_by_email
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:39:    user_to_delete = get_user_by_email(user_email.user_email, db_session)
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:45:    should_delete_tenant = num_admin_users == 1
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:52:            await delete_user_from_control_plane(tenant_id, user_to_delete.email)
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:56:                "Failed to delete user from control plane for tenant %s: %s",
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:66:    delete_user_from_db(user_to_delete, db_session)
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:71:        remove_users_from_tenant([user_to_delete.email], tenant_id)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:260:@router.delete("/user-group/{group_id}/rate-limit/{rate_limit_id}")
HEAD:backend/ee/onyx/server/user_group/api.py:23:from ee.onyx.db.user_group import delete_user_group as db_delete_user_group
HEAD:backend/ee/onyx/server/user_group/api.py:418:@router.delete("/admin/user-group/{user_group_id}")
HEAD:backend/ee/onyx/server/user_group/api.py:419:def delete_user_group(
HEAD:backend/ee/onyx/server/user_group/api.py:424:    assert_group_config_is_editable(db_session, user_group_id, "delete")
HEAD:backend/ee/onyx/server/user_group/api.py:438:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/user_group/api.py:453:            db_delete_user_group(db_session, user_group)
HEAD:backend/onyx/db/api_key.py:22:from onyx.db.permissions import recompute_user_permissions__no_commit
HEAD:backend/onyx/db/api_key.py:25:    delete_user_from_db,
HEAD:backend/onyx/db/api_key.py:256:    recompute_user_permissions__no_commit(api_key_user.id, db_session)
HEAD:backend/onyx/db/api_key.py:291:    delete_user_from_db(user_associated_with_key, db_session)
HEAD:backend/onyx/db/chat.py:350:def delete_all_chat_sessions_for_user(
HEAD:backend/onyx/db/connector_credential_pair.py:868:            "delete_user__ext_group_for_cc_pair__no_commit",
HEAD:backend/onyx/db/credentials.py:371:def delete_credential_for_user(
HEAD:backend/onyx/db/credentials.py:377:    """Delete a credential that belongs to a specific user"""
HEAD:backend/onyx/db/discord_bot.py:19:from onyx.db.users import delete_user_from_db__no_commit
HEAD:backend/onyx/db/discord_bot.py:145:    # Also delete the associated user
HEAD:backend/onyx/db/discord_bot.py:154:        delete_user_from_db__no_commit(api_key_user, db_session)
HEAD:backend/onyx/db/external_app.py:691:            delete(UserSkillPreference).where(
HEAD:backend/onyx/db/external_app.py:780:        delete(ExternalAppUserCredential).where(
HEAD:backend/onyx/db/external_app.py:789:        delete(UserSkillPreference).where(
HEAD:backend/onyx/db/input_prompt.py:224:def disable_input_prompt_for_user(
HEAD:backend/onyx/db/llm.py:1070:        delete(LLMProvider__UserGroup).where(
HEAD:backend/onyx/db/mcp.py:357:def remove_user_from_mcp_server(
HEAD:backend/onyx/db/mcp.py:506:def delete_user_connection_configs_for_server(
HEAD:backend/onyx/db/mcp.py:509:    """Delete all connection configs for a user on a specific server"""
HEAD:backend/onyx/db/mcp.py:525:def delete_all_user_connection_configs_for_server_no_commit(
HEAD:backend/onyx/db/mcp.py:528:    """Delete all user connection configs for a specific MCP server"""
HEAD:backend/onyx/db/models.py:4192:        ForeignKey("user_group.id", ondelete="SET NULL"), nullable=True
HEAD:backend/onyx/db/models.py:5038:        ForeignKey("user_group.id", ondelete="CASCADE"), nullable=False
HEAD:backend/onyx/db/models.py:5085:    # rows with `is_current=False` should be deleted when the UserGroup
HEAD:backend/onyx/db/models.py:5126:        ForeignKey("user_group.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:7046:        ForeignKey("user_group.id", ondelete="CASCADE"), unique=True, nullable=False
HEAD:backend/onyx/db/notification.py:134:    """Hard-delete every notification of this type for all users, so an
HEAD:backend/onyx/db/oauth_config.py:108:    Cascades delete to user tokens.
HEAD:backend/onyx/db/oauth_config.py:169:def delete_user_oauth_token(
HEAD:backend/onyx/db/oauth_config.py:172:    """Delete user's OAuth token for a specific configuration"""
HEAD:backend/onyx/db/oauth_config.py:179:    db_session.delete(user_token)
HEAD:backend/onyx/db/permissions.py:52:def recompute_user_permissions__no_commit(
HEAD:backend/onyx/db/permissions.py:176:    recompute_user_permissions__no_commit(user_ids, db_session)
HEAD:backend/onyx/db/persona.py:202:    # deleted agents keep their tool rows, and MANAGE_AGENTS skips _add_user_filters
HEAD:backend/onyx/db/persona.py:204:        select(Persona).where(Persona.deleted.is_(False)), user, get_editable=True
HEAD:backend/onyx/db/persona.py:422:        and can_delete_persona(user, persona, db_session)
HEAD:backend/onyx/db/persona.py:516:    return can_delete_persona(user, persona, db_session, user_group_ids=user_group_ids)
HEAD:backend/onyx/db/persona.py:582:    # delete/publish also gate on ADD_AGENTS (GATE 1); edit/share don't. Per-user, not per-row.
HEAD:backend/onyx/db/persona.py:742:    if not can_delete_persona(user, persona, db_session):
HEAD:backend/onyx/db/persona.py:972:def remove_user_from_persona_shares(
HEAD:backend/onyx/db/persona.py:1786:            user is None or can_delete_persona(user, existing_persona, db_session)
HEAD:backend/onyx/db/pinned_personas.py:75:        delete(User__PinnedPersona).where(User__PinnedPersona.user_id == user.id)
HEAD:backend/onyx/db/port_orphan_candidate.py:116:    """User-file analog of _for_document: record the deleted file under its user scope
HEAD:backend/onyx/db/scheduled_task.py:150:    """Fetch a non-deleted task owned by ``user_id``.
HEAD:backend/onyx/db/scheduled_task.py:173:    """Return all non-deleted tasks for a user, newest first."""
HEAD:backend/onyx/db/skill.py:530:            delete(UserSkillPreference).where(
HEAD:backend/onyx/db/skill.py:581:        db_session.execute(delete(Skill__User).where(Skill__User.skill_id == skill.id))
HEAD:backend/onyx/db/skill.py:591:            delete(Skill__UserGroup).where(Skill__UserGroup.skill_id == skill.id)
HEAD:backend/onyx/db/skill.py:623:            delete(Skill__User).where(
HEAD:backend/onyx/db/user_file.py:241:    DELETING liveness guard. A hard-deleted user CASCADE-drops its port attempts, so
HEAD:backend/onyx/db/user_preferences.py:26:def deactivate_user(
HEAD:backend/onyx/db/user_preferences.py:30:    """Deactivate a user by setting is_active to False."""
HEAD:backend/onyx/db/user_preferences.py:274:    # Delete existing rows not in the incoming set (scoped to user_id)
HEAD:backend/onyx/db/user_preferences.py:351:    """Update the disabled tools for a specific assistant for a specific user."""
HEAD:backend/onyx/db/user_usage.py:42:DELETED_USER_EXPORT_EMAIL = "(deleted user)"
HEAD:backend/onyx/db/user_usage.py:280:    # Deleted users/API keys leave user_id NULL but keep their spend. An inner
HEAD:backend/onyx/db/user_usage.py:283:    email_label = func.coalesce(User.email, DELETED_USER_EXPORT_EMAIL)
HEAD:backend/onyx/db/user_usage.py:399:            delete(UserUsage).where(
HEAD:backend/onyx/db/users.py:16:from onyx.auth.invited_users import remove_user_from_invited_users
HEAD:backend/onyx/db/users.py:39:from onyx.db.permissions import recompute_user_permissions__no_commit
HEAD:backend/onyx/db/users.py:188:    if not removed_user_ids or not group_grants_full_admin(db_session, group_id):
HEAD:backend/onyx/db/users.py:286:    Replaces the removed ``PATCH /manage/set-user-role``. Editing groups directly is
HEAD:backend/onyx/db/users.py:322:    recompute_user_permissions__no_commit(target.id, db_session)
HEAD:backend/onyx/db/users.py:639:            delete(User__ExternalUserGroupId).where(
HEAD:backend/onyx/db/users.py:643:        db_session.delete(shadow_user)
HEAD:backend/onyx/db/users.py:900:    from onyx.db.permissions import recompute_user_permissions__no_commit
HEAD:backend/onyx/db/users.py:902:    recompute_user_permissions__no_commit(user.id, db_session)
HEAD:backend/onyx/db/users.py:935:def delete_user_from_db__no_commit(
HEAD:backend/onyx/db/users.py:936:    user_to_delete: User,
HEAD:backend/onyx/db/users.py:944:        "delete_user__ext_group_for_user__no_commit",
HEAD:backend/onyx/db/users.py:986:    db_session.delete(user_to_delete)
HEAD:backend/onyx/db/users.py:989:def delete_user_from_db(
HEAD:backend/onyx/db/users.py:990:    user_to_delete: User,
HEAD:backend/onyx/db/users.py:993:    delete_user_from_db__no_commit(user_to_delete, db_session)
HEAD:backend/onyx/db/users.py:998:    remove_user_from_invited_users(user_to_delete.email)
HEAD:backend/onyx/db/users.py:1063:        delete(User__UserGroup).where(User__UserGroup.user_id == user_id)
HEAD:backend/onyx/db/users.py:1076:    recompute_user_permissions__no_commit(user_id, db_session)
HEAD:backend/onyx/server/documents/credential.py:15:    delete_credential_for_user,
HEAD:backend/onyx/server/documents/credential.py:108:    """Same as the user endpoint, but can delete any credential (not just the user's own)"""
HEAD:backend/onyx/server/documents/credential.py:428:    delete_credential_for_user(
HEAD:backend/onyx/server/documents/credential.py:453:    delete_credential_for_user(credential_id, user, db_session, True)
HEAD:backend/onyx/server/features/build/db/user_library.py:196:def delete_user_file(db_session: Session, doc: DbDocument) -> None:
HEAD:backend/onyx/server/features/build/db/user_library.py:197:    """Delete a user file's blob from the file store and its document record."""
HEAD:backend/onyx/server/features/build/sandbox/README.md:106:- **Disabled tools**: Resolved deployment-wide (not per-user) via the
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:530:    soft_delete_scheduled_task(db_session=db_session, task_id=task_id, user_id=user.id)
HEAD:backend/onyx/server/features/build/session/api.py:334:        success = session_manager.delete_session(session_id, user.id)
HEAD:backend/onyx/server/features/build/session/api.py:835:        deleted = session_manager.delete_file(session_id, user_id, path)
HEAD:backend/onyx/server/features/build/user_library/api.py:33:    delete_user_file,
HEAD:backend/onyx/server/features/build/user_library/api.py:490:    delete_user_file(db_session, doc)
HEAD:backend/onyx/server/features/input_prompt/api.py:8:    disable_input_prompt_for_user,
HEAD:backend/onyx/server/features/input_prompt/api.py:146:    Endpoint that marks a seed (or any) prompt as disabled for the current user,
HEAD:backend/onyx/server/features/input_prompt/api.py:149:    disable_input_prompt_for_user(input_prompt_id, user.id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:49:    delete_all_user_connection_configs_for_server_no_commit,
HEAD:backend/onyx/server/features/mcp/api.py:52:    delete_user_connection_configs_for_server,
HEAD:backend/onyx/server/features/mcp/api.py:1098:@router.delete("/user-credentials/{server_id}")
HEAD:backend/onyx/server/features/mcp/api.py:1099:def delete_user_credentials(
HEAD:backend/onyx/server/features/mcp/api.py:1112:    delete_user_connection_configs_for_server(server_id, user.email, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1706:    delete_all_user_connection_configs_for_server_no_commit(mcp_server.id, db_session)
HEAD:backend/onyx/server/features/oauth_config/api.py:15:    delete_user_oauth_token,
HEAD:backend/onyx/server/features/oauth_config/api.py:304:    Revoke (delete) the current user's OAuth token for a specific OAuth config.
HEAD:backend/onyx/server/features/oauth_config/api.py:307:        delete_user_oauth_token(oauth_config_id, user.id, db_session)
HEAD:backend/onyx/server/features/persona/api.py:51:    remove_user_from_persona_shares,
HEAD:backend/onyx/server/features/persona/api.py:106:                detail=f"User Knowledge is disabled. Cannot {action} assistant with user files or projects.",
HEAD:backend/onyx/server/features/persona/api.py:569:        remove_user_from_persona_shares(
HEAD:backend/onyx/server/features/projects/api.py:518:def delete_user_file(
HEAD:backend/onyx/server/features/projects/api.py:524:    """Delete a user file belonging to the current user.
HEAD:backend/onyx/server/features/projects/api.py:557:        logger.info("Queued in-process delete for user_file_id=%s", user_file.id)
HEAD:backend/onyx/server/features/projects/api.py:562:            OnyxCeleryTask.DELETE_SINGLE_USER_FILE,
HEAD:backend/onyx/server/features/projects/api.py:568:            "Triggered delete for user_file_id=%s with task_id=%s",
HEAD:backend/onyx/server/features/skill/api.py:938:def delete_current_user_skill(
HEAD:backend/onyx/server/federated/api.py:629:    # Find and delete the user's OAuth token
HEAD:backend/onyx/server/manage/users.py:19:    remove_user_from_invited_users,
HEAD:backend/onyx/server/manage/users.py:61:    deactivate_user,
HEAD:backend/onyx/server/manage/users.py:83:    delete_user_from_db,
HEAD:backend/onyx/server/manage/users.py:692:                    "onyx.db.user_tenant_mapping", "remove_users_from_tenant", None
HEAD:backend/onyx/server/manage/users.py:749:            "onyx.db.user_tenant_mapping", "remove_users_from_tenant", None
HEAD:backend/onyx/server/manage/users.py:751:    number_of_invited_users = remove_user_from_invited_users(user_email.user_email)
HEAD:backend/onyx/server/manage/users.py:768:@router.patch("/manage/admin/deactivate-user", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/manage/users.py:769:def deactivate_user_api(
HEAD:backend/onyx/server/manage/users.py:779:    user_to_deactivate = get_user_by_email(
HEAD:backend/onyx/server/manage/users.py:787:        logger.warning("%s is already deactivated", user_to_deactivate.email)
HEAD:backend/onyx/server/manage/users.py:789:    deactivate_user(user_to_deactivate, db_session)
HEAD:backend/onyx/server/manage/users.py:808:@router.delete("/manage/admin/delete-user", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/manage/users.py:809:async def delete_user(
HEAD:backend/onyx/server/manage/users.py:816:    user_to_delete = get_user_by_email(
HEAD:backend/onyx/server/manage/users.py:823:        logger.warning("%s must be deactivated before deleting", user_to_delete.email)
HEAD:backend/onyx/server/manage/users.py:829:    deleted_user_id = str(user_to_delete.id)
HEAD:backend/onyx/server/manage/users.py:830:    deleted_user_email = user_to_delete.email
HEAD:backend/onyx/server/manage/users.py:838:            "onyx.db.user_tenant_mapping", "remove_users_from_tenant", None
HEAD:backend/onyx/server/manage/users.py:840:        delete_user_from_db(user_to_delete, db_session)
HEAD:backend/onyx/server/manage/users.py:841:        logger.info("Deleted user %s", user_to_delete.email)
HEAD:backend/onyx/server/manage/users.py:848:            resource_id=deleted_user_id,
HEAD:backend/onyx/server/manage/users.py:849:            extra={"target_email": deleted_user_email},
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:68:    OnyxCeleryQueues.USER_FILE_DELETE: "user_file_delete",
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:67:    delete_all_chat_sessions_for_user,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:673:        delete_all_chat_sessions_for_user(user=user, db_session=db_session)
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:677:        _teardown_incognito_after_delete(incognito_id, user.id, db_session)
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:710:        _teardown_incognito_after_delete(session_id, user.id, db_session)
HEAD:backend/onyx/server/settings/store.py:8:    DISABLE_USER_KNOWLEDGE,
HEAD:backend/onyx/server/settings/store.py:87:    if DISABLE_USER_KNOWLEDGE:
```
Group and permission changes can affect multiple downstream authorization
decisions.
## Chat / Session Deletion and Retention
Evidence lines: 284
```text
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:11:_HOOK_EXECUTION_LOG_RETENTION_DAYS: int = 30
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:25:                max_age_days=_HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:32:                    _HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:71:    """Deletes log-export artifacts past their retention window."""
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:5:from ee.onyx.background.celery_utils import should_perform_chat_ttl_check
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:8:    CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:9:    CHAT_TTL_DELETE_BATCH_SIZE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:15:from onyx.db.chat import delete_chat_session, get_chat_sessions_older_than
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:49:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:63:    retention_limit_days: float,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:73:    Each run hard-deletes at most ``CHAT_TTL_DELETE_BATCH_SIZE`` of the *oldest*
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:87:    fails to delete is retried on every run. If the oldest ``CHAT_TTL_DELETE_BATCH_SIZE``
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:88:    sessions can never be deleted, the chain loops on them indefinitely (across
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:97:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:98:        [chain_token, str(CELERY_CHAT_TTL_DELETE_TASK_EXPIRES)],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:104:        old_chat_sessions = get_chat_sessions_older_than(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:105:            retention_limit_days, db_session, limit=CHAT_TTL_DELETE_BATCH_SIZE
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:111:                delete_chat_session(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:127:    if len(old_chat_sessions) == CHAT_TTL_DELETE_BATCH_SIZE:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:132:                    "retention_limit_days": retention_limit_days,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:136:                queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:138:                expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:155:    """Start a chat-retention cleanup chain if one isn't already running.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:163:    retention_limit_days = settings.maximum_chat_retention_days
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:165:        if not should_perform_chat_ttl_check(retention_limit_days, db_session):
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:167:    if retention_limit_days is None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:175:        OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:178:        ex=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:186:                "retention_limit_days": retention_limit_days,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:190:            queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:192:            expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery_utils.py:3:from ee.onyx.background.task_name_builders import name_chat_ttl_task
HEAD:backend/ee/onyx/background/celery_utils.py:10:def should_perform_chat_ttl_check(
HEAD:backend/ee/onyx/background/celery_utils.py:11:    retention_limit_days: float | None, db_session: Session
HEAD:backend/ee/onyx/background/celery_utils.py:14:    if not retention_limit_days:
HEAD:backend/ee/onyx/background/celery_utils.py:17:    task_name = name_chat_ttl_task(retention_limit_days)
HEAD:backend/ee/onyx/background/task_name_builders.py:8:def name_chat_ttl_task(
HEAD:backend/ee/onyx/background/task_name_builders.py:9:    retention_limit_days: float,
HEAD:backend/ee/onyx/background/task_name_builders.py:12:    return f"chat_ttl_{retention_limit_days}_days"
HEAD:backend/ee/onyx/db/document_set.py:127:        db_session.delete(existing[document_set.id])
HEAD:backend/ee/onyx/db/license.py:162:        db_session.delete(existing)
HEAD:backend/ee/onyx/db/persona.py:64:            db_session.delete(row)
HEAD:backend/ee/onyx/db/scim.py:236:        self._session.delete(mapping)
HEAD:backend/ee/onyx/db/scim.py:545:        self._session.delete(mapping)
HEAD:backend/ee/onyx/db/scim.py:596:        self._session.delete(group)
HEAD:backend/ee/onyx/db/scim.py:746:        self._session.delete(group)
HEAD:backend/ee/onyx/db/standard_answer.py:150:    db_session.delete(category)
HEAD:backend/ee/onyx/db/user_group.py:100:        db_session.delete(user__user_group_relationship)
HEAD:backend/ee/onyx/db/user_group.py:178:        db_session.delete(token_rate_limit__user_group_relationship)
HEAD:backend/ee/onyx/db/user_group.py:194:        db_session.delete(user_group__cc_pair_relationship)
HEAD:backend/ee/onyx/db/user_group.py:1081:    db_session.delete(user_group)
HEAD:backend/ee/onyx/db/user_group.py:1116:    db_session.execute(delete_stmt)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:498:            db_session.delete(mapping)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:603:                db_session.delete(mapping)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:790:                        db_session.delete(candidate)
HEAD:backend/ee/onyx/server/log_export/storage.py:43:LOG_EXPORT_RETENTION = timedelta(hours=12)
HEAD:backend/ee/onyx/server/log_export/storage.py:319:    """Deletes log-export artifacts older than ``LOG_EXPORT_RETENTION``.
HEAD:backend/ee/onyx/server/log_export/storage.py:324:    cutoff = datetime.now(tz=timezone.utc) - LOG_EXPORT_RETENTION
HEAD:backend/ee/onyx/server/query_history/api.py:185:        raise ValueError("Chat session does not exist or has been deleted")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:317:                    db_session.delete(available_tenant)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:635:        async with session.delete(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:718:                db_session.delete(available_tenant)
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:65:    db_session.expunge(user_to_delete)
HEAD:backend/ee/onyx/server/user_group/api.py:424:    assert_group_config_is_editable(db_session, user_group_id, "delete")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:571:                db_session.delete(connector)
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:35:    OLD_INDEX_RETENTION_HOURS,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:155:    """SOAKING: wait out the retention window, then require the new PRESENT index can
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:160:    if datetime.now(timezone.utc) - anchor < timedelta(hours=OLD_INDEX_RETENTION_HOURS):
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:179:        "chat_ttl_deletion_queue_length": OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:977:                db_session.delete(user_file)
HEAD:backend/onyx/cache/postgres_backend.py:249:            session.execute(delete(CacheStore).where(CacheStore.key == key))
HEAD:backend/onyx/cache/postgres_backend.py:342:                        session.delete(row)
HEAD:backend/onyx/chat/incognito.py:170:    Only Bifrost honors a per-request retention switch. FULL_HISTORY sends
HEAD:backend/onyx/chat/incognito.py:196:    deployment-wide param must not re-enable provider-side retention.
HEAD:backend/onyx/chat/incognito.py:217:    """The per-provider retention suppression a turn under this mode carries.
HEAD:backend/onyx/chat/incognito.py:220:    Bedrock, Nebius, local servers) get an empty policy: their retention is an
HEAD:backend/onyx/chat/incognito.py:248:    The file record carries the session stamp, so deleting the blob deletes the
HEAD:backend/onyx/chat/incognito_context.py:233:    client.set(_context_key(chat_session_id), _TOMBSTONE, ex=_TOMBSTONE_TTL_SECONDS)
HEAD:backend/onyx/chat/process_message.py:1772:            # session on its record, which is what teardown deletes by.
HEAD:backend/onyx/chat/save_chat.py:153:                db_session.delete(tool_call_obj)
HEAD:backend/onyx/chat/stream_buffer.py:21:    CHAT_STREAM_BUFFER_DONE_TTL_S,
HEAD:backend/onyx/chat/stream_buffer.py:23:    CHAT_STREAM_BUFFER_TTL_S,
HEAD:backend/onyx/chat/stream_buffer.py:118:                self._write_meta(CHAT_STREAM_BUFFER_TTL_S)
HEAD:backend/onyx/chat/stream_buffer.py:130:                ex=CHAT_STREAM_BUFFER_TTL_S,
HEAD:backend/onyx/chat/stream_buffer.py:134:            self._write_meta(CHAT_STREAM_BUFFER_TTL_S)
HEAD:backend/onyx/chat/stream_buffer.py:144:                self._write_meta(CHAT_STREAM_BUFFER_TTL_S)
HEAD:backend/onyx/chat/stream_buffer.py:175:            self._write_meta(CHAT_STREAM_BUFFER_DONE_TTL_S)
HEAD:backend/onyx/chat/stream_buffer.py:179:                    CHAT_STREAM_BUFFER_DONE_TTL_S,
HEAD:backend/onyx/configs/app_configs.py:1116:OLD_INDEX_RETENTION_HOURS = _non_negative_int_env("OLD_INDEX_RETENTION_HOURS", 24)
HEAD:backend/onyx/configs/app_configs.py:1501:# Finer grained chunking for more detail retention
HEAD:backend/onyx/configs/chat_configs.py:59:CHAT_STREAM_BUFFER_TTL_S = int(os.environ.get("CHAT_STREAM_BUFFER_TTL_S") or 3600)
HEAD:backend/onyx/configs/chat_configs.py:60:# Retention after the run is done.
HEAD:backend/onyx/configs/chat_configs.py:61:CHAT_STREAM_BUFFER_DONE_TTL_S = int(
HEAD:backend/onyx/configs/chat_configs.py:62:    os.environ.get("CHAT_STREAM_BUFFER_DONE_TTL_S") or 600
HEAD:backend/onyx/configs/constants.py:233:# Chat-retention (TTL) cleanup tuning. Each delete task removes the oldest
HEAD:backend/onyx/configs/constants.py:234:# CHAT_TTL_DELETE_BATCH_SIZE expired sessions and chains the next task, so
HEAD:backend/onyx/configs/constants.py:237:CHAT_TTL_DELETE_BATCH_SIZE = 100
HEAD:backend/onyx/configs/constants.py:240:CELERY_CHAT_TTL_DELETE_TASK_EXPIRES = 60 * 60  # 1 hour (in seconds)
HEAD:backend/onyx/configs/constants.py:476:    # Chat retention (TTL) hard-deletion queue, consumed by the light worker.
HEAD:backend/onyx/configs/constants.py:478:    CHAT_TTL_DELETION = "chat_ttl_deletion"
HEAD:backend/onyx/configs/constants.py:531:    # In-flight marker: set while a chat-TTL cleanup chain is active (spanning
HEAD:backend/onyx/configs/constants.py:533:    CHAT_TTL_CHAIN_ACTIVE = "da_lock:chat_ttl_chain_active"
HEAD:backend/onyx/configs/constants.py:696:    # chat retention
HEAD:backend/onyx/configs/constants.py:715:    # Hook execution log retention
HEAD:backend/onyx/connectors/slack/utils.py:147:                # Common per-message condition: user was deleted, workspace
HEAD:backend/onyx/context/search/federated/slack_search.py:1075:    # carries request policy (e.g. incognito retention headers) that a freshly
HEAD:backend/onyx/db/api_key.py:287:    db_session.delete(existing_api_key)
HEAD:backend/onyx/db/chat.py:79:    if not include_deleted and chat_session.deleted:
HEAD:backend/onyx/db/chat.py:80:        raise ValueError("Chat session has been deleted")
HEAD:backend/onyx/db/chat.py:151:        stmt = stmt.where(ChatSession.deleted == deleted)
HEAD:backend/onyx/db/chat.py:207:        db_session.delete(doc)
HEAD:backend/onyx/db/chat.py:211:def delete_messages_and_files_from_chat_session(
HEAD:backend/onyx/db/chat.py:233:    # Delete ChatMessage records - CASCADE constraints will automatically handle:
HEAD:backend/onyx/db/chat.py:236:        delete(ChatMessage).where(ChatMessage.chat_session_id == chat_session_id)
HEAD:backend/onyx/db/chat.py:332:    if chat_session.deleted:
HEAD:backend/onyx/db/chat.py:351:    user: User, db_session: Session, hard_delete: bool = HARD_DELETE_CHATS
HEAD:backend/onyx/db/chat.py:363:            delete_messages_and_files_from_chat_session(chat_session.id, db_session)
HEAD:backend/onyx/db/chat.py:379:def delete_chat_session(
HEAD:backend/onyx/db/chat.py:393:    if chat_session.deleted and not include_deleted:
HEAD:backend/onyx/db/chat.py:397:        delete_messages_and_files_from_chat_session(chat_session_id, db_session)
HEAD:backend/onyx/db/chat.py:398:        db_session.execute(delete(ChatSession).where(ChatSession.id == chat_session_id))
HEAD:backend/onyx/db/chat.py:403:        chat_session.deleted = True
HEAD:backend/onyx/db/chat.py:408:def get_chat_sessions_older_than(
HEAD:backend/onyx/db/chat_search.py:43:            stmt = stmt.where(ChatSession.deleted.is_(False))
HEAD:backend/onyx/db/chat_search.py:66:        base_conditions.append(ChatSession.deleted.is_(False))
HEAD:backend/onyx/db/connector.py:165:            success=True, message="Connector was already deleted", data=connector_id
HEAD:backend/onyx/db/connector.py:168:    db_session.delete(connector)
HEAD:backend/onyx/db/connector.py:170:        success=True, message="Connector deleted successfully", data=connector_id
HEAD:backend/onyx/db/connector_credential_pair.py:873:        db_session.delete(association)
HEAD:backend/onyx/db/credentials.py:345:                db_session.delete(doc_cc_pair)
HEAD:backend/onyx/db/credentials.py:349:                db_session.delete(connector)
HEAD:backend/onyx/db/credentials.py:367:    db_session.delete(credential)
HEAD:backend/onyx/db/credentials.py:438:        db_session.delete(credential)
HEAD:backend/onyx/db/discord_bot.py:60:    result = db_session.execute(delete(DiscordBotConfig))
HEAD:backend/onyx/db/discord_bot.py:152:    db_session.delete(existing_key)
HEAD:backend/onyx/db/discord_bot.py:426:            db_session.delete(config)
HEAD:backend/onyx/db/document.py:1201:    db_session.execute(delete(DbDocument).where(DbDocument.id.in_(document_ids)))
HEAD:backend/onyx/db/document_set.py:496:        db_session.execute(delete_stmt)
HEAD:backend/onyx/db/document_set.py:537:    db_session.delete(document_set_row)
HEAD:backend/onyx/db/document_set.py:577:        db_session.execute(delete_stmt)
HEAD:backend/onyx/db/document_set.py:609:    result = db_session.execute(delete_stmt)
HEAD:backend/onyx/db/encrypted_kv_store.py:40:        deleted = db_session.query(EncryptedKeyValueStore).filter_by(key=key).delete()
HEAD:backend/onyx/db/entities.py:293:    db_session.query(KGEntity).filter(KGEntity.document_id.in_(document_ids)).delete(
HEAD:backend/onyx/db/enums.py:234:    SOAKING: the old index stopped being read; waiting out the retention window.
HEAD:backend/onyx/db/external_app.py:696:    db_session.delete(app)
HEAD:backend/onyx/db/external_app.py:699:            db_session.delete(skill)
HEAD:backend/onyx/db/federated.py:235:        db_session.delete(mapping)
HEAD:backend/onyx/db/federated.py:332:    db_session.delete(federated_connector)
HEAD:backend/onyx/db/feedback.py:266:    # Delete all feedback for this message
HEAD:backend/onyx/db/file_content.py:78:    db_session.query(FileContent).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:105:    db_session.query(FileRecord).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:153:    attempt no longer exists in the DB at all (deleted by retention,
HEAD:backend/onyx/db/file_record.py:235:    """Ids of blobs a content-free session produced and has not deleted yet."""
HEAD:backend/onyx/db/hierarchy.py:932:    db_session.execute(delete(HierarchyNode).where(HierarchyNode.id.in_(orphan_ids)))
HEAD:backend/onyx/db/image_generation.py:160:    db_session.delete(config)
HEAD:backend/onyx/db/index_attempt.py:186:        db_session.delete(index_attempt)
HEAD:backend/onyx/db/input_prompt.py:117:    db_session.delete(input_prompt)
HEAD:backend/onyx/db/input_prompt.py:141:    db_session.delete(input_prompt)
HEAD:backend/onyx/db/mcp.py:321:    db_session.delete(server)
HEAD:backend/onyx/db/mcp.py:502:    db_session.delete(config)
HEAD:backend/onyx/db/mcp.py:520:        db_session.delete(config)
HEAD:backend/onyx/db/memory.py:137:            db_session.delete(existing[0])
HEAD:backend/onyx/db/models.py:810:        ForeignKey("chat_message.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:884:        ForeignKey("chat_message.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:3283:        # failed-session check, retention/GC deletes and the cascade delete of
HEAD:backend/onyx/db/models.py:3309:        ForeignKey("chat_message.id", ondelete="SET NULL"),
HEAD:backend/onyx/db/models.py:3316:        ForeignKey("chat_message.id", ondelete="SET NULL"), nullable=True
HEAD:backend/onyx/db/models.py:3422:        PGUUID(as_uuid=True), ForeignKey("chat_session.id", ondelete="CASCADE")
HEAD:backend/onyx/db/models.py:3428:        ForeignKey("chat_message.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:3571:        ForeignKey("chat_message.id", ondelete="SET NULL"), nullable=True
HEAD:backend/onyx/db/models.py:3596:        ForeignKey("chat_message.id", ondelete="SET NULL"), nullable=True
HEAD:backend/onyx/db/models.py:5588:    # first message and adopts it. No foreign key: the session row is deleted
HEAD:backend/onyx/db/models.py:6391:        "Artifact", back_populates="session", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:6394:        "ActionReceipt", back_populates="session", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:6397:        "BuildMessage", back_populates="session", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:6400:        "Snapshot", back_populates="session", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:6497:        ForeignKey("build_session.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:6563:        ForeignKey("build_session.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:6630:        ForeignKey("build_session.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:6670:        ForeignKey("build_session.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:6709:        ForeignKey("build_session.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:6744:    `ScheduledTaskRun` row pointing back at the session. Soft-deleted tasks
HEAD:backend/onyx/db/models.py:6842:    session delete the FK is cleared (SET NULL) so the run row survives
HEAD:backend/onyx/db/models.py:6858:        ForeignKey("build_session.id", ondelete="SET NULL"),
HEAD:backend/onyx/db/models.py:7159:    Retention: rows older than 30 days are deleted by a nightly Celery task.
HEAD:backend/onyx/db/notification.py:137:    db_session.query(Notification).filter(Notification.notif_type == notif_type).delete(
HEAD:backend/onyx/db/oauth_config.py:116:    db_session.delete(oauth_config)
HEAD:backend/onyx/db/oauth_config.py:179:    db_session.delete(user_token)
HEAD:backend/onyx/db/persona.py:275:            db_session.delete(row)
HEAD:backend/onyx/db/persona.py:1448:        persona_id=persona_id, user=user, db_session=db_session, include_deleted=True
HEAD:backend/onyx/db/persona.py:2079:    db_session.query(PersonaLabel).filter(PersonaLabel.id == label_id).delete()
HEAD:backend/onyx/db/relationships.py:589:    db_session.query(KGEntity).filter(KGEntity.document_id == document_id).delete(
HEAD:backend/onyx/db/skill.py:16:immediately (skills sync via S3-backed bundles, so blob retention isn't
HEAD:backend/onyx/db/skill.py:581:        db_session.execute(delete(Skill__User).where(Skill__User.skill_id == skill.id))
HEAD:backend/onyx/db/skill.py:659:    db_session.delete(skill)
HEAD:backend/onyx/db/slack_bot.py:75:    db_session.delete(slack_bot)
HEAD:backend/onyx/db/slack_channel_config.py:39:        db_session.delete(rel)
HEAD:backend/onyx/db/slack_channel_config.py:235:    db_session.delete(slack_channel_config)
HEAD:backend/onyx/db/tag.py:157:        db_session.execute(delete_stmt)
HEAD:backend/onyx/db/tag.py:265:    result = db_session.execute(delete_stmt)
HEAD:backend/onyx/db/targeted_reindex.py:308:    we update them, so it survives the eventual retention cleanup of
HEAD:backend/onyx/db/tasks.py:79:    db_session.execute(delete(TaskQueueState).where(TaskQueueState.task_id == task_id))
HEAD:backend/onyx/db/token_limit.py:178:    db_session.delete(token_limit)
HEAD:backend/onyx/db/tools.py:283:                db_session.delete(oauth_config)
HEAD:backend/onyx/db/tools.py:296:    db_session.delete(tool)
HEAD:backend/onyx/db/tools.py:307:                db_session.delete(oauth_config)
HEAD:backend/onyx/db/tracing.py:62:    db_session.delete(provider)
HEAD:backend/onyx/db/users.py:319:        db_session.delete(membership)
HEAD:backend/onyx/db/users.py:643:        db_session.delete(shadow_user)
HEAD:backend/onyx/db/users.py:940:        db_session.delete(oauth_account)
HEAD:backend/onyx/db/users.py:986:    db_session.delete(user_to_delete)
HEAD:backend/onyx/db/voice.py:120:        db_session.delete(provider)
HEAD:backend/onyx/db/web_search.py:166:    db_session.delete(provider)
HEAD:backend/onyx/db/web_search.py:322:    db_session.delete(provider)
HEAD:backend/onyx/external_apps/providers/gmail.py:169:# full draft lifecycle — but not permanent message delete, which keeps the
HEAD:backend/onyx/key_value_store/store.py:49:                db_session.query(KVStore).filter_by(key=key).delete()  # just in case
HEAD:backend/onyx/key_value_store/store.py:99:            result = db_session.query(KVStore).filter_by(key=key).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:21:    db_session.query(KGRelationship).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:22:    db_session.query(KGRelationshipType).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:23:    db_session.query(KGEntity).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:24:    db_session.query(KGRelationshipExtractionStaging).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:25:    db_session.query(KGEntityExtractionStaging).delete()
HEAD:backend/onyx/kg/resets/reset_index.py:26:    db_session.query(KGRelationshipTypeExtractionStaging).delete()
HEAD:backend/onyx/llm/cost_overrides.py:168:    db_session.delete(row)
HEAD:backend/onyx/llm/factory.py:494:    # Last on purpose: policy headers (e.g. incognito retention suppression)
HEAD:backend/onyx/llm/interfaces.py:26:    """Per-request policy an LLM call must carry (e.g. incognito retention
HEAD:backend/onyx/llm/multi_llm.py:567:        # policy-supplied value wins. Incognito retention flags live here, and
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:58:async def _try_delete_message(message: discord.Message) -> bool:
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:59:    """Attempt to delete a message. Returns True if successful."""
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:62:        await message.delete()
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:66:        logger.warning("Failed to delete message %s: %s", message.id, e)
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:143:        await _try_delete_message(message)
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:150:        await _try_delete_message(message)
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:273:    # Note: we need to use the webhook and the respond_url to update/delete ephemeral messages
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:331:                # for now we delete the original ephemeral message and post a new one
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:557:    # Delete the message with the option to mark resolved
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:565:            logger.error("Unable to delete message for resolved")
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:115:        client.chat_deleteScheduledMessage(
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:123:                "Unable to delete the scheduled message. It must have already been posted"
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:244:                client.chat_deleteScheduledMessage(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1025:                # FK cascade dropped the row (build_session deleted).
HEAD:backend/onyx/server/documents/credential.py:118:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/documents/credential.py:443:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/documents/credential.py:464:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/features/build/db/build_session.py:299:    db_session.delete(session)
HEAD:backend/onyx/server/features/build/db/sandbox.py:331:    db_session.delete(snapshot)
HEAD:backend/onyx/server/features/build/db/sandbox.py:342:    db_session.delete(snapshot)
HEAD:backend/onyx/server/features/build/sandbox/base.py:13:- cleanup_session_workspace() removes session workspace on session delete
HEAD:backend/onyx/server/features/build/sandbox/base.py:227:        """Clean up a session workspace on session delete: stop the
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1481:        """Clean up a session workspace (on session delete). Executes
HEAD:backend/onyx/server/features/build/session/api.py:334:        success = session_manager.delete_session(session_id, user.id)
HEAD:backend/onyx/server/features/build/session/api.py:835:        deleted = session_manager.delete_file(session_id, user_id, path)
HEAD:backend/onyx/server/features/build/session/manager.py:916:                                "Best-effort opencode session delete returned false "
HEAD:backend/onyx/server/features/build/session/manager.py:923:                            "Best-effort opencode session delete failed for "
HEAD:backend/onyx/server/features/build/session/manager.py:944:                    # Log but don't fail - session can still be deleted even if
HEAD:backend/onyx/server/features/build/timeouts.py:126:# Post-terminal retention of the turn record and the client_request_id →
HEAD:backend/onyx/server/features/build/timeouts.py:129:TURN_RETENTION_SECONDS = 15 * 60
HEAD:backend/onyx/server/features/build/timeouts.py:130:REQUEST_ID_TTL_SECONDS = ACTIVE_TURN_TTL_SECONDS + TURN_RETENTION_SECONDS
HEAD:backend/onyx/server/features/build/timeouts.py:133:# client-paced or opaque (session delete, subagent turns) — all interactive-
HEAD:backend/onyx/server/features/input_prompt/api.py:115:            user, input_prompt_id, db_session, delete_public=delete_public
HEAD:backend/onyx/server/features/oauth_config/api.py:191:        return {"message": "OAuth configuration deleted successfully"}
HEAD:backend/onyx/server/features/projects/api.py:512:    db_session.delete(project)
HEAD:backend/onyx/server/federated/api.py:637:        db_session.delete(oauth_token)
HEAD:backend/onyx/server/manage/users.py:833:    db_session.expunge(user_to_delete)
HEAD:backend/onyx/server/pat/api.py:107:    return {"message": "Token deleted successfully"}
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:68:    delete_chat_session,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:237:        raise ValueError("Chat session does not exist or has been deleted")
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:387:        if not include_deleted and existing_chat_session.deleted:
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:388:            raise HTTPException(status_code=404, detail="Chat session has been deleted")
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:457:        deleted=chat_session.deleted,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:681:def delete_chat_session_by_id(
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:704:        delete_chat_session(
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:705:            user_id, session_id, db_session, hard_delete=actual_hard_delete
HEAD:backend/onyx/server/settings/api.py:108:        # Search Mode is Business+, Chat Retention is Enterprise-only. Same error
HEAD:backend/onyx/server/settings/api.py:119:            merged.maximum_chat_retention_days != existing.maximum_chat_retention_days
HEAD:backend/onyx/server/settings/api.py:124:                "Chat history retention requires the Enterprise plan.",
HEAD:backend/onyx/server/settings/models.py:44:    maximum_chat_retention_days: float | None = None
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:536:> **Security note:** State files contain session tokens in plaintext. Add them to `.gitignore`, delete when no longer needed, and set `AGENT_BROWSER_ENCRYPTION_KEY` for encryption at rest. See [Security Best Practices](#security-best-practices).
HEAD:backend/onyx/skills/builtin/gmail/SKILL.md.template:33:`draft-send`; there is no permanent message delete. `me` is always the
HEAD:backend/onyx/skills/builtin/pptx/components.md:87:C.titleSlide(pres, theme, { title: "Q4 in review.", subtitle: "Revenue, retention, roadmap.", meta: "ACME · Q4 2026" });
HEAD:backend/onyx/skills/builtin/pptx/components.md:93:    { value: "98%", label: "Retention" },
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:89:    staged + extracted, yield the session id, and delete the session on exit.
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:466:        response = self.session.delete(url, timeout=30)
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:513:        response = self.session.delete(url, timeout=10)
```
Persisted chat history is a security and privacy asset with its own retention
and deletion lifecycle.
## File and Object-Storage Deletion
Evidence lines: 145
```text
HEAD:backend/ee/onyx/server/log_export/storage.py:330:        file_store.delete_file(record.file_id, error_on_missing=False)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:378:                file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/ee/onyx/server/scim/api.py:303:# Entra ID frees a soft-deleted user's UPN by prefixing the 32-hex objectId.
HEAD:backend/ee/onyx/server/scim/api.py:310:    Entra syncs objectId-prefixed values for soft-deleted users. Writing one
HEAD:backend/onyx/background/celery/celery_utils.py:33:    delete_files_best_effort,
HEAD:backend/onyx/background/celery/celery_utils.py:241:        delete_files_best_effort(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:70:    delete_files_best_effort,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:374:        delete_files_best_effort(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:602:        delete_files_best_effort(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:702:                delete_files_best_effort(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:956:            file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:957:            file_store.delete_file(
HEAD:backend/onyx/background/indexing/checkpointing_utils.py:201:    file_store.delete_file(index_attempt.checkpoint_pointer)
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:46:    delete_files_best_effort,
HEAD:backend/onyx/background/indexing/run_targeted_reindex.py:327:        delete_files_best_effort(
HEAD:backend/onyx/chat/incognito.py:246:    """Delete the blobs the session's tools saved. True when none remain.
HEAD:backend/onyx/chat/incognito.py:255:            file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/configs/app_configs.py:2037:# Which backend to use for file storage: "s3" (S3/MinIO) or "postgres" (PostgreSQL Large Objects)
HEAD:backend/onyx/configs/app_configs.py:2044:# S3_ENDPOINT_URL is for MinIO and other S3-compatible storage. Leave blank for AWS S3.
HEAD:backend/onyx/configs/app_configs.py:2048:# S3/MinIO Access Keys
HEAD:backend/onyx/configs/app_configs.py:2052:# Well-known MinIO default; deployments left on it expose all stored files.
HEAD:backend/onyx/configs/app_configs.py:2053:DEFAULT_OBJECT_STORAGE_CREDENTIAL = "minioadmin"
HEAD:backend/onyx/configs/app_configs.py:2061:    # Only for self-hosted MinIO (has an endpoint URL); real AWS S3 has none.
HEAD:backend/onyx/configs/app_configs.py:2071:        "Object storage is using the well-known default 'minioadmin' credentials. "
HEAD:backend/onyx/configs/app_configs.py:2072:        "Anyone who can reach the MinIO/S3 endpoint can read or modify stored files "
HEAD:backend/onyx/configs/app_configs.py:2074:        "S3_AWS_SECRET_ACCESS_KEY (and MINIO_ROOT_USER / MINIO_ROOT_PASSWORD) to "
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:1:"""Kept around since it's used in the migration to move to S3/MinIO"""
HEAD:backend/onyx/db/chat.py:231:            file_store.delete_file(file_id=file_info["id"], error_on_missing=False)
HEAD:backend/onyx/db/document.py:58:from onyx.file_store.staging import delete_files_best_effort
HEAD:backend/onyx/db/document.py:1297:    delete_files_best_effort(file_ids_to_delete)
HEAD:backend/onyx/db/file_content.py:74:def delete_file_content_by_file_id(
HEAD:backend/onyx/db/file_record.py:101:def delete_filerecord_by_file_id(
HEAD:backend/onyx/db/models.py:4852:    # External storage support (S3, MinIO, Azure Blob, etc.)
HEAD:backend/onyx/db/models.py:4873:    Used when FILE_STORE_BACKEND=postgres to avoid needing S3/MinIO."""
HEAD:backend/onyx/db/skill.py:408:    Returns the old bundle file id so the caller can delete the old blob from
HEAD:backend/onyx/file_store/README.md:3:The Onyx file store provides a unified interface for storing files and large binary objects. It supports four storage backends: S3-compatible storage (AWS S3, MinIO, Digital Ocean Spaces, etc.), Google Cloud Storage (GCS), Azure Blob Storage, and PostgreSQL Large Objects.
HEAD:backend/onyx/file_store/README.md:29:| `s3` (default) | S3-compatible | AWS S3, MinIO, Digital Ocean Spaces, etc. |
HEAD:backend/onyx/file_store/README.md:53:### MinIO
HEAD:backend/onyx/file_store/README.md:58:S3_ENDPOINT_URL=http://localhost:9000  # MinIO endpoint
HEAD:backend/onyx/file_store/README.md:59:S3_AWS_ACCESS_KEY_ID=minioadmin
HEAD:backend/onyx/file_store/README.md:60:S3_AWS_SECRET_ACCESS_KEY=minioadmin
HEAD:backend/onyx/file_store/README.md:101:- `storage.objects.create`, `storage.objects.get`, `storage.objects.delete` (CRUD operations)
HEAD:backend/onyx/file_store/README.md:139:(`mcr.microsoft.com/azure-storage/azurite`) emulates Azure Blob Storage, playing the role MinIO
HEAD:backend/onyx/file_store/README.md:161:- `S3BackedFileStore` (`file_store.py`): For S3-compatible storage (AWS S3, MinIO, etc.)
HEAD:backend/onyx/file_store/README.md:178:- `delete_file(file_id)`: Delete a file and its metadata
HEAD:backend/onyx/file_store/README.md:223:file_store.delete_file(file_id)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:20:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:266:                    blob_client.delete_blob()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:345:    def delete_file(
HEAD:backend/onyx/file_store/azure_blob_file_store.py:369:                    delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:380:                    blob_client.delete_blob()
HEAD:backend/onyx/file_store/azure_blob_file_store.py:393:                        "delete_file: File %s not found in Azure Blob Storage "
HEAD:backend/onyx/file_store/azure_blob_file_store.py:399:                delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/azure_blob_file_store.py:443:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=db_session)
HEAD:backend/onyx/file_store/document_batch_storage.py:227:        self.file_store.delete_file(batch_file_name, error_on_missing=False)
HEAD:backend/onyx/file_store/file_store.py:28:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/file_store.py:163:    def delete_file(self, file_id: str, error_on_missing: bool = True) -> None:
HEAD:backend/onyx/file_store/file_store.py:198:    """Isn't necessarily S3, but is any S3-compatible storage (e.g. MinIO)"""
HEAD:backend/onyx/file_store/file_store.py:232:                # Add endpoint URL if specified (for MinIO, etc.)
HEAD:backend/onyx/file_store/file_store.py:237:                        s3={"addressing_style": "path"},  # Required for MinIO
HEAD:backend/onyx/file_store/file_store.py:258:                    # Use IAM role or default credentials (not typically used with MinIO)
HEAD:backend/onyx/file_store/file_store.py:319:                    # For us-east-1 or MinIO/other S3-compatible services
HEAD:backend/onyx/file_store/file_store.py:497:    def delete_file(
HEAD:backend/onyx/file_store/file_store.py:520:                    delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:527:                    s3_client.delete_object(
HEAD:backend/onyx/file_store/file_store.py:535:                            "delete_file: File %s not found in file store (key: %s), cleaning up database record.",
HEAD:backend/onyx/file_store/file_store.py:543:                delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:585:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=db_session)
HEAD:backend/onyx/file_store/file_store.py:703:    - No external storage service (S3/MinIO) is required.
HEAD:backend/onyx/file_store/file_store.py:706:    - Supports AWS S3, MinIO, and other S3-compatible storage.
HEAD:backend/onyx/file_store/gcs_file_store.py:21:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/gcs_file_store.py:299:    def delete_file(
HEAD:backend/onyx/file_store/gcs_file_store.py:323:                    delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/gcs_file_store.py:336:                        "delete_file: File %s not found in GCS "
HEAD:backend/onyx/file_store/gcs_file_store.py:342:                delete_filerecord_by_file_id(file_id=file_id, db_session=db_session)
HEAD:backend/onyx/file_store/gcs_file_store.py:386:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=db_session)
HEAD:backend/onyx/file_store/postgres_file_store.py:4:eliminating the need for an external S3/MinIO service.
HEAD:backend/onyx/file_store/postgres_file_store.py:22:    delete_file_content_by_file_id,
HEAD:backend/onyx/file_store/postgres_file_store.py:30:    delete_filerecord_by_file_id,
HEAD:backend/onyx/file_store/postgres_file_store.py:87:def _delete_large_object(raw_conn: Any, oid: int) -> None:
HEAD:backend/onyx/file_store/postgres_file_store.py:88:    """Unlink (delete) a Large Object by OID."""
HEAD:backend/onyx/file_store/postgres_file_store.py:173:                        _delete_large_object(raw_conn, old_oid)
HEAD:backend/onyx/file_store/postgres_file_store.py:186:                        _delete_large_object(raw_conn, oid)
HEAD:backend/onyx/file_store/postgres_file_store.py:189:                        "Failed to delete large object %s for file %s", oid, file_id
HEAD:backend/onyx/file_store/postgres_file_store.py:235:    def delete_file(
HEAD:backend/onyx/file_store/postgres_file_store.py:255:                    _delete_large_object(raw_conn, file_content.lobj_oid)
HEAD:backend/onyx/file_store/postgres_file_store.py:263:                delete_file_content_by_file_id(file_id=file_id, db_session=session)
HEAD:backend/onyx/file_store/postgres_file_store.py:264:                delete_filerecord_by_file_id(file_id=file_id, db_session=session)
HEAD:backend/onyx/file_store/postgres_file_store.py:321:                delete_filerecord_by_file_id(file_id=old_file_id, db_session=session)
HEAD:backend/onyx/file_store/staging.py:88:def delete_files_best_effort(
HEAD:backend/onyx/file_store/staging.py:101:            file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/file_store/staging.py:150:    return delete_files_best_effort(
HEAD:backend/onyx/file_store/staging.py:175:    return delete_files_best_effort(
HEAD:backend/onyx/indexing/indexing_pipeline.py:534:            file_store.delete_file(old_file_id, error_on_missing=False)
HEAD:backend/onyx/kg/clustering/clustering.py:443:    # Delete the transferred objects from the staging tables
HEAD:backend/onyx/server/features/build/db/user_library.py:97:    Returns (doc_id, file_id, old_blob_id_to_delete). The new blob is saved
HEAD:backend/onyx/server/features/build/db/user_library.py:98:    first; the caller must delete the returned old_blob_id *after* its final
HEAD:backend/onyx/server/features/build/db/user_library.py:140:    """Delete superseded file-store blobs. Call after the final DB commit."""
HEAD:backend/onyx/server/features/build/db/user_library.py:146:            file_store.delete_file(blob_id, error_on_missing=False)
HEAD:backend/onyx/server/features/build/db/user_library.py:148:            logger.warning("Failed to delete stale blob %s: %s", blob_id, e)
HEAD:backend/onyx/server/features/build/db/user_library.py:197:    """Delete a user file's blob from the file store and its document record."""
HEAD:backend/onyx/server/features/build/db/user_library.py:203:                get_default_file_store().delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/server/features/build/db/user_library.py:205:                logger.warning("Failed to delete file blob %s: %s", file_id, e)
HEAD:backend/onyx/server/features/build/sandbox/README.md:36:   - Snapshots tar-streamed through api_server-owned `FileStore` — agent containers never receive S3/MinIO credentials
HEAD:backend/onyx/server/features/build/sandbox/README.md:39:   - Sandboxes join only the dedicated `onyx_craft_sandbox` bridge — `postgres` / `redis` / `minio` / model servers are not reachable by compose DNS
HEAD:backend/onyx/server/features/build/sandbox/README.md:263:- **Sandbox app containers and sidecar init containers** do not receive FileStore, S3, or MinIO credentials
HEAD:backend/onyx/server/features/build/sandbox/README.md:267:- **Docker network isolation** is enforced by joining only the dedicated `onyx_craft_sandbox` bridge — compose's default network (postgres/redis/minio/model servers) is unreachable by DNS from inside a sandbox
HEAD:backend/onyx/server/features/build/sandbox/base.py:532:    def delete_file(
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:30:- no S3 / MinIO / Postgres / Redis / FileStore credentials in env
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:36:  postgres, redis, minio, and model_server remain unreachable by service name.
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:341:    "minio",
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:532:      No caller can inject anything else. No S3/MinIO/Postgres/Redis
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:541:      redis, and minio remain unreachable by service name.
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:679:        # No docker socket mount. No S3/MinIO env. No FileStore credentials.
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1865:    def delete_file(
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/opencode_history.py:46:def _remove_file_or_tree(path: Path) -> None:
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/opencode_history.py:80:    _remove_file_or_tree(staged_db)
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/opencode_history.py:82:        _remove_file_or_tree(staged_db.with_name(f"{staged_db.name}{suffix}"))
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/opencode_history.py:143:        _remove_file_or_tree(child)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:2403:    def delete_file(
HEAD:backend/onyx/server/features/build/sandbox/snapshot_manager.py:208:        self._file_store.delete_file(storage_path, error_on_missing=False)
HEAD:backend/onyx/server/features/build/sandbox/snapshot_manager.py:244:        """Delete a snapshot's blob from the file store.
HEAD:backend/onyx/server/features/build/sandbox/snapshot_manager.py:258:            self._file_store.delete_file(storage_path, error_on_missing=False)
HEAD:backend/onyx/server/features/build/session/api.py:819:def delete_file_endpoint(
HEAD:backend/onyx/server/features/build/session/api.py:835:        deleted = session_manager.delete_file(session_id, user_id, path)
HEAD:backend/onyx/server/features/build/session/manager.py:1819:    def delete_file(
HEAD:backend/onyx/server/features/build/session/manager.py:1844:        deleted = self._sandbox_manager.delete_file(
HEAD:backend/onyx/server/features/build/user_library/api.py:483:def delete_file(
HEAD:backend/onyx/server/features/mcp/api.py:2659:    """Delete an MCP server and cascading related objects (tools, configs)."""
HEAD:backend/onyx/server/features/skill/api.py:87:    delete_bundle_blob,
HEAD:backend/onyx/server/features/skill/api.py:172:    delete_bundle_blob(file_store, old_file_id)
HEAD:backend/onyx/server/features/skill/api.py:589:    delete_bundle_blob(file_store, old_file_id)
HEAD:backend/onyx/server/features/skill/api.py:733:            delete_bundle_blob(file_store, new_bundle_file_id)
HEAD:backend/onyx/server/features/skill/api.py:744:        delete_bundle_blob(file_store, old_bundle_file_id)
HEAD:backend/onyx/server/features/skill/api.py:960:        delete_bundle_blob(get_default_file_store(), old_file_id)
HEAD:backend/onyx/server/manage/administrative.py:229:            file_store.delete_file(file_id)
HEAD:backend/onyx/skills/builtin/google-drive/gslides_api.py:185:        "createShape, insertText, updateTextStyle, deleteObject)",
HEAD:backend/onyx/skills/builtin/google-drive/sheets.md:51:objects (e.g. `addSheet`, `deleteSheet`, `repeatCell`, `mergeCells`,
HEAD:backend/onyx/skills/builtin/google-drive/slides.md:49:objects (e.g. `createShape`, `createTable`, `updateTextStyle`, `deleteObject`,
HEAD:backend/onyx/skills/ingest.py:120:        delete_bundle_blob(file_store, ingested.bundle_file_id)
HEAD:backend/onyx/skills/ingest.py:124:def delete_bundle_blob(file_store: FileStore, file_id: str) -> None:
HEAD:backend/onyx/skills/ingest.py:127:        file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/onyx/skills/ingest.py:129:        logger.warning("Failed to delete bundle blob %s", file_id, exc_info=True)
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:509:    def delete_file(self, file_id: str) -> None:
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:512:                        client.delete_file(ci_file_id)
```
File metadata deletion and underlying object/blob deletion are distinct
operations unless runtime behavior proves otherwise.
## Credential and Token Revocation
Evidence lines: 310
```text
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:46:    """Delete the chain marker only if ``chain_token`` still owns it."""
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/scim.py:75:        # Revoke any currently active tokens
HEAD:backend/ee/onyx/db/scim.py:106:    def revoke_token(self, token_id: int) -> None:
HEAD:backend/ee/onyx/db/user_group.py:178:        db_session.delete(token_rate_limit__user_group_relationship)
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:62:    refresh_token: str
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:124:    refresh_token: RefreshTokenData,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:133:    account_id = str(refresh_token.userinfo["userId"])
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:134:    account_email = str(refresh_token.userinfo["email"])
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:145:        new_access_token = refresh_token.access_token
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:146:        new_refresh_token = refresh_token.refresh_token
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:149:            refresh_token.session["exp"] / 1000, tz=timezone.utc
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:164:            refresh_token=new_refresh_token,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:386:    revokes all previous tokens. The raw token value is returned exactly once
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:51:        refresh_token: str
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:224:                "confluence_refresh_token": token_response.refresh_token,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:180:        authorized_user_info["refresh_token"] = authorization_response["refresh_token"]
HEAD:backend/ee/onyx/server/scim/models.py:363:# where admins create/revoke the bearer tokens that IdPs use to authenticate.
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:18:    delete_token_rate_limit,
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:100:@router.delete("/rate-limit/{token_rate_limit_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:101:def delete_token_limit_settings(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:106:    delete_token_rate_limit(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:261:def delete_group_token_limit_settings(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:272:    delete_token_rate_limit(db_session=db_session, token_rate_limit_id=rate_limit_id)
HEAD:backend/onyx/auth/captcha.py:144:        await redis.delete(_replay_cache_key(token))
HEAD:backend/onyx/auth/login_claims_capture.py:368:                "has_refresh_token": bool(token.get("refresh_token")),
HEAD:backend/onyx/auth/oauth_refresher.py:305:    if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:327:                    "refresh_token": oauth_account.refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:328:                    "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_refresher.py:342:            new_refresh_token = token_data.get(
HEAD:backend/onyx/auth/oauth_refresher.py:343:                "refresh_token", oauth_account.refresh_token
HEAD:backend/onyx/auth/oauth_refresher.py:357:                "refresh_token": new_refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:405:        if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:415:            # refreshed `expires_at` (and `refresh_token` for IdPs that
HEAD:backend/onyx/auth/oauth_refresher.py:460:async def check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:468:    return bool(oauth_account.refresh_token)
HEAD:backend/onyx/auth/oauth_refresher.py:471:async def get_oauth_accounts_requiring_refresh_token(user: User) -> List[OAuthAccount]:
HEAD:backend/onyx/auth/oauth_refresher.py:481:        has_refresh_token = await check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:484:        if not has_refresh_token:
HEAD:backend/onyx/auth/oauth_token_manager.py:175:            if "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:177:                    return self.refresh_token(user_token)
HEAD:backend/onyx/auth/oauth_token_manager.py:186:    def refresh_token(self, user_token: OAuthUserToken) -> str:
HEAD:backend/onyx/auth/oauth_token_manager.py:202:            "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_token_manager.py:203:            "refresh_token": token_data["refresh_token"],
HEAD:backend/onyx/auth/oauth_token_manager.py:225:        # Preserve refresh_token if not returned (some providers don't return it)
HEAD:backend/onyx/auth/oauth_token_manager.py:226:        if "refresh_token" not in new_token_data and "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:227:            new_token_data["refresh_token"] = token_data["refresh_token"]
HEAD:backend/onyx/auth/scoped_permissions.py:182:    """Admin-only gate for delete and other ops that share a bundle token with
HEAD:backend/onyx/auth/users.py:1006:        refresh_token: Optional[str] = None,
HEAD:backend/onyx/auth/users.py:1072:                "refresh_token": refresh_token,
HEAD:backend/onyx/auth/users.py:1671:    async def refresh_token(self, token: Optional[str], user: Any) -> str:
HEAD:backend/onyx/auth/users.py:1758:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1800:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1869:    async def refresh_token(
HEAD:backend/onyx/auth/users.py:1980:                supports_refresh = hasattr(strategy, "refresh_token") and callable(
HEAD:backend/onyx/auth/users.py:1981:                    getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:1986:                        refresh_method = getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:2677:            token.get("refresh_token"),
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:68:                    f"Skipping capability checks for deleted credential "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:30:    delete_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:35:    delete_all_documents_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:455:        credential_id_to_delete: int | None = None
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:527:            credential_id_to_delete = cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:530:            # Explicitly delete document by connector credential pair records before deleting the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:532:            delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:535:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:542:            # related to the deleted DocumentByConnectorCredentialPair during commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:546:            delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:549:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:558:            # if there are no credentials left, delete the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:621:                f"cc_pair={cc_pair_id} connector={connector_id_to_delete} credential={credential_id_to_delete}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:634:        f"credential={credential_id_to_delete} "
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:18:    delete_document_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:122:    To delete a connector / credential pair:
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:246:                delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:324:                    delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/connectors/capability_checks/runner.py:293:                f"Credential {credential_id} was deleted while the run was in flight."
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:38:    confluence_refresh_tokens,
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:251:        if "confluence_refresh_token" not in credential_json:
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:274:        new_credentials = confluence_refresh_tokens(
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:278:            credential_json["confluence_refresh_token"],
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:297:        if "confluence_refresh_token" in credentials:
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:482:        if "confluence_refresh_token" in credentials:
HEAD:backend/onyx/connectors/confluence/utils.py:40:    refresh_token: str
HEAD:backend/onyx/connectors/confluence/utils.py:302:def confluence_refresh_tokens(
HEAD:backend/onyx/connectors/confluence/utils.py:303:    client_id: str, client_secret: str, cloud_id: str, refresh_token: str
HEAD:backend/onyx/connectors/confluence/utils.py:313:            "grant_type": "refresh_token",
HEAD:backend/onyx/connectors/confluence/utils.py:316:            "refresh_token": refresh_token,
HEAD:backend/onyx/connectors/confluence/utils.py:331:    new_credentials["confluence_refresh_token"] = token_response.refresh_token
HEAD:backend/onyx/connectors/google_utils/google_auth.py:45:    """creds_json only needs to contain client_id, client_secret and refresh_token to
HEAD:backend/onyx/connectors/google_utils/google_auth.py:60:    if creds.expired and creds.refresh_token:
HEAD:backend/onyx/connectors/google_utils/google_auth.py:115:        authorized_user_info["refresh_token"] = credentials_dict["refresh_token"]
HEAD:backend/onyx/connectors/google_utils/google_auth.py:127:            if oauth_creds.refresh_token != authorized_user_info["refresh_token"]:
HEAD:backend/onyx/connectors/google_utils/google_kv.py:182:        delete_encrypted_kv(KV_CRED_KEY.format(str(credential_id)))
HEAD:backend/onyx/connectors/linear/connector.py:46:_REFRESH_TOKEN = "refresh_token"
HEAD:backend/onyx/connectors/linear/connector.py:154:            _REFRESH_TOKEN: token_data[_REFRESH_TOKEN],
HEAD:backend/onyx/connectors/linear/connector.py:166:                new_credentials = self.refresh_token(credentials)
HEAD:backend/onyx/connectors/linear/connector.py:178:    def refresh_token(self, credentials: dict[str, Any]) -> dict[str, Any]:
HEAD:backend/onyx/connectors/linear/connector.py:179:        if _REFRESH_TOKEN not in credentials:
HEAD:backend/onyx/connectors/linear/connector.py:183:            _REFRESH_TOKEN: credentials[_REFRESH_TOKEN],
HEAD:backend/onyx/connectors/linear/connector.py:186:            "grant_type": _REFRESH_TOKEN,
HEAD:backend/onyx/connectors/linear/connector.py:205:        # Per RFC 6749 §6, the refresh response MAY omit refresh_token, in
HEAD:backend/onyx/connectors/linear/connector.py:212:            _REFRESH_TOKEN: token_data.get(_REFRESH_TOKEN, credentials[_REFRESH_TOKEN]),
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:39:   - **Perform requests at any time** (`refresh_token`)
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:151:Confirm that the ECA has the `refresh_token` scope. Check the user's prior
HEAD:backend/onyx/connectors/salesforce/auth.py:53:        values.append(token_request.refresh_token)
HEAD:backend/onyx/connectors/salesforce/auth.py:129:    if not token_response.refresh_token:
HEAD:backend/onyx/connectors/salesforce/auth.py:137:        sf_refresh_token=token_response.refresh_token,
HEAD:backend/onyx/connectors/salesforce/auth.py:150:            refresh_token=credentials.sf_refresh_token,
HEAD:backend/onyx/connectors/salesforce/auth.py:158:        sf_refresh_token=token_response.refresh_token or credentials.sf_refresh_token,
HEAD:backend/onyx/connectors/salesforce/connector.py:90:_OAUTH_SCOPE = "api refresh_token"
HEAD:backend/onyx/connectors/salesforce/models.py:30:    REFRESH_TOKEN = "refresh_token"
HEAD:backend/onyx/connectors/salesforce/models.py:101:    sf_refresh_token: str = Field(min_length=1)
HEAD:backend/onyx/connectors/salesforce/models.py:111:    refresh_token: str | None = None
HEAD:backend/onyx/connectors/salesforce/models.py:127:    grant_type: Literal[SalesforceGrantType.REFRESH_TOKEN] = (
HEAD:backend/onyx/connectors/salesforce/models.py:128:        SalesforceGrantType.REFRESH_TOKEN
HEAD:backend/onyx/connectors/salesforce/models.py:130:    refresh_token: str = Field(min_length=1)
HEAD:backend/onyx/db/chunk.py:56:def delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/connector_credential_pair.py:676:def delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/connector_credential_pair.py:681:    stmt = delete(ConnectorCredentialPair).where(
HEAD:backend/onyx/db/credentials.py:318:def _delete_credential_internal(
HEAD:backend/onyx/db/credentials.py:343:            # Delete DocumentByConnectorCredentialPair records first
HEAD:backend/onyx/db/credentials.py:347:            # Then delete ConnectorCredentialPair records
HEAD:backend/onyx/db/credentials.py:356:                f"Cannot delete credential as it is still associated with "
HEAD:backend/onyx/db/credentials.py:367:    db_session.delete(credential)
HEAD:backend/onyx/db/credentials.py:371:def delete_credential_for_user(
HEAD:backend/onyx/db/credentials.py:377:    """Delete a credential that belongs to a specific user"""
HEAD:backend/onyx/db/credentials.py:385:    _delete_credential_internal(credential, credential_id, db_session, force)
HEAD:backend/onyx/db/credentials.py:388:def delete_credential(
HEAD:backend/onyx/db/credentials.py:393:    """Delete a credential regardless of ownership (admin function)"""
HEAD:backend/onyx/db/credentials.py:401:    _delete_credential_internal(credential, credential_id, db_session, force)
HEAD:backend/onyx/db/credentials.py:438:        db_session.delete(credential)
HEAD:backend/onyx/db/document.py:30:from onyx.db.chunk import delete_chunk_stats_by_connector_credential_pair__no_commit
HEAD:backend/onyx/db/document.py:1132:def delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1144:    delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1151:def delete_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1163:    stmt = delete(DocumentByConnectorCredentialPair).where(
HEAD:backend/onyx/db/document.py:1178:def delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1183:    """Deletes all document by connector credential pair entries for a specific connector and credential.
HEAD:backend/onyx/db/document.py:1186:    primary key in DocumentByConnectorCredentialPair, and attempting to delete the Connector
HEAD:backend/onyx/db/document.py:1191:    stmt = delete(DocumentByConnectorCredentialPair).where(
HEAD:backend/onyx/db/document.py:1264:    delete_chunk_stats_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/db/document.py:1269:    delete_documents_by_connector_credential_pair__no_commit(db_session, document_ids)
HEAD:backend/onyx/db/document.py:1300:def delete_all_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/document.py:1306:    """Delete all documents for a given connector credential pair.
HEAD:backend/onyx/db/document.py:1965:    """Delete a single document and its connector credential pair relationships.
HEAD:backend/onyx/db/document_set.py:98:    stmt = delete(DocumentSet__ConnectorCredentialPair).where(
HEAD:backend/onyx/db/document_set.py:599:    """Deletes all rows from DocumentSet__ConnectorCredentialPair where the
HEAD:backend/onyx/db/document_set.py:601:    delete_stmt = delete(DocumentSet__ConnectorCredentialPair).where(
HEAD:backend/onyx/db/external_app.py:780:        delete(ExternalAppUserCredential).where(
HEAD:backend/onyx/db/federated.py:330:    # Delete related OAuth tokens (cascade should handle this)
HEAD:backend/onyx/db/hierarchy.py:878:    stmt = delete(HierarchyNodeByConnectorCredentialPair).where(
HEAD:backend/onyx/db/models.py:329:    refresh_token: Mapped[str] = mapped_column(Text, nullable=False)
HEAD:backend/onyx/db/models.py:2119:        ForeignKey("credential.id", ondelete="CASCADE"), nullable=False, index=True
HEAD:backend/onyx/db/models.py:2512:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2730:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2847:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:2899:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:3129:        ForeignKey("credential.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:3142:        "Credential", back_populates="documents_by_credential", passive_deletes=True
HEAD:backend/onyx/db/models.py:4130:    #   "refresh_token": "...",  # Optional
HEAD:backend/onyx/db/models.py:5369:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:5423:        ForeignKey("connector_credential_pair.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:5947:    #   "refresh_token": "<token>",  # OAuth only
HEAD:backend/onyx/db/oauth_config.py:103:def delete_oauth_config(oauth_config_id: int, db_session: Session) -> None:
HEAD:backend/onyx/db/oauth_config.py:105:    Delete OAuth configuration.
HEAD:backend/onyx/db/oauth_config.py:108:    Cascades delete to user tokens.
HEAD:backend/onyx/db/oauth_config.py:116:    db_session.delete(oauth_config)
HEAD:backend/onyx/db/oauth_config.py:169:def delete_user_oauth_token(
HEAD:backend/onyx/db/oauth_config.py:172:    """Delete user's OAuth token for a specific configuration"""
HEAD:backend/onyx/db/oauth_config.py:179:    db_session.delete(user_token)
HEAD:backend/onyx/db/pat.py:45:    NOTE: Expired includes both naturally expired and user-revoked tokens (revocation sets expires_at=NOW()).
HEAD:backend/onyx/db/permission_sync_attempt.py:552:    """Delete all doc permission sync attempts for a connector credential pair.
HEAD:backend/onyx/db/permission_sync_attempt.py:574:    """Delete all external group permission sync attempts for a connector credential pair.
HEAD:backend/onyx/db/swap_index.py:15:    delete_all_documents_for_connector_credential_pair,
HEAD:backend/onyx/db/swap_index.py:88:                delete_all_documents_for_connector_credential_pair(
HEAD:backend/onyx/db/token_limit.py:166:def delete_token_rate_limit(
HEAD:backend/onyx/db/token_limit.py:178:    db_session.delete(token_limit)
HEAD:backend/onyx/db/tools.py:99:    """Owner-or-admin gate for every action on a custom action (edit, delete, toggle, OAuth
HEAD:backend/onyx/db/tools.py:124:    """The gate for every per-tool action (edit, delete, toggle, OAuth config). An MCP tool
HEAD:backend/onyx/db/tools.py:283:                db_session.delete(oauth_config)
HEAD:backend/onyx/db/tools.py:307:                db_session.delete(oauth_config)
HEAD:backend/onyx/db/users.py:939:    for oauth_account in user_to_delete.oauth_accounts:
HEAD:backend/onyx/db/users.py:940:        db_session.delete(oauth_account)
HEAD:backend/onyx/external_apps/providers/base.py:329:        refresh_token = stored.get("refresh_token")
HEAD:backend/onyx/external_apps/providers/base.py:330:        if not refresh_token:
HEAD:backend/onyx/external_apps/providers/base.py:345:                    refresh_token, client_id, client_secret
HEAD:backend/onyx/external_apps/providers/base.py:382:        self, refresh_token: str, client_id: str, client_secret: str
HEAD:backend/onyx/external_apps/providers/base.py:387:            "grant_type": "refresh_token",
HEAD:backend/onyx/external_apps/providers/base.py:390:            "refresh_token": refresh_token,
HEAD:backend/onyx/external_apps/providers/github.py:276:    # GitHub signals a dead refresh token with `bad_refresh_token` rather than
HEAD:backend/onyx/external_apps/providers/github.py:278:    terminal_refresh_errors = frozenset({"invalid_grant", "bad_refresh_token"})
HEAD:backend/onyx/external_apps/providers/github.py:284:        # (e.g. `bad_verification_code`, `bad_refresh_token`), so the generic
HEAD:backend/onyx/external_apps/providers/github.py:305:        if response_data.get("refresh_token"):
HEAD:backend/onyx/external_apps/providers/github.py:306:            creds["refresh_token"] = response_data["refresh_token"]
HEAD:backend/onyx/external_apps/providers/google_base.py:87:                # access_type=offline issues a refresh_token; prompt=consent
HEAD:backend/onyx/external_apps/providers/google_base.py:116:        if response_data.get("refresh_token"):
HEAD:backend/onyx/external_apps/providers/google_base.py:117:            creds["refresh_token"] = response_data["refresh_token"]
HEAD:backend/onyx/external_apps/providers/hubspot.py:212:    # HubSpot signals a dead refresh token with `BAD_REFRESH_TOKEN` rather than
HEAD:backend/onyx/external_apps/providers/hubspot.py:214:    terminal_refresh_errors = frozenset({"invalid_grant", "BAD_REFRESH_TOKEN"})
HEAD:backend/onyx/external_apps/providers/hubspot.py:220:        # `status` (e.g. `BAD_REFRESH_TOKEN`, `BAD_AUTH_CODE`) rather than the
HEAD:backend/onyx/external_apps/providers/hubspot.py:244:        if response_data.get("refresh_token"):
HEAD:backend/onyx/external_apps/providers/hubspot.py:245:            creds["refresh_token"] = response_data["refresh_token"]
HEAD:backend/onyx/external_apps/providers/linear.py:166:        if response_data.get("refresh_token"):
HEAD:backend/onyx/external_apps/providers/linear.py:167:            creds["refresh_token"] = response_data["refresh_token"]
HEAD:backend/onyx/external_apps/providers/slack.py:205:        if authed_user.get("refresh_token"):
HEAD:backend/onyx/external_apps/providers/slack.py:206:            creds["refresh_token"] = authed_user["refresh_token"]
HEAD:backend/onyx/federated_connectors/models.py:53:    refresh_token: Optional[str] = Field(
HEAD:backend/onyx/federated_connectors/slack/federated_connector.py:221:        refresh_token = authed_user.get("refresh_token")
HEAD:backend/onyx/federated_connectors/slack/federated_connector.py:237:            refresh_token=refresh_token,
HEAD:backend/onyx/server/auth/mobile.py:10:  - POST /auth/mobile/logout        revoke the current session token
HEAD:backend/onyx/server/documents/credential.py:14:    delete_credential,
HEAD:backend/onyx/server/documents/credential.py:15:    delete_credential_for_user,
HEAD:backend/onyx/server/documents/credential.py:102:@router.delete("/admin/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:103:def delete_credential_by_id_admin(
HEAD:backend/onyx/server/documents/credential.py:108:    """Same as the user endpoint, but can delete any credential (not just the user's own)"""
HEAD:backend/onyx/server/documents/credential.py:109:    delete_credential(db_session=db_session, credential_id=credential_id)
HEAD:backend/onyx/server/documents/credential.py:111:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/documents/credential.py:118:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/documents/credential.py:422:@router.delete("/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:423:def delete_credential_by_id(
HEAD:backend/onyx/server/documents/credential.py:428:    delete_credential_for_user(
HEAD:backend/onyx/server/documents/credential.py:435:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/documents/credential.py:443:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/documents/credential.py:447:@router.delete("/credential/force/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:448:def force_delete_credential_by_id(
HEAD:backend/onyx/server/documents/credential.py:453:    delete_credential_for_user(credential_id, user, db_session, True)
HEAD:backend/onyx/server/documents/credential.py:456:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/documents/credential.py:464:        success=True, message="Credential deleted successfully", data=credential_id
HEAD:backend/onyx/server/documents/credential_capabilities.py:206:            # credential (or the paired connector) was deleted concurrently and
HEAD:backend/onyx/server/features/build/external_apps/api.py:402:@router.delete("/apps/{external_app_id}/credentials")
HEAD:backend/onyx/server/features/mcp/api.py:442:        grant_types=["authorization_code", "refresh_token"],
HEAD:backend/onyx/server/features/mcp/api.py:1098:@router.delete("/user-credentials/{server_id}")
HEAD:backend/onyx/server/features/mcp/api.py:1099:def delete_user_credentials(
HEAD:backend/onyx/server/features/mcp/api.py:1897:        # to any of them invalidates existing user tokens, so it must trigger
HEAD:backend/onyx/server/features/mcp/client_metadata.py:15:REFRESH_TOKEN_GRANT = "refresh_token"
HEAD:backend/onyx/server/features/mcp/client_metadata.py:40:        grant_types=[AUTHORIZATION_CODE_GRANT, REFRESH_TOKEN_GRANT],
HEAD:backend/onyx/server/features/mcp/credentials.py:212:        return not tokens.get("refresh_token")
HEAD:backend/onyx/server/features/mcp/models.py:630:    grant_types: list[Literal["authorization_code", "refresh_token"]]
HEAD:backend/onyx/server/features/mcp/oauth.py:178:    preserve_existing_refresh_token: bool = True,
HEAD:backend/onyx/server/features/mcp/oauth.py:185:        token_dict.get("refresh_token")
HEAD:backend/onyx/server/features/mcp/oauth.py:187:        or not preserve_existing_refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:190:    existing_refresh = existing_tokens_raw.get("refresh_token")
HEAD:backend/onyx/server/features/mcp/oauth.py:192:        token_dict["refresh_token"] = existing_refresh
HEAD:backend/onyx/server/features/mcp/oauth.py:345:        await self._persist_tokens(tokens, preserve_existing_refresh_token=True)
HEAD:backend/onyx/server/features/mcp/oauth.py:350:        redeemed_refresh_token: str | None,
HEAD:backend/onyx/server/features/mcp/oauth.py:354:            preserve_existing_refresh_token=True,
HEAD:backend/onyx/server/features/mcp/oauth.py:355:            expected_refresh_token=redeemed_refresh_token,
HEAD:backend/onyx/server/features/mcp/oauth.py:356:            require_refresh_token_match=True,
HEAD:backend/onyx/server/features/mcp/oauth.py:368:            preserve_existing_refresh_token=False,
HEAD:backend/onyx/server/features/mcp/oauth.py:376:        preserve_existing_refresh_token: bool,
HEAD:backend/onyx/server/features/mcp/oauth.py:377:        expected_refresh_token: str | None = None,
HEAD:backend/onyx/server/features/mcp/oauth.py:378:        require_refresh_token_match: bool = False,
HEAD:backend/onyx/server/features/mcp/oauth.py:384:            if require_refresh_token_match and (
HEAD:backend/onyx/server/features/mcp/oauth.py:385:                expected_refresh_token is None
HEAD:backend/onyx/server/features/mcp/oauth.py:386:                or (existing_tokens_raw or {}).get("refresh_token")
HEAD:backend/onyx/server/features/mcp/oauth.py:387:                != expected_refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:442:                preserve_existing_refresh_token=preserve_existing_refresh_token,
HEAD:backend/onyx/server/features/mcp/oauth.py:480:                    "refresh_token_persisted": bool(
HEAD:backend/onyx/server/features/mcp/oauth.py:481:                        persisted_token_dict.get("refresh_token")
HEAD:backend/onyx/server/features/mcp/oauth.py:483:                    "refresh_token_replaced": bool(
HEAD:backend/onyx/server/features/mcp/oauth.py:484:                        tokens.refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:485:                        and tokens.refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:486:                        != (existing_tokens_raw or {}).get("refresh_token")
HEAD:backend/onyx/server/features/mcp/oauth.py:496:        self, redeemed_refresh_token: str | None
HEAD:backend/onyx/server/features/mcp/oauth.py:502:        ``redeemed_refresh_token``: a concurrent refresh or reconnect already
HEAD:backend/onyx/server/features/mcp/oauth.py:512:                redeemed_refresh_token is None
HEAD:backend/onyx/server/features/mcp/oauth.py:513:                or stored_tokens.get("refresh_token") != redeemed_refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:694:        self.redeemed_refresh_token: str | None = None
HEAD:backend/onyx/server/features/mcp/oauth.py:829:        if not context.can_refresh_token():
HEAD:backend/onyx/server/features/mcp/oauth.py:840:        refresh_request = await self._refresh_token()
HEAD:backend/onyx/server/features/mcp/oauth.py:874:    async def _refresh_token(self) -> httpx.Request:
HEAD:backend/onyx/server/features/mcp/oauth.py:878:        self.redeemed_refresh_token = (
HEAD:backend/onyx/server/features/mcp/oauth.py:879:            current_tokens.refresh_token if current_tokens else None
HEAD:backend/onyx/server/features/mcp/oauth.py:882:        request = await super()._refresh_token()
HEAD:backend/onyx/server/features/mcp/oauth.py:892:                refresh_token_present=bool(
HEAD:backend/onyx/server/features/mcp/oauth.py:894:                    and self.context.current_tokens.refresh_token
HEAD:backend/onyx/server/features/mcp/oauth.py:900:    async def _persist_refresh_tokens(self, tokens: OAuthToken) -> bool:
HEAD:backend/onyx/server/features/mcp/oauth.py:910:                self.redeemed_refresh_token,
HEAD:backend/onyx/server/features/mcp/oauth.py:938:                if await storage.discard_persisted_tokens(self.redeemed_refresh_token):
HEAD:backend/onyx/server/features/mcp/oauth.py:955:        if not await self._persist_refresh_tokens(token_response):
HEAD:backend/onyx/server/features/mcp/oauth.py:1014:            grant_types=["authorization_code", "refresh_token"],
HEAD:backend/onyx/server/features/oauth_config/api.py:14:    delete_oauth_config,
HEAD:backend/onyx/server/features/oauth_config/api.py:15:    delete_user_oauth_token,
HEAD:backend/onyx/server/features/oauth_config/api.py:173:@admin_router.delete("/{oauth_config_id}")
HEAD:backend/onyx/server/features/oauth_config/api.py:174:def delete_oauth_config_endpoint(
HEAD:backend/onyx/server/features/oauth_config/api.py:181:    """Delete an OAuth configuration (owner or admin)."""
HEAD:backend/onyx/server/features/oauth_config/api.py:190:        delete_oauth_config(oauth_config_id, db_session)
HEAD:backend/onyx/server/features/oauth_config/api.py:297:@router.delete("/{oauth_config_id}/token")
HEAD:backend/onyx/server/features/oauth_config/api.py:298:def revoke_oauth_token(
HEAD:backend/onyx/server/features/oauth_config/api.py:304:    Revoke (delete) the current user's OAuth token for a specific OAuth config.
HEAD:backend/onyx/server/features/oauth_config/api.py:307:        delete_user_oauth_token(oauth_config_id, user.id, db_session)
HEAD:backend/onyx/server/features/tool/api.py:103:    every action on it: edit, delete, toggle, and OAuth config."""
HEAD:backend/onyx/server/federated/api.py:617:@router.delete("/{id}/oauth")
HEAD:backend/onyx/server/federated/api.py:618:def disconnect_oauth_token(
HEAD:backend/onyx/server/federated/api.py:623:    """Disconnect OAuth token for the current user from a federated connector"""
HEAD:backend/onyx/server/federated/api.py:629:    # Find and delete the user's OAuth token
HEAD:backend/onyx/server/federated/api.py:637:        db_session.delete(oauth_token)
HEAD:backend/onyx/server/federated/models.py:35:    refresh_token: str | None = None
HEAD:backend/onyx/server/manage/administrative.py:170:        error = f"Connector with ID '{connector_id}' and credential ID '{credential_id}' does not exist. Has it already been deleted?"
HEAD:backend/onyx/server/pat/api.py:94:@router.delete("/{token_id}")
HEAD:backend/onyx/server/pat/api.py:95:def delete_token(
HEAD:backend/onyx/server/pat/api.py:100:    """Delete (revoke) personal access token. Only owner can revoke their own tokens."""
HEAD:backend/onyx/server/pat/api.py:101:    success = revoke_pat(db_session, token_id, user.id, pat_type=PatType.USER)
HEAD:backend/onyx/server/pat/api.py:106:    logger.info("User %s revoked token %s", user.email, token_id)
HEAD:backend/onyx/utils/audit.py:104:    CREDENTIAL_DELETE = "credential.delete"
HEAD:backend/onyx/utils/audit.py:150:    AuditAction.CREDENTIAL_DELETE: OCSFEventClass.API_ACTIVITY,
```
Credential revocation must be considered separately from capability removal.
## Asynchronous Queue Propagation
Evidence lines: 650
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
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:16:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:17:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:27:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:36:                    "Task with task.task_id=%r failed; it is being deleted now",
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:37:                    task.task_id,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:39:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:4:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:8:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:9:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:11:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:13:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:14:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:71:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:72:    name=OnyxCeleryTask.CLOUD_BEAT_TASK_GENERATOR,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:80:    queue: str = OnyxCeleryTask.DEFAULT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:81:    priority: int = OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:93:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:169:            if current_time - last_lock_time >= (CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:192:            self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:197:                queue=queue,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:8:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:9:from celery.exceptions import SoftTimeLimitExceeded
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:42:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:43:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:44:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:206:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:215:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:222:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:261:            # clear any permission fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:265:                r_celery = celery_get_broker_client(self.app)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:318:    app: Celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:373:            celery_task_id=None,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:377:        result = app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:384:            task_id=custom_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:385:            priority=OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:388:        # fill in the celery task id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:389:        payload.celery_task_id = result.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:409:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:454:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:475:        if payload.celery_task_id is None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:579:                celery_task_id=payload.celery_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:794:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:801:    queue_len = celery_get_queue_length(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:807:    queued_upsert_tasks = celery_get_queued_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:810:    reserved_generator_tasks = celery_get_unacked_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:829:            r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:843:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:852:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:862:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:907:    if not payload.celery_task_id:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:913:    found = celery_find_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:914:        payload.celery_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:916:        r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:919:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:923:    if payload.celery_task_id in reserved_tasks:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:924:        # the celery task was prefetched and is reserved within a worker
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:928:    # look up every task in the current taskset in the celery queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:929:    # every entry in the taskset should have an associated entry in the celery task queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:930:    # because we get the celery tasks first, the entries in our own permissions taskset
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:931:    # should be roughly a subset of the tasks in celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:936:    # TODO: if the number of tasks in celery is much lower than than the taskset length
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:938:    # must not exist in celery.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:941:    tasks_not_in_celery = 0  # a non-zero number after completing our check is bad
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:953:        tasks_not_in_celery += 1
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:959:    # we're active if there are still tasks to run and those tasks all exist in celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:960:    if tasks_scanned > 0 and tasks_not_in_celery == 0:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:966:    #     logger.info(f"{payload.celery_task_id} is currently executing.")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:968:    # if we get here, we didn't find any direct indication that the associated celery tasks exist,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:975:    # celery tasks don't exist and the active signal has expired, possibly due to a crash. Clean it up.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:978:        "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1017:        # NOTE: Celery's soft_time_limit does not work with thread pools,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1038:                CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:7:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:8:from celery.exceptions import SoftTimeLimitExceeded
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
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:163:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:164:    name=OnyxCeleryTask.CHECK_FOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:170:    # we need to use celery's redis client to access its redis data
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:177:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:235:            # clear fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:239:                r_celery = celery_get_broker_client(self.app)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:272:    app: Celery,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:314:            celery_task_id=None,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:318:        custom_task_id = f"{redis_connector.external_group_sync.taskset_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:320:        result = app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:321:            OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:326:            queue=OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:327:            task_id=custom_task_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:328:            priority=OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:331:        payload.celery_task_id = result.id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:351:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:352:    name=OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:378:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:400:        if payload.celery_task_id is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:418:        timeout=CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:578:                # NOTE: Celery's soft_time_limit does not work with thread pools,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:681:    celery_app: Celery,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:684:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:687:    reserved_tasks = celery_get_unacked_task_ids(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:688:        OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:704:            r_celery,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:715:    r_celery: Redis,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:717:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:724:    1.2. When the task is seen in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:734:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:778:    if not payload.celery_task_id:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:782:    found = celery_find_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:786:        # the celery task exists in the redis queue
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:790:    if payload.celery_task_id in reserved_tasks:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:795:    # if we get here, we didn't find any direct indication that the associated celery tasks exist,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:802:    # celery tasks don't exist and the active signal has expired, possibly due to a crash. Clean it up.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:806:            "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:1:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:4:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:14:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:15:    name=OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:2:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:16:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:24:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:25:    name=OnyxCeleryTask.CHECK_LICENSE_EXPIRY_NOTIFICATIONS,
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:4:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:19:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:82:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:83:    name=OnyxCeleryTask.RECLAIM_LICENSE,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:3:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:11:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:24:# TODO(andrei): Kubernetes coverage is partial by design as of now. A celery
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:32:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:33:    name=OnyxCeleryTask.EXPORT_LOGS_COLLECT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:62:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:63:    name=OnyxCeleryTask.EXPORT_LOGS_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:5:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:13:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:30:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:31:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:54:    task_id = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:66:                task_id=task_id,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:90:            logger.exception("Failed to export query history with task_id=%r", task_id)
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:93:                task_id=task_id,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:98:    report_name = construct_query_history_report_name(task_id)
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:117:                task_id=task_id,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:125:                task_id=task_id,
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:8:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:12:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:18:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:19:    name=OnyxCeleryTask.REVALIDATE_SSO_DOMAINS_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:9:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:12:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:16:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:17:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:37:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:38:    name=OnyxCeleryTask.CLOUD_CHECK_AVAILABLE_TENANTS,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:39:    queue=OnyxCeleryQueues.MONITORING,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:5:from ee.onyx.background.celery_utils import should_perform_chat_ttl_check
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:8:    CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:10:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:11:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:12:    OnyxCeleryTask,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:54:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:55:    name=OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:98:        [chain_token, str(CELERY_CHAT_TTL_DELETE_TASK_EXPIRES)],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:129:            self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:130:                OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:136:                queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:137:                priority=OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:138:                expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:147:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:148:    name=OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:178:        ex=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:183:        self.app.send_task(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:184:            OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:190:            queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:191:            priority=OnyxCeleryPriority.LOW,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:192:            expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:4:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:7:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:14:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:15:    name=OnyxCeleryTask.GENERATE_USAGE_REPORT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:9:from onyx.background.celery.apps.app_base import task_logger
HEAD:backend/ee/onyx/background/task_name_builders.py:3:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/background/task_name_builders.py:5:QUERY_HISTORY_TASK_NAME_PREFIX = OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK
HEAD:backend/ee/onyx/configs/app_configs.py:130:# Celery Job Frequency
HEAD:backend/ee/onyx/db/query_history.py:13:from onyx.db.models import ChatMessage, ChatMessageFeedback, ChatSession, TaskQueueState
HEAD:backend/ee/onyx/db/query_history.py:194:) -> list[TaskQueueState]:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:48:    celery soft_time_limit (inert on thread pools) never fire — every long
HEAD:backend/ee/onyx/hooks/executor.py:3:Usage (Celery tasks and FastAPI handlers):
HEAD:backend/ee/onyx/server/documents/cc_pair.py:6:from ee.onyx.background.celery.tasks.doc_permission_syncing.tasks import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:9:from ee.onyx.background.celery.tasks.external_group_syncing.tasks import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:13:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/server/evals/api.py:4:from onyx.background.celery.apps.client import celery_app as client_app
HEAD:backend/ee/onyx/server/evals/api.py:5:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/server/evals/api.py:25:    client_app.send_task(
HEAD:backend/ee/onyx/server/evals/api.py:26:        OnyxCeleryTask.EVAL_RUN_TASK,
HEAD:backend/ee/onyx/server/log_export/api.py:28:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/server/log_export/api.py:32:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/server/log_export/api.py:33:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/server/log_export/api.py:34:    OnyxCeleryTask,
HEAD:backend/ee/onyx/server/log_export/api.py:98:    "primary": OnyxCeleryQueues.PRIMARY,
HEAD:backend/ee/onyx/server/log_export/api.py:99:    "light": OnyxCeleryQueues.VESPA_METADATA_SYNC,
HEAD:backend/ee/onyx/server/log_export/api.py:100:    "heavy": OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/server/log_export/api.py:101:    "docprocessing": OnyxCeleryQueues.DOCPROCESSING,
HEAD:backend/ee/onyx/server/log_export/api.py:102:    "docfetching": OnyxCeleryQueues.CONNECTOR_DOC_FETCHING,
HEAD:backend/ee/onyx/server/log_export/api.py:103:    "user_file_processing": OnyxCeleryQueues.USER_FILE_PROCESSING,
HEAD:backend/ee/onyx/server/log_export/api.py:104:    "scheduled_tasks": OnyxCeleryQueues.SCHEDULED_TASKS,
HEAD:backend/ee/onyx/server/log_export/api.py:105:    "monitoring": OnyxCeleryQueues.MONITORING,
HEAD:backend/ee/onyx/server/log_export/api.py:142:    The fan-out is skipped on deployments that have no celery broker (the
HEAD:backend/ee/onyx/server/log_export/api.py:171:        # onyx-lite overlay), there is no broker behind ``send_task`` and no
HEAD:backend/ee/onyx/server/log_export/api.py:178:                "Log export fan-out skipped: this deployment has no celery "
HEAD:backend/ee/onyx/server/log_export/api.py:185:                    client_app.send_task(
HEAD:backend/ee/onyx/server/log_export/api.py:186:                        OnyxCeleryTask.EXPORT_LOGS_COLLECT_TASK,
HEAD:backend/ee/onyx/server/log_export/api.py:187:                        priority=OnyxCeleryPriority.HIGHEST,
HEAD:backend/ee/onyx/server/log_export/api.py:188:                        queue=queue,
HEAD:backend/ee/onyx/server/log_export/api.py:219:        # No celery worker runs in the api_server container, so its logs are
HEAD:backend/ee/onyx/server/log_export/collection.py:4:per-worker celery collector tasks once fan-out collection lands.
HEAD:backend/ee/onyx/server/log_export/storage.py:6:celery tasks and the log-export API endpoints.
HEAD:backend/ee/onyx/server/query_history/api.py:26:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/server/query_history/api.py:34:    OnyxCeleryPriority,
HEAD:backend/ee/onyx/server/query_history/api.py:35:    OnyxCeleryQueues,
HEAD:backend/ee/onyx/server/query_history/api.py:36:    OnyxCeleryTask,
HEAD:backend/ee/onyx/server/query_history/api.py:329:    task_id_uuid = uuid.uuid4()
HEAD:backend/ee/onyx/server/query_history/api.py:330:    task_id = str(task_id_uuid)
HEAD:backend/ee/onyx/server/query_history/api.py:336:        task_id=task_id,
HEAD:backend/ee/onyx/server/query_history/api.py:341:    client_app.send_task(
HEAD:backend/ee/onyx/server/query_history/api.py:342:        OnyxCeleryTask.EXPORT_QUERY_HISTORY_TASK,
HEAD:backend/ee/onyx/server/query_history/api.py:343:        task_id=task_id,
HEAD:backend/ee/onyx/server/query_history/api.py:344:        priority=OnyxCeleryPriority.MEDIUM,
HEAD:backend/ee/onyx/server/query_history/api.py:345:        queue=OnyxCeleryQueues.CSV_GENERATION,
HEAD:backend/ee/onyx/server/query_history/api.py:354:    return {"request_id": task_id}
HEAD:backend/ee/onyx/server/query_history/api.py:365:    task = get_task_with_id(db_session=db_session, task_id=request_id)
HEAD:backend/ee/onyx/server/query_history/api.py:424:    task = get_task_with_id(db_session=db_session, task_id=request_id)
HEAD:backend/ee/onyx/server/query_history/models.py:8:from onyx.background.task_utils import extract_task_id_from_query_history_report_name
HEAD:backend/ee/onyx/server/query_history/models.py:11:from onyx.db.models import ChatMessage, ChatSession, FileRecord, TaskQueueState
HEAD:backend/ee/onyx/server/query_history/models.py:221:    task_id: str
HEAD:backend/ee/onyx/server/query_history/models.py:230:        task_queue_state: TaskQueueState,
HEAD:backend/ee/onyx/server/query_history/models.py:232:        start_end = task_queue_state.task_name.removeprefix(
HEAD:backend/ee/onyx/server/query_history/models.py:237:        if not task_queue_state.start_time:
HEAD:backend/ee/onyx/server/query_history/models.py:241:            task_id=task_queue_state.task_id,
HEAD:backend/ee/onyx/server/query_history/models.py:242:            status=task_queue_state.status,
HEAD:backend/ee/onyx/server/query_history/models.py:245:            start_time=task_queue_state.start_time,
HEAD:backend/ee/onyx/server/query_history/models.py:259:        task_id = extract_task_id_from_query_history_report_name(file.file_id)
HEAD:backend/ee/onyx/server/query_history/models.py:262:            task_id=task_id,
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:17:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:18:from onyx.configs.constants import OnyxCeleryTask
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:57:    client_app.send_task(
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:58:        OnyxCeleryTask.GENERATE_USAGE_REPORT_TASK,
HEAD:backend/ee/onyx/server/user_group/api.py:53:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/ee/onyx/server/user_group/api.py:54:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/server/user_group/api.py:56:from onyx.configs.constants import PUBLIC_API_TAGS, OnyxCeleryPriority, OnyxCeleryTask
HEAD:backend/ee/onyx/server/user_group/api.py:605:        client_app.send_task(
HEAD:backend/ee/onyx/server/user_group/api.py:606:            OnyxCeleryTask.CHECK_FOR_VESPA_SYNC_TASK,
HEAD:backend/ee/onyx/server/user_group/api.py:608:            priority=OnyxCeleryPriority.HIGH,
HEAD:backend/ee/onyx/utils/license.py:26:from onyx.background.celery.versioned_apps.client import app as client_app
HEAD:backend/ee/onyx/utils/license.py:30:from onyx.configs.constants import OnyxCeleryPriority, OnyxCeleryTask
HEAD:backend/ee/onyx/utils/license.py:522:    # Both the debounce and the broker behind send_task are this Redis. Where
HEAD:backend/ee/onyx/utils/license.py:546:            client_app.send_task(
HEAD:backend/ee/onyx/utils/license.py:547:                OnyxCeleryTask.RECLAIM_LICENSE,
HEAD:backend/ee/onyx/utils/license.py:549:                priority=OnyxCeleryPriority.HIGH,
HEAD:backend/ee/onyx/utils/telemetry.py:18:    is ``None`` outside a request (e.g. Celery), in which case ``$ip``
HEAD:backend/onyx/background/README.md:15:| Primary                   | `apps/primary.py`              | `celery`                                                                                                             |
HEAD:backend/onyx/background/README.md:22:| Background (consolidated) | `apps/background.py`           | All queues above except `celery`                                                                                     |
HEAD:backend/onyx/background/README.md:28:| **Beat**   | `beat.py`   | Celery beat scheduler with `DynamicTenantScheduler` that generates per-tenant periodic task schedules |
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
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
HEAD:backend/onyx/background/celery/apps/app_base.py:20:from sentry_sdk.integrations.celery import CeleryIntegration
HEAD:backend/onyx/background/celery/apps/app_base.py:24:from onyx.background.celery.apps.task_formatters import (
HEAD:backend/onyx/background/celery/apps/app_base.py:25:    CeleryTaskColoredFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:26:    CeleryTaskJsonFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:27:    CeleryTaskPlainFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:29:from onyx.background.celery.celery_utils import (
HEAD:backend/onyx/background/celery/apps/app_base.py:30:    celery_is_worker_primary,
HEAD:backend/onyx/background/celery/apps/app_base.py:33:from onyx.background.celery.tasks.vespa.document_sync import (
HEAD:backend/onyx/background/celery/apps/app_base.py:42:from onyx.configs.constants import ONYX_CLOUD_CELERY_TASK_PREFIX, OnyxRedisLocks
HEAD:backend/onyx/background/celery/apps/app_base.py:69:    SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:83:        traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:84:        integrations=[CeleryIntegration()],
HEAD:backend/onyx/background/celery/apps/app_base.py:99:    Intentionally ungated, like Celery's built-in shutdown/terminate/revoke control
HEAD:backend/onyx/background/celery/apps/app_base.py:102:    from celery.worker import state as worker_state
HEAD:backend/onyx/background/celery/apps/app_base.py:113:    abstract = True  # So Celery knows not to register this as a real task.
HEAD:backend/onyx/background/celery/apps/app_base.py:131:@before_task_publish.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:142:@task_prerun.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:145:    task_id: str | None = None,  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:162:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/app_base.py:185:        "Task %s (ID: %s) completed with state: %s", task.name, task_id, state
HEAD:backend/onyx/background/celery/apps/app_base.py:191:    if not task_id:
HEAD:backend/onyx/background/celery/apps/app_base.py:194:    if task.name.startswith(ONYX_CLOUD_CELERY_TASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:198:    # Get tenant_id directly from kwargs- each celery task has a tenant_id kwarg
HEAD:backend/onyx/background/celery/apps/app_base.py:200:        logger.error("Task %s (ID: %s) is missing kwargs", task.name, task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:208:        task_id,
HEAD:backend/onyx/background/celery/apps/app_base.py:218:    if task_id.startswith(DOCUMENT_SYNC_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:219:        r.srem(DOCUMENT_SYNC_TASKSET_KEY, task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:222:    if task_id.startswith(RedisDocumentSet.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:223:        document_set_id = RedisDocumentSet.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:226:            r.srem(rds.taskset_key, task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:229:    if task_id.startswith(RedisUserGroup.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:230:        usergroup_id = RedisUserGroup.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:233:            r.srem(rug.taskset_key, task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:237:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:242:    if task_id.startswith(RedisConnectorPrune.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:243:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:245:            RedisConnectorPrune.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:248:    if task_id.startswith(RedisConnectorPermissionSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:249:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:252:                int(cc_pair_id), task_id, r
HEAD:backend/onyx/background/celery/apps/app_base.py:256:    if task_id.startswith(RedisConnectorExternalGroupSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:257:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:260:                int(cc_pair_id), task_id, r
HEAD:backend/onyx/background/celery/apps/app_base.py:275:    task_id = getattr(request, "id", None)  # ods: ignore[getattr]
HEAD:backend/onyx/background/celery/apps/app_base.py:276:    if not task_id:
HEAD:backend/onyx/background/celery/apps/app_base.py:279:    if not task_id.startswith(DOCUMENT_SYNC_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:286:    r.srem(DOCUMENT_SYNC_TASKSET_KEY, task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:289:def on_celeryd_init(
HEAD:backend/onyx/background/celery/apps/app_base.py:294:    """The first signal sent on celery worker startup"""
HEAD:backend/onyx/background/celery/apps/app_base.py:328:    Will raise WorkerShutdown to kill the celery worker if the timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:370:    Will raise WorkerShutdown to kill the celery worker if the timeout is reached."""
HEAD:backend/onyx/background/celery/apps/app_base.py:410:    logger.info("Running as a secondary celery worker: pid=%s", os.getpid())
HEAD:backend/onyx/background/celery/apps/app_base.py:444:    # https://medium.com/ambient-innovation/health-checks-for-celery-in-kubernetes-cf3274a3e106
HEAD:backend/onyx/background/celery/apps/app_base.py:445:    # https://github.com/celery/celery/issues/4079#issuecomment-1270085680
HEAD:backend/onyx/background/celery/apps/app_base.py:460:    if not celery_is_worker_primary(sender):
HEAD:backend/onyx/background/celery/apps/app_base.py:485:    Returns True iff --loglevel or -l was explicitly passed on the celery CLI.
HEAD:backend/onyx/background/celery/apps/app_base.py:489:    Celery substitutes its own default. To distinguish "operator passed it" (CLI
HEAD:backend/onyx/background/celery/apps/app_base.py:490:    should win) from "Celery defaulted it" (LOG_LEVEL env should win) we have to
HEAD:backend/onyx/background/celery/apps/app_base.py:506:    Returns the (level, human-readable explanation) for celery worker logging.
HEAD:backend/onyx/background/celery/apps/app_base.py:508:    Precedence: explicit --loglevel CLI flag > LOG_LEVEL env var > Celery
HEAD:backend/onyx/background/celery/apps/app_base.py:511:    server, model servers, and all Celery workers.
HEAD:backend/onyx/background/celery/apps/app_base.py:519:        return cli_loglevel, "celery --loglevel CLI arg"
HEAD:backend/onyx/background/celery/apps/app_base.py:528:    return cli_loglevel, "celery default (no --loglevel, no LOG_LEVEL)"
HEAD:backend/onyx/background/celery/apps/app_base.py:539:    # celery's config
HEAD:backend/onyx/background/celery/apps/app_base.py:590:        "Celery effective log level: %s (source: %s)",
HEAD:backend/onyx/background/celery/apps/app_base.py:601:        CeleryTaskJsonFormatter()
HEAD:backend/onyx/background/celery/apps/app_base.py:603:        else CeleryTaskColoredFormatter(log_format, datefmt="%m/%d/%Y %I:%M:%S %p")
HEAD:backend/onyx/background/celery/apps/app_base.py:613:            CeleryTaskJsonFormatter()
HEAD:backend/onyx/background/celery/apps/app_base.py:615:            else CeleryTaskPlainFormatter(log_format, datefmt="%m/%d/%Y %I:%M:%S %p")
HEAD:backend/onyx/background/celery/apps/app_base.py:623:    # hide celery task received spam
HEAD:backend/onyx/background/celery/apps/app_base.py:627:    # uncomment this to hide celery task succeeded/failed spam
HEAD:backend/onyx/background/celery/apps/app_base.py:656:@task_postrun.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:659:    task_id: str | None = None,  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:704:    requires = {"celery.worker.components:Timer"}
HEAD:backend/onyx/background/celery/apps/app_base.py:736:    "onyx.background.celery.tasks.connector_deletion",
HEAD:backend/onyx/background/celery/apps/app_base.py:737:    "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/app_base.py:738:    "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/app_base.py:739:    "onyx.background.celery.tasks.pruning",
HEAD:backend/onyx/background/celery/apps/app_base.py:740:    "onyx.background.celery.tasks.vespa",
HEAD:backend/onyx/background/celery/apps/app_base.py:741:    "onyx.background.celery.tasks.opensearch_migration",
HEAD:backend/onyx/background/celery/apps/app_base.py:742:    "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:743:    "onyx.background.celery.tasks.hierarchyfetching",
HEAD:backend/onyx/background/celery/apps/app_base.py:745:    "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:746:    "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:748:# NOTE: "onyx.background.celery.tasks.shared" is intentionally NOT in the set
HEAD:backend/onyx/background/celery/apps/app_base.py:749:# above. It contains celery_beat_heartbeat (which only writes to Redis) alongside
HEAD:backend/onyx/background/celery/apps/beat.py:5:from celery import Celery, signals
HEAD:backend/onyx/background/celery/apps/beat.py:6:from celery.beat import PersistentScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:7:from celery.signals import beat_init
HEAD:backend/onyx/background/celery/apps/beat.py:8:from celery.utils.log import get_task_logger
HEAD:backend/onyx/background/celery/apps/beat.py:10:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/beat.py:11:from onyx.background.celery.celery_utils import make_probe_path
HEAD:backend/onyx/background/celery/apps/beat.py:12:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:13:from onyx.configs.constants import POSTGRES_CELERY_BEAT_APP_NAME
HEAD:backend/onyx/background/celery/apps/beat.py:22:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/beat.py:23:celery_app.config_from_object("onyx.background.celery.configs.beat")
HEAD:backend/onyx/background/celery/apps/beat.py:84:        """Given a list of tenant id's, generates a new beat schedule for celery."""
HEAD:backend/onyx/background/celery/apps/beat.py:91:                "onyx.background.celery.tasks.beat_schedule",
HEAD:backend/onyx/background/celery/apps/beat.py:117:            "onyx.background.celery.tasks.beat_schedule", "get_tasks_to_schedule"
HEAD:backend/onyx/background/celery/apps/beat.py:155:        """Only updates the actual beat schedule on the celery app when it changes"""
HEAD:backend/onyx/background/celery/apps/beat.py:254:    # Celery beat shouldn't touch the db at all. But just setting a low minimum here.
HEAD:backend/onyx/background/celery/apps/beat.py:255:    SqlEngine.set_app_name(POSTGRES_CELERY_BEAT_APP_NAME)
HEAD:backend/onyx/background/celery/apps/beat.py:275:celery_app.conf.beat_scheduler = DynamicTenantScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:276:celery_app.conf.task_default_base = app_base.TenantAwareTask
HEAD:backend/onyx/background/celery/apps/client.py:1:from celery import Celery
HEAD:backend/onyx/background/celery/apps/client.py:3:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/client.py:5:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/client.py:6:celery_app.config_from_object("onyx.background.celery.configs.client")
HEAD:backend/onyx/background/celery/apps/client.py:7:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/docfetching.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docfetching.py:5:from celery.signals import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:6:    celeryd_init,
HEAD:backend/onyx/background/celery/apps/docfetching.py:13:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/docfetching.py:14:from onyx.background.celery.tasks.docfetching.worker_shutdown import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:17:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docfetching.py:19:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:20:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:21:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:22:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/docfetching.py:23:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docfetching.py:24:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docfetching.py:36:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docfetching.py:37:celery_app.config_from_object("onyx.background.celery.configs.docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:38:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:41:@signals.task_prerun.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:44:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/docfetching.py:50:    app_base.on_task_prerun(sender, task_id, task, args, kwargs, **kwds)
HEAD:backend/onyx/background/celery/apps/docfetching.py:51:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/docfetching.py:52:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:55:@signals.task_postrun.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:58:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/docfetching.py:66:    app_base.on_task_postrun(sender, task_id, task, args, kwargs, retval, state, **kwds)
HEAD:backend/onyx/background/celery/apps/docfetching.py:67:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/docfetching.py:68:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docfetching.py:71:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:73:    # task_retry signal doesn't pass task_id in kwargs; get it from
HEAD:backend/onyx/background/celery/apps/docfetching.py:75:    task_id = getattr(  # ods: ignore[getattr]
HEAD:backend/onyx/background/celery/apps/docfetching.py:80:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/docfetching.py:83:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:86:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/docfetching.py:89:@signals.task_rejected.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:92:    # The task name must be extracted from the Celery message headers.
HEAD:backend/onyx/background/celery/apps/docfetching.py:100:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/docfetching.py:103:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:104:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:105:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:112:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docfetching.py:157:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docfetching.py:159:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docfetching.py:162:            "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/docprocessing.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/docprocessing.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docprocessing.py:5:from celery.signals import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:6:    celeryd_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:13:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/docprocessing.py:14:from onyx.background.celery.tasks.docprocessing.batch_counters import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:18:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docprocessing.py:20:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:21:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:22:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:23:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:24:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:25:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:37:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:38:celery_app.config_from_object("onyx.background.celery.configs.docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:39:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docprocessing.py:42:@signals.task_prerun.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:45:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:51:    app_base.on_task_prerun(sender, task_id, task, args, kwargs, **kwds)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:52:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:53:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:54:    on_docprocessing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:57:@signals.task_postrun.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:60:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:68:    app_base.on_task_postrun(sender, task_id, task, args, kwargs, retval, state, **kwds)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:69:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:70:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:71:    on_docprocessing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:74:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:76:    # task_retry signal doesn't pass task_id in kwargs; get it from
HEAD:backend/onyx/background/celery/apps/docprocessing.py:78:    task_id = getattr(  # ods: ignore[getattr]
HEAD:backend/onyx/background/celery/apps/docprocessing.py:83:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:86:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:89:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:92:@signals.task_rejected.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:95:    # The task name must be extracted from the Celery message headers.
HEAD:backend/onyx/background/celery/apps/docprocessing.py:103:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:106:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:107:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:108:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:115:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:166:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:168:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docprocessing.py:171:            "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/docprocessing.py:172:            "onyx.background.celery.tasks.port",
HEAD:backend/onyx/background/celery/apps/heavy.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/heavy.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/heavy.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/heavy.py:7:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/heavy.py:8:from onyx.configs.constants import POSTGRES_CELERY_WORKER_HEAVY_APP_NAME
HEAD:backend/onyx/background/celery/apps/heavy.py:10:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/heavy.py:11:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/heavy.py:12:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/heavy.py:13:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/heavy.py:14:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/heavy.py:15:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/heavy.py:23:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/heavy.py:24:celery_app.config_from_object("onyx.background.celery.configs.heavy")
HEAD:backend/onyx/background/celery/apps/heavy.py:25:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/heavy.py:28:@signals.task_prerun.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:31:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/heavy.py:37:    app_base.on_task_prerun(sender, task_id, task, args, kwargs, **kwds)
HEAD:backend/onyx/background/celery/apps/heavy.py:38:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/heavy.py:41:@signals.task_postrun.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:44:    task_id: str | None = None,
HEAD:backend/onyx/background/celery/apps/heavy.py:52:    app_base.on_task_postrun(sender, task_id, task, args, kwargs, retval, state, **kwds)
HEAD:backend/onyx/background/celery/apps/heavy.py:53:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/heavy.py:56:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:58:    task_id = getattr(  # ods: ignore[getattr]
HEAD:backend/onyx/background/celery/apps/heavy.py:63:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/heavy.py:66:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:69:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/heavy.py:72:@signals.task_rejected.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:81:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/heavy.py:84:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:85:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:86:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:93:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_HEAVY_APP_NAME)
HEAD:backend/onyx/background/celery/apps/heavy.py:128:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/heavy.py:130:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/heavy.py:133:            "onyx.background.celery.tasks.pruning",
HEAD:backend/onyx/background/celery/apps/heavy.py:135:            "onyx.background.celery.tasks.build",
HEAD:backend/onyx/background/celery/apps/heavy.py:136:            "onyx.background.celery.tasks.hierarchyfetching",
HEAD:backend/onyx/background/celery/apps/heavy.py:137:            "onyx.background.celery.tasks.capability_checks",
HEAD:backend/onyx/background/celery/apps/light.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/light.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/light.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/light.py:7:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/light.py:8:from onyx.background.celery.celery_utils import httpx_init_vespa_pool
HEAD:backend/onyx/background/celery/apps/light.py:14:from onyx.configs.constants import POSTGRES_CELERY_WORKER_LIGHT_APP_NAME
HEAD:backend/onyx/background/celery/apps/light.py:16:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/light.py:17:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/light.py:18:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/light.py:19:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/light.py:20:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/light.py:21:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/light.py:29:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/light.py:30:celery_app.config_from_object("onyx.background.celery.configs.light")
HEAD:backend/onyx/background/celery/apps/light.py:31:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/light.py:34:@signals.task_prerun.connect
```
Asynchronous processing introduces delay, retries, failure states and
eventual-consistency windows.
## Background Lifecycle Tasks
Evidence lines: 650
```text
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:4:from ee.onyx.configs.app_configs import CHECK_TTL_MANAGEMENT_TASK_FREQUENCY_IN_HOURS
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:34:        "name": "check-ttl-management",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:35:        "task": OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:36:        "schedule": timedelta(hours=CHECK_TTL_MANAGEMENT_TASK_FREQUENCY_IN_HOURS),
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:43:        "name": "export-query-history-cleanup-task",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:44:        "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:59:            # Revoking stale routing is a security cleanup, so it must reach
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:71:            "name": "hook-execution-log-cleanup",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:72:            "task": OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:98:            "name": "check-ttl-management",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:99:            "task": OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:100:            "schedule": timedelta(hours=CHECK_TTL_MANAGEMENT_TASK_FREQUENCY_IN_HOURS),
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:107:            "name": "export-query-history-cleanup-task",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:108:            "task": OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:116:        # Log export is rejected in multi-tenant deployments, so its cleanup
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:119:            "name": "export-logs-cleanup-task",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:120:            "task": OnyxCeleryTask.EXPORT_LOGS_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:125:                # Cleanup belongs on the heavy worker; it shares the queue the
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:126:                # query-history cleanup uses rather than minting a new one,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:10:from onyx.db.tasks import delete_task_with_id
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:17:    name=OnyxCeleryTask.EXPORT_QUERY_HISTORY_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:21:def export_query_history_cleanup_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:27:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:36:                    "Task with task.task_id=%r failed; it is being deleted now",
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:39:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:20:    cleanup_expired,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:135:                        ttl_s = OnyxRuntime.get_tenant_work_gating_ttl_seconds()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:136:                        cleanup_expired(ttl_s)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:139:                            "tenant work gating: cleanup_expired failed"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:142:                    ttl_s = OnyxRuntime.get_tenant_work_gating_ttl_seconds()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:143:                    active_tenants = get_active_tenants(ttl_s)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:158:        # to ~10k+ inactive tenants. A small number of cleanup tasks (connector deletion,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:159:        # checkpoint/index attempt cleanup) need to run on gated tenants and pass
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:24:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:141:"""Jobs / utils for kicking off doc permissions sync tasks."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:317:def try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:347:        if redis_connector.prune.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:583:            callback = PermissionSyncCallback(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:630:                    f"Permission sync task timed out or stop signal detected: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:663:            f"Completed doc permission sync attempt {attempt_id}: {tasks_generated} docs, {docs_with_errors} errors"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:814:    # validate all existing permission sync jobs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:851:    1. This function renews the active signal with a 5 minute TTL under the following conditions
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:859:    3. The TTL allows us to get through the transitions on fence startup
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:862:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:889:    # it's a little sloppy, but just reset the fence for now if that happens
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:890:    # TODO: add intentional cleanup/abort logic
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1006:        self.last_tag: str = "PermissionSyncCallback.__init__"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:3:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:4:    source_group_sync_is_cc_pair_agnostic,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:6:from onyx.db.connector import mark_cc_pair_as_external_group_synced
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:11:def _get_all_cc_pair_ids_to_mark_as_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:14:    if not source_group_sync_is_cc_pair_agnostic(cc_pair.connector.source):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:23:def mark_all_relevant_cc_pairs_as_external_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:26:    """For some source types, one successful group sync run should count for all
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:28:    cc_pair_ids = _get_all_cc_pair_ids_to_mark_as_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:30:        mark_cc_pair_as_external_group_synced(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:13:from ee.onyx.background.celery.tasks.external_group_syncing.group_sync_utils import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:14:    mark_all_relevant_cc_pairs_as_external_group_synced,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:26:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:27:    get_all_cc_pair_agnostic_group_sync_sources,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:40:    CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:59:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:60:    complete_external_group_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:61:    create_external_group_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:62:    mark_external_group_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:63:    mark_external_group_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:67:from onyx.redis.redis_connector_ext_group_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:68:    RedisConnectorExternalGroupSync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:69:    RedisConnectorExternalGroupSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:75:    inc_group_sync_errors,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:76:    inc_group_sync_groups_processed,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:77:    inc_group_sync_users_processed,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:78:    observe_group_sync_duration,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:79:    observe_group_sync_upsert_duration,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:92:def _fail_external_group_sync_attempt(attempt_id: int, error_msg: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:93:    """Helper to mark an external group sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:95:        mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:118:def _is_external_group_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:119:    """Returns boolean indicating if external group sync is due."""
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:123:            f"Received non-sync CC Pair {cc_pair.id} for external group sync. Actual access type: {cc_pair.access_type}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:129:            f"Skipping group sync for CC Pair {cc_pair.id} - CC Pair is being deleted"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:136:            f"Skipping group sync for CC Pair {cc_pair.id} - no sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:140:    # If there is not group sync function for the connector, we don't run the sync
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:142:    if sync_config.group_sync_config is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:144:            f"Skipping group sync for CC Pair {cc_pair.id} - no group sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:149:    last_ext_group_sync = cc_pair.last_time_external_group_sync
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:150:    if last_ext_group_sync is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:153:    source_sync_period = sync_config.group_sync_config.group_sync_frequency
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:156:    next_sync = last_ext_group_sync + timedelta(seconds=source_sync_period)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:164:    name=OnyxCeleryTask.CHECK_FOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:169:def check_for_external_group_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:193:            for source in get_all_cc_pair_agnostic_group_sync_sources():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:212:                if _is_external_group_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:216:        # whenever external-group sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:218:            maybe_mark_tenant_active(tenant_id, caller="external_group_sync")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:222:            payload_id = try_creating_external_group_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:229:                f"External group sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:234:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:240:                validate_external_group_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:245:                    "Exception while validating external group sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:249:                OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:260:            f"Unexpected check_for_external_group_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:267:    task_logger.info(f"check_for_external_group_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:271:def try_creating_external_group_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:285:        if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:287:                "Skipping external group sync for CC Pair %s - already running.",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:292:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:293:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:308:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:310:        payload = RedisConnectorExternalGroupSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:316:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:318:        custom_task_id = f"{redis_connector.external_group_sync.taskset_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:321:            OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:326:            queue=OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:332:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:338:            f"Unexpected try_creating_external_group_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:341:            f"Unexpected exception while trying to create external group sync task: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:346:        f"try_creating_external_group_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:352:    name=OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:359:def connector_external_group_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:365:    External group sync task for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:380:                f"connector_external_group_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:381:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:386:        if not redis_connector.external_group_sync.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:388:                f"connector_external_group_sync_generator_task - fence not found: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:389:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:394:        payload = redis_connector.external_group_sync.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:396:            msg = "connector_external_group_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:402:                "connector_external_group_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:403:                redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:409:            "connector_external_group_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:410:            redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:416:        OnyxRedisLocks.CONNECTOR_EXTERNAL_GROUP_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:418:        timeout=CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:424:            f"External group sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:430:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:432:        _perform_external_group_sync(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:447:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:450:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:453:        msg = f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:465:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:466:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:470:        redis_connector.external_group_sync.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:475:        f"External group sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:479:def _perform_external_group_sync(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:488:        attempt_id = create_external_group_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:493:            "Created external group sync attempt: %s for cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:499:        connector_type = _timed_perform_external_group_sync(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:506:        observe_group_sync_duration(time.monotonic() - sync_start, connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:509:def _timed_perform_external_group_sync(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:530:            _fail_external_group_sync_attempt(attempt_id, msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:533:        if sync_config.group_sync_config is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:534:            msg = f"No group sync config found for {source_type} for cc_pair: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:536:            _fail_external_group_sync_attempt(attempt_id, msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:539:        ext_group_sync_func = sync_config.group_sync_config.group_sync_func
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:542:        # This ensures cleanup always runs regardless of whether the current
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:543:        # sync succeeds — previously, cleanup only ran at the END of the sync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:562:        mark_external_group_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:563:        logger.info("Marked external group sync attempt %s as in progress", attempt_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:571:        total_group_memberships_synced = 0
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:575:            external_user_group_generator = ext_group_sync_func(tenant_id, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:583:                        f"External group sync task timed out: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:594:                total_group_memberships_synced += len(external_user_group.user_emails)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:625:            mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:633:            inc_group_sync_errors(connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:642:        observe_group_sync_upsert_duration(cumulative_upsert_time, connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:655:        complete_external_group_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:660:            total_group_memberships_synced=total_group_memberships_synced,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:664:            "Completed external group sync attempt %s: %s groups, %s users, %s memberships",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:668:            total_group_memberships_synced,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:671:        inc_group_sync_groups_processed(connector_type, total_groups_processed)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:672:        inc_group_sync_users_processed(connector_type, total_users_processed)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:674:        mark_all_relevant_cc_pairs_as_external_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:679:def validate_external_group_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:688:        OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:691:    # validate all existing external group sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:700:        validate_external_group_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:711:def validate_external_group_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:723:    1. This function renews the active signal with a 5 minute TTL under the following conditions
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:731:    3. The TTL allows us to get through the transitions on fence startup
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:734:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:745:            f"validate_external_group_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:761:        payload = redis_connector.external_group_sync.payload
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:764:            "validate_external_group_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:772:        redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:787:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:792:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:799:    if redis_connector.external_group_sync.active():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:805:            "validate_external_group_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:814:    redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:6:from onyx.db.hook import cleanup_old_execution_logs__no_commit
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:11:_HOOK_EXECUTION_LOG_RETENTION_DAYS: int = 30
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:15:    name=OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:20:def hook_execution_log_cleanup_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:23:            deleted: int = cleanup_old_execution_logs__no_commit(
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:25:                max_age_days=_HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:28:            if deleted:
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:30:                    "Deleted %s hook execution log(s) older than %s days.",
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:31:                    deleted,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:32:                    _HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:29:_THROTTLE_KEY_LEAD_UP = "license_reclaim_throttle"
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:30:_THROTTLE_KEY_URGENT = "license_reclaim_throttle_urgent"
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:32:# Consecutive attempts that found nothing newer. Outlives the throttle it sizes.
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:34:_IDLE_ROUNDS_TTL_SEC = 24 * 60 * 60
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:49:    Fails open: losing the throttle costs extra control-plane requests, and
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:53:    key = _THROTTLE_KEY_URGENT if urgent else _THROTTLE_KEY_LEAD_UP
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:58:        logger.debug("License reclaim throttle unavailable: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:70:            redis_client.delete(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:76:        pipe.expire(_IDLE_ROUNDS_KEY, _IDLE_ROUNDS_TTL_SEC)
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:8:    delete_expired_log_exports,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:63:    name=OnyxCeleryTask.EXPORT_LOGS_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:67:def export_logs_cleanup_task(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:71:    """Deletes log-export artifacts past their retention window."""
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:72:    delete_expired_log_exports()
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:18:    delete_task_with_id,
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:115:            delete_task_with_id(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:5:from ee.onyx.background.celery_utils import should_perform_chat_ttl_check
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:8:    CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:9:    CHAT_TTL_DELETE_BATCH_SIZE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:15:from onyx.db.chat import delete_chat_session, get_chat_sessions_older_than
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:46:    """Delete the chain marker only if ``chain_token`` still owns it."""
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:49:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:55:    name=OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:61:def perform_ttl_management_task(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:63:    retention_limit_days: float,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:71:    """Delete the oldest batch of expired chat sessions, then chain the next task.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:73:    Each run hard-deletes at most ``CHAT_TTL_DELETE_BATCH_SIZE`` of the *oldest*
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:76:    full batch is deleted (more sessions likely remain) it enqueues the next task
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:78:    in-flight marker so ``check_ttl_management_task`` can start a fresh chain.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:83:    extend nor delete the new chain's marker — it just exits. Only one chain runs
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:84:    per tenant at a time, so at most one light-worker thread does TTL work.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:87:    fails to delete is retried on every run. If the oldest ``CHAT_TTL_DELETE_BATCH_SIZE``
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:88:    sessions can never be deleted, the chain loops on them indefinitely (across
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:97:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:98:        [chain_token, str(CELERY_CHAT_TTL_DELETE_TASK_EXPIRES)],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:105:            retention_limit_days, db_session, limit=CHAT_TTL_DELETE_BATCH_SIZE
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:111:                delete_chat_session(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:115:                    include_deleted=True,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:116:                    hard_delete=True,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:120:                "Failed to delete chat session user_id=%s session_id=%s, continuing with remaining sessions",
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:127:    if len(old_chat_sessions) == CHAT_TTL_DELETE_BATCH_SIZE:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:130:                OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:132:                    "retention_limit_days": retention_limit_days,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:136:                queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:138:                expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:148:    name=OnyxCeleryTask.CHECK_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:154:def check_ttl_management_task(self: Task, *, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:155:    """Start a chat-retention cleanup chain if one isn't already running.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:157:    Deletion happens in ``perform_ttl_management_task``, which chains itself
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:163:    retention_limit_days = settings.maximum_chat_retention_days
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:165:        if not should_perform_chat_ttl_check(retention_limit_days, db_session):
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:167:    if retention_limit_days is None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:175:        OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:178:        ex=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:184:            OnyxCeleryTask.PERFORM_TTL_MANAGEMENT_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:186:                "retention_limit_days": retention_limit_days,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:190:            queue=OnyxCeleryQueues.CHAT_TTL_DELETION,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:192:            expires=CELERY_CHAT_TTL_DELETE_TASK_EXPIRES,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:4:    delete_user_group,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:6:    mark_user_group_as_synced,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:45:        f"User group sync progress: usergroup_id={usergroup_id} remaining={count} initial={initial_count}"
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:64:                mark_user_group_as_synced(db_session, user_group)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:66:                delete_user_group(db_session=db_session, user_group=user_group)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:77:                    f"Deleted usergroup: name={usergroup_name} id={usergroup_id}"
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:80:                mark_user_group_as_synced(db_session=db_session, user_group=user_group)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:23:from onyx.server.features.build.configs import SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:39:CLOUD_DOC_PERMISSION_SYNC_MULTIPLIER_DEFAULT = 1.0
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:53:        "name": "check-for-incognito-file-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:54:        "task": OnyxCeleryTask.CHECK_FOR_INCOGNITO_FILE_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:74:        "name": "check-for-user-file-delete",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:75:        "task": OnyxCeleryTask.CHECK_FOR_USER_FILE_DELETE,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:113:            # reclaim an index once its reindex has truly completed (a gated tenant's
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:114:            # deferred reindex never swaps / never drains, so it's never fetched).
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:120:        "name": "check-for-checkpoint-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:121:        "task": OnyxCeleryTask.CHECK_FOR_CHECKPOINT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:144:        "name": "check-for-index-attempt-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:145:        "task": OnyxCeleryTask.CHECK_FOR_INDEX_ATTEMPT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:227:        "name": "cleanup-stuck-scheduled-runs",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:228:        "task": OnyxCeleryTask.SCHEDULED_TASKS_CLEANUP_STUCK,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:238:        "name": "cleanup-idle-sandboxes",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:239:        "task": OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:242:        # the effective interval is SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS * 8;
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:244:        "schedule": timedelta(seconds=SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS),
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:260:                "name": "check-for-doc-permissions-sync",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:261:                "task": OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:270:                "name": "check-for-external-group-sync",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:271:                "task": OnyxCeleryTask.CHECK_FOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:329:                # If the task was not dequeued in this time, revoke it.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:346:    "check-for-checkpoint-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:347:    "check-for-index-attempt-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:348:    "check-for-doc-permissions-sync",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:349:    "check-for-external-group-sync",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:1:"""Celery tasks for sandbox operations (cleanup, etc.)."""
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:33:    name=OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:38:def cleanup_idle_sandboxes_task(self: Task, *, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:58:    task_logger.info(f"cleanup_idle_sandboxes_task starting for tenant {tenant_id}")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:62:        OnyxRedisLocks.CLEANUP_IDLE_SANDBOXES_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:68:        task_logger.info("cleanup_idle_sandboxes_task - lock not acquired, skipping")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:82:            maybe_mark_tenant_active(tenant_id, caller="sandbox_cleanup")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:211:        task_logger.exception("Error in cleanup_idle_sandboxes_task")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:218:    task_logger.info("cleanup_idle_sandboxes_task completed")
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:66:                # Deleted since the trigger; its report rows cascaded with it.
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:68:                    f"Skipping capability checks for deleted credential "
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:77:                    # Deleted since the trigger; its report row cascaded with
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:80:                        f"Skipping capability checks for deleted connector "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:30:    delete_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:35:    delete_all_documents_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:38:from onyx.db.document_set import delete_document_set_cc_pair_relationship__no_commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:46:from onyx.db.hierarchy import cleanup_unowned_hierarchy_nodes
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:47:from onyx.db.index_attempt import delete_index_attempts, get_recent_attempts_for_cc_pair
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:48:from onyx.db.permission_sync_attempt import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:49:    delete_doc_permission_sync_attempts__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:50:    delete_external_group_permission_sync_attempts__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:55:    cleanup_sync_records,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:59:from onyx.db.tag import delete_orphan_tags__no_commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:61:from onyx.redis.redis_connector_delete import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:62:    RedisConnectorDelete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:63:    RedisConnectorDeletePayload,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:87:def revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:104:                app.control.revoke(recent_index_attempts[0].celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:106:                    f"Revoked indexing task {recent_index_attempts[0].celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:112:        permissions_sync_payload = redis_connector.permissions.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:113:        if permissions_sync_payload and permissions_sync_payload.celery_task_id:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:114:            app.control.revoke(permissions_sync_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:116:                f"Revoked permissions sync task {permissions_sync_payload.celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:119:        task_logger.exception("Exception while revoking permissions sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:122:        prune_payload = redis_connector.prune.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:123:        if prune_payload and prune_payload.celery_task_id:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:124:            app.control.revoke(prune_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:125:            task_logger.info(f"Revoked pruning task {prune_payload.celery_task_id}.")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:130:        external_group_sync_payload = redis_connector.external_group_sync.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:131:        if external_group_sync_payload and external_group_sync_payload.celery_task_id:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:132:            app.control.revoke(external_group_sync_payload.celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:134:                f"Revoked external group sync task {external_group_sync_payload.celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:137:        task_logger.exception("Exception while revoking external group sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:177:        # collect cc_pair_ids and note whether any are in DELETING status
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:179:        has_deleting_cc_pair = False
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:184:                if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:185:                    has_deleting_cc_pair = True
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:188:        # DELETING status. Marking on bare cc_pair existence would keep
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:190:        # but almost none are actively being deleted on any given cycle.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:191:        if has_deleting_cc_pair:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:194:        # try running cleanup on the cc_pair_ids
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:199:                    try_generate_document_cc_pair_cleanup_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:203:                    # this means we wanted to start deleting but dependent tasks were running
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:204:                    # on the first error, we set a stop signal and revoke the dependent tasks
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:210:                        # one time revoke of celery tasks
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:212:                        revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:225:                            redis_connector.prune.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:227:                            redis_connector.external_group_sync.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:245:            if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:260:def try_generate_document_cc_pair_cleanup_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:281:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:294:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:297:        cleanup_sync_records(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:305:    redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:306:    fence_payload = RedisConnectorDeletePayload(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:311:    redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:334:            # A running port could re-add docs we're deleting (create-only write).
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:337:            # after its last write — making cleanup the last writer. A dead port is
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:351:        if redis_connector.prune.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:364:        redis_connector.delete.taskset_clear()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:370:        tasks_generated = redis_connector.delete.generate_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:386:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:390:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:405:        redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:426:    fence_data = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:439:    if r.exists(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:455:        credential_id_to_delete: int | None = None
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:456:        connector_id_to_delete: int | None = None
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:475:                    f"docs_deleted={fence_data.num_tasks} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:481:                redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:488:            delete_index_attempts(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:493:            # permission sync attempts
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:494:            delete_doc_permission_sync_attempts__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:498:            delete_external_group_permission_sync_attempts__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:504:            delete_document_set_cc_pair_relationship__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:511:            cleanup_user_groups = fetch_versioned_implementation_with_fallback(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:513:                "delete_user_group_cc_pair_relationship__no_commit",
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:516:            cleanup_user_groups(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:521:            # best-effort bounded orphan tag cleanup; a full drain would balloon
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:523:            delete_orphan_tags__no_commit(db_session)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:526:            connector_id_to_delete = cc_pair.connector_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:527:            credential_id_to_delete = cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:530:            # Explicitly delete document by connector credential pair records before deleting the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:531:            # This is needed because connector_id is a primary key in that table and cascading deletes won't work
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:532:            delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:534:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:535:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:542:            # related to the deleted DocumentByConnectorCredentialPair during commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:545:            # finally, delete the cc-pair
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:546:            delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:548:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:549:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:553:            deleted_raw_ids, reparented_nodes = cleanup_unowned_hierarchy_nodes(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:558:            # if there are no credentials left, delete the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:561:                connector_id=connector_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:565:                    "Connector deletion - Connector already deleted, skipping connector cleanup"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:569:                    "Connector deletion - Found no credentials left for connector, deleting connector"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:571:                db_session.delete(connector)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:574:            if deleted_raw_ids or reparented_nodes:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:586:                    f"Connector deletion hierarchy cleanup: cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:587:                    f"nodes_deleted={len(deleted_raw_ids)} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:621:                f"cc_pair={cc_pair_id} connector={connector_id_to_delete} credential={credential_id_to_delete}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:633:        f"connector={connector_id_to_delete} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:634:        f"credential={credential_id_to_delete} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:635:        f"docs_deleted={fence_data.num_tasks}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:638:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:666:        if not key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:693:    1. This function renews the active signal with a 5 minute TTL under the following conditions
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:701:    3. The TTL allows us to get through the transitions on fence startup
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:704:    More TTL clarification: it is seemingly impossible to exactly query Celery for
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:710:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:727:    if not redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:731:    # it's a little sloppy, but just reset the fence for now if that happens
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:732:    # TODO: add intentional cleanup/abort logic
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:734:        payload = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:743:        redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:766:    for member in r.sscan_iter(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:781:        redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:792:    if redis_connector.delete.active():
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:804:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:25:    reindex: bool,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:56:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:69:            from_beginning=reindex,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:177:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:182:            f"fence={redis_connector.delete.fence_key}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:361:    7) pulls all document IDs from the source and compares those IDs to locally stored documents and deletes
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:376:    - non-checkpointed connectors/ new runs in general => delete the old document batches from the file store and do the new run
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:1:"""Celery task for executing a targeted reindex.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:7:`onyx.background.indexing.run_targeted_reindex`.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:19:from onyx.db.targeted_reindex import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:20:    get_index_attempts_for_targeted_reindex_job,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:21:    get_targeted_reindex_job,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:27:_TARGETED_REINDEX_SOFT_TIME_LIMIT = 60 * 30  # 30 minutes
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:28:_TARGETED_REINDEX_TIME_LIMIT = _TARGETED_REINDEX_SOFT_TIME_LIMIT + 60
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:31:def run_targeted_reindex(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:32:    targeted_reindex_job_id: int,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:35:    """Body of the targeted-reindex task. Lifted out of the @shared_task
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:38:    from onyx.background.indexing.run_targeted_reindex import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:46:            "targeted_reindex_job_id": targeted_reindex_job_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:52:        job = get_targeted_reindex_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:61:        attempts = get_index_attempts_for_targeted_reindex_job(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:62:            db_session, targeted_reindex_job_id
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:77:            target_rows = get_targets_for_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:81:                "Targeted reindex starting: %d cc_pair(s), %d target(s)",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:120:                        "cc_pair_id=%s connector does not support targeted reindex",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:129:                db_session, targeted_reindex_job_id, landed_keys
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:163:            # The cleanup itself is wrapped so a secondary failure (e.g.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:167:            log.exception("Targeted reindex task failed; marking job FAILED")
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:170:                job = get_targeted_reindex_job(db_session, targeted_reindex_job_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:172:                    attempts = get_index_attempts_for_targeted_reindex_job(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:173:                        db_session, targeted_reindex_job_id
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:191:        "Targeted reindex done: resolved=%d runtime_skipped=%d still_failing=%d",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:199:    name=OnyxCeleryTask.TARGETED_REINDEX_TASK,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:200:    soft_time_limit=_TARGETED_REINDEX_SOFT_TIME_LIMIT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:201:    time_limit=_TARGETED_REINDEX_TIME_LIMIT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:204:def targeted_reindex_task(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:207:    targeted_reindex_job_id: int,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:210:    run_targeted_reindex(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:211:        targeted_reindex_job_id=targeted_reindex_job_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:33:from onyx.background.celery.tasks.docprocessing.targeted_reindex_task import (  # noqa: F401  # registers @shared_task with celery
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:34:    targeted_reindex_task,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:43:    cleanup_checkpoint,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:47:    cleanup_index_attempts,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:117:from onyx.file_store.staging import cleanup_staged_files_for_attempt
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:204:                    # Synthetic attempts spawned by the targeted-reindex flow
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:207:                    IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:508:            storage.cleanup_all_batches()
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:510:            logger.exception("Failed to cleanup storage after monitoring failure")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:666:        storage.cleanup_all_batches()
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:676:        with get_session_with_current_tenant() as cleanup_session:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:677:            cleanup_staged_files_for_attempt(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:679:                db_session=cleanup_session,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:683:            "Failed to run attempt-end staging cleanup; orphans will be "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:807:        reindex = False
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:810:            if cc_pair.indexing_trigger == IndexingMode.REINDEX:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:811:                reindex = True
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:828:            reindex,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1105:                        IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1165:                        IndexAttempt.targeted_reindex_job_id.is_(None),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1222:    name=OnyxCeleryTask.CHECK_FOR_CHECKPOINT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1226:def check_for_checkpoint_cleanup(self: Task, *, tenant_id: str) -> None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1231:        OnyxRedisLocks.CHECK_CHECKPOINT_CLEANUP_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1248:                    OnyxCeleryTask.CLEANUP_CHECKPOINT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1253:                    queue=OnyxCeleryQueues.CHECKPOINT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1257:        task_logger.exception("Unexpected exception during checkpoint cleanup")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1265:                    f"check_for_checkpoint_cleanup - Lock not owned on completion: tenant={tenant_id}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1271:    name=OnyxCeleryTask.CLEANUP_CHECKPOINT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1274:def cleanup_checkpoint_task(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1286:            cleanup_checkpoint(db_session, index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1291:            f"cleanup_checkpoint_task completed: tenant_id={tenant_id} index_attempt_id={index_attempt_id} elapsed={elapsed:.2f}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1297:    name=OnyxCeleryTask.CHECK_FOR_INDEX_ATTEMPT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1301:def check_for_index_attempt_cleanup(self: Task, *, tenant_id: str) -> None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1306:        OnyxRedisLocks.CHECK_INDEX_ATTEMPT_CLEANUP_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1313:            f"check_for_index_attempt_cleanup - Lock not acquired: tenant={tenant_id}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1323:            # of index attempts since they were never deleted. After that, the number will be
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1327:                    "check_for_index_attempt_cleanup - No index attempts to cleanup"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1334:                    f"check_for_index_attempt_cleanup - Cleaning up index attempts {len(batch)}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1337:                    OnyxCeleryTask.CLEANUP_INDEX_ATTEMPT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1342:                    queue=OnyxCeleryQueues.INDEX_ATTEMPT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1346:        task_logger.exception("Unexpected exception during index attempt cleanup check")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1354:                    f"check_for_index_attempt_cleanup - Lock not owned on completion: tenant={tenant_id}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1360:    name=OnyxCeleryTask.CLEANUP_INDEX_ATTEMPT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1363:def cleanup_index_attempt_task(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1374:            cleanup_index_attempts(db_session, index_attempt_ids)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1380:            f"cleanup_index_attempt_task completed: tenant_id={tenant_id} "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1977:        storage.delete_batch_by_num(batch_num)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1987:        # via the _cleanup_thread_local decorator in search_nlp_models.py
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:2011:        # all post-indexing bookkeeping (coord update, telemetry, cleanup).
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:225:    # Legacy FUTURE reindex indexes once, then stops so the swap can fire. A
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:131:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:381:            if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:383:                    f"Skipping hierarchy fetching for deleting connector: cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:1:"""Old-index reclamation: delete every reclaim-tracked PAST index after a reindex.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:9:    SOAKING  -> (soak elapsed + new index can serve)                                -> DELETING
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:10:    DELETING -> (old index data gone, count-verified)                               -> RECLAIMED (row kept)
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:35:    OLD_INDEX_RETENTION_HOURS,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:45:    mark_cc_pairs_deleting_if_still_wont_port__no_commit,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:55:    advance_to_deleting__no_commit,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:76:# Per-DELETING-row wall-clock budget. On a whale (multi-tenant delete_by_query is
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:80:_DELETE_TIME_BUDGET_S = 60
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:82:# Per-row lock TTL. Must exceed a single dispatch's max runtime (the delete budget +
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:85:_RECLAIM_TASK_LOCK_TTL_S = 60 * 5
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:90:    IndexReclaimStatus.DELETING,
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:99:    """The new PRESENT index is healthy enough to serve before we delete the old one.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:123:    move the still-not-recoverable consented connectors to DELETING and start the soak."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:129:    # connector re-activated after consent was captured can't be clobbered into DELETING.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:130:    deleted = mark_cc_pairs_deleting_if_still_wont_port__no_commit(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:136:    if deleted:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:137:        # Kick the connector-deletion pipeline (crash-resumable) now that DELETING is
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:138:        # committed and the worker can see it; mirrors administrative.py's delete trigger.
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:147:            "Old-index reclaim %s -> SOAKING (index=%s, cc_pairs deleted=%d).",
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:150:            len(deleted),
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:155:    """SOAKING: wait out the retention window, then require the new PRESENT index can
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:156:    serve before deleting the old one."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:160:    if datetime.now(timezone.utc) - anchor < timedelta(hours=OLD_INDEX_RETENTION_HOURS):
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:172:    if advance_to_deleting__no_commit(search_settings):
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:175:            "Old-index reclaim %s -> DELETING (index=%s).",
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:181:def _drive_deleting(db_session: Session, search_settings: SearchSettings) -> None:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:182:    """DELETING: delete the old index's data, looping bounded batches within a time
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:184:    RECLAIMED and KEEP it (we only delete the OpenSearch index, not the PAST row).
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:185:    INCOMPLETE leaves it DELETING for next tick."""
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:186:    # Don't delete while a canceled port task may still be writing to this FUTURE's index;
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:197:            f"{search_settings.index_name}; refusing to delete it."
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:205:    deadline = time.monotonic() + _DELETE_TIME_BUDGET_S
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:219:        # a bounded batch was deleted (progress) — reset attempts so a long drain can't trip BLOCKED
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:246:        elif status == IndexReclaimStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:247:            _drive_deleting(db_session, search_settings)
```
## Cache / Redis Invalidation
Evidence lines: 523
```text
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:70:            redis_client.delete(_IDLE_ROUNDS_KEY)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:76:        pipe.expire(_IDLE_ROUNDS_KEY, _IDLE_ROUNDS_TTL_SEC)
HEAD:backend/ee/onyx/db/license.py:26:LICENSE_CACHE_TTL_SECONDS = 86400  # 24 hours
HEAD:backend/ee/onyx/db/license.py:164:        # Under the cache lock: a store that committed just before this delete
HEAD:backend/ee/onyx/db/license.py:166:        # entry either lands before this invalidate or is never written.
HEAD:backend/ee/onyx/db/license.py:169:                invalidate_license_cache()
HEAD:backend/ee/onyx/db/license.py:171:            logger.warning("License deleted but cache invalidation failed: %s", e)
HEAD:backend/ee/onyx/db/license.py:258:def invalidate_license_cache(tenant_id: str | None = None) -> None:
HEAD:backend/ee/onyx/db/license.py:260:    Invalidate the license metadata cache (not the license itself).
HEAD:backend/ee/onyx/db/license.py:262:    Deletes the cached LicenseMetadata. The actual license in the database
HEAD:backend/ee/onyx/db/license.py:270:    cache.delete(LICENSE_METADATA_KEY)
HEAD:backend/ee/onyx/db/license.py:271:    logger.info("License cache invalidated")
HEAD:backend/ee/onyx/db/license.py:293:    # two reads caches the old status for the full default TTL.
HEAD:backend/ee/onyx/db/license.py:317:    ttl = LICENSE_CACHE_TTL_SECONDS
HEAD:backend/ee/onyx/db/license.py:376:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:390:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:449:        invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/user_group.py:912:    db_session.expire(db_user_group)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:5:from cachetools import TTLCache
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:20:_CACHE_TTL_SECONDS = 3600
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:24:_SALESFORCE_CLIENT_CACHE: TTLCache[tuple[str, int], tuple[datetime, OnyxSalesforce]] = (
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:25:    TTLCache(maxsize=_SALESFORCE_CLIENT_CACHE_MAX_SIZE, ttl=_CACHE_TTL_SECONDS)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:27:_CACHED_SF_EMAIL_TO_ID_MAP: TTLCache[
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:29:] = TTLCache(maxsize=_SALESFORCE_USER_ID_CACHE_MAX_SIZE, ttl=_CACHE_TTL_SECONDS)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:32:def _clear_cached_user_ids_for_client(
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:66:                _clear_cached_user_ids_for_client(cache_key[0], cached[1])
HEAD:backend/ee/onyx/server/billing/api.py:34:    invalidate_billing_cache as invalidate_indexing_trial_cache,
HEAD:backend/ee/onyx/server/billing/api.py:96:BILLING_INFO_CACHE_TTL_SECONDS = 300
HEAD:backend/ee/onyx/server/billing/api.py:145:        redis_client.delete(BILLING_CIRCUIT_BREAKER_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:213:    invalidate_billing_info_cache()
HEAD:backend/ee/onyx/server/billing/api.py:263:def invalidate_billing_info_cache() -> None:
HEAD:backend/ee/onyx/server/billing/api.py:274:            redis_client.delete(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/billing/api.py:279:        invalidate_indexing_trial_cache(get_current_tenant_id())
HEAD:backend/ee/onyx/server/billing/api.py:349:                ex=BILLING_INFO_CACHE_TTL_SECONDS,
HEAD:backend/ee/onyx/server/billing/api.py:396:    invalidate_billing_info_cache()
HEAD:backend/ee/onyx/server/billing/api.py:428:    invalidate_billing_info_cache()
HEAD:backend/ee/onyx/server/billing/billing_cache.py:28:from onyx.configs.app_configs import BILLING_CACHE_TTL_SECONDS
HEAD:backend/ee/onyx/server/billing/billing_cache.py:85:    ``BILLING_CACHE_TTL_SECONDS`` TTL.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:128:        redis.setex(key, BILLING_CACHE_TTL_SECONDS, _serialize(info))
HEAD:backend/ee/onyx/server/billing/billing_cache.py:152:def invalidate_billing_cache(tenant_id: str) -> bool:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:161:        get_shared_redis_client().delete(_cache_key(tenant_id))
HEAD:backend/ee/onyx/server/billing/billing_cache.py:165:            "billing cache invalidate failed for tenant %s: %s", tenant_id, e
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:67:    "extended-cache-ttl",
HEAD:backend/ee/onyx/server/license/api.py:23:from ee.onyx.server.billing.api import invalidate_billing_info_cache
HEAD:backend/ee/onyx/server/license/api.py:146:        invalidate_billing_info_cache()
HEAD:backend/ee/onyx/server/license/api.py:257:    Admin only - removes license from database and invalidates cache.
HEAD:backend/ee/onyx/server/license/api.py:265:    # db_delete_license invalidates after its commit and under the cache lock,
HEAD:backend/ee/onyx/server/settings/api.py:103:            # Cache miss (e.g. after TTL expiry). Fall back to DB so
HEAD:backend/ee/onyx/server/tenants/billing_api.py:26:from ee.onyx.server.billing.billing_cache import invalidate_billing_cache
HEAD:backend/ee/onyx/server/tenants/billing_api.py:131:        invalidated = invalidate_billing_cache(tier_update_request.tenant_id)
HEAD:backend/ee/onyx/server/tenants/billing_api.py:136:    if invalidated:
HEAD:backend/ee/onyx/server/tenants/proxy.py:40:BILLING_INFO_CACHE_TTL_SEC = 300
HEAD:backend/ee/onyx/server/tenants/proxy.py:54:        get_redis_client(tenant_id=tenant_id).delete(BILLING_INFO_CACHE_KEY)
HEAD:backend/ee/onyx/server/tenants/proxy.py:383:    Caches the response in Redis per tenant for BILLING_INFO_CACHE_TTL_SEC.
HEAD:backend/ee/onyx/server/tenants/proxy.py:428:                BILLING_INFO_CACHE_TTL_SEC,
HEAD:backend/ee/onyx/server/tenants/proxy.py:473:    # plan invalidates rather than leaving a snapshot beside it.
HEAD:backend/ee/onyx/server/tenants/tier_management.py:15:# Per-tenant cached CustomerTier; TTL bounds upgrade-visible delay if push is missed.
HEAD:backend/ee/onyx/server/tenants/tier_management.py:17:TENANT_TIER_CACHE_TTL_SECONDS = 86400  # 24h fallback; CP push is the primary refresh
HEAD:backend/ee/onyx/server/tenants/tier_management.py:61:    redis_client.set(TENANT_TIER_KEY, payload, ex=TENANT_TIER_CACHE_TTL_SECONDS)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:33:    invalidate_any_rate_limit_exists_cache,
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:71:    # clear cache in case this was the first rate limit created
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:72:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:96:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:111:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:184:    # clear cache in case this was the first rate limit created
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:185:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:256:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:273:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:301:    # clear cache in case this was the first rate limit created
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:302:    invalidate_any_rate_limit_exists_cache()
HEAD:backend/ee/onyx/utils/license.py:95:        get_redis_client().delete(_LICENSE_CLAIM_COOLDOWN_KEY)
HEAD:backend/ee/onyx/utils/license.py:272:    from ee.onyx.db.license import invalidate_license_cache, publish_license_metadata
HEAD:backend/ee/onyx/utils/license.py:279:            invalidate_license_cache()
HEAD:backend/ee/onyx/utils/license.py:280:        except Exception as invalidate_error:
HEAD:backend/ee/onyx/utils/license.py:285:                invalidate_error,
HEAD:backend/ee/onyx/utils/license.py:489:        get_cache_backend().delete(_LICENSE_RECLAIM_BLOCKED_KEY)
HEAD:backend/ee/onyx/utils/license.py:493:        get_redis_client().delete(_LICENSE_RECLAIM_DEBOUNCE_KEY)
HEAD:backend/ee/onyx/utils/license.py:555:            redis_client.delete(_LICENSE_RECLAIM_DEBOUNCE_KEY)
HEAD:backend/onyx/auth/captcha.py:60:_REPLAY_CACHE_TTL_SECONDS = 120
HEAD:backend/onyx/auth/captcha.py:125:            ex=_REPLAY_CACHE_TTL_SECONDS,
HEAD:backend/onyx/auth/captcha.py:144:        await redis.delete(_replay_cache_key(token))
HEAD:backend/onyx/auth/login_claims_capture.py:187:    pipe.expire(key, _IDP_CLAIMS_TTL_SECONDS)
HEAD:backend/onyx/auth/oauth_refresher.py:37:# negative-caches a failed fetch (short TTL) so a hard-down IdP is not re-tried
HEAD:backend/onyx/auth/oauth_refresher.py:43:OIDC_DISCOVERY_CACHE_TTL_SECONDS: int = int(
HEAD:backend/onyx/auth/oauth_refresher.py:44:    os.environ.get("OIDC_DISCOVERY_CACHE_TTL_SECONDS") or 3600
HEAD:backend/onyx/auth/oauth_refresher.py:76:# IdPs that rotate refresh tokens (e.g. Microsoft Entra) would invalidate one
HEAD:backend/onyx/auth/oauth_refresher.py:109:        OIDC_DISCOVERY_CACHE_TTL_SECONDS
HEAD:backend/onyx/auth/oauth_refresher.py:120:    the setting is not bypassed for the endpoint's remaining cache TTL."""
HEAD:backend/onyx/auth/signup_rate_limit.py:51:        pipe.expire(key, _BUCKET_SECONDS)
HEAD:backend/onyx/auth/users.py:524:def _invalidate_license_cache_after_seat_change() -> None:
HEAD:backend/onyx/auth/users.py:525:    """Invalidate license cache so middleware re-reads ``used_seats``."""
HEAD:backend/onyx/auth/users.py:527:        "onyx.db.license", "invalidate_license_cache", None
HEAD:backend/onyx/auth/users.py:853:                    self.user_db.session.expire(user)
HEAD:backend/onyx/auth/users.py:885:                    self.user_db.session.expire(user)
HEAD:backend/onyx/auth/users.py:947:            _invalidate_license_cache_after_seat_change()
HEAD:backend/onyx/auth/users.py:1254:                    _invalidate_license_cache_after_seat_change()
HEAD:backend/onyx/auth/users.py:1258:                self.user_db.session.expire(user)
HEAD:backend/onyx/auth/users.py:1831:    JWTs cannot be server-side invalidated.
HEAD:backend/onyx/auth/users.py:1861:        # JWTs are stateless — nothing to invalidate server-side.
HEAD:backend/onyx/auth/users.py:2477:    # Validate WS token in Redis (single-use, deleted after retrieval)
HEAD:backend/onyx/background/celery/apps/app_base.py:47:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/primary.py:31:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/primary.py:197:    RedisConnectorDelete.reset_all(r)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:61:from onyx.redis.redis_connector_delete import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:62:    RedisConnectorDelete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:63:    RedisConnectorDeletePayload,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:65:from onyx.redis.redis_hierarchy import invalidate_hierarchy_cache_for_source
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:245:            if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:281:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:305:    redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:306:    fence_payload = RedisConnectorDeletePayload(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:311:    redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:364:        redis_connector.delete.taskset_clear()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:370:        tasks_generated = redis_connector.delete.generate_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:386:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:390:        redis_connector.delete.set_fence(None)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:405:        redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:426:    fence_data = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:439:    if r.exists(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:481:                redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:543:            db_session.expire(cc_pair)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:577:                        invalidate_hierarchy_cache_for_source(r, source)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:582:                                "Connector deletion - failed to invalidate hierarchy node cache: "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:638:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:666:        if not key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:727:    if not redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:734:        payload = redis_connector.delete.payload
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:743:        redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:766:    for member in r.sscan_iter(redis_connector.delete.taskset_key):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:781:        redis_connector.delete.set_active()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:792:    if redis_connector.delete.active():
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:804:    redis_connector.delete.reset()
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:177:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:182:            f"fence={redis_connector.delete.fence_key}",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:272:            # set), use the Redis counters to decide whether to invalidate:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:274:            #   in_flight > 0               → workers crashed holding batches → invalidate
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:276:            #   in_flight = 0, pending = 0  → no work anywhere, stuck → invalidate
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:302:                    # no crash, just backlog. Do not invalidate.
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1206:        redis_std.delete(_VERSION_TELEMETRY_EMITTED_KEY)
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:388:        if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:735:                evict_hierarchy_nodes_from_cache(redis_client, source, deleted_raw_ids)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:117:    return f"{OnyxRedisLocks.USER_FILE_DELETE_LOCK_PREFIX}:{user_file_id}"
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:128:    return f"{OnyxRedisLocks.USER_FILE_DELETE_QUEUED_PREFIX}:{user_file_id}"
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:169:        redis_client.delete(queued_key)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:270:                    redis_client.delete(queued_key)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:646:        redis_client.delete(_user_file_queued_key(user_file_id))
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:774:       Redis key (TTL = CELERY_USER_FILE_DELETE_TASK_EXPIRES).  If that key
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:786:        OnyxRedisLocks.USER_FILE_DELETE_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:846:                    redis_client.delete(queued_key)
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:874:        redis_client.delete(_user_file_delete_queued_key(user_file_id))
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1090:        redis_client.delete(_user_file_project_sync_queued_key(user_file_id))
HEAD:backend/onyx/background/celery/tasks/vespa/document_sync.py:130:        r.expire(DOCUMENT_SYNC_TASKSET_KEY, TASKSET_TTL)
HEAD:backend/onyx/cache/interface.py:71:    """Thin abstraction over a key-value cache with TTL, locks, and blocking lists.
HEAD:backend/onyx/cache/interface.py:118:    def expire(self, key: str, seconds: int) -> None:
HEAD:backend/onyx/cache/interface.py:122:    def ttl(self, key: str) -> int:
HEAD:backend/onyx/cache/postgres_backend.py:170:            delete(CacheStore)
HEAD:backend/onyx/cache/postgres_backend.py:249:            session.execute(delete(CacheStore).where(CacheStore.key == key))
HEAD:backend/onyx/cache/postgres_backend.py:271:    def expire(self, key: str, seconds: int) -> None:
HEAD:backend/onyx/cache/postgres_backend.py:282:    def ttl(self, key: str) -> int:
HEAD:backend/onyx/cache/postgres_backend.py:373:            delete(CacheStore).where(
HEAD:backend/onyx/cache/redis_backend.py:85:    def expire(self, key: str, seconds: int) -> None:
HEAD:backend/onyx/cache/redis_backend.py:86:        self._r.expire(key, seconds)
HEAD:backend/onyx/cache/redis_backend.py:88:    def ttl(self, key: str) -> int:
HEAD:backend/onyx/cache/redis_backend.py:89:        return self._r.ttl(key)
HEAD:backend/onyx/chat/chat_processing_checker.py:46:        cache.set(fence_key, run_id if run_id is not None else 0, ex=FENCE_TTL)
HEAD:backend/onyx/chat/chat_processing_checker.py:48:        cache.delete(fence_key)
HEAD:backend/onyx/chat/incognito.py:73:    authorize against a revoked setting for the cache TTL.
HEAD:backend/onyx/chat/incognito.py:105:    second api_server can hold the pre-save mode for the cache TTL, and this
HEAD:backend/onyx/chat/process_message.py:871:    # invalidate the reservation.
HEAD:backend/onyx/chat/stop_signal_checker.py:33:        cache.delete(fence_key)
HEAD:backend/onyx/chat/stop_signal_checker.py:35:    cache.set(fence_key, 0, ex=FENCE_TTL)
HEAD:backend/onyx/chat/stop_signal_checker.py:58:    cache.delete(_get_fence_key(chat_session_id))
HEAD:backend/onyx/chat/stream_buffer.py:158:                self._cache.delete(_meta_key(self._chat_session_id, self._run_id))
HEAD:backend/onyx/chat/stream_buffer.py:160:                    self._cache.delete(
HEAD:backend/onyx/chat/stream_buffer.py:177:                self._cache.expire(
HEAD:backend/onyx/configs/app_configs.py:105:    QUERY_EMBEDDING_CACHE_TTL_S := int(
HEAD:backend/onyx/configs/app_configs.py:106:        os.environ.get("QUERY_EMBEDDING_CACHE_TTL_S", "900")
HEAD:backend/onyx/configs/app_configs.py:108:) > 0, "QUERY_EMBEDDING_CACHE_TTL_S must be positive."
HEAD:backend/onyx/configs/app_configs.py:217:BILLING_CACHE_TTL_SECONDS = int(os.environ.get("BILLING_CACHE_TTL_SECONDS", "3600"))
HEAD:backend/onyx/configs/app_configs.py:751:# them, letting the pool invalidate them cleanly.
HEAD:backend/onyx/configs/app_configs.py:1768:# Per-process cache TTL for the resolved tracing config; bounds how quickly a UI
HEAD:backend/onyx/configs/app_configs.py:1770:TRACING_CONFIG_CACHE_TTL_SECONDS = float(
HEAD:backend/onyx/configs/app_configs.py:1771:    os.environ.get("TRACING_CONFIG_CACHE_TTL_SECONDS") or "30"
HEAD:backend/onyx/configs/model_configs.py:141:# Cache TTL multiplier - store caches slightly longer than provider TTL
HEAD:backend/onyx/configs/model_configs.py:143:PROMPT_CACHE_REDIS_TTL_MULTIPLIER = float(
HEAD:backend/onyx/configs/model_configs.py:144:    os.environ.get("PROMPT_CACHE_REDIS_TTL_MULTIPLIER") or 1.2
HEAD:backend/onyx/connectors/google_drive/connector.py:1584:            # drive/folder: a regression changes the listing query, invalidates
HEAD:backend/onyx/connectors/slack/source_operations.py:200:        ttl_ms = self._redis.pttl(self._delay_key)
HEAD:backend/onyx/connectors/slack/source_operations.py:296:        delay_ms = self._redis.pttl(self._delay_key)
HEAD:backend/onyx/context/search/federated/slack_search.py:56:CHANNEL_METADATA_CACHE_TTL = 60 * 60 * 24  # 24 hours
HEAD:backend/onyx/context/search/federated/slack_search.py:57:USER_PROFILE_CACHE_TTL = 60 * 60 * 24  # 24 hours
HEAD:backend/onyx/context/search/federated/slack_search.py:158:                    ex=CHANNEL_METADATA_CACHE_TTL,
HEAD:backend/onyx/context/search/federated/slack_search.py:161:                    "Cached %s channels for team %s (TTL: %ss, key: %s)",
HEAD:backend/onyx/context/search/federated/slack_search.py:164:                    CHANNEL_METADATA_CACHE_TTL,
HEAD:backend/onyx/context/search/federated/slack_search.py:293:                ex=USER_PROFILE_CACHE_TTL,
HEAD:backend/onyx/context/search/federated/slack_search.py:316:            redis_client.set(cache_key, "", ex=USER_PROFILE_CACHE_TTL)
HEAD:backend/onyx/context/search/utils.py:9:    QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/context/search/utils.py:122:        ttl_seconds=QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/context/search/utils.py:143:        ttl_seconds=QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/db/credentials.py:224:    db_session.expire(credential)
HEAD:backend/onyx/db/credentials.py:266:    db_session.expire(credential)
HEAD:backend/onyx/db/credentials.py:287:    db_session.expire(credential)
HEAD:backend/onyx/db/credentials.py:304:    db_session.expire(credential)
HEAD:backend/onyx/db/engine/shard_routing.py:7:2. In-process TTL cache, invalidated across processes by the Redis version
HEAD:backend/onyx/db/engine/shard_routing.py:94:    Entries record `_generation` as of when their lookup *started*; `invalidate()`
HEAD:backend/onyx/db/engine/shard_routing.py:110:        # and `invalidate` rebinds `_entries` rather than emptying it in place.
HEAD:backend/onyx/db/engine/shard_routing.py:123:                # Invalidated while this lookup was in flight; drop the result.
HEAD:backend/onyx/db/engine/shard_routing.py:131:    def invalidate(cls, tenant_id: str | None = None) -> None:
HEAD:backend/onyx/db/engine/shard_routing.py:140:def invalidate_shard_cache(tenant_id: str | None = None) -> None:
HEAD:backend/onyx/db/engine/shard_routing.py:143:    To invalidate fleet-wide — which is what a migrator flip requires — call
HEAD:backend/onyx/db/engine/shard_routing.py:146:    _ShardCache.invalidate(tenant_id)
HEAD:backend/onyx/db/engine/shard_routing.py:220:        _ShardCache.invalidate()
HEAD:backend/onyx/db/engine/shard_version.py:17:- **A Redis failure does not invalidate** — the cache is left alone and the TTL is the
HEAD:backend/onyx/db/engine/shard_version.py:172:    cached mapping until it expires on its own. The TTL is therefore the real
HEAD:backend/onyx/db/engine/sql_engine.py:506:    we log and move on — SQLAlchemy internally invalidates the connection
HEAD:backend/onyx/db/engine/sql_engine.py:513:            "DB connection lost during session cleanup — the connection will be invalidated and recycled by the pool."
HEAD:backend/onyx/db/hierarchy.py:909:    Returns the list of raw_node_ids that were deleted (for cache eviction).
HEAD:backend/onyx/db/hierarchy.py:989:    Returns (deleted raw_node_ids, reparented nodes) for cache updates.
HEAD:backend/onyx/db/models.py:6511:    # upsert with a different hash bumps version and invalidates the archive.
HEAD:backend/onyx/db/tenant_shard.py:11:from onyx.db.engine.shard_routing import invalidate_shard_cache, is_undefined_table
HEAD:backend/onyx/db/tenant_shard.py:41:    # A lookup before this write caches "default" for a full TTL, which would send the
HEAD:backend/onyx/db/tenant_shard.py:43:    invalidate_shard_cache(tenant_id)
HEAD:backend/onyx/db/user_usage.py:13:from cachetools import TTLCache
HEAD:backend/onyx/db/user_usage.py:38:_invalid_cost_budget_warning_cache: TTLCache[tuple[str | None, int, int], None] = (
HEAD:backend/onyx/db/user_usage.py:39:    TTLCache(maxsize=10_000, ttl=_INVALID_COST_BUDGET_WARNING_TTL_SECONDS)
HEAD:backend/onyx/federated_connectors/oauth_utils.py:84:    cache.set(cache_key, json.dumps(session.to_dict()), ex=ttl)
HEAD:backend/onyx/federated_connectors/oauth_utils.py:120:    cache.delete(cache_key)
HEAD:backend/onyx/key_value_store/store.py:92:            self._get_cache().delete(REDIS_KEY_PREFIX + key)
HEAD:backend/onyx/key_value_store/store.py:95:                "Failed to delete value from cache for key '%s': %s", key, str(e)
HEAD:backend/onyx/llm/cost_overrides.py:6:from cachetools import LRUCache, TTLCache
HEAD:backend/onyx/llm/cost_overrides.py:26:_CACHE_TTL_SECONDS = 60.0
HEAD:backend/onyx/llm/cost_overrides.py:33:_cache: TTLCache[str, dict[_OverrideKey, CostOverrideRates]] = TTLCache(
HEAD:backend/onyx/llm/cost_overrides.py:35:    ttl=_CACHE_TTL_SECONDS,
HEAD:backend/onyx/llm/cost_overrides.py:97:def invalidate_override_cache() -> None:
HEAD:backend/onyx/llm/cost_overrides.py:126:    Caller commits + invalidates cache."""
HEAD:backend/onyx/llm/litellm_singleton/config.py:150:        # Clear the model name parser cache since enrichments are now loaded
HEAD:backend/onyx/llm/prompt_cache/README.md:142:- `get_cache_ttl_seconds()`: Cache TTL
HEAD:backend/onyx/llm/prompt_cache/README.md:161:- Invalid cache metadata: Cleared and proceed without cache
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:7:from onyx.configs.model_configs import PROMPT_CACHE_REDIS_TTL_MULTIPLIER
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:17:# Cache TTL multiplier - store caches slightly longer than provider TTL
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:19:# Value is configurable via PROMPT_CACHE_REDIS_TTL_MULTIPLIER env var (default: 1.2)
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:20:CACHE_TTL_MULTIPLIER = PROMPT_CACHE_REDIS_TTL_MULTIPLIER
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:141:    def delete_cache_metadata(
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:148:        """Delete cache metadata.
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:160:            self._kv_store.delete(cache_key)
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:162:                "Deleted cache metadata for provider=%s, model=%s, cache_key=%s...",
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:169:            logger.warning("Failed to delete cache metadata: %s", str(e))
HEAD:backend/onyx/llm/prompt_cache/providers/anthropic.py:95:    def get_cache_ttl_seconds(self) -> int:
HEAD:backend/onyx/llm/prompt_cache/providers/anthropic.py:96:        """Get cache TTL for Anthropic (5 minutes default)."""
HEAD:backend/onyx/llm/prompt_cache/providers/base.py:63:    def get_cache_ttl_seconds(self) -> int:
HEAD:backend/onyx/llm/prompt_cache/providers/base.py:64:        """Get cache TTL in seconds for this provider.
HEAD:backend/onyx/llm/prompt_cache/providers/noop.py:51:    def get_cache_ttl_seconds(self) -> int:
HEAD:backend/onyx/llm/prompt_cache/providers/openai.py:67:    def get_cache_ttl_seconds(self) -> int:
HEAD:backend/onyx/llm/prompt_cache/providers/openai.py:68:        """Get cache TTL for OpenAI (1 hour max)."""
HEAD:backend/onyx/llm/prompt_cache/providers/vertex.py:80:    def get_cache_ttl_seconds(self) -> int:
HEAD:backend/onyx/llm/prompt_cache/providers/vertex.py:81:        """Get cache TTL for Vertex AI (5 minutes)."""
HEAD:backend/onyx/llm/well_known_providers/auto_update_service.py:25:_CACHE_TTL_SECONDS = 60 * 60 * 24  # 24 hours
HEAD:backend/onyx/llm/well_known_providers/auto_update_service.py:43:            ex=_CACHE_TTL_SECONDS,
HEAD:backend/onyx/llm/well_known_providers/auto_update_service.py:148:        get_cache_backend().delete(_CACHE_KEY_LAST_UPDATED_AT)
HEAD:backend/onyx/llm/well_known_providers/llm_provider_options.py:42:_RECOMMENDATIONS_CACHE_TTL_SECONDS = 300
HEAD:backend/onyx/llm/well_known_providers/llm_provider_options.py:86:        and (now - _cached_recommendations_time) < _RECOMMENDATIONS_CACHE_TTL_SECONDS
HEAD:backend/onyx/llm/well_known_providers/llm_provider_options.py:95:            < _RECOMMENDATIONS_CACHE_TTL_SECONDS
HEAD:backend/onyx/natural_language_processing/query_embedding_cache.py:155:            cache_backend.expire(key, ttl_seconds)
HEAD:backend/onyx/natural_language_processing/query_embedding_cache.py:186:    """Writes each (query, embedding) pair into the cache with the given TTL.
HEAD:backend/onyx/natural_language_processing/query_embedding_cache.py:237:            cache_backend.set(key, packed, ex=ttl_seconds)
HEAD:backend/onyx/onyxbot/discord/DISCORD_MULTITENANT_README.md:184:    # 4. Clear cache
HEAD:backend/onyx/onyxbot/discord/cache.py:190:        """Clear all caches."""
HEAD:backend/onyx/onyxbot/discord/client.py:110:        # Clear cache (safe now - no concurrent operations possible)
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:391:                invalidate_license_cache_fn = fetch_ee_implementation_or_noop(
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:393:                    "invalidate_license_cache",
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:396:                invalidate_license_cache_fn()
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:451:                    invalidate_fn = fetch_ee_implementation_or_noop(
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:453:                        "invalidate_license_cache",
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:456:                    invalidate_fn()
HEAD:backend/onyx/redis/redis_connector.py:1:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/redis/redis_connector.py:24:        self.delete = RedisConnectorDelete(tenant_id, cc_pair_id, self.redis)
HEAD:backend/onyx/redis/redis_connector_delete.py:24:class RedisConnectorDeletePayload(BaseModel):
HEAD:backend/onyx/redis/redis_connector_delete.py:29:class RedisConnectorDelete:
HEAD:backend/onyx/redis/redis_connector_delete.py:56:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_delete.py:67:    def payload(self) -> RedisConnectorDeletePayload | None:
HEAD:backend/onyx/redis/redis_connector_delete.py:74:        payload = RedisConnectorDeletePayload.model_validate_json(fence_str)
HEAD:backend/onyx/redis/redis_connector_delete.py:78:    def set_fence(self, payload: RedisConnectorDeletePayload | None) -> None:
HEAD:backend/onyx/redis/redis_connector_delete.py:81:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_delete.py:141:            self.redis.expire(self.taskset_key, self.TASKSET_TTL)
HEAD:backend/onyx/redis/redis_connector_delete.py:164:        self.redis.delete(self.active_key)
HEAD:backend/onyx/redis/redis_connector_delete.py:165:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_delete.py:166:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_delete.py:170:        taskset_key = f"{RedisConnectorDelete.TASKSET_PREFIX}_{id}"
HEAD:backend/onyx/redis/redis_connector_delete.py:177:        for key in r.scan_iter(RedisConnectorDelete.ACTIVE_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_delete.py:180:        for key in r.scan_iter(RedisConnectorDelete.TASKSET_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_delete.py:183:        for key in r.scan_iter(RedisConnectorDelete.FENCE_PREFIX + "*"):
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:85:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:88:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:89:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:129:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:165:            self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:267:        self.redis.delete(self.active_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:268:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:269:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:270:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:271:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:64:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:67:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:68:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:107:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:144:            self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:159:        self.redis.delete(self.active_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:160:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:161:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:162:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:163:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:87:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:90:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:91:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:92:        self.redis.delete(self.generator_failed_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:131:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:158:        self.redis.delete(self.failure_backoff_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:184:            self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:222:            self.redis.expire(self.taskset_key, self.TASKSET_TTL)
HEAD:backend/onyx/redis/redis_connector_prune.py:245:        self.redis.delete(self.active_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:246:        self.redis.delete(self.generator_progress_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:247:        self.redis.delete(self.generator_complete_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:248:        self.redis.delete(self.generator_failed_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:249:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_connector_prune.py:250:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_stop.py:31:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_connector_utils.py:26:    if redis_connector.delete.fenced:
HEAD:backend/onyx/redis/redis_connector_utils.py:29:            task_name=redis_connector.delete.fence_key,
HEAD:backend/onyx/redis/redis_connector_utils.py:36:            task_name=redis_connector.delete.fence_key,
HEAD:backend/onyx/redis/redis_docprocessing.py:82:            self.redis.expire(self.pending_key, _COUNTER_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_docprocessing.py:101:        self.redis.delete(self.pending_key, self.in_flight_key)
HEAD:backend/onyx/redis/redis_document_set.py:39:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_document_set.py:88:            redis_client.expire(self.taskset_key, self.TASKSET_TTL)
HEAD:backend/onyx/redis/redis_document_set.py:104:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_document_set.py:105:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_hierarchy.py:11:- Nodes are cached per source type with a 6-hour TTL
HEAD:backend/onyx/redis/redis_hierarchy.py:13:- If the cache is stale (TTL expired during long-running job), one worker does
HEAD:backend/onyx/redis/redis_hierarchy.py:37:# Cache TTL: 6 hours in seconds
HEAD:backend/onyx/redis/redis_hierarchy.py:38:HIERARCHY_CACHE_TTL_SECONDS = 6 * 60 * 60
HEAD:backend/onyx/redis/redis_hierarchy.py:152:        redis_client.expire(source_node_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:155:    redis_client.expire(cache_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:156:    redis_client.expire(raw_id_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:201:        redis_client.expire(source_node_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:203:    redis_client.expire(cache_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:204:    redis_client.expire(raw_id_key, HIERARCHY_CACHE_TTL_SECONDS)
HEAD:backend/onyx/redis/redis_hierarchy.py:231:def invalidate_hierarchy_cache_for_source(
HEAD:backend/onyx/redis/redis_hierarchy.py:240:    redis_client.delete(
HEAD:backend/onyx/redis/redis_hierarchy.py:538:def clear_hierarchy_cache(
HEAD:backend/onyx/redis/redis_hierarchy.py:541:    """Clear the hierarchy cache for a source (useful for testing)."""
HEAD:backend/onyx/redis/redis_hierarchy.py:545:    redis_client.delete(cache_key)
HEAD:backend/onyx/redis/redis_hierarchy.py:546:    redis_client.delete(raw_id_key)
HEAD:backend/onyx/redis/redis_hierarchy.py:547:    redis_client.delete(source_node_key)
HEAD:backend/onyx/redis/redis_pool.py:609:    pipe.expire(rate_limit_key, WS_TOKEN_RATE_LIMIT_WINDOW_SECONDS)
HEAD:backend/onyx/redis/redis_pool.py:669:    ttl = raw.ttl(name)
HEAD:backend/onyx/redis/redis_usergroup.py:45:            self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_usergroup.py:104:            redis_client.expire(self.taskset_key, self.TASKSET_TTL)
HEAD:backend/onyx/redis/redis_usergroup.py:120:        self.redis.delete(self.taskset_key)
HEAD:backend/onyx/redis/redis_usergroup.py:121:        self.redis.delete(self.fence_key)
HEAD:backend/onyx/redis/redis_utils.py:1:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/redis/redis_utils.py:14:    if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/redis/tenant_redis_client.py:789:    def ttl(self, name: KeyArg) -> int:
HEAD:backend/onyx/redis/tenant_redis_client.py:799:        return cast(int, self._r.ttl(_prefix_key(self._prefix, name)))
HEAD:backend/onyx/redis/tenant_redis_client.py:801:    def pttl(self, name: KeyArg) -> int:
HEAD:backend/onyx/redis/tenant_redis_client.py:811:        return cast(int, self._r.pttl(_prefix_key(self._prefix, name)))
HEAD:backend/onyx/redis/tenant_redis_client.py:813:    def expire(
HEAD:backend/onyx/redis/tenant_redis_client.py:838:            self._r.expire(
HEAD:backend/onyx/redis/tenant_redis_client.py:872:    def pexpire(
HEAD:backend/onyx/redis/tenant_redis_client.py:896:            self._r.pexpire(
HEAD:backend/onyx/redis/tenant_redis_client.py:1290:    def expire(
HEAD:backend/onyx/redis/tenant_redis_client.py:1312:        self._p.expire(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:20:from cachetools import TTLCache, cachedmethod
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:197:_GRANT_CACHE_TTL_S = 60.0
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:257:        self._grant_cache: TTLCache[UUID, ScheduledRunGrants] = TTLCache(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:258:            maxsize=_GRANT_CACHE_MAX_ENTRIES, ttl=_GRANT_CACHE_TTL_S
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:54:    cache.expire(announce_key(session_id), ANNOUNCE_TTL_S)
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:148:        cache.expire(key, SESSION_GRANT_TTL_S)
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:185:    cache.expire(_wake_key(approval_id), WAKE_TTL_S)
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:28:regenerating (which would invalidate trust stores already populated from the
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:84:            # Fail loud: regenerating would invalidate sandboxes already
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:16:from cachetools import TTLCache
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:60:_TARGET_CACHE_TTL_S = 30.0
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:66:    def __init__(self, cache_ttl_s: float = _TARGET_CACHE_TTL_S) -> None:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:70:        self._targets_by_tenant: TTLCache[str, tuple[CraftMCPTarget, ...]] = TTLCache(
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:71:            maxsize=10_000, ttl=cache_ttl_s
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:76:            TTLCache(maxsize=10_000, ttl=cache_ttl_s)
HEAD:backend/onyx/server/features/build/approvals/api.py:172:        db_session.expire(current)
HEAD:backend/onyx/server/features/build/approvals/api.py:250:        db_session.expire(current)
HEAD:backend/onyx/server/features/build/connect_app.py:63:    cache.expire(key, _ANNOUNCE_TTL_S)
HEAD:backend/onyx/server/features/build/connect_app.py:87:    cache.set(_pending_key(request_id), pending.model_dump_json(), ex=_PENDING_TTL_S)
HEAD:backend/onyx/server/features/build/connect_app.py:104:def clear_pending(request_id: str, cache: CacheBackend) -> None:
HEAD:backend/onyx/server/features/build/connect_app.py:105:    cache.delete(_pending_key(request_id))
HEAD:backend/onyx/server/features/build/db/artifact.py:5:archive invalidated) or a metadata touch. Helpers flush and never commit,
HEAD:backend/onyx/server/features/build/external_apps/api.py:272:        db_session.expire(app, ["associated_skills"])
HEAD:backend/onyx/server/features/build/external_apps/api.py:472:    connect_app.clear_pending(request_id, cache)
HEAD:backend/onyx/server/features/build/interactive_turns/executor.py:580:                    clear_interrupt(session_id, cache)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:98:    _save_turn(cache, turn, ex=ACTIVE_TURN_TTL_SECONDS)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:146:        cache.delete(_active_turn_key(session_id))
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:150:        cache.delete(_active_turn_key(session_id))
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:153:        cache.delete(_active_turn_key(session_id))
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:200:        _save_turn(cache, turn, ex=ACTIVE_TURN_TTL_SECONDS)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:233:        _save_turn(cache, turn, ex=ACTIVE_TURN_TTL_SECONDS)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:234:        cache.expire(_active_turn_key(turn.session_id), ACTIVE_TURN_TTL_SECONDS)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:268:        _save_turn(cache, turn, ex=REQUEST_ID_TTL_SECONDS)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:272:            cache.delete(_active_turn_key(turn.session_id))
HEAD:backend/onyx/server/features/build/sandbox/base.py:588:        self-invalidates the stamp past the hard cap so a failed next-turn
HEAD:backend/onyx/server/features/build/sandbox/base.py:615:        """Invalidate the stamp at normal turn end so a failed next-turn
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:870:        # Re-provision: clear tombstone + cached info so subscribes can build a
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:874:        self._invalidate_serve_connection_info(sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1104:                # Re-provision: clear tombstone + cached info so subscribes
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1108:                self._invalidate_serve_connection_info(sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:172:        cached until ``_invalidate_serve_connection_info``. Return ``None``
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:200:    def _invalidate_serve_connection_info(self, sandbox_id: UUID) -> None:
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:209:        self._invalidate_serve_connection_info(sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:552:        self._invalidate_serve_connection_info(sandbox_id)
HEAD:backend/onyx/server/features/build/session/interrupt_signal.py:28:    cache.set(_fence_key(session_id), 0, ex=FENCE_TTL)
HEAD:backend/onyx/server/features/build/session/interrupt_signal.py:35:def clear_interrupt(session_id: UUID, cache: CacheBackend) -> None:
HEAD:backend/onyx/server/features/build/session/interrupt_signal.py:37:    cache.delete(_fence_key(session_id))
HEAD:backend/onyx/server/features/build/session/manager.py:324:            cache.delete(dispose_pending_key)
HEAD:backend/onyx/server/features/build/session/manager.py:355:        cache.delete(dispose_pending_key)
HEAD:backend/onyx/server/features/build/webapp_proxy.py:158:    cache.set(key, url, ex=_SANDBOX_URL_TTL)
HEAD:backend/onyx/server/features/build/webapp_proxy.py:375:        _webapp_access_cache_key(session_id, user.id), b"1", ex=_WEBAPP_ACCESS_TTL
HEAD:backend/onyx/server/features/build/webapp_proxy.py:415:            get_cache_backend().delete(_sandbox_url_cache_key(session_id))
HEAD:backend/onyx/server/features/mcp/api.py:1702:def _invalidate_mcp_user_credentials(
HEAD:backend/onyx/server/features/mcp/api.py:1897:        # to any of them invalidates existing user tokens, so it must trigger
HEAD:backend/onyx/server/features/mcp/api.py:1945:                _invalidate_mcp_user_credentials(mcp_server, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1969:                _invalidate_mcp_user_credentials(mcp_server, db_session)
HEAD:backend/onyx/server/features/notifications/api.py:4:from cachetools import TTLCache
HEAD:backend/onyx/server/features/notifications/api.py:48:_polled_ensure_cache: TTLCache[UUID, bool] = TTLCache(
HEAD:backend/onyx/server/features/persona/api.py:83:from onyx.server.manage.llm.provider_cache import invalidate_provider_listing_cache
HEAD:backend/onyx/server/features/persona/api.py:393:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/features/release_notes/constants.py:19:# Cache TTL: 24 hours
HEAD:backend/onyx/server/features/release_notes/constants.py:20:REDIS_CACHE_TTL = 60 * 60 * 24
HEAD:backend/onyx/server/features/release_notes/utils.py:18:    REDIS_CACHE_TTL,
HEAD:backend/onyx/server/features/release_notes/utils.py:149:        cache.set(REDIS_KEY_FETCHED_AT, now.isoformat(), ex=REDIS_CACHE_TTL)
HEAD:backend/onyx/server/features/release_notes/utils.py:151:            cache.set(REDIS_KEY_ETAG, etag, ex=REDIS_CACHE_TTL)
HEAD:backend/onyx/server/features/skill/api.py:169:    db_session.expire(skill)
HEAD:backend/onyx/server/features/skill/api.py:586:    db_session.expire(skill)
HEAD:backend/onyx/server/features/skill/api.py:736:    db_session.expire(skill)
HEAD:backend/onyx/server/features/skill/api.py:851:    db_session.expire(skill)
HEAD:backend/onyx/server/features/skill/api.py:925:    db_session.expire(skill)
HEAD:backend/onyx/server/features/usage/api.py:52:    invalidate_override_cache,
HEAD:backend/onyx/server/features/usage/api.py:447:    invalidate_override_cache()
HEAD:backend/onyx/server/features/usage/api.py:463:    invalidate_override_cache()
HEAD:backend/onyx/server/manage/discord_bot/api.py:226:    """Delete guild config (invalidates registration key).
HEAD:backend/onyx/server/manage/get_state.py:8:from cachetools import TTLCache
HEAD:backend/onyx/server/manage/get_state.py:43:# Admin mutations invalidate this pod directly. Other pods ride the TTL.
HEAD:backend/onyx/server/manage/get_state.py:45:_SSO_OPTIONS_CACHE: TTLCache[str, list[SSOProviderOption]] = TTLCache(
HEAD:backend/onyx/server/manage/get_state.py:57:def invalidate_sso_provider_options_cache() -> None:
HEAD:backend/onyx/server/manage/get_state.py:68:    # The lock spans the DB read so a mutation's invalidate cannot land between
HEAD:backend/onyx/server/manage/get_state.py:69:    # read and cache write, which would pin a pre-mutation snapshot for a TTL.
HEAD:backend/onyx/server/manage/image_generation/api.py:40:from onyx.server.manage.llm.provider_cache import invalidate_provider_listing_cache
HEAD:backend/onyx/server/manage/image_generation/api.py:361:        invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/image_generation/api.py:488:        invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/image_generation/api.py:523:        invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:119:    invalidate_provider_listing_cache,
HEAD:backend/onyx/server/manage/llm/api.py:245:        invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:729:        invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:764:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:778:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:792:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:806:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:817:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:831:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/api.py:841:    invalidate_provider_listing_cache()
HEAD:backend/onyx/server/manage/llm/provider_cache.py:11:version token, so a single token rewrite invalidates every entry at once.
HEAD:backend/onyx/server/manage/llm/provider_cache.py:145:def invalidate_provider_listing_cache() -> None:
HEAD:backend/onyx/server/manage/llm/provider_cache.py:150:            "LLM provider listing cache invalidation failed; entries expire via TTL",
HEAD:backend/onyx/server/manage/sso/api.py:27:from onyx.server.manage.get_state import invalidate_sso_provider_options_cache
HEAD:backend/onyx/server/manage/sso/api.py:192:    invalidate_sso_provider_options_cache()
HEAD:backend/onyx/server/manage/sso/api.py:232:    invalidate_sso_provider_options_cache()
HEAD:backend/onyx/server/manage/sso/api.py:276:    invalidate_sso_provider_options_cache()
HEAD:backend/onyx/server/manage/sso/api.py:368:    invalidate_sso_provider_options_cache()
HEAD:backend/onyx/server/manage/users.py:800:    # Invalidate license cache so used_seats reflects the new count
HEAD:backend/onyx/server/manage/users.py:804:            "onyx.db.license", "invalidate_license_cache", None
HEAD:backend/onyx/server/manage/users.py:852:        # Invalidate license cache so used_seats reflects the new count
HEAD:backend/onyx/server/manage/users.py:856:                "onyx.db.license", "invalidate_license_cache", None
HEAD:backend/onyx/server/manage/users.py:896:    # Invalidate license cache so used_seats reflects the new count
HEAD:backend/onyx/server/manage/users.py:900:            "onyx.db.license", "invalidate_license_cache", None
HEAD:backend/onyx/server/manage/users.py:970:            ttl = cast(int, redis.ttl(redis_key))
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:8:Results are cached for a configurable TTL (default 30s) so a 15s scrape cadence
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:37:# Default cache TTL in seconds. Scrapes hitting within this window return
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:39:_DEFAULT_CACHE_TTL = 30.0
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:95:        cache_ttl: float = _DEFAULT_CACHE_TTL,
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:98:        self._cache_ttl = cache_ttl
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:119:                and now - self._last_collect_time < self._cache_ttl
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:220:    def __init__(self, cache_ttl: float = _DEFAULT_CACHE_TTL) -> None:
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:221:        super().__init__(cache_ttl)
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:310:    def __init__(self, cache_ttl: float = _DEFAULT_CACHE_TTL) -> None:
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:311:        super().__init__(cache_ttl)
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:479:    def __init__(self, cache_ttl: float = 30.0) -> None:
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:480:        super().__init__(cache_ttl)
HEAD:backend/onyx/server/metrics/postgres_connection_pool.py:11:2. SQLAlchemy pool event listeners (checkout, checkin, connect, invalidate) for
HEAD:backend/onyx/server/metrics/postgres_connection_pool.py:153:    Listens to checkout, checkin, connect, and invalidate events.
HEAD:backend/onyx/server/metrics/postgres_connection_pool.py:197:    @event.listens_for(engine, "invalidate")
HEAD:backend/onyx/server/metrics/postgres_connection_pool.py:198:    def on_invalidate(
HEAD:backend/onyx/server/metrics/shard_capacity.py:23:_CACHE_TTL_SECONDS = 300.0
HEAD:backend/onyx/server/metrics/shard_capacity.py:38:    def __init__(self, ttl_seconds: float = _CACHE_TTL_SECONDS) -> None:
HEAD:backend/onyx/server/oidc_multi.py:20:from cachetools import TTLCache
HEAD:backend/onyx/server/oidc_multi.py:96:_CLIENT_CACHE_TTL_SECONDS = 600
HEAD:backend/onyx/server/oidc_multi.py:101:_CLIENT_CACHE: TTLCache[tuple[str, str, SSOProviderType, str], BaseOAuth2[Any]] = (
HEAD:backend/onyx/server/oidc_multi.py:102:    TTLCache(maxsize=128, ttl=_CLIENT_CACHE_TTL_SECONDS)
HEAD:backend/onyx/server/query_and_chat/token_limit.py:6:from cachetools import TTLCache
HEAD:backend/onyx/server/query_and_chat/token_limit.py:231:_ANY_RATE_LIMIT_EXISTS_CACHE_TTL_SECONDS = 60
HEAD:backend/onyx/server/query_and_chat/token_limit.py:236:_any_rate_limit_exists_cache: TTLCache[str, bool] = TTLCache(
HEAD:backend/onyx/server/query_and_chat/token_limit.py:237:    maxsize=10_000, ttl=_ANY_RATE_LIMIT_EXISTS_CACHE_TTL_SECONDS
HEAD:backend/onyx/server/query_and_chat/token_limit.py:267:def invalidate_any_rate_limit_exists_cache() -> None:
HEAD:backend/onyx/server/security/store.py:7:from cachetools import TTLCache
HEAD:backend/onyx/server/security/store.py:44:_CACHE_TTL_SECONDS = 10.0
HEAD:backend/onyx/server/security/store.py:48:_CACHE: TTLCache[str, SecuritySettings] = TTLCache(
HEAD:backend/onyx/server/security/store.py:49:    maxsize=10_000, ttl=_CACHE_TTL_SECONDS, timer=time.monotonic
HEAD:backend/onyx/server/security/store.py:65:        _CACHE = TTLCache(maxsize=maxsize, ttl=ttl, timer=timer)
HEAD:backend/onyx/server/security/store.py:197:    invalidate_security_cache(_current_tenant_id_or_default())
HEAD:backend/onyx/server/security/store.py:366:def invalidate_security_cache(tenant_id: str) -> None:
HEAD:backend/onyx/server/settings/store.py:78:            cache.set(OnyxRedisLocks.ANONYMOUS_USER_ENABLED, "0", ex=SETTINGS_TTL)
HEAD:backend/onyx/server/sso_discovery.py:74:        pipe.expire(key, _BUCKET_SECONDS)
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1896:**IMPORTANT**: Refs are invalidated when the page changes!
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:18:_HEALTH_CACHE_TTL_SECONDS = 30
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:266:                if time.monotonic() - cached_at < _HEALTH_CACHE_TTL_SECONDS:
HEAD:backend/onyx/tracing/dynamic_processor.py:15:from onyx.configs.app_configs import TRACING_CONFIG_CACHE_TTL_SECONDS
HEAD:backend/onyx/tracing/dynamic_processor.py:107:    def __init__(self, ttl_seconds: float = TRACING_CONFIG_CACHE_TTL_SECONDS) -> None:
```
Cached identity, authorization or application state can preserve stale access
after the authoritative database has changed.
## Locks, Fences and Concurrency Controls
Evidence lines: 550
```text
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:5:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:11:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:15:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:18:from onyx.redis.redis_pool import get_redis_client, redis_lock_dump
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:38:    atomically-enough (it's a best-effort counter, not a lock)."""
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:91:    lock_beat: RedisLock = redis_client.lock(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:92:        f"{OnyxRedisLocks.CLOUD_BEAT_TASK_GENERATOR_LOCK}:{task_name}",
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:93:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:97:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:100:    last_lock_time = time.monotonic()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:114:        # Gating setup is inside the try block so any exception still
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:115:        # reaches the finally that releases the beat lock.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:169:            if current_time - last_lock_time >= (CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4):
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:170:                lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:171:                last_lock_time = current_time
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:206:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:211:        if not lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:213:                "cloud_beat_task_generator - Lock not owned on completion"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:215:            redis_lock_dump(lock_beat, redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:217:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:2:import traceback
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:12:from redis.exceptions import LockError
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:13:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:37:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:39:    CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:40:    DANSWER_REDIS_FUNCTION_LOCK_PREFIX,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:46:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:90:    redis_lock_dump,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:123:def _get_fence_validation_block_expiration() -> int:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:125:    Compute the expiration time for the fence validation block signal.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:147:    full_exception_trace: str | None = None,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:157:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:213:    # TODO(rkuo): merge into check function after lookup table for fences is added
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:220:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:222:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:226:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:246:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:259:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:261:            # clear any permission fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:277:                ex=_get_fence_validation_block_expiration(),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:280:        # use a lookup table to find active fences. We still have to verify the fence
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:282:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:283:        keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:288:                r.srem(OnyxRedisConstants.ACTIVE_FENCES, key_bytes)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:300:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:311:        if lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:312:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:325:    LOCK_TIMEOUT = 30
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:331:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:333:        timeout=LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:336:    acquired = lock.acquire(blocking_timeout=LOCK_TIMEOUT / 2)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:347:        if redis_connector.prune.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:355:        # create before setting fence to avoid race condition where the monitoring
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:367:        # set a basic fence to start
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:400:        if lock.owned():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:401:            lock.release()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:424:    This task assumes that the task has already been properly fenced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:449:    # this wait is needed to avoid a race condition where
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:451:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:454:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:492:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:499:    acquired = lock.acquire(blocking=False)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:573:                raise ValueError(f"No fence payload found: cc_pair={cc_pair_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:584:                redis_connector, lock, r, timeout_seconds=JOB_TIMEOUT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:636:                lock=lock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:670:        full_exception_trace = traceback.format_exc()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:682:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:693:        if lock.owned():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:694:            lock.release()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:795:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:815:    lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:816:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:832:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:847:    Being in this bad state means the fence will never clear without help, so this function
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:856:    2.1. The fence is created
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:859:    3. The TTL allows us to get through the transitions on fence startup
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:871:    # if the fence doesn't exist, there's nothing to do
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:872:    fence_key = key_bytes.decode("utf-8")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:884:    # check to see if the fence/payload exists
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:889:    # it's a little sloppy, but just reset the fence for now if that happens
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:896:            "Resetting fence because fence schema is out of date: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:898:            f"fence={fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:965:    # if redis_connector_index.generator_locked():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:978:        "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:980:        f"fence={fence_key} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:994:        redis_lock: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1000:        self.redis_lock: RedisLock = redis_lock
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1004:        self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1007:        self.last_lock_reacquire: datetime = datetime.now(timezone.utc)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1008:        self.last_lock_monotonic = time.monotonic()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1013:        if self.redis_connector.stop.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1037:            if current_time - self.last_lock_monotonic >= (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1038:                CELERY_GENERIC_BEAT_LOCK_TIMEOUT / 4
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1040:                self.redis_lock.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1041:                self.last_lock_reacquire = datetime.now(timezone.utc)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1042:                self.last_lock_monotonic = time.monotonic()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1045:        except LockError:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1048:                self.redis_lock.timeout,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1051:                self.last_lock_reacquire,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1055:            redis_lock_dump(self.redis_lock, self.redis_client)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1068:    fence_key = key_bytes.decode("utf-8")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1072:            f"monitor_ccpair_permissions_taskset: could not parse cc_pair_id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:2:import traceback
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:11:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:40:    CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:41:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:42:    CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:47:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:100:def _get_fence_validation_block_expiration() -> int:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:102:    Compute the expiration time for the fence validation block signal.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:175:    lock_beat: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:177:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:181:    if not lock_beat.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:220:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:233:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:234:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:235:            # clear fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:240:                validate_external_group_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:245:                    "Exception while validating external group sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:249:                OnyxRedisSignals.BLOCK_VALIDATE_EXTERNAL_GROUP_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:251:                ex=_get_fence_validation_block_expiration(),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:255:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:264:        if lock_beat.owned():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:265:            lock_beat.release()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:285:        if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:295:        # create before setting fence to avoid race condition where the monitoring
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:307:        # Signal active before creating fence
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:316:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:332:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:366:    This task assumes that the task has already been properly fenced
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:373:    # this wait is needed to avoid a race condition where
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:375:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:378:        if time.monotonic() - start > CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:380:                f"connector_external_group_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:381:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:386:        if not redis_connector.external_group_sync.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:388:                f"connector_external_group_sync_generator_task - fence not found: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:389:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:402:                "connector_external_group_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:403:                redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:409:            "connector_external_group_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:410:            redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:415:    lock: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:416:        OnyxRedisLocks.CONNECTOR_EXTERNAL_GROUP_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:418:        timeout=CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:421:    acquired = lock.acquire(blocking=False)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:430:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:469:        # we always want to clear the fence after the task is done or failed so it doesn't get stuck
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:470:        redis_connector.external_group_sync.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:471:        if lock.owned():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:472:            lock.release()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:629:                full_exception_trace=traceback.format_exc(),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:679:def validate_external_group_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:685:    lock_beat: RedisLock,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:692:    lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:693:    keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:700:        validate_external_group_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:707:        lock_beat.reacquire()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:711:def validate_external_group_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:717:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:719:    Being in this bad state means the fence will never clear without help, so this function
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:728:    2.1. The fence is created
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:731:    3. The TTL allows us to get through the transitions on fence startup
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:740:    # if the fence doesn't exist, there's nothing to do
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:741:    fence_key = key_bytes.decode("utf-8")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:745:            f"validate_external_group_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:756:    # check to see if the fence/payload exists
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:764:            "validate_external_group_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:765:            "Resetting fence because fence schema is out of date: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:767:            f"fence={fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:805:            "validate_external_group_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:806:            "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:808:            f"fence={fence_key} "
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:53:        if stage == ExpiryWarningStage.GRACE:
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:78:    A renewal, if one happened, lands exactly when grace begins, so this runs
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:10:from redis.lock import Lock as RedisLock
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:18:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:59:    lock_check: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:60:        OnyxRedisLocks.CHECK_AVAILABLE_TENANTS_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:65:    if not lock_check.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:118:            lock_check.release()
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:121:                "Could not release check lock (likely expired), continuing"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:189:    lock_provision: RedisLock = r.lock(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:190:        OnyxRedisLocks.CLOUD_PRE_PROVISION_TENANT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:195:    if not lock_provision.acquire(blocking=False):
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:197:            "Skipping pre_provision_tenant — could not acquire provision lock"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:232:            # Use a transaction to ensure atomicity
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:271:            lock_provision.release()
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:274:                "Could not release provision lock (likely expired), continuing"
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:13:    OnyxRedisLocks,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:49:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:80:    ``chain_token`` fences the chain: each run extends the lease only if it still
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:97:        [OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE],
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:158:    batch-by-batch and holds a token-fenced in-flight marker for the whole chain.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:175:        OnyxRedisLocks.CHAT_TTL_CHAIN_ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:23:    fence_key = key_bytes.decode("utf-8")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:24:    usergroup_id_str = RedisUserGroup.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:26:        task_logger.warning(f"Could not parse usergroup id from {fence_key}")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:36:    if not rug.fenced:
HEAD:backend/onyx/auth/captcha.py:116:    """Claim a token fingerprint via ``SETNX``. A concurrent replay within
HEAD:backend/onyx/auth/captcha.py:118:    not block legitimate signups."""
HEAD:backend/onyx/auth/captcha.py:231:    # Claim before the Google round-trip so a concurrent replay of the
HEAD:backend/onyx/auth/disposable_email_validator.py:2:Utility to validate and block disposable/temporary email addresses.
HEAD:backend/onyx/auth/disposable_email_validator.py:33:    _lock = threading.Lock()
HEAD:backend/onyx/auth/disposable_email_validator.py:37:            with cls._lock:
HEAD:backend/onyx/auth/disposable_email_validator.py:58:        self._spawn_lock = threading.Lock()
HEAD:backend/onyx/auth/disposable_email_validator.py:63:        # This ensures we block at least these even if the remote fetch fails
HEAD:backend/onyx/auth/disposable_email_validator.py:77:        # Set initialized flag last to prevent race conditions
HEAD:backend/onyx/auth/disposable_email_validator.py:169:        with self._spawn_lock:
HEAD:backend/onyx/auth/disposable_email_validator.py:174:                # Re-check staleness under the lock: a refresh may have
HEAD:backend/onyx/auth/disposable_email_validator.py:255:    expiry, this blocks until the refresh completes.
HEAD:backend/onyx/auth/email_utils.py:104:      display: inline-block;
HEAD:backend/onyx/auth/email_utils.py:145:        {cta_block}
HEAD:backend/onyx/auth/email_utils.py:172:        cta_block = f'<a class="cta-button" href="{cta_link}">{cta_text}</a>'
HEAD:backend/onyx/auth/email_utils.py:174:        cta_block = ""
HEAD:backend/onyx/auth/email_utils.py:180:        cta_block=cta_block,
HEAD:backend/onyx/auth/jwt.py:45:    block_loopback_and_link_local: bool,
HEAD:backend/onyx/auth/jwt.py:46:    block_link_local_only: bool,
HEAD:backend/onyx/auth/jwt.py:63:                block_loopback_and_link_local=block_loopback_and_link_local,
HEAD:backend/onyx/auth/jwt.py:64:                block_link_local_only=block_link_local_only,
HEAD:backend/onyx/auth/jwt.py:109:        ssrf_params.block_loopback_and_link_local,
HEAD:backend/onyx/auth/jwt.py:110:        ssrf_params.block_link_local_only,
HEAD:backend/onyx/auth/login_claims_capture.py:167:        # Retained sources must not block fresh data from landing: fall back
HEAD:backend/onyx/auth/login_claims_capture.py:554:    # {label: value} for the "Organization Profile" prompt block.
HEAD:backend/onyx/auth/login_claims_capture.py:586:    "Organization Profile" prompt block. Best-effort like ``get_idp_profile``."""
HEAD:backend/onyx/auth/mobile_sso/code_store.py:11:  * single-use  -- atomic ``GETDEL`` burns the code on first read
HEAD:backend/onyx/auth/mobile_sso/code_store.py:51:    """Atomically redeem ``code`` and return the token, or ``None`` on any failure.
HEAD:backend/onyx/auth/mobile_sso/code_store.py:60:    # Atomic get-and-delete enforces single use (Redis 6.2+).
HEAD:backend/onyx/auth/oauth_refresher.py:10:from fastapi.concurrency import run_in_threadpool
HEAD:backend/onyx/auth/oauth_refresher.py:50:# Per-discovery-URL locks so one IdP's hanging fetch never blocks another's.
HEAD:backend/onyx/auth/oauth_refresher.py:52:_OIDC_DISCOVERY_LOCKS: Dict[str, asyncio.Lock] = {}
HEAD:backend/onyx/auth/oauth_refresher.py:53:_OIDC_DISCOVERY_LOCKS_GUARD: Optional[asyncio.Lock] = None
HEAD:backend/onyx/auth/oauth_refresher.py:56:def _get_discovery_locks_guard() -> asyncio.Lock:
HEAD:backend/onyx/auth/oauth_refresher.py:57:    """Lazy-init the meta-lock that protects the per-URL lock dict itself."""
HEAD:backend/onyx/auth/oauth_refresher.py:58:    global _OIDC_DISCOVERY_LOCKS_GUARD
HEAD:backend/onyx/auth/oauth_refresher.py:59:    if _OIDC_DISCOVERY_LOCKS_GUARD is None:
HEAD:backend/onyx/auth/oauth_refresher.py:60:        _OIDC_DISCOVERY_LOCKS_GUARD = asyncio.Lock()
HEAD:backend/onyx/auth/oauth_refresher.py:61:    return _OIDC_DISCOVERY_LOCKS_GUARD
HEAD:backend/onyx/auth/oauth_refresher.py:64:async def _get_discovery_lock(config_url: str) -> asyncio.Lock:
HEAD:backend/onyx/auth/oauth_refresher.py:65:    """Get-or-create the discovery lock for one discovery URL."""
HEAD:backend/onyx/auth/oauth_refresher.py:66:    async with _get_discovery_locks_guard():
HEAD:backend/onyx/auth/oauth_refresher.py:67:        lock = _OIDC_DISCOVERY_LOCKS.get(config_url)
HEAD:backend/onyx/auth/oauth_refresher.py:68:        if lock is None:
HEAD:backend/onyx/auth/oauth_refresher.py:69:            lock = asyncio.Lock()
HEAD:backend/onyx/auth/oauth_refresher.py:70:            _OIDC_DISCOVERY_LOCKS[config_url] = lock
HEAD:backend/onyx/auth/oauth_refresher.py:71:        return lock
HEAD:backend/onyx/auth/oauth_refresher.py:74:# Per-user locks coalescing concurrent token-refresh attempts. Without this,
HEAD:backend/onyx/auth/oauth_refresher.py:77:# of them with `400 invalid_grant`. The lock pairs with a re-read inside
HEAD:backend/onyx/auth/oauth_refresher.py:80:_USER_REFRESH_LOCKS: Dict[uuid.UUID, asyncio.Lock] = {}
HEAD:backend/onyx/auth/oauth_refresher.py:81:_USER_REFRESH_LOCKS_GUARD: Optional[asyncio.Lock] = None
HEAD:backend/onyx/auth/oauth_refresher.py:84:def _get_user_refresh_locks_guard() -> asyncio.Lock:
HEAD:backend/onyx/auth/oauth_refresher.py:85:    """Lazy-init the meta-lock that protects the per-user lock dict itself."""
HEAD:backend/onyx/auth/oauth_refresher.py:86:    global _USER_REFRESH_LOCKS_GUARD
HEAD:backend/onyx/auth/oauth_refresher.py:87:    if _USER_REFRESH_LOCKS_GUARD is None:
HEAD:backend/onyx/auth/oauth_refresher.py:88:        _USER_REFRESH_LOCKS_GUARD = asyncio.Lock()
HEAD:backend/onyx/auth/oauth_refresher.py:89:    return _USER_REFRESH_LOCKS_GUARD
HEAD:backend/onyx/auth/oauth_refresher.py:92:async def _get_user_refresh_lock(user_id: uuid.UUID) -> asyncio.Lock:
HEAD:backend/onyx/auth/oauth_refresher.py:93:    """Get-or-create a per-user lock keyed by `user.id`."""
HEAD:backend/onyx/auth/oauth_refresher.py:94:    async with _get_user_refresh_locks_guard():
HEAD:backend/onyx/auth/oauth_refresher.py:95:        lock = _USER_REFRESH_LOCKS.get(user_id)
HEAD:backend/onyx/auth/oauth_refresher.py:96:        if lock is None:
HEAD:backend/onyx/auth/oauth_refresher.py:97:            lock = asyncio.Lock()
HEAD:backend/onyx/auth/oauth_refresher.py:98:            _USER_REFRESH_LOCKS[user_id] = lock
HEAD:backend/onyx/auth/oauth_refresher.py:99:        return lock
HEAD:backend/onyx/auth/oauth_refresher.py:133:    lock + double check coalesce concurrent fetches into one request.
HEAD:backend/onyx/auth/oauth_refresher.py:143:        # Off the event loop: the guard resolves the host, which is blocking DNS.
HEAD:backend/onyx/auth/oauth_refresher.py:151:    async with await _get_discovery_lock(config_url):
HEAD:backend/onyx/auth/oauth_refresher.py:152:        # Re-check inside the lock — another coroutine may have populated
HEAD:backend/onyx/auth/oauth_refresher.py:413:            # Coalesce concurrent refreshes for the same user. Re-read the
HEAD:backend/onyx/auth/oauth_refresher.py:414:            # account inside the lock so the second coroutine sees the
HEAD:backend/onyx/auth/oauth_refresher.py:417:            user_lock = await _get_user_refresh_lock(user.id)
HEAD:backend/onyx/auth/oauth_refresher.py:418:            async with user_lock:
HEAD:backend/onyx/auth/oauth_refresher.py:426:                    # state we'd see without the lock.
HEAD:backend/onyx/auth/oauth_refresher.py:430:                    # This User was loaded before any concurrent refresh. Its
HEAD:backend/onyx/auth/oauth_token_manager.py:23:    VALIDATE_* levels private/internal targets are blocked; when DISABLED,
HEAD:backend/onyx/auth/oauth_token_manager.py:24:    private + loopback become reachable while cloud-metadata stays blocked.
HEAD:backend/onyx/auth/oauth_token_manager.py:32:        block_loopback_and_link_local=params.block_loopback_and_link_local,
HEAD:backend/onyx/auth/oauth_token_manager.py:33:        block_link_local_only=params.block_link_local_only,
HEAD:backend/onyx/auth/oauth_token_manager.py:255:        # Add 60 second buffer to avoid race conditions
HEAD:backend/onyx/auth/session_tokens.py:3:Token values embed their logical expiry; the physical TTL adds a grace window
HEAD:backend/onyx/auth/session_tokens.py:6:(no entry: cookie outlived the grace window, or Redis dropped the key),
HEAD:backend/onyx/auth/session_tokens.py:33:SESSION_TOKEN_GRACE_PERIOD_SECONDS = 60 * 60
HEAD:backend/onyx/auth/session_tokens.py:130:    return lifetime_seconds + SESSION_TOKEN_GRACE_PERIOD_SECONDS
HEAD:backend/onyx/auth/session_tokens.py:220:            "the grace window, or Redis dropped the key (restart/eviction/flush)."
HEAD:backend/onyx/auth/sso_url_guard.py:36:            block_loopback_and_link_local=params.block_loopback_and_link_local,
HEAD:backend/onyx/auth/sso_url_guard.py:37:            block_link_local_only=params.block_link_local_only,
HEAD:backend/onyx/auth/users.py:85:    SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:119:    OnyxRedisLocks,
HEAD:backend/onyx/auth/users.py:292:    value = cache.get(OnyxRedisLocks.ANONYMOUS_USER_ENABLED)
HEAD:backend/onyx/auth/users.py:426:        # Only block dotted Gmail on new signups — existing users must still be
HEAD:backend/onyx/auth/users.py:456:    lock_session: Session | None = None,
HEAD:backend/onyx/auth/users.py:462:    ``enforce_seat_limit_locked`` when followed by a write in the same
HEAD:backend/onyx/auth/users.py:473:            db_session=lock_session,
HEAD:backend/onyx/auth/users.py:485:def enforce_seat_limit_locked(db_session: Session, seats_needed: int = 1) -> None:
HEAD:backend/onyx/auth/users.py:486:    """Acquire the tenant advisory lock on ``db_session``, then enforce.
HEAD:backend/onyx/auth/users.py:488:    Self-hosted: lock + ``check_seat_availability`` on the caller's
HEAD:backend/onyx/auth/users.py:491:    Cloud: lock + ``get_tenant_count`` + Stripe modify also held on the
HEAD:backend/onyx/auth/users.py:495:    fetch_ee_implementation_or_noop("onyx.db.license", "acquire_seat_lock", None)(
HEAD:backend/onyx/auth/users.py:499:    enforce_seat_limit(db_session, seats_needed=seats_needed, lock_session=db_session)
HEAD:backend/onyx/auth/users.py:537:    row lock from ``reconcile_user_email__no_commit``; a second connection
HEAD:backend/onyx/auth/users.py:538:    would wait on that lock until the callback returns, which it never does.
HEAD:backend/onyx/auth/users.py:540:    Locks the row again rather than trusting that one: an email change commits
HEAD:backend/onyx/auth/users.py:541:    the reconcile before this runs, which drops it. Re-locking on the same
HEAD:backend/onyx/auth/users.py:542:    connection is a no-op when it is still held, and serializes concurrent
HEAD:backend/onyx/auth/users.py:551:    # The caller decided to promote from a read taken before this lock. Confirm
HEAD:backend/onyx/auth/users.py:552:    # the row is still a placeholder now that it is held: a concurrent login may
HEAD:backend/onyx/auth/users.py:563:        enforce_seat_limit_locked(db_session, seats_needed=1)
HEAD:backend/onyx/auth/users.py:713:            # Log blocked disposable email attempts
HEAD:backend/onyx/auth/users.py:721:                    "Blocked disposable email registration attempt: %s",
HEAD:backend/onyx/auth/users.py:804:                # Lock + check on the same session that does the insert.
HEAD:backend/onyx/auth/users.py:810:                        lambda s: enforce_seat_limit_locked(s, seats_needed=1)
HEAD:backend/onyx/auth/users.py:818:                    # Race condition: another request created the same user after the
HEAD:backend/onyx/auth/users.py:925:                    enforce_seat_limit_locked(sync_db, seats_needed=1)
HEAD:backend/onyx/auth/users.py:1144:                    # signup block: the provider vouches for one canonical email
HEAD:backend/onyx/auth/users.py:1151:                    # Lock + check on the same session that does the insert.
HEAD:backend/onyx/auth/users.py:1153:                        lambda s: enforce_seat_limit_locked(s, seats_needed=1)
HEAD:backend/onyx/auth/users.py:1243:                # lock taken by reconcile_user_email__no_commit above. A second
HEAD:backend/onyx/auth/users.py:1244:                # connection would wait on that lock for the whole callback.
HEAD:backend/onyx/auth/users.py:1336:            # Must happen inside the try block while tenant context is active,
HEAD:backend/onyx/auth/users.py:1514:            # so on-call needs the traceback to tell which one broke.
HEAD:backend/onyx/auth/users.py:1642:# The cookie outlives the logical expiry by the grace window so a dead token is
HEAD:backend/onyx/auth/users.py:1646:    cookie_max_age=SESSION_EXPIRE_TIME_SECONDS + SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:1684:    Token values embed their logical expiry and outlive it by a grace window;
HEAD:backend/onyx/auth/users.py:1755:            ex=SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:2116:                    "Inactive user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/auth/users.py:2122:                    "Non-web-login user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
HEAD:backend/onyx/background/README.md:49:- acquires the singleton lock
HEAD:backend/onyx/background/README.md:72:Fast and short living tasks that are not resource intensive. High concurrency:
HEAD:backend/onyx/background/README.md:73:Can have 24 concurrent workers, each with a prefetch of 8 for a total of 192 tasks in flight at once.
HEAD:backend/onyx/background/README.md:83:Long running, resource intensive tasks, handles pruning and sandbox operations. Low concurrency - max concurrency of 4 with 1 prefetch.
HEAD:backend/onyx/background/celery/apps/app_base.py:12:from celery.app import trace
HEAD:backend/onyx/background/celery/apps/app_base.py:19:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/apps/app_base.py:42:from onyx.configs.constants import ONYX_CLOUD_CELERY_TASK_PREFIX, OnyxRedisLocks
HEAD:backend/onyx/background/celery/apps/app_base.py:69:    SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:83:        traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:136:    """Stamp the current wall-clock time into the task message headers so that
HEAD:backend/onyx/background/celery/apps/app_base.py:273:    taskset non-empty and wedges the sync fence until its 7-day TTL.
HEAD:backend/onyx/background/celery/apps/app_base.py:297:    # But something is blocking set_start_method from working in the cloud unless
HEAD:backend/onyx/background/celery/apps/app_base.py:420:        if r.exists(OnyxRedisLocks.PRIMARY_WORKER):
HEAD:backend/onyx/background/celery/apps/app_base.py:463:    if not hasattr(sender, "primary_worker_lock"):
HEAD:backend/onyx/background/celery/apps/app_base.py:464:        # primary_worker_lock will not exist when MULTI_TENANT is True
HEAD:backend/onyx/background/celery/apps/app_base.py:467:    if not sender.primary_worker_lock:
HEAD:backend/onyx/background/celery/apps/app_base.py:470:    logger.info("Releasing primary worker lock.")
HEAD:backend/onyx/background/celery/apps/app_base.py:471:    lock: RedisLock = sender.primary_worker_lock
HEAD:backend/onyx/background/celery/apps/app_base.py:473:        if lock.owned():
HEAD:backend/onyx/background/celery/apps/app_base.py:475:                lock.release()
HEAD:backend/onyx/background/celery/apps/app_base.py:476:                sender.primary_worker_lock = None
HEAD:backend/onyx/background/celery/apps/app_base.py:478:                logger.exception("Failed to release primary worker lock")
HEAD:backend/onyx/background/celery/apps/app_base.py:480:        logger.exception("Failed to check if primary worker lock is owned")
HEAD:backend/onyx/background/celery/apps/app_base.py:629:    trace.logger.setLevel(logging.WARNING)
HEAD:backend/onyx/background/celery/apps/app_base.py:635:    trace.logger.setLevel(logLevel)
HEAD:backend/onyx/background/celery/apps/docfetching.py:113:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/docfetching.py:138:        "worker_shutting_down received, flagging docfetching for graceful interrupt."
HEAD:backend/onyx/background/celery/apps/docprocessing.py:121:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/heavy.py:94:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/light.py:98:    EXTRA_CONCURRENCY = 8  # small extra fudge factor for connection limits
HEAD:backend/onyx/background/celery/apps/light.py:103:        "Concurrency: %s",
HEAD:backend/onyx/background/celery/apps/light.py:104:        sender.concurrency,  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/light.py:109:        pool_size=sender.concurrency,  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/light.py:110:        max_overflow=EXTRA_CONCURRENCY,
HEAD:backend/onyx/background/celery/apps/light.py:115:            sender.concurrency + EXTRA_CONCURRENCY,  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/light.py:121:            sender.concurrency + EXTRA_CONCURRENCY  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/monitoring.py:63:    SqlEngine.init_engine(pool_size=sender.concurrency, max_overflow=3)
HEAD:backend/onyx/background/celery/apps/primary.py:15:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/apps/primary.py:23:    CELERY_PRIMARY_WORKER_LOCK_TIMEOUT,
HEAD:backend/onyx/background/celery/apps/primary.py:26:    OnyxRedisLocks,
HEAD:backend/onyx/background/celery/apps/primary.py:123:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/primary.py:159:    r.delete(OnyxRedisLocks.PRIMARY_WORKER)
HEAD:backend/onyx/background/celery/apps/primary.py:161:    # this process wide lock is taken to help other workers start up in order.
HEAD:backend/onyx/background/celery/apps/primary.py:162:    # it is planned to use this lock to enforce singleton behavior on the primary
HEAD:backend/onyx/background/celery/apps/primary.py:167:    # reacquire the lock with
HEAD:backend/onyx/background/celery/apps/primary.py:168:    lock: RedisLock = r.lock(
HEAD:backend/onyx/background/celery/apps/primary.py:169:        OnyxRedisLocks.PRIMARY_WORKER,
HEAD:backend/onyx/background/celery/apps/primary.py:170:        timeout=CELERY_PRIMARY_WORKER_LOCK_TIMEOUT,
HEAD:backend/onyx/background/celery/apps/primary.py:174:    logger.info("Primary worker lock: Acquire starting.")
HEAD:backend/onyx/background/celery/apps/primary.py:175:    acquired = lock.acquire(blocking_timeout=CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 2)
HEAD:backend/onyx/background/celery/apps/primary.py:177:        logger.info("Primary worker lock: Acquire succeeded.")
HEAD:backend/onyx/background/celery/apps/primary.py:179:        logger.error("Primary worker lock: Acquire failed!")
HEAD:backend/onyx/background/celery/apps/primary.py:180:        raise WorkerShutdown("Primary worker lock could not be acquired!")
HEAD:backend/onyx/background/celery/apps/primary.py:183:    sender.primary_worker_lock = lock  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/primary.py:187:    r.delete(OnyxRedisLocks.CHECK_VESPA_SYNC_BEAT_LOCK)
HEAD:backend/onyx/background/celery/apps/primary.py:189:    r.delete(OnyxRedisConstants.ACTIVE_FENCES)
HEAD:backend/onyx/background/celery/apps/primary.py:273:    """Regularly reacquires the primary worker lock outside of the task queue.
HEAD:backend/onyx/background/celery/apps/primary.py:284:        self.interval = CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8  # Interval in seconds
HEAD:backend/onyx/background/celery/apps/primary.py:305:            if not hasattr(worker, "primary_worker_lock"):
HEAD:backend/onyx/background/celery/apps/primary.py:308:            lock: RedisLock = worker.primary_worker_lock
HEAD:backend/onyx/background/celery/apps/primary.py:312:            if lock.owned():
HEAD:backend/onyx/background/celery/apps/primary.py:313:                task_logger.debug("Reacquiring primary worker lock.")
HEAD:backend/onyx/background/celery/apps/primary.py:314:                lock.reacquire()
HEAD:backend/onyx/background/celery/apps/primary.py:317:                    "Full acquisition of primary worker lock. Reasons could be worker restart or lock expiration."
HEAD:backend/onyx/background/celery/apps/primary.py:319:                lock = r.lock(
HEAD:backend/onyx/background/celery/apps/primary.py:320:                    OnyxRedisLocks.PRIMARY_WORKER,
HEAD:backend/onyx/background/celery/apps/primary.py:321:                    timeout=CELERY_PRIMARY_WORKER_LOCK_TIMEOUT,
HEAD:backend/onyx/background/celery/apps/primary.py:324:                task_logger.info("Primary worker lock: Acquire starting.")
HEAD:backend/onyx/background/celery/apps/primary.py:325:                acquired = lock.acquire(
HEAD:backend/onyx/background/celery/apps/primary.py:326:                    blocking_timeout=CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 2
HEAD:backend/onyx/background/celery/apps/primary.py:329:                    task_logger.info("Primary worker lock: Acquire succeeded.")
HEAD:backend/onyx/background/celery/apps/primary.py:330:                    worker.primary_worker_lock = lock
HEAD:backend/onyx/background/celery/apps/primary.py:332:                    task_logger.error("Primary worker lock: Acquire failed!")
HEAD:backend/onyx/background/celery/apps/primary.py:333:                    raise TimeoutError("Primary worker lock could not be acquired!")
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:94:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/apps/user_file_processing.py:67:    pool_size = cast(int, sender.concurrency)  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/background/celery/celery_redis.py:18:_broker_client_lock = threading.Lock()
HEAD:backend/onyx/background/celery/celery_redis.py:28:    Thread-safe via lock — safe for use in Celery thread-pool workers.
HEAD:backend/onyx/background/celery/celery_redis.py:35:    with _broker_client_lock:
HEAD:backend/onyx/background/celery/celery_redis.py:119:    This operation is not atomic."""
HEAD:backend/onyx/background/celery/celery_redis.py:137:    This operation is not atomic.
HEAD:backend/onyx/background/celery/configs/docfetching.py:2:from onyx.configs.app_configs import CELERY_WORKER_DOCFETCHING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/docfetching.py:23:worker_concurrency = CELERY_WORKER_DOCFETCHING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/docprocessing.py:2:from onyx.configs.app_configs import CELERY_WORKER_DOCPROCESSING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/docprocessing.py:30:worker_concurrency = CELERY_WORKER_DOCPROCESSING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/heavy.py:2:from onyx.configs.app_configs import CELERY_WORKER_HEAVY_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/heavy.py:22:worker_concurrency = CELERY_WORKER_HEAVY_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/light.py:3:    CELERY_WORKER_LIGHT_CONCURRENCY,
HEAD:backend/onyx/background/celery/configs/light.py:25:worker_concurrency = CELERY_WORKER_LIGHT_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/monitoring.py:2:from onyx.configs.app_configs import CELERY_WORKER_MONITORING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/monitoring.py:23:worker_concurrency = CELERY_WORKER_MONITORING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/primary.py:2:from onyx.configs.app_configs import CELERY_WORKER_PRIMARY_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/primary.py:22:worker_concurrency = CELERY_WORKER_PRIMARY_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/scheduled_tasks.py:2:from onyx.configs.app_configs import CELERY_WORKER_SCHEDULED_TASKS_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/scheduled_tasks.py:25:worker_concurrency = CELERY_WORKER_SCHEDULED_TASKS_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/user_file_processing.py:2:from onyx.configs.app_configs import CELERY_WORKER_USER_FILE_PROCESSING_CONCURRENCY
HEAD:backend/onyx/background/celery/configs/user_file_processing.py:23:worker_concurrency = CELERY_WORKER_USER_FILE_PROCESSING_CONCURRENCY
HEAD:backend/onyx/background/celery/memory_monitoring.py:5:import tracemalloc
HEAD:backend/onyx/background/celery/memory_monitoring.py:12:    INDEXING_WORKER_TRACEMALLOC,
HEAD:backend/onyx/background/celery/memory_monitoring.py:87:# log a tracemalloc snapshot (when enabled) so allocation sites are captured
HEAD:backend/onyx/background/celery/memory_monitoring.py:93:_TRACEMALLOC_FRAMES = 10
HEAD:backend/onyx/background/celery/memory_monitoring.py:104:    if INDEXING_WORKER_TRACEMALLOC and not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:105:        tracemalloc.start(_TRACEMALLOC_FRAMES)
HEAD:backend/onyx/background/celery/memory_monitoring.py:149:    if not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:151:            "tracemalloc is disabled; set INDEXING_WORKER_TRACEMALLOC=true to "
HEAD:backend/onyx/background/celery/memory_monitoring.py:156:    snapshot = tracemalloc.take_snapshot()
HEAD:backend/onyx/background/celery/memory_monitoring.py:159:        logger.warning("tracemalloc top allocation: %s", stat)
HEAD:backend/onyx/background/celery/memory_monitoring.py:161:        for line in stats[0].traceback.format():
HEAD:backend/onyx/background/celery/memory_monitoring.py:162:            logger.warning("tracemalloc largest site: %s", line)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:216:        # SKIP LOCKED path for tenants with no due tasks.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:7:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:10:from onyx.configs.constants import OnyxCeleryTask, OnyxRedisLocks
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:41:    Background snapshots bound data loss from ungraceful pod death (kubelet
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:50:    from onyx.server.features.build.session.locks import get_session_creation_lock
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:61:    lock: RedisLock = redis_client.lock(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:62:        OnyxRedisLocks.CLEANUP_IDLE_SANDBOXES_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:67:    if not lock.acquire(blocking=False):
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:68:        task_logger.info("cleanup_idle_sandboxes_task - lock not acquired, skipping")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:101:                session_creation_lock = get_session_creation_lock(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:110:                        session_creation_lock=session_creation_lock,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:131:                    session_creation_lock = get_session_creation_lock(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:134:                    if not session_creation_lock.acquire(blocking=False):
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:148:                            session_creation_lock,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:151:                        if session_creation_lock.owned():
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:152:                            session_creation_lock.release()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:215:        if lock.owned():
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:216:            lock.release()
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:6:writer model). A run that fails gracefully records FAILED_TO_RUN itself; only
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:47:    # Serialized UUID; None only for tasks enqueued before the fence deployed,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:53:    Terminal writes are fenced on ``run_id``: if this attempt was retired and
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:61:        # locks for the whole run. ``credential`` stays readable after the close
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:1:import traceback
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:9:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:20:    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:24:    OnyxRedisLocks,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:70:    inc_deletion_blocked,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:72:    inc_deletion_fence_reset,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:87:def revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:151:    lock_beat: RedisLock = r.lock(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:152:        OnyxRedisLocks.CHECK_CONNECTOR_DELETION_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:153:        timeout=CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:157:    if not lock_beat.acquire(blocking=False):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:162:        lock_beat.reacquire()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:163:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_CONNECTOR_DELETION_FENCES):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:164:            # clear fences that don't have associated celery tasks in progress
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:167:                validate_connector_deletion_fences(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:168:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:172:                    "Exception while validating connector deletion fences"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:175:            r.set(OnyxRedisSignals.BLOCK_VALIDATE_CONNECTOR_DELETION_FENCES, 1, ex=300)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:200:                        self.app, cc_pair_id, db_session, lock_beat, tenant_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:205:                    # on subsequent errors, we hard reset blocking fences after our specified timeout
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:209:                    if not redis_connector.stop.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:211:                        task_logger.info("Revoking any tasks blocking deletion.")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:212:                        revoke_tasks_blocking_deletion(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:215:                        redis_connector.stop.set_fence(True)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:220:                            # waiting too long, just reset blocking fences
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:222:                                "Timed out waiting for tasks blocking deletion. Resetting blocking fences."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:233:                    redis_connector.stop.set_fence(False)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:235:        lock_beat.reacquire()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:236:        keys = cast(set[Any], r_replica.smembers(OnyxRedisConstants.ACTIVE_FENCES))
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:241:                r.srem(OnyxRedisConstants.ACTIVE_FENCES, key_bytes)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:245:            if key_str.startswith(RedisConnectorDelete.FENCE_PREFIX):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:249:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:254:        if lock_beat.owned():
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:255:            lock_beat.release()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:264:    lock_beat: RedisLock,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:276:    lock_beat.reacquire()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:281:    if redis_connector.delete.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:284:    # we need to load the state of the object inside the fence
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:285:    # to avoid a race condition with db.commit/fence deletion
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:304:    # set a basic fence to start
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:306:    fence_payload = RedisConnectorDeletePayload(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:311:    redis_connector.delete.set_fence(fence_payload)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:327:                inc_deletion_blocked(tenant_id, "indexing")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:344:                inc_deletion_blocked(tenant_id, "port")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:351:        if redis_connector.prune.fenced:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:352:            inc_deletion_blocked(tenant_id, "pruning")
```
These mechanisms are relevant to race conditions between indexing, deletion,
permission synchronization and repeated background jobs.
## Retry and Failure Semantics
Evidence lines: 550
```text
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:28:            elif task.status == TaskStatus.FAILURE:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:36:                    "Task with task.task_id=%r failed; it is being deleted now",
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:4:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:45:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:46:        task_logger.exception(f"full-fanout timestamp read failed: task={task_name}")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:64:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:65:            task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:66:                f"full-fanout timestamp write failed: task={task_name}"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:114:        # Gating setup is inside the try block so any exception still
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:120:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:121:                task_logger.exception("tenant work gating: runtime flag read failed")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:125:                redis_failed = False
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:137:                    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:138:                        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:139:                            "tenant work gating: cleanup_expired failed"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:147:                        redis_failed = True
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:150:                # skip the ZCARD if we just failed open due to a Redis error.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:151:                if not redis_failed:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:208:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:209:        task_logger.exception("Unexpected exception during cloud_beat_task_generator")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:9:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:12:from redis.exceptions import LockError
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:16:    retry,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:17:    retry_if_exception,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:80:from onyx.db.utils import DocumentRow, SortOrder, is_retryable_sqlalchemy_error
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:113:DOCUMENT_PERMISSIONS_UPDATE_MAX_RETRIES = 3
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:118:# 5 seconds more than RetryDocumentIndex STOP_AFTER+MAX_WAIT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:135:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:147:    full_exception_trace: str | None = None,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:157:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:269:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:270:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:302:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:307:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:364:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:365:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:393:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:541:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:542:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:668:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:670:        full_exception_trace = traceback.format_exc()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:675:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:682:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:702:@retry(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:703:    retry=retry_if_exception(is_retryable_sqlalchemy_error),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:777:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:778:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:894:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1046:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1089:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:8:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:62:    mark_external_group_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:93:    """Helper to mark an external group sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:95:        mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:112:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:243:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:244:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:245:                    "Exception while validating external group sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:257:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:260:            f"Unexpected check_for_external_group_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:262:        task_logger.exception(f"Unexpected exception: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:304:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:305:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:335:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:338:            f"Unexpected try_creating_external_group_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:340:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:341:            f"Unexpected exception while trying to create external group sync task: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:444:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:447:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:449:        task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:450:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:453:        msg = f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:454:        task_logger.exception(msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:462:                sync_status=SyncStatus.FAILED,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:469:        # we always want to clear the fence after the task is done or failed so it doesn't get stuck
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:544:        # so if the sync failed (e.g. DB connection killed by
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:621:        except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:624:            # Mark as failed (this also updates progress to show partial progress)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:625:            mark_external_group_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:629:                full_exception_trace=traceback.format_exc(),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:634:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:769:        task_logger.exception(msg)
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:34:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:35:        logger.exception("Failed to clean up hook execution logs")
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:41:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:42:                "Failed to verify license during expiry-notification check"
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:93:    except (requests.RequestException, ValueError) as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:94:        logger.warning("License renewal check failed: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:41:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:42:        logger.debug("License reclaim backoff state unavailable: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:57:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:63:    """Reset the backoff when something arrived, widen it when nothing did.
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:78:    except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:79:        logger.debug("License reclaim backoff update failed: %s", e)
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:128:        except (requests.RequestException, ValueError) as e:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:132:                "Failed to reclaim license for tenant %s: %s", payload.tenant_id, e
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:89:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:90:            logger.exception("Failed to export query history with task_id=%r", task_id)
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:119:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:120:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:121:                "Failed to save query history export file; report_name=%r", report_name
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:4:failed on-save projection self-heals) and drops verification for any verified
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:26:    isolated so its failure can't skip the DNS re-check, which is the part that
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:32:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:33:        logger.exception("Failed to re-project login domains for %s", tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:103:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:104:                task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:105:                    f"Failed to provision tenant {i + 1}/{batch_size}, continuing with remaining tenants"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:113:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:114:        task_logger.exception("Error in check_available_tenants task")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:119:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:164:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:165:            task_logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:166:                f"Failed to migrate pool tenant {tenant_id}, skipping"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:245:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:246:                db_session.rollback()
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:248:                    f"Failed to store pre-provisioned tenant: {tenant_id}",
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:253:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:255:        # If we have a tenant_id, attempt to rollback any partially completed provisioning
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:258:                f"Rolling back failed tenant provisioning for: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:262:                    rollback_tenant_provisioning,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:265:                asyncio.run(rollback_tenant_provisioning(tenant_id))
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:266:            except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:267:                task_logger.exception(f"Error during rollback for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:272:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:90:    keeping the task simple; each failure is logged.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:118:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:119:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:120:                "Failed to delete chat session user_id=%s session_id=%s, continuing with remaining sessions",
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:140:        except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:194:    except Exception:
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:32:        task_logger.exception(f"usergroup_id ({usergroup_id_str}) is not an integer!")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:93:        except Exception as e:
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:98:                sync_status=SyncStatus.FAILED,
HEAD:backend/onyx/background/README.md:51:- mark orphaned index attempts failed
HEAD:backend/onyx/background/README.md:103:- Queue lengths, connector success/failure, connector latencies
HEAD:backend/onyx/background/celery/apps/app_base.py:13:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/app_base.py:174:    This function runs after any task completes (both success and failure)
HEAD:backend/onyx/background/celery/apps/app_base.py:175:    Note that this signal does not fire on a task that failed to complete and is going
HEAD:backend/onyx/background/celery/apps/app_base.py:305:    except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:307:            "Multiprocessing set_start_method exceptioned. Trying force=True..."
HEAD:backend/onyx/background/celery/apps/app_base.py:313:        except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:315:                "Multiprocessing set_start_method force=True exceptioned even with force=True."
HEAD:backend/onyx/background/celery/apps/app_base.py:344:        except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:385:        except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:477:            except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:478:                logger.exception("Failed to release primary worker lock")
HEAD:backend/onyx/background/celery/apps/app_base.py:479:    except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:480:        logger.exception("Failed to check if primary worker lock is owned")
HEAD:backend/onyx/background/celery/apps/app_base.py:566:            except Exception:
HEAD:backend/onyx/background/celery/apps/app_base.py:627:    # uncomment this to hide celery task succeeded/failed spam
HEAD:backend/onyx/background/celery/apps/beat.py:73:                task_logger.exception("Failed to process task configuration")
HEAD:backend/onyx/background/celery/apps/beat.py:74:            except Exception:
HEAD:backend/onyx/background/celery/apps/beat.py:75:                task_logger.exception("Unexpected error updating tasks")
HEAD:backend/onyx/background/celery/apps/beat.py:169:        except Exception:
HEAD:backend/onyx/background/celery/apps/docfetching.py:23:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docfetching.py:71:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:72:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/docfetching.py:73:    # task_retry signal doesn't pass task_id in kwargs; get it from
HEAD:backend/onyx/background/celery/apps/docfetching.py:80:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:24:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:74:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:75:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/docprocessing.py:76:    # task_retry signal doesn't pass task_id in kwargs; get it from
HEAD:backend/onyx/background/celery/apps/docprocessing.py:83:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/heavy.py:14:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/heavy.py:56:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:57:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/heavy.py:63:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/light.py:20:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/light.py:62:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/light.py:63:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/light.py:69:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/monitoring.py:93:    except Exception:
HEAD:backend/onyx/background/celery/apps/monitoring.py:94:        logger.exception("Failed to register Prometheus indexing pipeline collectors")
HEAD:backend/onyx/background/celery/apps/monitoring.py:102:    `start_metrics_server`, so letting a failure here fall into its handler would take
HEAD:backend/onyx/background/celery/apps/monitoring.py:112:    except Exception:
HEAD:backend/onyx/background/celery/apps/monitoring.py:113:        logger.exception("Failed to register the Prometheus shard capacity collector")
HEAD:backend/onyx/background/celery/apps/monitoring.py:125:            "Skipping Prometheus metrics server — collector registration failed"
HEAD:backend/onyx/background/celery/apps/primary.py:12:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/primary.py:43:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/primary.py:85:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/primary.py:86:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/primary.py:92:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/primary.py:179:        logger.error("Primary worker lock: Acquire failed!")
HEAD:backend/onyx/background/celery/apps/primary.py:203:    # mark orphaned index attempts as failed
HEAD:backend/onyx/background/celery/apps/primary.py:230:                # Task is orphaned - mark as failed
HEAD:backend/onyx/background/celery/apps/primary.py:231:                failure_reason = (
HEAD:backend/onyx/background/celery/apps/primary.py:238:                logger.warning(failure_reason)
HEAD:backend/onyx/background/celery/apps/primary.py:239:                mark_attempt_canceled(attempt.id, db_session, failure_reason)
HEAD:backend/onyx/background/celery/apps/primary.py:241:            except Exception:
HEAD:backend/onyx/background/celery/apps/primary.py:332:                    task_logger.error("Primary worker lock: Acquire failed!")
HEAD:backend/onyx/background/celery/apps/primary.py:335:        except Exception:
HEAD:backend/onyx/background/celery/apps/primary.py:336:            task_logger.exception("Periodic task failed.")
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:14:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:56:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:57:def on_task_retry(sender: Any | None = None, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:63:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/celery_redis.py:41:            except Exception:
HEAD:backend/onyx/background/celery/celery_redis.py:44:                except Exception:
HEAD:backend/onyx/background/celery/celery_redis.py:50:            except Exception:
HEAD:backend/onyx/background/celery/celery_redis.py:61:            retry_on_timeout=True,
HEAD:backend/onyx/background/celery/celery_utils.py:26:    ConnectorFailure,
HEAD:backend/onyx/background/celery/celery_utils.py:64:) -> Generator[list[Document | HierarchyNode | ConnectorFailure], None, None]:
HEAD:backend/onyx/background/celery/celery_utils.py:78:        batch: list[Document | HierarchyNode | ConnectorFailure] = []
HEAD:backend/onyx/background/celery/celery_utils.py:79:        for document, hierarchy_node, failure, next_checkpoint in wrapper(
HEAD:backend/onyx/background/celery/celery_utils.py:86:            elif failure is not None:
HEAD:backend/onyx/background/celery/celery_utils.py:87:                batch.append(failure)
HEAD:backend/onyx/background/celery/celery_utils.py:99:def _get_failure_id(failure: ConnectorFailure) -> str | None:
HEAD:backend/onyx/background/celery/celery_utils.py:100:    """Extract the document/entity ID from a ConnectorFailure."""
HEAD:backend/onyx/background/celery/celery_utils.py:101:    if failure.failed_document:
HEAD:backend/onyx/background/celery/celery_utils.py:102:        return failure.failed_document.document_id
HEAD:backend/onyx/background/celery/celery_utils.py:103:    if failure.failed_entity:
HEAD:backend/onyx/background/celery/celery_utils.py:104:        return failure.failed_entity.entity_id
HEAD:backend/onyx/background/celery/celery_utils.py:115:    doc_list: Sequence[Document | SlimDocument | HierarchyNode | ConnectorFailure],
HEAD:backend/onyx/background/celery/celery_utils.py:119:    ConnectorFailure items have their failed document/entity IDs added to the
HEAD:backend/onyx/background/celery/celery_utils.py:120:    ID dict so that failed-to-retrieve documents are not accidentally pruned.
HEAD:backend/onyx/background/celery/celery_utils.py:128:        elif isinstance(item, ConnectorFailure):
HEAD:backend/onyx/background/celery/celery_utils.py:129:            failed_id = _get_failure_id(item)
HEAD:backend/onyx/background/celery/celery_utils.py:130:            if failed_id:
HEAD:backend/onyx/background/celery/celery_utils.py:131:                ids[failed_id] = None
HEAD:backend/onyx/background/celery/celery_utils.py:133:                "Failed to retrieve document %s: %s", failed_id, item.failure_message
HEAD:backend/onyx/background/celery/celery_utils.py:155:    returned in the result. ConnectorFailure items have their IDs preserved
HEAD:backend/onyx/background/celery/celery_utils.py:156:    so that failed-to-retrieve documents are not accidentally pruned.
HEAD:backend/onyx/background/celery/celery_utils.py:177:        Iterator[Sequence[Document | SlimDocument | HierarchyNode | ConnectorFailure]]
HEAD:backend/onyx/background/celery/celery_utils.py:229:    except Exception as e:
HEAD:backend/onyx/background/celery/celery_utils.py:232:        # some use SDK-specific exceptions (e.g. google.api_core.exceptions.ResourceExhausted)
HEAD:backend/onyx/background/celery/celery_utils.py:234:        # TODO(Bo): replace with a standard ConnectorRateLimitError exception that all
HEAD:backend/onyx/background/celery/configs/base.py:120:broker_connection_retry_on_startup = True
HEAD:backend/onyx/background/celery/configs/base.py:129:    "retry_on_timeout": True,
HEAD:backend/onyx/background/celery/configs/base.py:143:redis_retry_on_timeout = True
HEAD:backend/onyx/background/celery/configs/beat.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/beat.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/client.py:4:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/client.py:10:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/docfetching.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/docfetching.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/docprocessing.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/docprocessing.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/heavy.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/heavy.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/light.py:8:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/light.py:14:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/monitoring.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/monitoring.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/primary.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/primary.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/scheduled_tasks.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/scheduled_tasks.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/configs/user_file_processing.py:5:broker_connection_retry_on_startup = shared_config.broker_connection_retry_on_startup
HEAD:backend/onyx/background/celery/configs/user_file_processing.py:11:redis_retry_on_timeout = shared_config.redis_retry_on_timeout
HEAD:backend/onyx/background/celery/memory_monitoring.py:81:    except Exception:
HEAD:backend/onyx/background/celery/memory_monitoring.py:82:        logger.exception("Error monitoring process memory.")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:47:    fail-closed: snapshot failure on a reachable pod keeps the sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:48:    RUNNING for retry next sweep.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:112:                except Exception as e:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:114:                        f"Failed to sweep sandbox {sandbox.id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:117:                    db_session.rollback()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:154:                    # Background snapshot failures are log-only (unlike the
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:181:                        except Exception as e:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:183:                                f"Failed to create snapshot for session {session_id}: {e}"
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:185:                            db_session.rollback()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:197:                        except Exception as e:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:199:                                f"Background opencode history snapshot failed "
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:203:                except Exception as e:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:205:                        f"Failed to sweep sandbox {sandbox_id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:208:                    db_session.rollback()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:210:    except Exception:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:211:        task_logger.exception("Error in cleanup_idle_sandboxes_task")
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:6:writer model). A run that fails gracefully records FAILED_TO_RUN itself; only
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:27:    mark_capability_run_failed,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:28:    mark_stale_capability_runs_failed,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:54:    the scope re-triggered, both the completion and the failure write no-op
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:117:    except Exception:
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:118:        # The worker is alive, so record the failure now: without this the scope
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:122:            mark_capability_run_failed(
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:143:    A sweep rather than lazy recovery at trigger time: a re-trigger immediately
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:144:    re-marks the scope RUNNING, so only a sweep can surface FAILED_TO_RUN to a
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:146:    after being retired overwrites FAILED_TO_RUN with its report (the completion
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:151:            retired = mark_stale_capability_runs_failed(
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:159:                    f"{source.value} to FAILED_TO_RUN (tenant {tenant_id})."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:6:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:29:    add_deletion_failure_message,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:108:        except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:109:            task_logger.exception("Exception while revoking indexing task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:118:    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:119:        task_logger.exception("Exception while revoking permissions sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:126:    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:127:        task_logger.exception("Exception while revoking pruning task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:136:    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:137:        task_logger.exception("Exception while revoking external group sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:170:            except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:171:                task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:172:                    "Exception while validating connector deletion fences"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:251:    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:252:        task_logger.exception("Unexpected exception during connector deletion check")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:338:            # failed by the stall watchdog.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:382:        except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:383:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:388:    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:389:        task_logger.exception("Unexpected exception")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:480:                # our attempt and letting the deletion restart is a good way to recover
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:579:                    except Exception:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:581:                            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:582:                                "Connector deletion - failed to invalidate hierarchy node cache: "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:605:        except Exception as e:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:606:            db_session.rollback()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:609:            add_deletion_failure_message(db_session, cc_pair_id, error_message)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:615:                sync_status=SyncStatus.FAILED,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:619:            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:620:                f"Connector deletion exceptioned: "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:626:            observe_deletion_taskset_duration(tenant_id, "failure", duration)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:627:            inc_deletion_completed(tenant_id, "failure")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:736:        task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:15:from onyx.db.index_attempt import mark_attempt_failed
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:99:            raise RuntimeError("send_task for connector_doc_fetching_task failed.")
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:111:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:112:        task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:113:            f"try_creating_indexing_task - Unexpected exception: cc_pair={cc_pair.id} search_settings={search_settings.id}"
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:116:        # Clean up on failure
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:118:            mark_attempt_failed(index_attempt_id, db_session)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:33:    SimpleJobException,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:42:from onyx.connectors.exceptions import ConnectorValidationError
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:49:    mark_attempt_failed,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:76:            raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:82:            raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:88:            raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:97:            raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:106:            raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:131:    NOTE: if an exception is raised out of this task, the primary worker will detect
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:178:        raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:187:        raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:203:                raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:214:                raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:243:        raise SimpleJobException(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:244:            f"Indexing task failed: attempt={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:251:    except Exception as e:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:252:        logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:253:            "Indexing spawned task failed: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:260:        # special bulletproofing ... truncate long exception messages
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:261:        # for exception types that require more args, this will fail
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:267:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:320:        job_level_exception = job.exception()
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:321:        result.exception_str = f"Docfetching returned exit code {result.exit_code} with exception: {job_level_exception}"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:358:    4) embeds chunks (embed_chunks_with_failure_handling) via a call to the model server
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:359:    5) write chunks to vespa (write_chunks_to_vector_db_with_backoff)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:367:      The watchdog is responsible for monitoring the docfetching_task and marking the index attempt as failed
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:375:    How we deal with failures/ partial indexing:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:382:    - progress based liveliness check: if nothing is done in 3-6 hours, mark the attempt as failed
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:441:        result.status = IndexingWatchdogTerminalStatus.SPAWN_FAILED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:483:    memory_limit_failure_reason: str | None = None
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:531:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:532:                    task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:534:                            "Indexing watchdog - transient exception marking index "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:542:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:543:                    task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:545:                            "Indexing watchdog - exception while terminating "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:559:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:560:                    task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:562:                            "Indexing watchdog - spawned task exceptioned"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:589:                # "No heartbeat received" failure. Checked every loop iteration
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:612:                        memory_limit_failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:620:                        # mark failed before terminating so the subprocess's own
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:624:                                mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:627:                                    memory_limit_failure_reason,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:629:                        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:630:                            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:632:                                    "Indexing watchdog - transient exception marking "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:633:                                    "index attempt as failed after memory limit"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:641:                        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:642:                            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:644:                                    "Indexing watchdog - exception while terminating "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:652:            # if the IndexAttempt row has been marked terminal (failed/canceled/
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:669:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:670:                task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:672:                        "Indexing watchdog - transient exception looking up index attempt"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:690:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:691:                task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:693:                        "Indexing watchdog - exception while terminating subprocess "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:701:    except Exception as e:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:702:        result.status = IndexingWatchdogTerminalStatus.WATCHDOG_EXCEPTIONED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:705:            result.exception_str = str(e)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:707:            result.exception_str = traceback.format_exc()
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:711:    if result.exception_str is not None:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:712:        # print with exception
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:717:                # only mark failures if not already terminal,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:720:                    failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:721:                        f"Spawned task exceptioned: exit_code={result.exit_code}"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:723:                    mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:726:                        failure_reason=failure_reason,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:727:                        full_exception_trace=result.exception_str,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:729:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:730:            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:732:                    "Indexing watchdog - transient exception marking index attempt as failed"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:736:        normalized_exception_str = "None"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:737:        if result.exception_str:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:738:            normalized_exception_str = result.exception_str.replace(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:748:                exception=f'"{normalized_exception_str}"',
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:752:        raise RuntimeError(f"Exception encountered: traceback={result.exception_str}")
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:754:    # print without exception
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:758:                logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:767:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:768:            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:770:                    "Indexing watchdog - transient exception marking index attempt as canceled"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:778:                mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:785:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:786:            logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:788:                    "Indexing watchdog - transient exception marking index attempt as failed"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:796:        # (e.g. heartbeat watchdog marking it FAILED, user requesting cancellation,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:803:        # watchdog is the fallback if that write failed, so nothing to do here.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:807:        # in-loop mark_attempt_failed hit a transient DB error — otherwise the
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:814:                    mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:817:                        memory_limit_failure_reason
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:820:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:821:            task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:823:                    "Indexing watchdog - transient exception marking index attempt "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:824:                    "as failed after memory limit"
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:58:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:60:            "Failed to emit heartbeat on prerun for attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:68:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:70:            "Failed to update docprocessing counters on prerun for attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:95:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:97:            "Failed to update docprocessing counters on postrun for attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:28:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:29:                logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:30:                    "Failed to update heartbeat counter for index attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:23:    resolve_failure_derived_targets,
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:92:            failed_keys: set[tuple[int, str]] = set()
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:102:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:106:                    log.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:110:                    failed_keys.update((cc_pair_id, t.document_id) for t in cc_targets)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:115:                failed_keys.update(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:116:                    (cc_pair_id, doc_id) for doc_id in result.failed_doc_ids
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:126:            #    whose target failed to land stay open so the admin can
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:127:            #    retry.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:128:            resolved_count, summary = resolve_failure_derived_targets(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:132:            still_failing_count = len(failed_keys)
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:142:            # resolved (landed + had a source error) nor failed (connector/
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:157:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:158:            # Recover from any mid-task failure: roll back uncommitted
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:159:            # work, then mark the job + synthetic IndexAttempts FAILED so
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:160:            # the FE poll surfaces the failure instead of waiting on a
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:163:            # The cleanup itself is wrapped so a secondary failure (e.g.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:164:            # connection reset during the FAILED-state commit) does not
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:165:            # mask the original exception: we always re-raise the root
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:167:            log.exception("Targeted reindex task failed; marking job FAILED")
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:169:                db_session.rollback()
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:178:                            attempt.status = IndexingStatus.FAILED
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:180:                    job.status = IndexingStatus.FAILED
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:183:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:184:                log.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:185:                    "Failed to mark job FAILED during error recovery; "
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:186:                    "row may remain IN_PROGRESS until the celery retry"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:11:from celery.exceptions import SoftTimeLimitExceeded
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:69:from onyx.connectors.models import ConnectorFailure, Document, IndexAttemptMetadata
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:96:    mark_attempt_failed,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:112:from onyx.error_handling.exceptions import OnyxError
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:179:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:190:    If no heartbeat has been received for a certain amount of time, mark the attempt as failed.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:288:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:289:                    task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:290:                        f"Failed to read batch counters for attempt {fresh_attempt.id}, "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:310:                    failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:316:                    # progress possible — all batches either failed or were lost.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:317:                    failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:319:                        f"no pending or in-flight batches — all batches failed or lost"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:325:                failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:337:                mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:340:                    failure_reason=failure_reason,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:344:                    f"Marked attempt {fresh_attempt.id} as failed due to heartbeat timeout"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:347:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:348:                task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:349:                    f"Failed to mark attempt {fresh_attempt.id} as failed due to heartbeat timeout"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:357:        # the Celery task is truly gone before marking failed.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:384:                    f"{attempt.celery_task_id} no longer exists — marking failed."
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:387:                    mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:390:                        failure_reason="Task never started — Celery task lost before pickup",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:392:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:393:                    task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:394:                        f"Failed to mark lost NOT_STARTED attempt {attempt.id} as failed"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:469:            f"total_failures={coordination_status.total_failures}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:485:    except Exception as e:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:486:        logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:487:            "Failed to monitor document processing completion: attempt=%s error=%s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:492:        # Mark the attempt as failed if monitoring fails
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:495:                mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:498:                    failure_reason=f"Processing monitoring failed: {str(e)}",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:499:                    full_exception_trace=traceback.format_exc(),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:502:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:503:            logger.exception("Failed to mark attempt as failed")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:507:            logger.info("Cleaning up storage after monitoring failure: %s", storage)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:509:        except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:510:            logger.exception("Failed to cleanup storage after monitoring failure")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:549:        "Indexing status: indexing_completed=%s batches_processed=%s/%s total_docs=%s total_chunks=%s total_failures=%s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:555:        coordination_status.total_failures,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:569:    total_failures = coordination_status.total_failures
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:572:        if total_failures == 0:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:578:                "Index attempt %s completed with %s failures",
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:580:                total_failures,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:667:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:668:        logger.exception("Failed to clean up document batches - continuing")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:681:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:682:        logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:683:            "Failed to run attempt-end staging cleanup; orphans will be "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:734:    failed_to_create: int = 0
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:743:            + self.failed_to_create
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:841:                f"Failed to create indexing task: cc_pair={cc_pair.id} search_settings={search_settings.id}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:843:            result.failed_to_create += 1
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:864:    w.r.t previous failed attempt, checkpointing, etc is handled in the docfetching task.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:983:                # recover.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1021:                            f"The {source} connector has failed repeatedly "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1034:                    # to prevent continued indexing retry attempts burning through embedding credits.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1036:                    # models. Also, they are more prone to repeated failures -> eventual success.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1124:                failure_reason = (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1130:                task_logger.error(failure_reason)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1131:                mark_attempt_failed(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1132:                    attempt.id, db_session, failure_reason=failure_reason
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1143:            except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1144:                task_logger.exception(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1145:                    "Exception while validating active indexing attempts"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1175:                except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1176:                    task_logger.exception(f"Error monitoring attempt {attempt.id}")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1184:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1185:        task_logger.exception("Unexpected exception during indexing check")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1205:        f"failed={primary_result.failed_to_create}]"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1212:            f"failed={secondary_result.failed_to_create}]"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1256:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1257:        task_logger.exception("Unexpected exception during checkpoint cleanup")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1345:    except Exception:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1346:        task_logger.exception("Unexpected exception during index attempt cleanup check")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1396:def _check_failure_threshold(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1397:    total_failures: int,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1400:    last_failure: ConnectorFailure | None,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1402:    """Check if we've hit the failure threshold and raise an appropriate exception if so.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1405:    1. We have more than 3 failures AND
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1406:    2. Failures account for more than 10% of processed documents
```
A lifecycle operation is not secure merely because its happy path exists.
Failed or partially completed transitions must later be tested.
## Eventual-Consistency / Stale-State Signals
Evidence lines: 600
```text
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:80:    propagating."""
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:8:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:8:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:9:            "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:59:            # Revoking stale routing is a security cleanup, so it must reach
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:28:from shared_configs.configs import IGNORED_SYNCING_TENANT_LIST
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:159:        # checkpoint/index attempt cleanup) need to run on gated tenants and pass
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:174:            if IGNORED_SYNCING_TENANT_LIST and tenant_id in IGNORED_SYNCING_TENANT_LIST:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:206:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:2:import traceback
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:18:    stop_after_delay,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:81:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:147:    full_exception_trace: str | None = None,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:157:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:300:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:324:    Returns None if no syncing is required."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:355:        # create before setting fence to avoid race condition where the monitoring
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:449:    # this wait is needed to avoid a race condition where
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:567:            logger.info("Syncing docs for %s with cc_pair=%s", source_type, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:670:        full_exception_trace = traceback.format_exc()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:682:            full_exception_trace=full_exception_trace,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:707:    stop=stop_after_delay(DOCUMENT_PERMISSIONS_UPDATE_STOP_AFTER),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:864:    1. An unknown task id is always returned as state PENDING.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:2:import traceback
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:13:from ee.onyx.background.celery.tasks.external_group_syncing.group_sync_utils import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:22:    mark_old_external_groups_as_stale,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:23:    remove_stale_external_groups,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:255:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:277:    """Returns an int if syncing is needed. The int represents the number of sync tasks generated.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:278:    Returns None if no syncing is required."""
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:295:        # create before setting fence to avoid race condition where the monitoring
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:373:    # this wait is needed to avoid a race condition where
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:541:        # Clean up stale rows from previous cycle BEFORE marking new ones.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:545:        # idle_in_transaction_session_timeout during long API calls), stale
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:548:            "Removing stale external groups from prior cycle for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:552:        remove_stale_external_groups(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:555:            "Marking old external groups as stale for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:559:        mark_old_external_groups_as_stale(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:566:            "Syncing external groups for %s for cc_pair: %s", source_type, cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:629:                full_exception_trace=traceback.format_exc(),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:635:                "Error syncing external groups for %s for cc_pair: %s %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:645:            "Removing stale external groups for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:649:        remove_stale_external_groups(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:736:    1. An unknown task id is always returned as state PENDING.
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:53:        if stage == ExpiryWarningStage.GRACE:
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:78:    A renewal, if one happened, lands exactly when grace begins, so this runs
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:111:        _migrate_stale_pool_tenants()
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:125:def _migrate_stale_pool_tenants() -> None:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:145:        f"Checking {len(tenant_ids)} pool tenant(s) for pending migrations"
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:21:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:35:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:56:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:86:    Override this if your connector needs to validate permissions syncing.
HEAD:backend/ee/onyx/db/document_set.py:31:    ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/document_set.py:34:    ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/document_set.py:73:    # that happens to be syncing.
HEAD:backend/ee/onyx/db/document_set.py:83:    syncing = next(
HEAD:backend/ee/onyx/db/document_set.py:91:    if syncing is not None:
HEAD:backend/ee/onyx/db/document_set.py:93:            f"Document set '{syncing.name}' is still syncing. "
HEAD:backend/ee/onyx/db/document_set.py:141:    ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/document_set.py:145:    ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/external_perm.py:62:def mark_old_external_groups_as_stale(
HEAD:backend/ee/onyx/db/external_perm.py:69:        .values(stale=True)
HEAD:backend/ee/onyx/db/external_perm.py:74:        .values(stale=True)
HEAD:backend/ee/onyx/db/external_perm.py:80:    # to fail and stale cleanup to never run.
HEAD:backend/ee/onyx/db/external_perm.py:96:      sets stale=False
HEAD:backend/ee/onyx/db/external_perm.py:97:    - For new rows, inserts with stale=False
HEAD:backend/ee/onyx/db/external_perm.py:141:                    "stale": False,
HEAD:backend/ee/onyx/db/external_perm.py:150:                    "stale": False,
HEAD:backend/ee/onyx/db/external_perm.py:170:            set_={"stale": False},
HEAD:backend/ee/onyx/db/external_perm.py:188:            set_={"stale": False},
HEAD:backend/ee/onyx/db/external_perm.py:195:def remove_stale_external_groups(
HEAD:backend/ee/onyx/db/external_perm.py:202:            User__ExternalUserGroupId.stale.is_(True),
HEAD:backend/ee/onyx/db/external_perm.py:208:            PublicExternalUserGroup.stale.is_(True),
HEAD:backend/ee/onyx/db/license.py:276:    grace_period_end: datetime | None = None,
HEAD:backend/ee/onyx/db/license.py:284:        get_grace_period_end,
HEAD:backend/ee/onyx/db/license.py:288:    # Default the grace window to 14 days past expires_at so the license-
HEAD:backend/ee/onyx/db/license.py:289:    # enforcement middleware returns GRACE_PERIOD (not GATED_ACCESS) during
HEAD:backend/ee/onyx/db/license.py:291:    effective_grace_end = grace_period_end or get_grace_period_end(payload.expires_at)
HEAD:backend/ee/onyx/db/license.py:295:    status = get_license_status(payload, effective_grace_end, now=now)
HEAD:backend/ee/onyx/db/license.py:308:        grace_period_end=effective_grace_end,
HEAD:backend/ee/onyx/db/license.py:318:    for boundary in (payload.expires_at, effective_grace_end):
HEAD:backend/ee/onyx/db/license.py:326:    grace_period_end: datetime | None = None,
HEAD:backend/ee/onyx/db/license.py:331:    All statuses are cached (ACTIVE, GRACE_PERIOD, GATED_ACCESS): the frontend
HEAD:backend/ee/onyx/db/license.py:334:    metadata, ttl = build_license_metadata(payload, grace_period_end, tenant_id)
HEAD:backend/ee/onyx/db/license.py:386:            # The lease expired mid-publish, so this write raced whatever
HEAD:backend/ee/onyx/db/mcp.py:19:        ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/mcp.py:27:        ).delete(synchronize_session="fetch")
HEAD:backend/ee/onyx/db/persona.py:150:    the pending value before the read below, so deriving it here reads back the new state.
HEAD:backend/ee/onyx/db/standard_answer.py:280:    in `keyword` exists in `query`, depending on the state of `match_any_keywords`
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:10:A domain only routes once it is verified. Declaring a domain records a pending
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:14:same domain pending, but only one can verify it.
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:93:    """Record this workspace's pending claim on the domains it declares, and drop
HEAD:backend/ee/onyx/db/user_group.py:110:    ).delete(synchronize_session=False)
HEAD:backend/ee/onyx/db/user_group.py:119:    ).delete(synchronize_session=False)
HEAD:backend/ee/onyx/db/user_group.py:128:    ).delete(synchronize_session=False)
HEAD:backend/ee/onyx/db/user_group.py:137:    ).delete(synchronize_session=False)
HEAD:backend/ee/onyx/db/user_group.py:465:        # syncing group used to be indistinguishable from a deleted one.
HEAD:backend/ee/onyx/db/user_group.py:467:            OnyxErrorCode.RESOURCE_SYNCING,
HEAD:backend/ee/onyx/db/user_group.py:468:            "Specified user group is currently syncing. Wait until the current "
HEAD:backend/ee/onyx/db/user_group.py:578:    A removed cc_pair keeps a stale ``is_current=False`` row until the Vespa sync
HEAD:backend/ee/onyx/db/user_group.py:910:    # Core writes above leave the loaded ORM collections stale, and sessions run
HEAD:backend/ee/onyx/db/user_group.py:945:    # (no membership change) otherwise leaves the route-gate flag stale.
HEAD:backend/ee/onyx/db/user_group.py:1121:    holding the row lock. A caller diffing before and after would race a concurrent
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:17:    get_pending_users,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:19:    write_pending_users,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:65:        # Only auto-join a single pending invitation. Choosing among several
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:83:                ).update({"active": True}, synchronize_session=False)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:87:                    "Multiple pending invitations for one address require selection"
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:91:                    "Multiple pending workspace invitations require an explicit "
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:104:    ``get_tenant_id_for_email`` it must not accept a pending invitation on the
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:128:        pending_tenant_ids = (
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:138:        return pending_tenant_ids[0] if len(pending_tenant_ids) == 1 else None
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:149:    address that maps nowhere or to several pending invitations.
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:257:    active in another workspace, or an invitation was already pending, the
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:664:    # Consume the pending request. It is stored as the requester typed it, so an
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:665:    # exact match would leave a stale entry behind to authorize a later move.
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:666:    pending_users = get_pending_users()
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:667:    remaining_pending = [
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:668:        pending for pending in pending_users if pending.lower() != email
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:670:    if len(remaining_pending) != len(pending_users):
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:671:        write_pending_users(remaining_pending)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:856:        pending_users = get_invited_users()
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:857:        if email in pending_users:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:858:            pending_users.remove(email)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:859:            write_invited_users(pending_users)
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:12:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:21:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:12:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:21:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:18:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:32:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:34:    {operations: [...]} envelope, depending on patch version. Accept both
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:27:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:39:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:45:    document permissions accordingly without using checkpoints.
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:19:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:28:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:48:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:32:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:69:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:379:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:63:    """Have to get all folders since the group syncing system assumes all groups
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:10:@retry_builder(tries=3, delay=2, backoff=2)
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:12:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:24:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:52:# depending on Jira version and endpoint.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:13:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface  # noqa
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:20:    from the database, typically used in permission synchronization workflows.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:37:    from the database, typically used in permission synchronization workflows.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:55:        Optional[IndexingHeartbeatInterface],
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:36:        stale_keys = [
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:41:        for key in stale_keys:
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:12:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:24:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:27:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:192:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:236:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:244:    # the connector's rotation lock and rate-limit delay keys now coordinate
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:2:THIS IS NOT USEFUL OR USED FOR PERMISSION SYNCING
HEAD:backend/ee/onyx/external_permissions/sync_params.py:38:    from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface  # noqa
HEAD:backend/ee/onyx/external_permissions/sync_params.py:49:        callback: Optional["IndexingHeartbeatInterface"],
HEAD:backend/ee/onyx/external_permissions/sync_params.py:212:    callback: Optional["IndexingHeartbeatInterface"],  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/sync_params.py:344:    """Checks if the given DocumentSource requires doc syncing."""
HEAD:backend/ee/onyx/external_permissions/sync_params.py:351:    """Checks if the given DocumentSource requires external group syncing."""
HEAD:backend/ee/onyx/external_permissions/sync_params.py:363:    """Checks if the given DocumentSource requires external group syncing."""
HEAD:backend/ee/onyx/external_permissions/sync_params.py:375:    """Returns the set of sources that have external group syncing that is cc_pair agnostic."""
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:12:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:25:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/utils.py:15:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/external_permissions/utils.py:32:    callback: IndexingHeartbeatInterface | None,
HEAD:backend/ee/onyx/external_permissions/utils.py:38:    A convenience function for performing a generic document synchronization.
HEAD:backend/ee/onyx/onyxbot/slack/handlers/handle_standard_answers.py:86:    Potentially respond to the user message depending on whether the user's message matches
HEAD:backend/ee/onyx/server/billing/api.py:212:    # post-checkout subscription snapshot isn't delayed by the cache.
HEAD:backend/ee/onyx/server/billing/api.py:269:    usage limits on stale trial status for up to a full TTL.
HEAD:backend/ee/onyx/server/billing/api.py:322:                # Stale schema or partial write — try SubscriptionStatusResponse
HEAD:backend/ee/onyx/server/billing/api.py:366:    For self-hosted, the frontend should call /license/claim after a short delay
HEAD:backend/ee/onyx/server/billing/api.py:387:    # short delay to get the freshly generated license.
HEAD:backend/ee/onyx/server/billing/billing_cache.py:155:    stale entry may survive until its TTL, True otherwise (no-op included).
HEAD:backend/ee/onyx/server/documents/cc_pair.py:6:from ee.onyx.background.celery.tasks.doc_permission_syncing.tasks import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:9:from ee.onyx.background.celery.tasks.external_group_syncing.tasks import (
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:48:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:49:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:237:def _gateway_trace(flow: LLMFlow, model: str) -> Trace:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:238:    return trace("llm_gateway", metadata={"flow": flow.value, "model": model})
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:274:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:336:                # at least visible in traces.
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:368:    # StreamingResponse, so the trace must be opened here rather than in the
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:369:    # endpoint for the generation span to see an active trace.
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:371:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:466:                            # model_config so it is at least visible in traces.
HEAD:backend/ee/onyx/server/gateway/api.py:115:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/api.py:116:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/api.py:140:def _gateway_trace(flow: LLMFlow, model: str) -> Trace:
HEAD:backend/ee/onyx/server/gateway/api.py:141:    return trace("llm_gateway", metadata={"flow": flow.value, "model": model})
HEAD:backend/ee/onyx/server/gateway/api.py:319:    # StreamingResponse, so the trace must be opened here rather than in the
HEAD:backend/ee/onyx/server/gateway/api.py:320:    # endpoint for the generation span to see an active trace.
HEAD:backend/ee/onyx/server/gateway/api.py:322:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:396:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:617:    # StreamingResponse, so the trace must be opened here rather than in the
HEAD:backend/ee/onyx/server/gateway/api.py:618:    # endpoint for the generation span to see an active trace.
HEAD:backend/ee/onyx/server/gateway/api.py:620:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:775:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:1117:    # StreamingResponse, so the trace must be opened here rather than in the
HEAD:backend/ee/onyx/server/gateway/api.py:1118:    # endpoint for the generation span to see an active trace.
HEAD:backend/ee/onyx/server/gateway/api.py:1120:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/api.py:1324:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:46:from onyx.tracing.framework.create import trace
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:47:from onyx.tracing.framework.traces import Trace
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:265:def _gateway_trace(flow: LLMFlow, model: str) -> Trace:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:266:    return trace("llm_gateway", metadata={"flow": flow.value, "model": model})
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:301:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:380:                # in traces instead.
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:425:    # Runs on its own thread after the endpoint returned, so the trace must be
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:426:    # opened here or the generation span sees no active trace.
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:428:        _gateway_trace(flow, llm.config.model_name),
HEAD:backend/ee/onyx/server/license/api.py:71:        grace_period_end=metadata.grace_period_end,
HEAD:backend/ee/onyx/server/license/api.py:145:        # cached beside it is now stale.
HEAD:backend/ee/onyx/server/license/api.py:241:        grace_period_end=metadata.grace_period_end,
HEAD:backend/ee/onyx/server/license/models.py:40:    grace_period_days: int = 30
HEAD:backend/ee/onyx/server/license/models.py:91:    grace_period_end: datetime | None = None
HEAD:backend/ee/onyx/server/license/models.py:109:    grace_period_end: datetime | None = None
HEAD:backend/ee/onyx/server/log_export/api.py:58:    belongs to the current hold, so a stale holder (or a duplicate release) can
HEAD:backend/ee/onyx/server/log_export/api.py:82:        """Releases the hold identified by ``token``; stale tokens are ignored."""
HEAD:backend/ee/onyx/server/log_export/api.py:117:# Never cleared, only overwritten by the next start: releasing a stale token is
HEAD:backend/ee/onyx/server/log_export/api.py:257:        pending_worker_names=[
HEAD:backend/ee/onyx/server/log_export/models.py:86:    pending_worker_names: list[str]
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:33:Eventually, ENTERPRISE_EDITION_ENABLED will be removed and license
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:50:3. Valid license (ACTIVE, GRACE_PERIOD, PAYMENT_REMINDER):
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:53:   - GRACE_PERIOD / PAYMENT_REMINDER are for notifications only, not
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:175:                    # GRACE_PERIOD and PAYMENT_REMINDER are notification-only,
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:189:        # Don't `return` while an exception is propagating — it would swallow it
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:91:    # eventually for Confluence Data Center
HEAD:backend/ee/onyx/server/query_history/api.py:290:        pending_tasks = [
HEAD:backend/ee/onyx/server/query_history/api.py:298:        merged = pending_tasks + generated_files
HEAD:backend/ee/onyx/server/query_history/api.py:337:        status=TaskStatus.PENDING,
HEAD:backend/ee/onyx/server/query_history/api.py:431:    if task.status in [TaskStatus.STARTED, TaskStatus.PENDING]:
HEAD:backend/ee/onyx/server/scim/api.py:283:    and race past the seat cap.
HEAD:backend/ee/onyx/server/scim/api.py:392:      moves to it and the stale source account is deactivated. Without this,
HEAD:backend/ee/onyx/server/scim/api.py:432:                "deactivated stale %s",
HEAD:backend/ee/onyx/server/scim/api.py:446:# Unique constraints a concurrent provisioning race can trip: the email, the
HEAD:backend/ee/onyx/server/scim/api.py:447:# provisioned userName, and the one-mapping-per-user key (adoption races).
HEAD:backend/ee/onyx/server/scim/api.py:448:_PROVISIONING_RACE_CONSTRAINTS = (
HEAD:backend/ee/onyx/server/scim/api.py:461:    """Update the user, turning a uniqueness race into a SCIM 409.
HEAD:backend/ee/onyx/server/scim/api.py:464:    the pending rename and can hit the email unique index there.
HEAD:backend/ee/onyx/server/scim/api.py:470:        if any(is_unique_violation(e, c) for c in _PROVISIONING_RACE_CONSTRAINTS):
HEAD:backend/ee/onyx/server/scim/api.py:486:    """Sync the mapping and commit, turning a uniqueness race into a SCIM 409.
HEAD:backend/ee/onyx/server/scim/api.py:501:        if any(is_unique_violation(e, c) for c in _PROVISIONING_RACE_CONSTRAINTS):
HEAD:backend/ee/onyx/server/scim/api.py:539:      pending user INSERT is deferred and its ``ix_user_email`` unique violation
HEAD:backend/ee/onyx/server/scim/api.py:540:      surfaces here via autoflush rather than at ``add_user``. That specific race
HEAD:backend/ee/onyx/server/scim/api.py:545:      surfaced as a structured SCIM 500 with a full traceback.
HEAD:backend/ee/onyx/server/scim/api.py:553:        # Only provisioning races are expected, benign 409s. Every other
HEAD:backend/ee/onyx/server/scim/api.py:557:            is_unique_violation(e, c) for c in _PROVISIONING_RACE_CONSTRAINTS
HEAD:backend/ee/onyx/server/settings/api.py:57:            # Has a valid license (GRACE_PERIOD/PAYMENT_REMINDER still allow EE features)
HEAD:backend/ee/onyx/server/settings/api.py:125:                # Has a valid license (GRACE_PERIOD/PAYMENT_REMINDER still allow EE features)
HEAD:backend/ee/onyx/server/settings/api.py:131:                # syncing) means indexed data may need protection.
HEAD:backend/ee/onyx/server/tenants/billing.py:203:    Stripe errors propagate (fail closed). No-op when current quantity
HEAD:backend/ee/onyx/server/tenants/models.py:132:class PendingUserSnapshot(BaseModel):
HEAD:backend/ee/onyx/server/tenants/product_gating.py:30:        # merge onto a stale snapshot and drop application_status.
HEAD:backend/ee/onyx/server/tenants/provisioning.py:697:    Uses row-level locking to prevent race conditions when multiple processes
HEAD:backend/ee/onyx/server/tenants/provisioning.py:707:            # Get the oldest available tenant with FOR UPDATE lock to prevent race conditions
HEAD:backend/ee/onyx/server/tenants/proxy.py:410:            # Stale schema or partial write — fall through to live proxy.
HEAD:backend/ee/onyx/server/tenants/tier_management.py:15:# Per-tenant cached CustomerTier; TTL bounds upgrade-visible delay if push is missed.
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:10:    PendingUserSnapshot,
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:19:    get_pending_users,
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:20:    write_pending_users,
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:39:    # The pending list lives in the target tenant's KV store, not the caller's.
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:42:        pending_users = get_pending_users()
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:43:        if email in pending_users:
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:45:        write_pending_users(pending_users + [email])
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:52:    body's tenant_id is an unchecked write into any tenant's pending list."""
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:81:@router.get("/users/pending")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:82:def list_pending_users(
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:84:) -> list[PendingUserSnapshot]:
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:85:    pending_emails = get_pending_users()
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:86:    return [PendingUserSnapshot(email=email) for email in pending_emails]
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:97:    if email not in {pending.lower() for pending in get_pending_users()}:
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:99:            OnyxErrorCode.BAD_REQUEST, "No pending join request for this email"
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:41:# Spending limits are an Enterprise feature, so every endpoint here is mounted
HEAD:backend/ee/onyx/utils/license.py:38:# stale license. Redis key TTL is the debounce. Redis rather than the cache
HEAD:backend/ee/onyx/utils/license.py:244:def _is_stale_replacement(stored_data: str, incoming: LicensePayload) -> bool:
HEAD:backend/ee/onyx/utils/license.py:284:                "License stored but its stale cache entry survives: %s",
HEAD:backend/ee/onyx/utils/license.py:326:    # map would hand back those stale attributes. Expire so the read below is
HEAD:backend/ee/onyx/utils/license.py:348:    if stored and _is_stale_replacement(stored.license_data, payload):
HEAD:backend/ee/onyx/utils/license.py:351:        # sync is what a user clicks to clear staleness.
HEAD:backend/ee/onyx/utils/license.py:564:    grace_period_end: datetime | None = None,
HEAD:backend/ee/onyx/utils/license.py:572:        grace_period_end: Optional grace period end datetime
HEAD:backend/ee/onyx/utils/license.py:581:    # Check if grace period has expired
HEAD:backend/ee/onyx/utils/license.py:582:    if grace_period_end and now > grace_period_end:
HEAD:backend/ee/onyx/utils/license.py:587:        if grace_period_end and now <= grace_period_end:
HEAD:backend/ee/onyx/utils/license.py:588:            return ApplicationStatus.GRACE_PERIOD
HEAD:backend/ee/onyx/utils/license_expiry.py:9:    NONE  more than 30 days remain, or grace period already exhausted
HEAD:backend/ee/onyx/utils/license_expiry.py:13:    GRACE license already expired, within the 14-day grace window
HEAD:backend/ee/onyx/utils/license_expiry.py:22:LICENSE_GRACE_PERIOD_DAYS = 14
HEAD:backend/ee/onyx/utils/license_expiry.py:72:    GRACE = "grace"
HEAD:backend/ee/onyx/utils/license_expiry.py:99:    if days_remaining > -LICENSE_GRACE_PERIOD_DAYS:
HEAD:backend/ee/onyx/utils/license_expiry.py:100:        return ExpiryWarningStage.GRACE
HEAD:backend/ee/onyx/utils/license_expiry.py:104:def get_grace_period_end(expires_at: datetime) -> datetime:
HEAD:backend/ee/onyx/utils/license_expiry.py:105:    return expires_at + timedelta(days=LICENSE_GRACE_PERIOD_DAYS)
HEAD:backend/ee/onyx/utils/license_expiry.py:108:def get_grace_days_remaining(expires_at: datetime) -> int:
HEAD:backend/ee/onyx/utils/license_expiry.py:109:    grace_end_date = get_grace_period_end(expires_at).date()
HEAD:backend/ee/onyx/utils/license_expiry.py:111:    return max(0, (grace_end_date - today).days)
HEAD:backend/ee/onyx/utils/license_notifications.py:20:    get_grace_days_remaining,
HEAD:backend/ee/onyx/utils/license_notifications.py:37:    stage: ExpiryWarningStage, expires_str: str, grace_days_remaining: int
HEAD:backend/ee/onyx/utils/license_notifications.py:41:    if stage == ExpiryWarningStage.GRACE:
HEAD:backend/ee/onyx/utils/license_notifications.py:43:            f"Onyx trial ended. {grace_days_remaining} grace days remaining",
HEAD:backend/ee/onyx/utils/license_notifications.py:45:            f"You have {grace_days_remaining} day(s) of access remaining. Check "
HEAD:backend/ee/onyx/utils/license_notifications.py:47:            f"Onyx trial ended. {grace_days_remaining} grace days remaining",
HEAD:backend/ee/onyx/utils/license_notifications.py:63:    grace_days_remaining: int,
HEAD:backend/ee/onyx/utils/license_notifications.py:75:            f"{renewal_error} You have {grace_days_remaining} day(s) of grace "
HEAD:backend/ee/onyx/utils/license_notifications.py:83:            f"failed: {renewal_error} You have {grace_days_remaining} day(s) of "
HEAD:backend/ee/onyx/utils/license_notifications.py:84:            "grace access remaining.",
HEAD:backend/ee/onyx/utils/license_notifications.py:88:        return _build_trial_copy(stage, expires_str, grace_days_remaining)
HEAD:backend/ee/onyx/utils/license_notifications.py:110:    if stage == ExpiryWarningStage.GRACE:
HEAD:backend/ee/onyx/utils/license_notifications.py:112:            f"Onyx license expired. {grace_days_remaining} grace days remaining",
HEAD:backend/ee/onyx/utils/license_notifications.py:114:            f"{grace_days_remaining} day(s) of grace access remaining before "
HEAD:backend/ee/onyx/utils/license_notifications.py:116:            f"Onyx license expired. {grace_days_remaining} grace days remaining",
HEAD:backend/ee/onyx/utils/license_notifications.py:153:        # day's ordinary grace reminder and get silently dropped.
HEAD:backend/ee/onyx/utils/license_notifications.py:155:    if stage == ExpiryWarningStage.GRACE:
HEAD:backend/ee/onyx/utils/license_notifications.py:156:        # Grace period sends one notification per UTC date so admins are
HEAD:backend/ee/onyx/utils/license_notifications.py:165:    """t_1d, grace, and failed renewals are errors; earlier stages warn.
HEAD:backend/ee/onyx/utils/license_notifications.py:167:    if renewal_error or stage in (ExpiryWarningStage.T_1D, ExpiryWarningStage.GRACE):
HEAD:backend/ee/onyx/utils/license_notifications.py:200:    grace_days = get_grace_days_remaining(expires_at)
HEAD:backend/ee/onyx/utils/license_notifications.py:202:        stage, expires_at, grace_days, renewal_error, is_trial
HEAD:backend/ee/onyx/utils/license_notifications.py:266:    grace_days = get_grace_days_remaining(payload.expires_at)
HEAD:backend/ee/onyx/utils/license_notifications.py:268:        stage, payload.expires_at, grace_days, is_trial=payload.ends_with_trial
HEAD:backend/ee/onyx/utils/posthog_client.py:40:# We should eventually unify them into a single posthog project,
HEAD:backend/onyx/access/models.py:58:        This is especially helpful to use when you are performing permission-syncing, and some document's permissions aren't able
HEAD:backend/onyx/access/models.py:73:    together. It's used for syncing document permissions to Vespa.
HEAD:backend/onyx/access/models.py:113:    Used for syncing hierarchy node permissions (e.g., folder permissions).
HEAD:backend/onyx/auth/captcha.py:163:        logger.warning("Captcha token stale: age=%ss", format(age_seconds, ".1f"))
HEAD:backend/onyx/auth/captcha.py:223:    mismatch, stale createTime, action mismatch, hard-reject reason, or
HEAD:backend/onyx/auth/disposable_email_validator.py:26:    stale-while-revalidate: callers always get the cached set (or the
HEAD:backend/onyx/auth/disposable_email_validator.py:77:        # Set initialized flag last to prevent race conditions
HEAD:backend/onyx/auth/disposable_email_validator.py:174:                # Re-check staleness under the lock: a refresh may have
HEAD:backend/onyx/auth/disposable_email_validator.py:191:        Stale-while-revalidate: a stale cache triggers a background
HEAD:backend/onyx/auth/invited_users.py:3:from onyx.configs.constants import KV_PENDING_USERS_KEY, KV_USER_STORE_KEY
HEAD:backend/onyx/auth/invited_users.py:34:def get_pending_users() -> list[str]:
HEAD:backend/onyx/auth/invited_users.py:37:        return cast(list, store.load(KV_PENDING_USERS_KEY))
HEAD:backend/onyx/auth/invited_users.py:42:def write_pending_users(emails: list[str]) -> int:
HEAD:backend/onyx/auth/invited_users.py:44:    store.store(KV_PENDING_USERS_KEY, cast(JSON_ro, emails))
HEAD:backend/onyx/auth/oauth_refresher.py:425:                    # at worst the second coroutine sees the same stale
HEAD:backend/onyx/auth/oauth_refresher.py:431:                    # oidc_expiry is re-read so a stale one cannot reject the request.
HEAD:backend/onyx/auth/oauth_refresher.py:435:                        "Could not reload oidc_expiry for %s, a stale value may "
HEAD:backend/onyx/auth/oauth_token_manager.py:255:        # Add 60 second buffer to avoid race conditions
HEAD:backend/onyx/auth/session_tokens.py:3:Token values embed their logical expiry; the physical TTL adds a grace window
HEAD:backend/onyx/auth/session_tokens.py:6:(no entry: cookie outlived the grace window, or Redis dropped the key),
HEAD:backend/onyx/auth/session_tokens.py:33:SESSION_TOKEN_GRACE_PERIOD_SECONDS = 60 * 60
HEAD:backend/onyx/auth/session_tokens.py:130:    return lifetime_seconds + SESSION_TOKEN_GRACE_PERIOD_SECONDS
HEAD:backend/onyx/auth/session_tokens.py:220:            "the grace window, or Redis dropped the key (restart/eviction/flush)."
HEAD:backend/onyx/auth/users.py:85:    SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:818:                    # Race condition: another request created the same user after the
HEAD:backend/onyx/auth/users.py:1089:                    # the row is stale: the IdP re-issued its subjects (a new Entra
HEAD:backend/onyx/auth/users.py:1091:                    stale_link: OAuthAccount | None = next(
HEAD:backend/onyx/auth/users.py:1114:                            stale_link is not None
HEAD:backend/onyx/auth/users.py:1126:                    if stale_link is None:
HEAD:backend/onyx/auth/users.py:1135:                            stale_link.account_id,
HEAD:backend/onyx/auth/users.py:1139:                            user, stale_link, oauth_account_dict
HEAD:backend/onyx/auth/users.py:1200:            # user by subject and so arrives here with a stale email too.
HEAD:backend/onyx/auth/users.py:1514:            # so on-call needs the traceback to tell which one broke.
HEAD:backend/onyx/auth/users.py:1642:# The cookie outlives the logical expiry by the grace window so a dead token is
HEAD:backend/onyx/auth/users.py:1646:    cookie_max_age=SESSION_EXPIRE_TIME_SECONDS + SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:1684:    Token values embed their logical expiry and outlive it by a grace window;
HEAD:backend/onyx/auth/users.py:1755:            ex=SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:2116:                    "Inactive user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/auth/users.py:2122:                    "Non-web-login user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/background/README.md:7:3. Cleaning up checkpoints and logic around indexing work (indexing indexing checkpoints and index attempt metadata)
HEAD:backend/onyx/background/README.md:16:| Light                     | `apps/light.py`                | `vespa_metadata_sync`, `connector_deletion`, `doc_permissions_upsert`, `checkpoint_cleanup`, `index_attempt_cleanup` |
HEAD:backend/onyx/background/README.md:58:| `check_for_vespa_sync_task`       | 20s       | Finds stale documents/document sets → dispatches sync tasks to `VESPA_METADATA_SYNC` queue |
HEAD:backend/onyx/background/README.md:62:| `check_for_checkpoint_cleanup`    | 1h        | Cleans up old indexing checkpoints                                                         |
HEAD:backend/onyx/background/README.md:64:| `celery_beat_heartbeat`           | 1m        | Heartbeat for Beat watchdog                                                                |
HEAD:backend/onyx/background/README.md:66:Watchdog is a separate Python process managed by supervisord which runs alongside celery workers. It checks the ONYX_CELERY_BEAT_HEARTBEAT_KEY in
HEAD:backend/onyx/background/README.md:67:Redis to ensure Celery Beat is not dead. Beat schedules the celery_beat_heartbeat for Primary to touch the key and share that it's still alive.
HEAD:backend/onyx/background/README.md:79:- Cleanup of checkpoints and index attempts
HEAD:backend/onyx/background/celery/apps/app_base.py:12:from celery.app import trace
HEAD:backend/onyx/background/celery/apps/app_base.py:69:    SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:83:        traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:94:    The set lives only in memory, propagates between workers via mingle, and its
HEAD:backend/onyx/background/celery/apps/app_base.py:621:    task_logger.propagate = False
HEAD:backend/onyx/background/celery/apps/app_base.py:629:    trace.logger.setLevel(logging.WARNING)
HEAD:backend/onyx/background/celery/apps/app_base.py:635:    trace.logger.setLevel(logLevel)
HEAD:backend/onyx/background/celery/apps/app_base.py:742:    "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:745:    "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:746:    "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:749:# above. It contains celery_beat_heartbeat (which only writes to Redis) alongside
HEAD:backend/onyx/background/celery/apps/beat.py:18:from shared_configs.configs import IGNORED_SYNCING_TENANT_LIST, MULTI_TENANT
HEAD:backend/onyx/background/celery/apps/beat.py:54:        # An initial schedule is required ... otherwise, the scheduler will delay
HEAD:backend/onyx/background/celery/apps/beat.py:123:            if IGNORED_SYNCING_TENANT_LIST and tenant_id in IGNORED_SYNCING_TENANT_LIST:
HEAD:backend/onyx/background/celery/apps/beat.py:125:                    "Skipping tenant %s as it is in the ignored syncing list",
HEAD:backend/onyx/background/celery/apps/docfetching.py:136:    # in-flight attempt for a fast checkpoint resume, not the heartbeat timeout.
HEAD:backend/onyx/background/celery/apps/docfetching.py:138:        "worker_shutting_down received, flagging docfetching for graceful interrupt."
HEAD:backend/onyx/background/celery/apps/light.py:164:            "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/monitoring.py:81:    broker Redis client on each scrape (rather than holding a stale reference).
HEAD:backend/onyx/background/celery/apps/primary.py:226:                # If the task is not in PENDING state, it exists in Celery
HEAD:backend/onyx/background/celery/apps/primary.py:227:                if result.state != "PENDING":
HEAD:backend/onyx/background/celery/celery_utils.py:14:from onyx.connectors.connector_runner import CheckpointOutputWrapper
HEAD:backend/onyx/background/celery/celery_utils.py:18:    CheckpointedConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:19:    ConnectorCheckpoint,
HEAD:backend/onyx/background/celery/celery_utils.py:36:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/onyx/background/celery/celery_utils.py:45:CT = TypeVar("CT", bound=ConnectorCheckpoint)
HEAD:backend/onyx/background/celery/celery_utils.py:60:def _checkpointed_batched_items(
HEAD:backend/onyx/background/celery/celery_utils.py:61:    connector: CheckpointedConnector[CT],
HEAD:backend/onyx/background/celery/celery_utils.py:65:    """Loop through all checkpoint steps and yield batched items.
HEAD:backend/onyx/background/celery/celery_utils.py:67:    Some checkpointed connectors (e.g. IMAP) are multi-step: the first
HEAD:backend/onyx/background/celery/celery_utils.py:68:    checkpoint call may only initialize internal state without yielding
HEAD:backend/onyx/background/celery/celery_utils.py:69:    any documents. This function loops until checkpoint.has_more is False
HEAD:backend/onyx/background/celery/celery_utils.py:72:    checkpoint = connector.build_dummy_checkpoint()
HEAD:backend/onyx/background/celery/celery_utils.py:74:        checkpoint_output = connector.load_from_checkpoint(
HEAD:backend/onyx/background/celery/celery_utils.py:75:            start=start, end=end, checkpoint=checkpoint
HEAD:backend/onyx/background/celery/celery_utils.py:77:        wrapper: CheckpointOutputWrapper[CT] = CheckpointOutputWrapper()
HEAD:backend/onyx/background/celery/celery_utils.py:79:        for document, hierarchy_node, failure, next_checkpoint in wrapper(
HEAD:backend/onyx/background/celery/celery_utils.py:80:            checkpoint_output
HEAD:backend/onyx/background/celery/celery_utils.py:89:            if next_checkpoint is not None:
HEAD:backend/onyx/background/celery/celery_utils.py:90:                checkpoint = next_checkpoint
HEAD:backend/onyx/background/celery/celery_utils.py:95:        if not checkpoint.has_more:
HEAD:backend/onyx/background/celery/celery_utils.py:148:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/onyx/background/celery/celery_utils.py:192:    elif isinstance(runnable_connector, CheckpointedConnector):
HEAD:backend/onyx/background/celery/celery_utils.py:195:        raw_batch_generator = _checkpointed_batched_items(
HEAD:backend/onyx/background/celery/memory_monitoring.py:5:import tracemalloc
HEAD:backend/onyx/background/celery/memory_monitoring.py:12:    INDEXING_WORKER_TRACEMALLOC,
HEAD:backend/onyx/background/celery/memory_monitoring.py:87:# log a tracemalloc snapshot (when enabled) so allocation sites are captured
HEAD:backend/onyx/background/celery/memory_monitoring.py:93:_TRACEMALLOC_FRAMES = 10
HEAD:backend/onyx/background/celery/memory_monitoring.py:99:    """Mirrors the heartbeat thread pattern; call from the spawned process
HEAD:backend/onyx/background/celery/memory_monitoring.py:104:    if INDEXING_WORKER_TRACEMALLOC and not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:105:        tracemalloc.start(_TRACEMALLOC_FRAMES)
HEAD:backend/onyx/background/celery/memory_monitoring.py:149:    if not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:151:            "tracemalloc is disabled; set INDEXING_WORKER_TRACEMALLOC=true to "
HEAD:backend/onyx/background/celery/memory_monitoring.py:156:    snapshot = tracemalloc.take_snapshot()
HEAD:backend/onyx/background/celery/memory_monitoring.py:159:        logger.warning("tracemalloc top allocation: %s", stat)
HEAD:backend/onyx/background/celery/memory_monitoring.py:161:        for line in stats[0].traceback.format():
HEAD:backend/onyx/background/celery/memory_monitoring.py:162:            logger.warning("tracemalloc largest site: %s", line)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:120:        "name": "check-for-checkpoint-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:121:        "task": OnyxCeleryTask.CHECK_FOR_CHECKPOINT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:126:            # Run on gated tenants too — they may still have stale checkpoints to clean.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:132:        "name": "check-for-stale-capability-runs",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:133:        "task": OnyxCeleryTask.CHECK_FOR_STALE_CAPABILITY_RUNS,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:150:            # Run on gated tenants too — they may still have stale index attempts.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:240:        # Ticks are cheap (DB-only when nothing is stale); snapshot pacing is
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:346:    "check-for-checkpoint-cleanup",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:456:                "name": "celery-beat-heartbeat",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:457:                "task": OnyxCeleryTask.CELERY_BEAT_HEARTBEAT,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:19:    user_has_stale_active_session,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:41:    Background snapshots bound data loss from ungraceful pod death (kubelet
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:126:                    if not user_has_stale_active_session(
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:6:writer model). A run that fails gracefully records FAILED_TO_RUN itself; only
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:20:    capability_check_run_stale_after,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:28:    mark_stale_capability_runs_failed,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:119:        # would read RUNNING until the sweep's staleness window expires. Hard
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:133:    name=OnyxCeleryTask.CHECK_FOR_STALE_CAPABILITY_RUNS,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:136:def check_for_stale_capability_runs(
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:151:            retired = mark_stale_capability_runs_failed(
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:154:                stale_after=capability_check_run_stale_after(source),
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:158:                    f"Retired {retired} stale capability run(s) for source "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:1:import traceback
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:249:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:267:    """Returns an int if syncing is needed. The int represents the number of sync tasks generated.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:268:    Note that syncing can still be required even if the number of sync tasks generated is zero.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:269:    Returns None if no syncing is required.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:280:    # don't generate sync tasks if tasks are still pending
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:285:    # to avoid a race condition with db.commit/fence deletion
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:329:                    "Connector deletion - Delayed (indexing in progress): "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:346:                    "Connector deletion - Delayed (waiting for in-progress port to stop): "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:354:                f"Connector deletion - Delayed (pruning in progress): cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:360:                f"Connector deletion - Delayed (permissions in progress): cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:607:            stack_trace = traceback.format_exc()
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:608:            error_message = f"Error: {str(e)}\n\nStack Trace:\n{stack_trace}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:706:    1. An unknown task id is always returned as state PENDING.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:4:import traceback
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:19:from onyx.background.celery.tasks.docprocessing.heartbeat import (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:20:    start_heartbeat,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:21:    stop_heartbeat,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:39:    CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:58:from shared_configs.configs import SENTRY_CELERY_TRACES_SAMPLE_RATE, SENTRY_DSN
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:136:    # Start heartbeat for this indexing attempt
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:137:    heartbeat_thread, stop_event = start_heartbeat(index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:146:        stop_heartbeat(heartbeat_thread, stop_event)  # Stop heartbeat before exiting
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:162:        init_sentry(traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:265:            sanitized_e.__traceback__ = e.__traceback__
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:348:        start and end time, from prev checkpoint or not), then run that connector. Specifically,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:376:    - non-checkpointed connectors/ new runs in general => delete the old document batches from the file store and do the new run
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:377:    - checkpointed connectors + resuming from checkpoint => reissue the old document batches and do a new run
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:381:    - Heartbeat spawned in docfetching and docprocessing is how check_for_indexing monitors liveliness
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:515:            # stop it. A fresh attempt resumes from checkpoint on the next beat.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:529:                                "from the last checkpoint.",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:540:                        CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:587:                # a kernel kill takes down the whole pod (the attempt heartbeat and
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:589:                # "No heartbeat received" failure. Checked every loop iteration
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:639:                                CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:689:                job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:704:            # No need to expose full stack trace for validation errors
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:707:            result.exception_str = traceback.format_exc()
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:718:                # otherwise we're overwriting potential real stack traces
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:727:                        full_exception_trace=result.exception_str,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:752:        raise RuntimeError(f"Exception encountered: traceback={result.exception_str}")
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:774:        job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:791:        job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:796:        # (e.g. heartbeat watchdog marking it FAILED, user requesting cancellation,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:802:        # already marked INTERRUPTED in the loop (best-effort). The heartbeat
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:808:        # attempt lingers in_progress until the heartbeat watchdog fails it with
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:809:        # the opaque "No heartbeat received" message this status exists to replace.
HEAD:backend/onyx/background/celery/tasks/docfetching/worker_shutdown.py:4:polls it and interrupts its in-flight attempt for a fast checkpoint resume instead
HEAD:backend/onyx/background/celery/tasks/docfetching/worker_shutdown.py:5:of the heartbeat timeout. Both run in the same process (handler on the main thread,
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:4:  docprocessing_pending_{id}   - batches dispatched but not yet picked up
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:8:from queue backlogs (in_flight = 0, pending > 0) when the heartbeat stops.
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:42:    # Emit a heartbeat before moving the counter to in_flight. This ensures
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:43:    # the monitor never sees in_flight > 0 with a stale heartbeat for a live
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:55:                .values(heartbeat_counter=IndexAttempt.heartbeat_counter + 1)
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:60:            "Failed to emit heartbeat on prerun for attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/batch_counters.py:67:        RedisDocprocessing(index_attempt_id, r).decr_pending_incr_in_flight()
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:6:from onyx.configs.constants import INDEXING_WORKER_HEARTBEAT_INTERVAL
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:14:def start_heartbeat(index_attempt_id: int) -> tuple[threading.Thread, threading.Event]:
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:15:    """Start a heartbeat thread for the given index attempt"""
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:18:    def heartbeat_loop() -> None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:19:        while not stop_event.wait(INDEXING_WORKER_HEARTBEAT_INTERVAL):
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:25:                        .values(heartbeat_counter=IndexAttempt.heartbeat_counter + 1)
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:30:                    "Failed to update heartbeat counter for index attempt %s",
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:36:    thread = threading.Thread(target=context.run, args=(heartbeat_loop,), daemon=True)
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:41:def stop_heartbeat(thread: threading.Thread, stop_event: threading.Event) -> None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:42:    """Stop the heartbeat thread"""
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:4:import traceback
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:29:from onyx.background.celery.tasks.docprocessing.heartbeat import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:30:    start_heartbeat,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:31:    stop_heartbeat,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:42:from onyx.background.indexing.checkpointing_utils import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:43:    cleanup_checkpoint,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:44:    get_index_attempts_with_old_checkpoints,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:94:    get_stale_not_started_index_attempts,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:156:# Heartbeat timeout: if no heartbeat received for 30 minutes, consider it dead.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:157:# This should be much longer than INDEXING_WORKER_HEARTBEAT_INTERVAL (30s).
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:158:HEARTBEAT_TIMEOUT_SECONDS = 30 * 60  # 30 minutes
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:189:    Validates that active indexing attempts are still alive by checking heartbeat.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:190:    If no heartbeat has been received for a certain amount of time, mark the attempt as failed.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:192:    This uses the heartbeat_counter field which is incremented by active worker threads
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:193:    every INDEXING_WORKER_HEARTBEAT_INTERVAL seconds.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:206:                    # the docprocessing heartbeat counter.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:218:            heartbeat_timeout_seconds = HEARTBEAT_TIMEOUT_SECONDS
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:225:            # Check if this attempt has been updated with heartbeat tracking
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:226:            if fresh_attempt.last_heartbeat_time is None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:227:                # First time seeing this attempt - initialize heartbeat tracking
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:228:                fresh_attempt.last_heartbeat_value = fresh_attempt.heartbeat_counter
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:229:                fresh_attempt.last_heartbeat_time = datetime.now(timezone.utc)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:233:                    f"Initialized heartbeat tracking for attempt {fresh_attempt.id}: counter={fresh_attempt.heartbeat_counter}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:237:            # Check if the heartbeat counter has advanced since last check
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:238:            current_counter = fresh_attempt.heartbeat_counter
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:239:            last_known_counter = fresh_attempt.last_heartbeat_value
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:240:            last_check_time = fresh_attempt.last_heartbeat_time
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:243:                f"Checking heartbeat for attempt {fresh_attempt.id}: "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:250:                # Heartbeat has advanced - worker is alive
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:251:                fresh_attempt.last_heartbeat_value = current_counter
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:252:                fresh_attempt.last_heartbeat_time = datetime.now(timezone.utc)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:256:                    f"Heartbeat advanced for attempt {fresh_attempt.id}: new_counter={current_counter}"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:261:                seconds=heartbeat_timeout_seconds
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:264:            # Heartbeat hasn't advanced - check if it's been too long
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:267:                    f"Heartbeat hasn't advanced for attempt {fresh_attempt.id} but still within timeout window"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:271:            # Heartbeat is stale. If docfetching has finished (total_batches is
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:275:            #   in_flight = 0, pending > 0  → batches in queue, no crash → wait
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:276:            #   in_flight = 0, pending = 0  → no work anywhere, stuck → invalidate
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:282:                pending = 0
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:287:                    pending = rd.pending()
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:295:                    f"Stale heartbeat for attempt {fresh_attempt.id}: "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:296:                    f"in_flight={in_flight} pending={pending} "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:300:                if in_flight == 0 and pending > 0:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:304:                        f"Attempt {fresh_attempt.id} has {pending} batches in queue, "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:311:                        f"Heartbeat stale for {heartbeat_timeout_seconds}s with "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:315:                    # in_flight == 0, pending == 0: no work anywhere, no forward
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:318:                        f"Heartbeat stale for {heartbeat_timeout_seconds}s with "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:319:                        f"no pending or in-flight batches — all batches failed or lost"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:323:                # worker process died. The heartbeat thread runs independently
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:324:                # of rate limiting, so a stale heartbeat here means a real crash.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:326:                    f"No heartbeat received for {heartbeat_timeout_seconds} seconds"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:331:                f"last_heartbeat_time={last_check_time} "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:344:                    f"Marked attempt {fresh_attempt.id} as failed due to heartbeat timeout"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:349:                    f"Failed to mark attempt {fresh_attempt.id} as failed due to heartbeat timeout"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:352:        # Separately handle NOT_STARTED attempts. Their heartbeat_counter never
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:353:        # advances (the task hasn't started), so the heartbeat loop above cannot
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:361:        stale_not_started = get_stale_not_started_index_attempts(db_session, cutoff)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:362:        if stale_not_started:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:371:            for attempt in stale_not_started:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:375:                # Brief sleep to rule out the race where the task was just
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:427:    Race condition handling:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:430:    - Handles concurrent completion gracefully
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:499:                    full_exception_trace=traceback.format_exc(),
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:674:    # filtered as stale by `index_doc_batch_prepare`).
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:697:    This prevents race conditions where multiple indexing attempts could be created.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:864:    w.r.t previous failed attempt, checkpointing, etc is handled in the docfetching task.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1036:                    # models. Also, they are more prone to repeated failures -> eventual success.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1182:            "Soft time limit exceeded, task is being terminated gracefully."
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1222:    name=OnyxCeleryTask.CHECK_FOR_CHECKPOINT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1226:def check_for_checkpoint_cleanup(self: Task, *, tenant_id: str) -> None:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1227:    """Clean up old checkpoints that are older than 7 days."""
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1231:        OnyxRedisLocks.CHECK_CHECKPOINT_CLEANUP_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1242:            old_attempts = get_index_attempts_with_old_checkpoints(db_session)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1245:                    f"Cleaning up checkpoint for index attempt {attempt.id}"
```
## Audit and Logging Signals
Evidence lines: 600
```text
HEAD:backend/ee/onyx/access/access.py:78:            logger.error("Document %s has no source", document_id)
HEAD:backend/ee/onyx/auth/users.py:30:        logger.warning("SUPER_CLOUD_API_KEY is not configured; rejecting request")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:121:                task_logger.exception("tenant work gating: runtime flag read failed")
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1117:    task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:122:        task_logger.error(
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
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:634:            logger.exception(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:644:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:663:        logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:748:        task_logger.error(msg)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:769:        task_logger.exception(msg)
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
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:243:                task_logger.info(f"Successfully pre-provisioned tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:247:                task_logger.error(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:254:        task_logger.error("Error in pre_provision_tenant task", exc_info=True)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:257:            task_logger.info(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:267:                task_logger.exception(f"Error during rollback for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:273:            task_logger.warning(
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:26:        task_logger.warning(f"Could not parse usergroup id from {fence_key}")
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:32:        task_logger.exception(f"usergroup_id ({usergroup_id_str}) is not an integer!")
HEAD:backend/ee/onyx/db/license.py:171:            logger.warning("License deleted but cache invalidation failed: %s", e)
HEAD:backend/ee/onyx/db/license.py:172:        logger.info("License deleted")
HEAD:backend/ee/onyx/db/license.py:254:        logger.warning("Failed to parse cached license metadata: %s", e)
HEAD:backend/ee/onyx/db/license.py:271:    logger.info("License cache invalidated")
HEAD:backend/ee/onyx/db/license.py:389:            logger.warning("License cache lease lost mid-publish, dropping entry")
HEAD:backend/ee/onyx/db/license.py:415:            logger.warning("License cache lock contended, serving uncached")
HEAD:backend/ee/onyx/db/license.py:417:        logger.warning("License cache lock errored (%s), serving uncached", e)
HEAD:backend/ee/onyx/db/license.py:448:        logger.error("Failed to verify license during cache refresh: %s", e)
HEAD:backend/ee/onyx/db/scim.py:234:            logger.warning("SCIM user mapping %d not found during delete", mapping_id)
HEAD:backend/ee/onyx/db/scim.py:543:            logger.warning("SCIM group mapping %d not found during delete", mapping_id)
HEAD:backend/ee/onyx/db/scim.py:715:        would strip every group manager on each sync, unaudited.
HEAD:backend/ee/onyx/db/user_group.py:69:from onyx.utils.audit import (
HEAD:backend/ee/onyx/db/user_group.py:70:    AuditAction,
HEAD:backend/ee/onyx/db/user_group.py:71:    AuditOutcome,
HEAD:backend/ee/onyx/db/user_group.py:73:    emit_audit_event,
HEAD:backend/ee/onyx/db/user_group.py:915:        emit_audit_event(
HEAD:backend/ee/onyx/db/user_group.py:916:            AuditAction.USER_GROUP_CHANGE,
HEAD:backend/ee/onyx/db/user_group.py:917:            AuditOutcome.SUCCESS,
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
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:83:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:142:        logger.warning("Email for userKey %s not found in Confluence", user_key)
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:145:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:208:            logger.warning("Email for user %s not found in Confluence", user_name)
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:211:        logger.warning(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:241:            logger.info(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:303:        logger.warning(
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
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:159:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:196:        logger.info(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:224:        # an audit-log based approach in the future so not doing it now.
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:237:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:247:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:306:        logger.warning("Folder missing ID, returning empty permissions")
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:340:                logger.warning("User permission without email for folder %s", folder_id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:346:                logger.warning(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:396:        logger.info("Drive perm sync: Processing %s documents", len(slim_doc_batch))
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:422:        logger.info("Drive perm sync: Processed %s total documents", total_processed)
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
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:184:                logger.info("Added user: %s", user_principal_name or mail)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:187:                    logger.error("No display name for group: %s", member_data.get("id"))
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:192:                logger.info("Added group: %s", name)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:194:                logger.warning("Could not identify member type for: %s", member_data)
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:225:            logger.warning(
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:248:    logger.info("Enumerated %s Entra groups via paginated Graph API", total_groups)
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:73:            logger.exception(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:57:    logger.info(
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:61:        logger.warning("User '%s' not found in Salesforce", user_email)
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:41:    logger.info("Processing %s sites for group sync", len(site_descriptors))
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:114:        logger.error(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:139:        logger.error("Failed to check if item %s is public: %s", drive_item.id, e)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:153:            logger.info("Login name %s is public", login_name)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:189:                    logger.warning(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:256:        logger.info(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:289:                    logger.warning("Group %s not found", group.login_name)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:336:        logger.warning("Group %s not found", group.login_name)
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
HEAD:backend/ee/onyx/server/billing/api.py:259:        logger.warning("Billing info cache client unavailable: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:276:            logger.warning("Billing info cache invalidation failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:316:            logger.warning("Billing info cache read failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:327:                    logger.warning("Billing info cache deserialize failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/api.py:352:            logger.warning("Billing info cache write failed: %s", exc)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:103:        logger.warning(
HEAD:backend/ee/onyx/server/billing/billing_cache.py:119:            logger.warning(
HEAD:backend/ee/onyx/server/billing/billing_cache.py:130:        logger.warning("billing cache write failed for tenant %s: %s", tenant_id, e)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:164:        logger.warning(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:103:    logger.info("Permissions sync queued: cc_pair=%s id=%s", cc_pair_id, payload_id)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:182:    logger.info("External group sync queued: cc_pair=%s id=%s", cc_pair_id, payload_id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:168:        logger.info("Successfully refreshed tokens for user %s", user.id)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:172:            logger.warning("Full authentication required for user %s", user.id)
HEAD:backend/ee/onyx/server/log_export/storage.py:333:        logger.info("Deleted %d expired log-export files", deleted_count)
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:82:                    logger.warning(
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:88:                    logger.info(
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:105:            logger.exception("Error in tenant ID middleware: %s", str(e))
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:172:                logger.error("Error decoding anonymous user cookie: %s", str(e))
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:185:        logger.error("Unexpected error in _get_tenant_id_from_request: %s", str(e))
HEAD:backend/ee/onyx/server/scim/api.py:111:            AuditAction.USER_GROUP_RENAME,
HEAD:backend/ee/onyx/server/scim/api.py:121:            AuditAction.USER_GROUP_CHANGE,
HEAD:backend/ee/onyx/server/scim/api.py:564:        logger.exception("Failed to assign SCIM user %s to default groups", email)
HEAD:backend/ee/onyx/server/scim/api.py:1375:        AuditAction.USER_GROUP_CREATE,
HEAD:backend/ee/onyx/server/scim/api.py:1590:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/seeding.py:112:                logger.error("Failed to seed tool %s: %s", tool.name, str(e))
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:50:                logger.warning(
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:61:        logger.warning(
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:66:        logger.error("Error parsing usage limit overrides: %s", e)
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:77:    logger.info("Loading tenant usage limit overrides from control plane...")
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:87:        logger.info("Loaded usage limit overrides for %s tenants", len(overrides))
HEAD:backend/ee/onyx/server/tenant_usage_limits.py:89:        logger.info("No tenant-specific usage limit overrides found")
HEAD:backend/ee/onyx/server/tenants/access.py:30:        logger.warning("Invalid API key")
HEAD:backend/ee/onyx/server/tenants/access.py:35:        logger.warning("Invalid authorization header")
HEAD:backend/ee/onyx/server/tenants/access.py:42:            logger.warning("Insufficient permissions")
HEAD:backend/ee/onyx/server/tenants/access.py:45:        logger.warning("Token has expired")
HEAD:backend/ee/onyx/server/tenants/access.py:48:        logger.warning("Invalid token")
HEAD:backend/ee/onyx/server/tenants/admin_api.py:11:from onyx.utils.audit import (
HEAD:backend/ee/onyx/server/tenants/admin_api.py:12:    AuditAction,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:13:    AuditActor,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:14:    AuditOutcome,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:16:    emit_audit_event,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:37:        logger.warning(detail)
HEAD:backend/ee/onyx/server/tenants/admin_api.py:38:        emit_audit_event(
HEAD:backend/ee/onyx/server/tenants/admin_api.py:39:            AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:40:            AuditOutcome.FAILURE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:64:    actor: AuditActor | None,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:74:            logger.warning(detail)
HEAD:backend/ee/onyx/server/tenants/admin_api.py:75:            emit_audit_event(
HEAD:backend/ee/onyx/server/tenants/admin_api.py:76:                AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:77:                AuditOutcome.FAILURE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:99:    emit_audit_event(
HEAD:backend/ee/onyx/server/tenants/admin_api.py:100:        AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:101:        AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:63:            logger.exception("Failed to modify anonymous user path: %s", str(e))
HEAD:backend/ee/onyx/server/tenants/billing.py:230:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/billing.py:237:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/billing_api.py:94:        logger.exception("Failed to gate product")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:114:        logger.exception("Failed to gate products during full sync")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:133:        logger.exception("Failed to apply tier update")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:150:    logger.info("Fetching billing information")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:179:        logger.exception("Failed to create customer portal session")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:202:        logger.exception("Failed to create checkout session")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:230:        logger.exception("Failed to create subscription session")
HEAD:backend/ee/onyx/server/tenants/product_gating.py:39:        logger.exception("Failed to gate product")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:136:                logger.exception(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:143:                    logger.exception(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:149:            logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:165:        logger.error(error_msg, exc_info=e)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:182:    logger.info("Creating new tenant %s for user %s", tenant_id, email)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:189:        logger.exception("Tenant provisioning failed: %s", str(e))
HEAD:backend/ee/onyx/server/tenants/provisioning.py:194:            logger.exception("Failed to rollback tenant provisioning for %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:231:        logger.exception("Failed to create tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:240:    logger.info("Fetching billing information")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:258:                logger.error("Control plane tenant creation failed: %s", error_text)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:269:    logger.info("Rolling back tenant provisioning for tenant_id: %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:279:        logger.info("Successfully dropped schema for tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:282:        logger.error(error_msg)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:294:                logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:302:        logger.error(error_msg)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:319:                    logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:327:        logger.error(error_msg)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:336:            logger.info("Successfully cleared shard mapping for tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:341:            logger.error(error_msg)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:344:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:352:        logger.error("Tenant rollback completed with %s errors", len(rollback_errors))
HEAD:backend/ee/onyx/server/tenants/provisioning.py:354:        logger.info("Tenant rollback completed successfully for tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:402:            logger.error("Failed to configure %s provider: %s", request.provider, e)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:408:            logger.error(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:431:            logger.error("Failed to create default image gen config: %s", e)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:433:        logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:442:            logger.error(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:462:        logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:471:            logger.error(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:495:        logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:503:            logger.error(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:532:        logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:545:            logger.info("Attempting to upsert Cohere cloud embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:547:            logger.info("Successfully upserted Cohere cloud embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:549:            logger.info("Updating search settings with Cohere embedding model details")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:576:            logger.info("Fetching updated search settings to verify changes")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:586:            logger.exception("Failed to configure Cohere embedding provider")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:588:        logger.info(
HEAD:backend/ee/onyx/server/tenants/provisioning.py:597:        logger.info("HUBSPOT_TRACKING_URL not set, skipping HubSpot submission")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:623:        logger.error("Failed to submit to HubSpot: %s", response.text)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:642:                logger.error("Control plane tenant creation failed: %s", error_text)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:676:            logger.error("Control plane tenant lookup failed: %s", response.text)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:689:        logger.error("Error fetching tenant by domain: %s", str(e))
HEAD:backend/ee/onyx/server/tenants/provisioning.py:720:                logger.info("Using pre-provisioned tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:726:            logger.exception("Error getting available tenant")
HEAD:backend/ee/onyx/server/tenants/provisioning.py:764:        logger.exception("Failed to set up tenant %s", tenant_id)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:786:        logger.exception("Failed to assign tenant %s to user %s", tenant_id, email)
HEAD:backend/ee/onyx/server/tenants/proxy.py:56:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/proxy.py:214:        logger.error("Control plane returned %s: %s", status_code, detail)
HEAD:backend/ee/onyx/server/tenants/proxy.py:217:        logger.exception("Failed to connect to control plane")
HEAD:backend/ee/onyx/server/tenants/proxy.py:311:        logger.error("Control plane returned incomplete claim response: %s", result)
HEAD:backend/ee/onyx/server/tenants/proxy.py:400:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/proxy.py:411:            logger.warning(
HEAD:backend/ee/onyx/server/tenants/proxy.py:432:            logger.warning(
HEAD:backend/ee/onyx/server/tenants/proxy.py:466:        logger.error("Control plane returned incomplete license response: %s", result)
HEAD:backend/ee/onyx/server/tenants/schema_management.py:39:    logger.info("Starting Alembic migrations for schema: %s", schema_name)
HEAD:backend/ee/onyx/server/tenants/schema_management.py:70:        logger.info(
HEAD:backend/ee/onyx/server/tenants/schema_management.py:75:        logger.exception(
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:48:        logger.info(
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:55:            logger.exception(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:33:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:40:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:75:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:83:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:92:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/tier_management.py:102:        logger.warning(
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:75:        logger.exception(
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:124:        logger.exception("Failed to accept invite: %s", str(e))
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:139:        logger.exception("Failed to deny invite: %s", str(e))
HEAD:backend/ee/onyx/server/user_group/api.py:69:from onyx.utils.audit import (
HEAD:backend/ee/onyx/server/user_group/api.py:70:    AuditAction,
HEAD:backend/ee/onyx/server/user_group/api.py:71:    AuditOutcome,
HEAD:backend/ee/onyx/server/user_group/api.py:73:    emit_audit_event,
HEAD:backend/ee/onyx/server/user_group/api.py:252:    emit_audit_event(
HEAD:backend/ee/onyx/server/user_group/api.py:253:        AuditAction.USER_GROUP_PERMISSION_CHANGE,
HEAD:backend/ee/onyx/server/user_group/api.py:254:        AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/server/user_group/api.py:283:    emit_audit_event(
HEAD:backend/ee/onyx/server/user_group/api.py:284:        AuditAction.USER_GROUP_CREATE,
HEAD:backend/ee/onyx/server/user_group/api.py:285:        AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/server/user_group/api.py:323:        emit_audit_event(
HEAD:backend/ee/onyx/server/user_group/api.py:324:            AuditAction.USER_GROUP_RENAME,
HEAD:backend/ee/onyx/server/user_group/api.py:325:            AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/server/user_group/api.py:437:    emit_audit_event(
HEAD:backend/ee/onyx/server/user_group/api.py:438:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/user_group/api.py:439:        AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/server/user_group/api.py:645:    emit_audit_event(
HEAD:backend/ee/onyx/server/user_group/api.py:646:        AuditAction.USER_GROUP_MANAGER_CHANGE,
HEAD:backend/ee/onyx/server/user_group/api.py:647:        AuditOutcome.SUCCESS,
HEAD:backend/ee/onyx/utils/license.py:277:        logger.warning("Failed to publish license cache: %s", cache_error)
HEAD:backend/ee/onyx/utils/license_notifications.py:138:        logger.exception("Failed to send license expiry email to %s", user_email)
HEAD:backend/ee/onyx/utils/posthog_client.py:82:        logger.error("Error identifying cloud posthog user: %s", e)
HEAD:backend/ee/onyx/utils/posthog_client.py:98:        logger.error("Error aliasing PostHog user: %s", e)
HEAD:backend/ee/onyx/utils/telemetry.py:63:        logger.error("Error identifying PostHog user: %s", e)
HEAD:backend/ee/onyx/utils/tier.py:84:        logger.warning("Self-hosted tier: license cache read failed: %s", e)
HEAD:backend/onyx/access/models.py:25:        """Prevent extremely long logs"""
HEAD:backend/onyx/auth/captcha.py:135:        logger.error("Captcha replay cache error (failing open): %s", e)
HEAD:backend/onyx/auth/captcha.py:146:        logger.error("Captcha replay cache release error (ignored): %s", e)
HEAD:backend/onyx/auth/login_claims_capture.py:337:                logger.warning("OAuth claims capture: userinfo fetch failed: %s", e)
HEAD:backend/onyx/auth/oauth_refresher.py:126:        logger.warning("Cached token endpoint now fails SSRF policy: %s", e)
HEAD:backend/onyx/auth/oauth_refresher.py:319:        logger.info("Refreshing OAuth token for %s's %s account", user.email, provider)
HEAD:backend/onyx/auth/oauth_refresher.py:379:            logger.info("Successfully refreshed OAuth token for %s", user.email)
HEAD:backend/onyx/auth/scoped_permissions.py:24:from onyx.utils.audit import (
HEAD:backend/onyx/auth/scoped_permissions.py:25:    AuditAction,
HEAD:backend/onyx/auth/scoped_permissions.py:26:    AuditOutcome,
HEAD:backend/onyx/auth/scoped_permissions.py:28:    emit_audit_event,
HEAD:backend/onyx/auth/scoped_permissions.py:39:    emit_audit_event(
HEAD:backend/onyx/auth/scoped_permissions.py:40:        AuditAction.PERMISSION_DENIED,
HEAD:backend/onyx/auth/scoped_permissions.py:41:        AuditOutcome.DENIED,
HEAD:backend/onyx/auth/users.py:159:from onyx.utils.audit import AuditAction, AuditActor, AuditOutcome, emit_audit_event
HEAD:backend/onyx/auth/users.py:200:        logger.warning(
HEAD:backend/onyx/auth/users.py:205:        logger.warning(
HEAD:backend/onyx/auth/users.py:236:        logger.warning(
HEAD:backend/onyx/auth/users.py:306:        logger.error("Could not load invite-only setting; failing closed (invite-only)")
HEAD:backend/onyx/auth/users.py:354:        logger.warning(
HEAD:backend/onyx/auth/users.py:378:        logger.warning(
HEAD:backend/onyx/auth/users.py:720:                logger.warning(
HEAD:backend/onyx/auth/users.py:821:                    logger.warning(
HEAD:backend/onyx/auth/users.py:942:                logger.warning(
HEAD:backend/onyx/auth/users.py:1289:            logger.exception("Error deleting anonymous user cookie")
HEAD:backend/onyx/auth/users.py:1297:        emit_audit_event(
HEAD:backend/onyx/auth/users.py:1298:            AuditAction.LOGIN,
HEAD:backend/onyx/auth/users.py:1299:            AuditOutcome.SUCCESS,
HEAD:backend/onyx/auth/users.py:1300:            actor=AuditActor(user_id=str(user.id), email=user.email),
HEAD:backend/onyx/auth/users.py:1409:        emit_audit_event(
HEAD:backend/onyx/auth/users.py:1410:            AuditAction.REGISTER,
HEAD:backend/onyx/auth/users.py:1411:            AuditOutcome.SUCCESS,
HEAD:backend/onyx/auth/users.py:1412:            actor=AuditActor(user_id=str(user.id), email=user.email),
HEAD:backend/onyx/auth/users.py:1426:            logger.error(
HEAD:backend/onyx/auth/users.py:1442:            logger.error("Failed to send password reset email to %s: %s", user.email, e)
HEAD:backend/onyx/auth/users.py:1448:        emit_audit_event(
HEAD:backend/onyx/auth/users.py:1449:            AuditAction.PASSWORD_FORGOT,
HEAD:backend/onyx/auth/users.py:1450:            AuditOutcome.SUCCESS,
HEAD:backend/onyx/auth/users.py:1451:            actor=AuditActor(user_id=str(user.id), email=user.email),
HEAD:backend/onyx/auth/users.py:1459:        emit_audit_event(
HEAD:backend/onyx/auth/users.py:1460:            AuditAction.PASSWORD_RESET,
HEAD:backend/onyx/auth/users.py:1461:            AuditOutcome.SUCCESS,
HEAD:backend/onyx/auth/users.py:1462:            actor=AuditActor(user_id=str(user.id), email=user.email),
HEAD:backend/onyx/auth/users.py:1472:            logger.error(
HEAD:backend/onyx/auth/users.py:1492:        # nor the branding the email is built from, and the audit event reads
HEAD:backend/onyx/auth/users.py:1507:            emit_audit_event(
HEAD:backend/onyx/auth/users.py:1508:                AuditAction.EMAIL_VERIFY,
HEAD:backend/onyx/auth/users.py:1509:                AuditOutcome.SUCCESS,
HEAD:backend/onyx/auth/users.py:1510:                actor=AuditActor(user_id=str(user.id), email=user.email),
HEAD:backend/onyx/auth/users.py:1515:            logger.exception("Failed to send verification email to %s", user.email)
HEAD:backend/onyx/auth/users.py:1529:        def _audit_login_failure(
HEAD:backend/onyx/auth/users.py:1530:            outcome: AuditOutcome = AuditOutcome.FAILURE,
HEAD:backend/onyx/auth/users.py:1532:            emit_audit_event(
HEAD:backend/onyx/auth/users.py:1533:                AuditAction.LOGIN_FAILURE,
HEAD:backend/onyx/auth/users.py:1535:                actor=AuditActor(email=email),
HEAD:backend/onyx/auth/users.py:1539:            _audit_login_failure(AuditOutcome.DENIED)
HEAD:backend/onyx/auth/users.py:1556:            logger.warning(
HEAD:backend/onyx/auth/users.py:1563:            _audit_login_failure()
HEAD:backend/onyx/auth/users.py:1579:                _audit_login_failure()
HEAD:backend/onyx/auth/users.py:1583:                _audit_login_failure(AuditOutcome.DENIED)
HEAD:backend/onyx/auth/users.py:1592:                _audit_login_failure()
HEAD:backend/onyx/auth/users.py:1970:                logger.info("Processing token refresh request for user %s", user.email)
HEAD:backend/onyx/auth/users.py:1988:                        logger.info(
HEAD:backend/onyx/auth/users.py:1994:                        logger.error("Error refreshing session token: %s", str(e))
HEAD:backend/onyx/auth/users.py:2000:                logger.info(
HEAD:backend/onyx/auth/users.py:2006:                logger.error("Unexpected error in refresh endpoint: %s", str(e))
HEAD:backend/onyx/auth/users.py:2054:            logger.warning("Invalid exp claim on JWT for user %s", user.email)
HEAD:backend/onyx/auth/users.py:2077:        logger.warning(
HEAD:backend/onyx/auth/users.py:2097:            logger.warning("Inactive user %s attempted JWT login; skipping", email)
HEAD:backend/onyx/auth/users.py:2102:        logger.info("Provisioning user %s from JWT login", email)
HEAD:backend/onyx/auth/users.py:2115:                logger.warning(
HEAD:backend/onyx/auth/users.py:2121:                logger.warning(
HEAD:backend/onyx/auth/users.py:2185:        logger.exception(
HEAD:backend/onyx/auth/users.py:2260:        logger.warning("Issue with validating authentication token")
HEAD:backend/onyx/auth/users.py:2468:        logger.warning("WS auth: missing Origin header")
HEAD:backend/onyx/auth/users.py:2472:        logger.warning(
HEAD:backend/onyx/auth/users.py:2487:        logger.error("WS auth: error during token validation: %s", e)
HEAD:backend/onyx/auth/users.py:2495:            logger.warning("WS auth: token missing tenant_id")
HEAD:backend/onyx/auth/users.py:2507:            logger.warning("WS auth: user not found for id=%s", token_data.get("sub"))
HEAD:backend/onyx/auth/users.py:2515:            logger.warning("WS auth: user %s is limited", user.email)
HEAD:backend/onyx/auth/users.py:2702:        # audit still fire. No web response, so its anon-cookie cleanup no-ops.
HEAD:backend/onyx/background/celery/apps/app_base.py:106:    task_logger.warning("clear_revoked: cleared %d revoked task ids", count)
HEAD:backend/onyx/background/celery/apps/monitoring.py:91:        logger.info("Prometheus indexing pipeline collectors registered")
HEAD:backend/onyx/background/celery/apps/monitoring.py:94:        logger.exception("Failed to register Prometheus indexing pipeline collectors")
HEAD:backend/onyx/background/celery/apps/user_file_processing.py:59:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:58:    task_logger.info(f"cleanup_idle_sandboxes_task starting for tenant {tenant_id}")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:109:            task_logger.exception("Exception while revoking indexing task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:119:        task_logger.exception("Exception while revoking permissions sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:125:            task_logger.info(f"Revoked pruning task {prune_payload.celery_task_id}.")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:137:        task_logger.exception("Exception while revoking external group sync task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:383:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:428:    task_logger.info("submitting docfetching_task with tenant_id=%s", tenant_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:195:    logger.info("Validating active indexing attempts")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:474:        task_logger.info(f"Indexing attempt {attempt.id} has been cancelled")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:566:    logger.info("Connector indexing finished for index attempt %s.", index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:574:            logger.info("Index attempt %s completed successfully", index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:665:        logger.info("Cleaning up storage after indexing completion: %s", storage)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:687:    logger.info("Database coordination completed for attempt %s", index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:873:    task_logger.warning("check_for_indexing - Starting")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1185:        task_logger.exception("Unexpected exception during indexing check")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1346:        task_logger.exception("Unexpected exception during index attempt cleanup check")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1464:            logger.info("Resolving IndexAttemptError for document '%s'", document_id)
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1883:                task_logger.warning(f"Failed to track chunk indexing usage: {e}")
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:96:        #             logger.exception("IndexingCallback - parent pid check exceptioned")
HEAD:backend/onyx/background/celery/tasks/evals/tasks.py:79:        logger.error("SCHEDULED_EVAL_PERMISSIONS_EMAIL not configured")
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:146:        task_logger.info(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:165:        task_logger.info(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:174:        task_logger.info(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:212:            task_logger.info(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:223:            task_logger.info(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:256:            task_logger.error(
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:264:            task_logger.warning(
HEAD:backend/onyx/background/celery/tasks/llm_model_update/tasks.py:40:                task_logger.info(f"Auto mode sync results: {results}")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:844:                    task_logger.error(f"Tenant {tenant_id} has no revision!")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:903:            task_logger.info(f"Out of date tenant: tenant={k} revision={v}")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1164:    # task_logger.info(f"Deleted idle pidbox: pidbox={key_str}")
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:330:    task_logger.info(f"check_for_pruning finished: tenant={tenant_id}")
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:424:            task_logger.exception("insert_sync_record exceptioned.")
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:203:    task_logger.info("check_user_file_processing - Starting")
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:224:            task_logger.warning(
```
Presence of logs does not prove complete, immutable or security-sufficient
audit coverage.
## Current State-Propagation Model
```text
Area | Static evidence status
-----|-----------------------
Document/connector deletion | OBSERVED
Search-index deletion/reindex | OBSERVED
Permission revocation/sync | OBSERVED
MCP/tool revocation | OBSERVED
User/group lifecycle | OBSERVED
Chat/session deletion/TTL | OBSERVED
File/object deletion | OBSERVED
Credential/token revocation | OBSERVED
Async/Celery queue propagation | OBSERVED
Background lifecycle tasks | OBSERVED
Cache/Redis invalidation | OBSERVED
Lock/fence/concurrency controls | OBSERVED
Retry/failure handling | OBSERVED
Stale/eventual consistency signals | OBSERVED
Audit/logging signals | OBSERVED
Runtime deletion completeness | NOT PROVEN
Runtime revocation latency | NOT PROVEN
Index consistency after revocation | NOT PROVEN
Cache consistency after revocation | NOT PROVEN
Object-store deletion completeness | NOT PROVEN
Audit completeness | NOT PROVEN
```
## Provisional Security Model
Static evidence supports a lifecycle in which security-relevant changes may
span several stores or workers:
1. authoritative state changes in relational data;
2. background or Celery work may be created;
3. document/search-index state may require update, deletion or reindexing;
4. Redis/cache state may require expiry or invalidation;
5. file/object state may require separate deletion;
6. access/permission synchronization can occur asynchronously;
7. failures may be retried or recorded;
8. logging provides operational evidence of some transitions.
## Critical Security Invariant
A revocation or deletion should not be considered effective until every
security-relevant copy or derived representation has converged.
For a protected document this may include:
database metadata ->
connector relationships ->
ACL state ->
search/index representation ->
cache state ->
saved search/chat references ->
stored files/objects.
## High-Value Future Tests
Later controlled runtime phases should measure:
- cross-tenant access immediately after revocation;
- cross-user access immediately after revocation;
- indexed-document availability after deletion;
- retrieval during permission-sync delay;
- retrieval during reindexing;
- stale user/group membership;
- stale MCP access after sharing removal;
- stale tool visibility after disablement;
- credential usability after disconnect/revocation;
- cache behavior after permission changes;
- repeated deletion/idempotency;
- queue failure during deletion;
- retry behavior after partial failure;
- race between delete and reindex;
- race between revoke and active chat;
- chat/session TTL deletion;
- user-file deletion completeness;
- generated-file deletion;
- object-store orphaning;
- audit visibility for sensitive state changes.
No vulnerability claim is made by Action 6.9.
## Interpretation Boundary
This action identifies static lifecycle mechanisms only.
It does not prove:
- deletion latency;
- deletion completeness;
- permission-revocation latency;
- absence of stale caches;
- absence of stale index records;
- correct retry semantics;
- race-condition safety;
- queue delivery guarantees;
- object-store cleanup completeness;
- audit-log completeness;
- audit-log integrity.
## Safety Record
During Action 6.9:
- Onyx application execution: NO
- Docker execution: NO
- database modification: NO
- document deletion: NO
- permission revocation: NO
- queue task execution: NO
- cache modification: NO
- index modification: NO
- file deletion: NO
- credential revocation: NO
- external-service call: NO
- production/customer data: NO
- vulnerability testing: NO
- Onyx source modification: NO
## Result
Action 6.9 lifecycle state propagation trace: **PASS**.
