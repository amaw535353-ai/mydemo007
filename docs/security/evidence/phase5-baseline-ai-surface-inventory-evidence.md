# Phase 5 Action 5.1 - AI Security Surface Baseline

## Provenance
- Phase 4 closure: `c3e04ac7be016fde9af23893116e7bf33e11fbc4`
- Phase 5 branch: `security/phase-5-ai-foundations`
- Phase 5 starting HEAD: `c3e04ac7be016fde9af23893116e7bf33e11fbc4`

## Observation boundary

**STATIC SOURCE INVENTORY ONLY. AI RUNTIME BEHAVIOR IS UNVERIFIED.**

## AI security-surface matrix

| Surface | Candidate files | Matching lines |
|---|---:|---:|
| Models and inference | 1174 | 8824 |
| AI provider integrations | 332 | 4167 |
| Prompts and instructions | 661 | 4271 |
| Tokens and context | 485 | 2803 |
| Embeddings and vectors | 223 | 2134 |
| RAG and retrieval | 1058 | 5928 |
| Agents and planning | 780 | 6602 |
| Tools and actions | 219 | 2484 |
| MCP | 303 | 3606 |
| Memory and conversation state | 494 | 2223 |
| AI safety and evaluation | 60 | 159 |
| AI libraries and dependencies | 597 | 6245 |

## Initial trust path

User/input -> prompt/instructions -> model/provider -> retrieval/memory -> agent reasoning -> tool/MCP action -> application output.

## Security questions established

- What data enters models and external/provider boundaries?
- Which instructions have authority and precedence?
- What content is retrieved and trusted?
- How are embeddings, vectors and retrieved documents authorized?
- What state or memory persists across interactions?
- What can agents decide autonomously?
- Which tools/actions can create side effects?
- Which MCP servers, tools and resources are trusted?
- Where can prompt injection cross trust boundaries?
- How are outputs evaluated, constrained and monitored?

## Safety

- No LLM invoked.
- No external AI API contacted.
- No embedding generated.
- No model downloaded.
- No model loaded.
- No agent executed.
- No MCP server contacted.
- No real credential used.
- No real customer data used.
- No billable service used.

## Result

Action 5.1 baseline inventory result: **PASS**
