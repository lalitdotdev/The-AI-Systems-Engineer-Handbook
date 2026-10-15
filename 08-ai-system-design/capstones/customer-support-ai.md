# Capstone — Enterprise Customer Support AI

## Goal

Build intent routing, RAG, ticket history, typed account tools, risk-tiered approval, and escalation.

## Suggested implementation milestones

1. Define functional requirements and measurable quality, latency, and cost targets.
2. Draw the architecture and record key alternatives in an ADR.
3. Implement the smallest vertical slice using synthetic or safely scoped data.
4. Add tests, traces, budgets, failure handling, and a reproducible evaluation.
5. Document limitations, threat model, deployment steps, and next improvements.

## Acceptance criteria

- [ ] Account access is authorized independently of the model.
- [ ] Side effects are idempotent and audited.
- [ ] High-risk actions pause for approval.
- [ ] The assistant never claims an unconfirmed action succeeded.
- [ ] Resolution quality is measured alongside deflection.

## Deliverables

- README with setup and demo instructions.
- Architecture diagram and at least one ADR.
- Automated tests and evaluation results.
- Threat model and known limitations.
- A short demo script or recording.
