# Volume VIII — AI System Design

> **From ambiguous requirements to production-ready AI systems.**

This volume teaches you to design, implement, evaluate, secure, and scale AI systems. It is a practical engineering curriculum—not a collection of architecture diagrams or vendor recommendations.

## Learning objectives

By the end of this volume, you should be able to:

- Translate product requirements into measurable system requirements.
- Estimate traffic, concurrency, latency, token use, storage, and operating cost.
- Choose between deterministic software, RAG, fine-tuning, workflows, and agents.
- Design enterprise RAG, live search, coding agents, support automation, analytics, and multi-agent platforms.
- Protect data, tools, code execution, and SQL workloads with explicit security boundaries.
- Build evaluation datasets, regression tests, observability, and cost controls.
- Design for partial failure, overload, provider outages, and recovery.
- Explain trade-offs in architecture reviews and system-design interviews.

## How to use this volume

For every lesson:

1. Clarify the requirements and record assumptions.
2. Quantify workload, latency, and cost.
3. Draw the simplest architecture that meets the requirements.
4. Deep-dive into the hardest components.
5. Threat-model data access and actions.
6. Define measurable evaluation criteria.
7. Test failure modes and scaling assumptions.
8. Implement a vertical slice and document trade-offs.

A diagram is a hypothesis. An implementation, test, and measured result provide evidence.

## Lessons

| Lesson | Topic | Deliverable |
|---|---|---|
| [89](89-system-design-fundamentals.md) | System Design Fundamentals | Requirements and capacity worksheet |
| [90](90-ai-system-design-framework.md) | AI System Design Framework | Design brief and architecture checklist |
| [91](91-enterprise-rag.md) | Enterprise RAG Knowledge Base | Cited answers, access control, evaluation |
| [92](92-ai-search.md) | AI Search and Answer Engine | Search, synthesis, source verification |
| [93](93-coding-agent.md) | Coding Agent | Sandboxed edit-test-review workflow |
| [94](94-customer-support-ai.md) | Customer Support AI | RAG, ticket state, controlled actions |
| [95](95-ai-analytics-platform.md) | AI Analytics Platform | Governed natural-language-to-SQL |
| [96](96-multi-agent-platform.md) | Multi-Agent Platform | Durable orchestration and shared budgets |

## Capstones

- [AI Knowledge Platform](capstones/knowledge-platform.md)
- [AI Coding Agent](capstones/coding-agent.md)
- [AI Research Platform](capstones/research-platform.md)
- [Enterprise Customer Support AI](capstones/customer-support-ai.md)
- [AI Analytics Platform](capstones/analytics-platform.md)
- [Composable AI Platform](capstones/composable-ai-platform.md)

## Templates and evaluation

- [Design brief](templates/design-brief.md)
- [Capacity estimate](templates/capacity-estimate.md)
- [Architecture decision record](templates/architecture-decision-record.md)
- [Threat model](templates/threat-model.md)
- [Evaluation plan](templates/evaluation-plan.md)
- [Evaluation reports guide](evaluations/README.md)
- [Sample evaluation report](evaluations/sample-report.md)

## Engineering principles

1. Prefer the simplest system that meets requirements.
2. Treat model output and retrieved content as untrusted input.
3. Enforce authorization outside prompts.
4. Bound autonomy, retries, tool calls, time, tokens, and cost.
5. Evaluate quality before optimizing it.
6. Make failures observable and recoverable.
7. Distinguish measured results from estimates.

## Prerequisites

Backend development, HTTP APIs, databases, testing, basic distributed systems, and foundational LLM concepts. Review earlier handbook volumes as needed.

## Suggested study plan

- **Week 1:** Lessons 89–90 and design templates.
- **Week 2:** Lesson 91 and the knowledge-platform capstone.
- **Week 3:** Lessons 92–93 and search/coding-agent experiments.
- **Week 4:** Lessons 94–95 and security-focused labs.
- **Week 5:** Lesson 96, integration, evaluation, and a design review.

Adjust the pace to your background. The goal is demonstrable engineering ability, not finishing a checklist quickly.

## Contribution standards

Contributions should add a reproducible implementation, clarify a difficult trade-off, improve an evaluation method, document a realistic failure mode, or strengthen security. State assumptions, verify links, test diagrams, and label measured results clearly.

## Final principle

The best AI system is not the one with the most agents or the newest model. It is the simplest system that meets its quality, safety, latency, cost, and reliability requirements—and has evidence that it does so.
