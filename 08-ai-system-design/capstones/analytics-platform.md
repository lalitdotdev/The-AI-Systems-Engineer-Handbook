# Capstone — AI Analytics Platform

## Goal

Build schema retrieval, NL-to-SQL, SQL AST validation, read-only execution, enforced data policies, and visualization.

## Suggested implementation milestones

1. Define functional requirements and measurable quality, latency, and cost targets.
2. Draw the architecture and record key alternatives in an ADR.
3. Implement the smallest vertical slice using synthetic or safely scoped data.
4. Add tests, traces, budgets, failure handling, and a reproducible evaluation.
5. Document limitations, threat model, deployment steps, and next improvements.

## Acceptance criteria

- [ ] DDL/DML and unauthorized tables are blocked.
- [ ] Query and resource limits are enforced outside the prompt.
- [ ] Ambiguous questions trigger clarification or documented assumptions.
- [ ] Results are checked against known-answer tests.
- [ ] Sensitive-data access attempts are tested.

## Deliverables

- README with setup and demo instructions.
- Architecture diagram and at least one ADR.
- Automated tests and evaluation results.
- Threat model and known limitations.
- A short demo script or recording.
