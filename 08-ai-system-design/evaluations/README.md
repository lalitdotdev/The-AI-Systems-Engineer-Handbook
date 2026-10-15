# Evaluation Reports

This directory contains reproducible evaluation reports for projects in Volume VIII.

## What every report should include

1. The task and success definition.
2. Dataset version, size, source, and known limitations.
3. Model, prompt, retrieval, and tool versions.
4. Metrics, aggregation method, and evaluation procedure.
5. Results with failures and uncertainty—not just a single headline score.
6. Cost and latency measurements, including the measurement environment.
7. Known failure modes and next steps.
8. Commands or scripts required to reproduce the result.

Never publish private customer data, credentials, or confidential prompts. Use synthetic or properly permissioned data. Label estimated results as estimates and measured results with the environment and date.

## Suggested workflow

1. Create a small hand-reviewed baseline dataset.
2. Freeze a held-out set before tuning.
3. Run deterministic checks first.
4. Add human review for ambiguous or high-impact cases.
5. Compare versions and inspect regressions.
6. Gate releases on explicit quality, safety, latency, and cost thresholds.
