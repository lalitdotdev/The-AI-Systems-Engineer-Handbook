# Capstone — AI Research Platform

## Goal

Build query decomposition, parallel source gathering, synthesis, citation verification, and resumable workflow state.

## Suggested implementation milestones

1. Define functional requirements and measurable quality, latency, and cost targets.
2. Draw the architecture and record key alternatives in an ADR.
3. Implement the smallest vertical slice using synthetic or safely scoped data.
4. Add tests, traces, budgets, failure handling, and a reproducible evaluation.
5. Document limitations, threat model, deployment steps, and next improvements.

## Acceptance criteria

- [ ] Sources and evidence spans are retained.
- [ ] Conflicting evidence is surfaced.
- [ ] A worker failure does not corrupt workflow state.
- [ ] Citation checks and cost limits are tested.

## Deliverables

- README with setup and demo instructions.
- Architecture diagram and at least one ADR.
- Automated tests and evaluation results.
- Threat model and known limitations.
- A short demo script or recording.
