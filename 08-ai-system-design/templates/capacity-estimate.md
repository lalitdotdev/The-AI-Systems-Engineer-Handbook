# Capacity and Cost Estimate

> Record assumptions. Replace estimates with measured data when available.

## Traffic

- Daily active users:
- Requests per user per day:
- Requests per day = DAU × requests/user/day:
- Average QPS = requests/day ÷ 86,400:
- Peak-to-average factor:
- Estimated peak QPS:

## Model usage

- Average input tokens per call:
- Average output tokens per call:
- Average model calls per user task:
- Input price per 1M tokens:
- Output price per 1M tokens:
- Estimated cost per call:
- Estimated cost per task:
- Estimated daily cost:

## Other costs

- Embeddings and reranking:
- Search/database:
- Queue and compute:
- Logging/tracing:
- Storage and egress:
- Retry/overhead allowance:

## Capacity risks

- Expected concurrency:
- Longest-running operation:
- Likely bottleneck:
- Load-test plan:
- Assumptions to validate:
