# Phase 5 Action 5.4 - Prompts & Instruction Hierarchy Foundations Evidence

## Provenance

- Branch: `security/phase-5-ai-foundations`
- Baseline HEAD: `59bd32900c27d5bdd75e15bb8b97b7c844be2256`

## Observation boundary

**STATIC SOURCE CANDIDATES ONLY. AI RUNTIME BEHAVIOR IS UNVERIFIED.**

## Review scope

System/developer/user instructions, prompt templates, prompt construction, message roles, retrieved instructions and trust-boundary questions related to prompt injection.

## Static observations

- Candidate files: **745**
- Matching lines: **4942**

## Representative candidate files

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py`
- `backend/alembic/versions/1b8206b29c5d_add_user_delete_cascades.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- `backend/alembic/versions/2c2430828bdf_add_unique_constraint_to_inputprompt_.py`
- `backend/alembic/versions/33ea50e88f24_foreign_key_input_prompts.py`
- `backend/alembic/versions/3c6531f32351_add_back_input_prompts.py`
- `backend/alembic/versions/41fa44bef321_remove_default_prompt_shortcuts.py`
- `backend/alembic/versions/4794bc13e484_update_prompt_length.py`
- `backend/alembic/versions/505c488f6662_merge_default_assistants_into_unified.py`
- `backend/alembic/versions/5ae8240accb3_add_research_agent_database_tables_and_.py`
- `backend/alembic/versions/5e6f7a8b9c0d_update_default_persona_prompt.py`
- `backend/alembic/versions/699221885109_nullify_default_task_prompt.py`
- `backend/alembic/versions/7e490836d179_nullify_default_system_prompt.py`
- `backend/alembic/versions/87c52ec39f84_update_default_system_prompt.py`
- `backend/alembic/versions/8818cf73fa1a_drop_include_citations.py`
- `backend/alembic/versions/9b66d3156fc6_user_file_schema_additions.py`
- `backend/alembic/versions/a852cbe15577_new_chat_history.py`
- `backend/alembic/versions/abbfec3a5ac5_merge_prompt_into_persona.py`

## Security questions

- Which instruction source has the highest authority?
- Can user content be confused with trusted instructions?
- Can retrieved documents introduce instructions?
- Are data and instructions structurally separated?
- Can templates permit attacker-controlled interpolation?
- What happens when instructions conflict?
- Which actions require enforcement outside the prompt?

## Interpretation

Keyword and source matches identify review targets only.

They do not prove model execution, exploitability, data exposure, prompt authority, context behavior or effective security controls.

## Safety

- No model downloaded.
- No model loaded.
- No inference executed.
- No external AI provider contacted.
- No real credential used.
- No real customer data used.
- No paid API used.

## Result

Action 5.4 static foundation result: **PASS**
