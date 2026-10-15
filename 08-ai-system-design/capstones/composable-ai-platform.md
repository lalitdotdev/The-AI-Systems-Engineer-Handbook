# Capstone — Composable AI Platform

## Goal

Build agent registry, durable orchestration, shared state, model/tool gateways, global budgets, rate limits, approvals, and tracing.

## Suggested implementation milestones

1. Define functional requirements and measurable quality, latency, and cost targets.
2. Draw the architecture and record key alternatives in an ADR.
3. Implement the smallest vertical slice using synthetic or safely scoped data.
4. Add tests, traces, budgets, failure handling, and a reproducible evaluation.
5. Document limitations, threat model, deployment steps, and next improvements.

## Acceptance criteria

- [ ] Workflows pause and resume after a worker restart.
- [ ] Cancellation stops unnecessary work.
- [ ] Shared provider limits apply across workflows.
- [ ] A trace follows the request through all agents and tools.
- [ ] Two earlier capstones can be invoked as controlled workflows.

## Deliverables

- README with setup and demo instructions.
- Architecture diagram and at least one ADR.
- Automated tests and evaluation results.
- Threat model and known limitations.
- A short demo script or recording.
