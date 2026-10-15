# Capstone — AI Knowledge Platform

## Goal

Build ingestion, hybrid RAG, citations, permission filters, abstention, traces, and offline evaluation.

## Suggested implementation milestones

1. Define functional requirements and measurable quality, latency, and cost targets.
2. Draw the architecture and record key alternatives in an ADR.
3. Implement the smallest vertical slice using synthetic or safely scoped data.
4. Add tests, traces, budgets, failure handling, and a reproducible evaluation.
5. Document limitations, threat model, deployment steps, and next improvements.

## Acceptance criteria

- [ ] Repeated ingestion is idempotent.
- [ ] Source updates and deletions propagate.
- [ ] Unauthorized documents never enter model context.
- [ ] Factual answers have verifiable source references or abstain.
- [ ] A versioned evaluation report can be reproduced.

## Deliverables

- README with setup and demo instructions.
- Architecture diagram and at least one ADR.
- Automated tests and evaluation results.
- Threat model and known limitations.
- A short demo script or recording.
