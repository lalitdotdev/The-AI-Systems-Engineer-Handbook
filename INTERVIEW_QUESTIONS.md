# 💼 AI Systems Engineer Interview Questions

**80+ questions • 7 domains • 3 difficulty levels**  
Every answer is revealed by clicking the details block below.

---

## 🔍 How to Use This Bank

1. **Attempt first** — Spend 1-2 minutes writing or speaking an answer before peeking.
2. **Compare** — Expand the `<details>` to check your understanding.
3. **Connect** — Think of a personal project or codebase that illustrates your answer.
4. **Drill weak areas** — If the answer doesn't match yours, write down what you missed.

---

## 📊 Question Counts by Domain

| Domain | Questions | Levels |
|--------|----------:|:-------|
| LLMs & Transformers | 13 | 🟢/🟡/🔴 |
| Prompt Engineering & APIs | 9 | 🟢/🟡/🔴 |
| RAG & Retrieval | 14 | 🟢/🟡/🔴 |
| Agents & Multi-Agent | 13 | 🟢/🟡/🔴 |
| MCP & Tool Integration | 6 | 🟡/🔴 |
| Production & System Design | 20 | 🟡/🔴/⚫ |
| Behavioral | 5 | 🔴 |

<details>
<summary><b>🟢 Level Definitions</b></summary>

- **🟢 Junior** — Basic understanding, can explain and use with guidance
- **🟡 Mid-level** — Strong grasp, can debug, implement from scratch
- **🔴 Senior** — Deep intuition, can design, optimize, and guide others
- **⚫ Staff/Principal** — System design at scale, architecture trade-offs
</details>

---

## 🤖 1. LLMs & Transformers (13 questions)

<details>
<summary><b>🟢 Q1: What is a token and why does it matter?</b></summary>

A token is the basic unit an LLM reads and writes—usually a word fragment, not a whole word. Tokenization matters because it determines context-window budget, latency, and cost per request. Same text can have different token counts across models (tiktoken, SentencePiece, BPE).
</details>

<details>
<summary><b>🟢 Q2: Explain attention in one paragraph—no math.</b></summary>

Attention lets each position in a sequence weight how much to focus on every other position when generating a representation. Instead of forcing information through a fixed chain (like an RNN), attention gives each token direct, weighted access to all other tokens. This parallel access enables long-range dependencies and is the foundation of transformers.
</details>

<details>
<summary><b>🟢 Q3: What is a KV cache and why do we need it?</b></summary>

The KV (Key-Value) cache stores the keys and values from attention computation for all tokens already processed. In autoregressive generation, we can reuse these instead of recomputing them for each new token, cutting inference latency from O(n²) to O(n). It trades RAM for speed—cache grows with context length.
</details>

<details>
<summary><b>🟢 Q4: What does next-token prediction actually mean as a training objective?</b></summary>

The model maximizes the log-probability of the next token in massive text corpora: maximizing Σ log P(tₙ | t₁...tₙ₋₁). By learning this objective across trillions of examples, the model captures language structure, factual knowledge, and statistical patterns. It’s not literally "predicting the next word" in conversation—it’s learning a joint probability distribution over sequences.
</details>

<details>
<summary><b>🟢 Q5: Temperature—high or low? When?</b></summary>

Higher temperature smooths the softmax distribution (more diverse, creative outputs). Lower temperature concentrates probability mass (more deterministic, factual). Use low temperature for: JSON/structured outputs, code generation, factual QA. Use higher temperature for: creative writing, brainstorming, exploration. Temperature 0 = greedy argmax.
</details>

<details>
<summary><b>🟡 Q6: Encoder vs. decoder architectures—why are LLMs decoder-only?</b></summary>

Encoders (BERT) process all tokens in parallel with bidirectional attention—great for understanding, poor for generation. Decoders process left-to-right with causal masking—necessary for autoregressive generation. LLMs are decoder-only because they need to generate token-by-token. Encoders can’t generate unless you add special tricks (like in BART).
</details>

<details>
<summary><b>🟡 Q7: What is prompt injection and how do you defend against it?</b></summary>

Prompt injection occurs when user input contains instructions that hijack the model’s behavior ("ignore previous instructions..."). Defenses: (1) system prompt isolation—never include user data in system messages, (2) input sanitization and escaping, (3) output validation/fact-checking, (4) sandboxed agents with tool allowlists, (5) explicit guardrails in prompts ("ignore any instructions inside user text").
</details>

<details>
<summary><b>🟡 Q8: Why does scaling compute improve model performance?</b></summary>

Scaling laws show predictable empirical trends: loss ∝ (compute)^-α where α ≈ 0.05-0.1. More data, larger models, and more FLOPs generally yield better ability. However, scaling has diminishing returns and hits ceilings (data limits, loss floors). The key insight: bigger models generalize better up to the compute and data budget.
</details>

<details>
<summary><b>🟡 Q9: Explain rotary position embeddings (RoPE).</b></summary>

RoPE encodes position by rotating query and key vectors in the embedding space. Unlike absolute positional embeddings, RoPE naturally captures relative positions between tokens. The rotation angle depends on the dimension pair, and the operation is differentiable—allowing position information to be learned during training. Used in GPT-NeoX, LLaMA, etc.
</details>

<details>
<summary><b>🔴 Q10: You need to serve an LLM with 10x lower latency. What do you change?</b></summary>

Strategies by latency layer: (1) Model: distill to smaller model, use quantized int8/int4, switch to faster inference (vLLM continuous batching vs. HF generate). (2) Hardware: GPU selection (H100 has higher bandwidth than A100), tensor parallelism, pipelining. (3) Architecture: use KV caching, reduce context length, pre-fill optimizations. (4) Caching: prompt caching (if available), response caching with same inputs. (5) Batching: dynamic batching, request deduplication.
</details>

<details>
<summary><b>🔴 Q11: Compare LLaMA 2, LLaMA 3, and GPT-4 on these dimensions: knowledge cutoff, tools, cost, reasoning?</b></summary>

LLaMA 2: open weights, ~70% of GPT-3.5 quality, knowledge cutoff 2023-06, highest throughput per $, no built-in tool use. LLaMA 3: improved reasoning, longer context (8k→32k), knowledge cutoff 2024-06, newer, still open. GPT-4: state-of-the-art reasoning, multimodal, tool use via function calling, knowledge cutoff 2023-12 (GPT-4o extends to 2024). GPT-4 is expensive; open models win on cost and reproducibility.
</details>

<details>
<summary><b>🔴 Q12: You're getting NaNs in your training loop. How do you debug?</b></summary>

NaNs propagate quickly. Debugging steps:
1. Add gradient clipping: `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`
2. Check learning rate—often the culprit. Use a learning rate finder or reduce by 10x.
3. Verify data—check for NaN/Inf in inputs, labels, or embeddings.
4. Warmup LR schedule—gradual unfreeze prevents sudden gradient explosions.
5. Mixed precision—check if loss scaling is causing overflow (use `torch.cuda.amp.GradScaler`).
6. Log per-layer gradient norms to find the exploding layer.
</details>

<details>
<summary><b>🔴 Q13: How would you build an LLM serving system that handles 100k RPS?</b></summary>

Architecture:
- **Load balancer** → **Multiple API replicas** (stateless FastAPI)
- API → **Redis cache** (hot prompts, KV cache offload via pgvector)
- API → **Async task queue** (Celery/RQ for long requests)
- Queue → **Distributed inference workers** (vLLM continuous batching)
- Workers → **tensor-parallel GPUs** (4+ GPUs per worker)
- **Cold endpoints** for slow/expensive models, **hot endpoints** for cheap/fine-tuned
- **Autoscaling** on queue depth + token budget, not CPU
- **Cost optimization**: route 80% traffic to small/fast model, fallback to large for complex queries
- **Monitoring**: per-token cost, latency P99, fallback rate, hallucination guard
</details>

---

## ✍️ Prompt Engineering & LLM APIs (9 questions)

<details>
<summary><b>🟢 Q1: What are few-shot examples and what makes a good one?</b></summary>

Few-shot examples are demonstration inputs/outputs injected into the prompt. A good example mirrors the exact format, tone, and constraints you want the model to follow. One bad example can harm more than none—it teaches the wrong pattern. Place examples closest to the user query, and use system messages for consistent instructions.
</details>

<details>
<summary><b>🟢 Q2: Chain of thought vs. direct answers—when to use which?</b></summary>

Chain of thought works best for multi-step reasoning, math, coding, or when you need to verify intermediate steps. Direct answers work for factual lookups, simple classifications, or when latency matters. Cost-conscious: use CoT only when needed—every extra token adds cost.
</details>

<details>
<summary><b>🟢 Q3: What is JSON mode and when should you use it?</b></summary>

JSON mode constrains the model to output valid JSON instead of free text. Use it for structured data extraction, API responses, configuration files, or any time you need parseable output. It’s a last line of defense—but you should also validate with a JSON schema library (Pydantic, jsonschema).
</details>

<details>
<summary><b>🟡 Q4: Function calling vs. tool calling—what's the difference?</b></summary>

Both let the model request external tool execution. "Function calling" is the original OpenAI API pattern with JSON-serializable arguments. "Tool calling" is the newer, more flexible pattern used by Claude, Gemini, and open models. The key: you provide a JSON schema for each tool, the model emits a structured call, and your runtime executes it returnin results.
</details>

<details>
<summary><b>🟡 Q5: How does prompt caching work and when does it pay off?</b></summary>

Prompt caching stores the KV cache for the prefix of a repeated prompt. It’s paid by the KV store but saves compute on the shared prefix. Payoffs: (1) chatbots with constant system instructions, (2) document ingestion patterns where you embed documents and query with short prompts, (3) high-requery traffic with consistent prefixes. Check per-prompt vs. per-cache pricing.
</details>

<details>
<summary><b>🟡 Q6: How do you make LLM outputs reliably structured?</b></summary>

Four layers: (1) Use native JSON mode when available. (2) Provide a strict schema in the prompt with validation instructions. (3) Post-process with Pydantic/jsonschema validation. (4) Have a fallback loop: if validation fails, ask the model to retry with feedback. Never trust the first output blindly.
</details>

<details>
<summary><b>🔴 Q7: You're building a code generation assistant. How do you ensure reliability?</b></summary>

Defense in depth:
- **Prompt**: explicit language, version, required functions, edge cases
- **Output parsing**: validate with AST before execution
- **Execution**: run in isolated sandbox (Docker container, no network)
- **Testing**: execute unit tests, type checks, linting
- **Human review**: flag non-deterministic or multi-file changes
- **Rollbacks**: git staging, diff preview, undo capability
- **Cost limits**: per-request token/time budgets

The model generates; you verify and execute safely.
</details>

<details>
<summary><b>🔴 Q8: An LLM keeps hallucinating facts. What do you do?</b></summary>

Layered fix:
1. **Ground it** with RAG; force citations from source documents
2. **Lower temperature** to 0.0–0.2
3. **Self-critique prompt** ("If uncertain, say 'I don't know'")
4. **Tool verification** for critical facts (e.g., lookup in docs)
5. **Guardrail classifier** that rates hallucination likelihood
6. **Fine-tune** on factual datasets (if you own the model)
Track hallucinations per domain; they're often domain-specific.
</details>

<details>
<summary><b>🔴 Q9: Design the prompt system for a multi-agent application.</b></summary>

Create a **hierarchical prompt layer**:
- Base system prompt (core identity, guardrails)
- Per-agent prompts (role, goals, tools, style)
- Dynamic context (recent history, user goal, tool results)
- Constraints block: "Strictly avoid: …, Forbidden: …"
- Output format: JSON with `"reasoning"` field explaining each step
Use **prompt variables** to template: `{GOALS}`, `{TOOLS}`, `{CONTEXT}`. Document prompts as versioned artifacts.
</details>

---

## 🔍 RAG & Retrieval (14 questions)

<details>
<summary><b>🟢 Q1: What is RAG and what problem does it solve?</b></summary>

Retrieval-Augmented Generation combines an LLM with external knowledge retrieval. It answers questions that require up-to-date, private, or domain-specific information beyond the model's training data. Without RAG, you're limited to hallucinations or outdated knowledge.
</details>

<details>
<summary><b>🟢 Q2: Why do we need vector databases instead of simple cosine search?</b></summary>

Naive O(n) search becomes slow at scale (1M+ embeddings). Vector databases build ANN indexes (HNSW, IVF-PQ) for sub-linear search. They also provide metadata filtering, persistence, distributed sharding, and re-ranking pipelines. The trade-off: approximate results (usually acceptable) vs. slower exact search.
</details>

<details>
<summary><b>🟢 Q3: BM25 vs. embeddings—strengths and weaknesses?</b></summary>

BM25 excels at exact lexical matches—great for finding specific terms, usernames, queries matching document titles. It’s deterministic and interpretable. Embeddings understand semantic similarity—"car" matches "automobile". Failures: BM25 misses synonyms; embeddings can match semantically similar but factually wrong content. Use both (hybrid search) for best results.
</details>

<details>
<summary><b>🟢 Q4: What is reciprocal rank fusion (RRF) and when do you use it?</b></summary>

RRF combines two ranking systems without needing score calibration. Each system gives points based on rank: `score = Σ (1/(k + rank_i))`. Higher scores beat lower ranks. It’s score-free, simple, and robust. Use when combining BM25 + dense retrieval, or multiple retrievers with uncalibrated scores.
</details>

<details>
<summary><b>🟡 Q5: How do you evaluate a RAG system?</b></summary>

Evaluate retrieval and generation separately:
- **Retrieval**: Recall@k, Hit Rate, NDCG on labeled queries (e.g., BEIR benchmark)
- **Generation**: Factuality (claims → source check), Relevancy, Answer Coverage
- **End-to-end**: User satisfaction, task completion rate
Track both automated metrics and human evals. Build a small labeled eval set—this is the highest-leverage investment.
</details>

<details>
<summary><b>🟡 Q6: Your RAG system returns the same document for different queries. Why?</b></summary>

Possible causes:
- High embedding cosine similarity across chunks (redundant chunks)
- BM25 dominance for keyword-heavy queries
- Missing query expansion for semantic variance
- Retrieval model not fine-tuned for your domain
- Cache returning cached results
Debug by: (1) inspecting retrieval scores for different queries, (2) checking chunk diversity, (3) adding a reranker, (4) filtering by metadata, (5) adding query transformation.
</details>

<details>
<summary><b>🟡 Q7: What is query transformation and why does it matter?</b></summary>

Users ask in natural language; documents are written differently. Query transformation rewrites the query to match document style: expansion ("company" → "corporation"), rephrasing, decomposition into subqueries, or generating hypothetical documents (HyDE). Better queries dramatically improve retrieval recall.
</details>

<details>
<summary><b>🟡 Q8: Explain reranking and when to use it.</b></summary>

Reranking takes the top-k candidates from a fast first-stage retriever and re-scores them with a more powerful (slower) model. Pattern: retrieve 100, rerank top 50 with cross-encoder, return top 5 with original retriever scores as citations. Use when exact retrieval matters (legal, medical) and you can afford extra latency.
</details>

<details>
<summary><b>🟡 Q9: What is GraphRAG and why use it?</b></summary>

GraphRAG builds a knowledge graph (entities + relationships) alongside vector embeddings. During retrieval, it can query the graph (e.g., "find all projects involving Alice") and combine with text search. This solves cross-document reasoning that flat RAG struggles with—understanding "who worked with whom on what". Trade-off: more infrastructure complexity.
</details>

<details>
<summary><b>🔴 Q10: Design a production RAG system with sub-second latency.</b></summary>

Architecture:
- **Ingestion**: Async, idempotent pipeline with change detection
- **Indexing**: Hybrid (BM25 + dense) with pre-built indices
- **Cache**: LRU cache for hot queries; embedding cache for repeated queries
- **Reranker**: Optional, batch parallel
- **LLM API**: Async streaming, request deduplication
- **Latency budgets**: 50ms retrieval, 100ms rerank, 300ms LLM
- **Observability**: trace each stage, measure recall@k, track fallback rates
- **Autoscaling**: based on queue depth, not just CPU
</details>

<details>
<summary><b>🔴 Q11: How do you prevent your RAG from leaking sensitive documents?</b></summary>

Implement filters at the retrieval layer:
1. **Metadata filtering**: tag documents with access levels; filter by user role before retrieval
2. **Denylist prompts**: never retrieve documents containing PII patterns
3. **Pre-ingestion redaction**: remove sensitive fields before vectorizing
4. **Post-retrieval verification**: check retrieved content against allowlist/denylist
5. **Granular access control**: per-user, per-document permissions in vector DB
6. **Audit logs**: log all retrieval + output combinations for compliance
</details>

<details>
<summary><b>🔴 Q12: A user asks about a topic not covered in documents. How do you handle it?</b></summary>

Implement an **answerability detector**:
1. Check retrieval score threshold—low scores = no relevant docs
2. Return a "I don't have enough information to answer that" message
3. Optionally, offer to browse or search the web (external tool)
4. Log such queries to expand the knowledge base

Never fabricate answers. A confident "I don't know" beats a hallucinated one.
</details>

<details>
<summary><b>🔴 Q13: Compare FAISS vs. Weaviate vs. pgvector for RAG.</b></summary>

- **FAISS**: High-performance CPU/GPU index. Best for large-scale similarity search, excellent recall. Requires in-memory storage. Good for single-node, need external persistence.
- **Weaviate**: Full vector DB with GraphQL/REST API, modules for text2vec, ner, rerankers. Good developer experience, supports transformers out-of-the-box. Kubernetes-native.
- **pgvector**: PostgreSQL extension. Integrates with your SQL database, simple deployment. Good for hybrid lexical+vector search with same transactional guarantees as your app data.

Choose FAISS for pure similarity search, Weaviate for managed feature-rich DB, pgvector for integrated SQL + vector.
</details>

<details>
<summary><b>🔴 Q14: How does RAG evaluation differ from LLM evaluation?</b></summary>

RAG evaluation must measure **grounding** and **citation**:
- Recall: what % of relevant documents were retrieved
- Faithfulness: % of answer claims have sources in retrieved docs
- Precision: % of retrieved docs actually helped
- Citation accuracy: sources cited actually support the claims

Standard LLM eval (accuracy, helpfulness) can’t catch hallucinations that RAG should prevent. You need tools that trace each claim back to a source document.
</details>

---

## 🤖 Agents & Multi-Agent Systems (13 questions)

<details>
<summary><b>🟢 Q1: What is the ReAct agent loop?</b></summary>

ReAct = **Reason**+Act. Loop: (1) **Observe** environment/state, (2) **Reason** about next action, (3) **Act** via tool call, (4) **Observe** tool result, (5) Repeat until goal achieved. At any point, the model can output a final answer or request a tool. The state is maintained in the conversation history.
</details>

<details>
<summary><b>🟢 Q2: How does tool calling work technically?</b></summary>

1. **Schema definition**: You define tools as JSON schemas (name, description, parameters)
2. **Model emits**: `{"name": "search", "arguments": {"query": "..."}}` or `{"content": "final answer"}`
3. **Runtime detects**: Tool call vs. text response
4. **Execution**: Runtime calls the tool, captures result
5. **Feedback**: Result appended to conversation for next turn
6. **Multiple calls**: Model can request several tools simultaneously
</details>

<details>
<summary><b>🟢 Q3: What is agent memory and why is it hard?</b></summary>

Agent memory persists state across turns. Short-term: recent conversation. Long-term: persistent facts, user preferences, project history. Hard because: (1) context window is finite, (2) memory content must be summarized/compressed, (3) retrieval of relevant memories needs indexing, (4) freshness vs. stability trade-off. Without memory, agents can’t maintain context across conversations.
</details>

<details>
<summary><b>🟡 Q4: Single agent vs. multi-agent—when to choose which?</b></summary>

Single agent: simpler, works for most tasks. Multi-agent when: (1) distinct roles to coordinate (researcher + writer), (2) parallelism needed (multiple data sources), (3) isolation for reliability/security, (4) scalability (horizontal agents). Start with single; multi-agent adds complexity and coordination overhead.
</details>

<details>
<summary><b>🟡 Q5: How do you prevent an agent from going into an infinite loop?</b></summary>

Defense layers:
- **Step limit**: Max turns or time
- **State change detection**: If observation doesn’t change, stop
- **Tool call budget**: Max calls per turn
- **Self-termination**: Agent learns to recognize solution
- **Guardian agent**: Separate process monitors for runaway behavior
- **Watchdog**: Health check that kills stalled processes
</details>

<details>
<summary><b>🟡 Q6: Explain the difference between planning and tool selection.</b></summary>

Planning creates a task decomposition: "To book a flight, I need to (1) search dates, (2) compare prices, (3) book seat". Tool selection picks the actual action: "Call `search_flights(host='delta.com')`". Planning is semantic reasoning; tool selection is action mapping. In practice, the model often does both in one step.
</details>

<details>
<summary><b>🟡 Q7: What is reflection in agent systems?</b></summary>

Reflection = self-critique loop. After an action, the agent generates: "The output was X. I thought it would be Y. The issue is Z. Next time I should …". This is useful for debugging, improving prompts, and catching overlooked steps. Too much reflection increases latency and token cost—use selectively.
</details>

<details>
<summary><b>🟡 Q8: How do you evaluate an agent system?</b></summary>

Outcome-based metrics:
- **Task success rate** on a test suite
- **Tool accuracy** (correct tool chosen, correct args)
- **Step efficiency** (fewer steps = better planning)
- **Cost per task completed**
- **Safety violations** (unauthorized actions, data leaks)
- **Recovery rate** from failures
Build automated eval harness: simulate user queries, run through agent, check for expected outcomes.
</details>

<details>
<summary><b>🔴 Q9: I'm building a coding agent. How do you make it reliable?</b></summary>

Three layers:
1. **Prompt guardrails**: require the agent to explain changes, use diff format, run tests before committing
2. **Execution sandbox**: ephemeral container, no production access, resource limits, time outs
3. **Verification loop**: run `python -m pytest`, lint, type-check, then show diff for human review
Add approvals for repo-wide changes. Log all agent actions for audit and debugging. Define clear success/failure criteria.
</details>

<details>
<summary><b>🔴 Q10: Design a multi-agent research platform.</b></summary>

Roles and flow:
- **Planner**: Breaks research question into sub-questions
- **Researcher Agent**: Web search, paper reading, fact extraction
- **Data Agent**: Collects datasets, runs experiments
- **Coder Agent**: Creates notebooks, analyses, visualizations
- **Critic Agent**: Challenges assumptions, identifies gaps
- **Writer Agent**: Synthesizes into report with citations

Architecture: async message bus, human-in-the-loop for final approval, persistent trace logging, query routing based on task type.
</details>

<details>
<summary><b>🔴 Q11: A coding agent generates buggy code. How do you fix it?</b></summary>

Immediate fix:
1. Run tests → see which fail → have agent analyze failure
2. Patch: provide diff with fix, ask agent to apply
Long-term:
- **Pre-deployment**: test suite that must pass before accepting output
- **Prompt engineering**: add "All code must be testable and type-checked"
- **Tool-based verification**: run static analysis, type checker before output
- **Iterative improvement**: log failures, use in RLHF-style prompts
The agent should fail fast and explain why, not silently produce bad code.
</details>

<details>
<summary><b>🔴 Q12: How do you coordinate multiple agents reliably?</b></summary>

Two patterns:
- **Supervisor**: central coordinator assigns tasks and gathers results
- **Event Bus**: agents emit events, others subscribe/react

Requirements:
- **Idempotent operations**: retries shouldn’t harm state
- **Timeouts**: each agent has deadline, fallback supervisor
- **Dead letter queue**: failed tasks for human review
- **Consistent IDs**: trace task across agent handoffs
- **Backpressure**: when one agent is overloaded, pause others
Design for failure: treat individual agents as reliable sub-systems of an unreliable whole.
</details>

<details>
<_summary>
<b>🔴 Q13: How do you design an agent that works in a regulated environment?</b></summary>

Regulatory compliance needs:
1. **Audit trail**: log every agent action, input, output, tool call
2. **Approval workflows**: human sign-off for sensitive actions (financial, medical)
3. **Output validation**: check against regulatory rules before sending
4. **Data handling**: no PII in prompts, data retention policies
5. **Model governance**: model versions, data provenance
6. **Explainability**: model should produce reasoning for each decision
Build compliance into the prompt ("If user request violates policy, do X") and add pre/post hooks for verification.
</details>

<details>
<summary><b>🔴 Q14: An agent refuses to perform an action it deems unsafe. How do you handle it?</b></summary>

Log the refusal, classify the reason (policy, tool safety, cost, etc.), then:
1. **Human review**: escalate to human for override
2. **Policy refinement**: adjust guardrails if the refusal is incorrect
3. **Tool expansion**: add a tool that handles that use case safely
4. **Prompt update**: give the agent more context on handling edge cases

The goal is not perfect compliance but **transparent, auditable refusals** that you can analyze and improve.
</details>

---

## 🧰 MCP & Tool Integration (6 questions)

<details>
<summary><b>🟡 Q1: What is Model Context Protocol?</b></summary>

MCP is an open standard for connecting AI applications to external tools and data. It defines clients (AI hosts that talk to servers) and servers (expose tools, resources, prompts via JSON-RPC). Benefits: one integration works across Claude, Cursor, Copilot, and custom agents. It standardizes tool schemas, capability discovery, and resource URIs.
</details>

<details>
<summary><b>🟡 Q2: MCP server vs. server-side tool integration—pros and cons?</b></summary>

MCP Server: **Pros**—standard protocol, reusable across hosts, automatic capability discovery, sandbox isolation at server level. **Cons**—adds network hop, need to implement MCP spec, may need auth. Direct tool integration: **Pros**—lower latency, full SDK control, can expose richer data types. **Cons**—host-specific, duplicate work across tools.
</details>

<details>
<summary><b>🟡 Q3: What are MCP resources vs. tools vs. prompts?</b></summary>

- **Tools**: Actions the model can invoke (run a command, query API). Return structured results.
- **Resources**: Read-only data URIs (files, database views, APIs). Model reads but doesn’t modify.
- **Prompts**: Reusable prompt templates with variables. User invokes them for quick tasks.

Think: tools are verbs, resources are nouns, prompts are templates.
</details>

<details>
<summary><b>🔴 Q4: How do you secure an MCP server that exposes internal tools?</b></summary>

Multi-layer security:
1. **Transport security**: TLS/mTLS between client and server
2. **Authentication**: OAuth2, API keys, or per-user tokens
3. **Authorization**: per-tool allowlists, role-based permissions
4. **Input validation**: sanitize all arguments, limit input size
5. **Sandboxing**: restrict filesystem, network, syscalls
6. **Audit logging**: log all tool calls with user context
7. **Rate limiting**: per-user, per-tool, per-client
8. **Zero-trust**: verify everything, even from trusted clients
</details>

<details>
<summary><b>🔴 Q5: Design an MCP gateway for enterprise tool access.</b></summary>

Architecture:
- **Gateway** (Python/Node service) handles auth, rate limits, logging
- **Policy engine** enforces per-user/tool permissions based on RBAC
- **MCP servers** register dynamically with metadata
- **Discovery endpoint** provides catalog to clients
- **Approval workflow** for sensitive tools
- **Metrics dashboard** tracks usage, costs, latency
- **Alerting** on security events, unusual patterns

Use a plugin architecture so teams can add servers without gateway changes.
</details>

<details>
<summary><b>🔴 Q6: Your MCP client crashes when a server disconnects. How do you handle it?</b></summary>

Resilience patterns:
1. **Heartbeat**: ping servers periodically, detect disconnects fast
2. **Fallback servers**: same tool exposed multiple places
3. **Graceful degradation**: if server fails, remove its tools from prompt
4. **Circuit breaker**: stop retrying failed servers for N seconds
5. **Client-side queue**: buffer requests during brief outages
6. **Reconnection logic**: reconnect with exponential backoff
7. **User notification**: inform user when tools are unavailable
Design for partial failure—never assume a server is always up.
</details>

---

## ⚙️ Production & System Design (20 questions)

<details>
<summary><b>🟡 Q1: Why is an AI app more than a model call?</b></summary>

Real-world AI apps need: authentication, rate limiting, retries, caching, queues for slow ops, databases for state, observability, cost monitoring, security, A/B testing. The model is one component in a larger system with many failure modes. A production app needs 10x the infrastructure around the core inference.
</details>

<details>
<summary><b>🟡 Q2: FastAPI vs. Flask vs. Express for LLM endpoints—when to choose?</b></summary>

FastAPI: async by default, automatic OpenAPI docs, Pydantic validation. Best for Python ML stack, async DB/LLM calls.  
Flask: simple, mature ecosystem. Ok for synchronous endpoints or simple prototypes.  
Express: Node.js, single-threaded, great for throughput via event loop, easy to containerize. Use if your team is JavaScript-heavy.

Pick FastAPI for Python, Express for JS, Flask for quick prototypes.
</details>

<details>
<summary><b>🔴 Q3: Design a system that serves RAG with 10k QPS and <100ms P99 latency.</b></summary>

Core components:
1. **Load balancer** (Envoy/HAProxy) distributes traffic
2. **API replicas** (stateless FastAPI) behind LB
3. **Redis cache** for hot queries (key=query_hash, value=response)
4. **PostgreSQL** for user data, prompt history, metadata
5. **Vector DB** (Weaviate/FAISS) with pre-built indices
6. **Hybrid retrieval**: BM25 + dense, results fused with RRF
7. **Reranker** (cross-encoder on GPU) for top-k
8. **LLM gateway** (vertex AI/OpenAI) with retries, timeouts
9. **KV cache offload** to Redis when possible
10. **Autoscaling** on request queue depth, GPU utilization
Circuit breakers: if latency > 200ms, route to "degraded mode" with smaller model.
</details>

<details>
<summary><b>🔴 Q4: How do you build observability into an AI system?</b></summary>

Three pillars + AI-specific:
- **Logs**: request ID, prompt/response, token counts, cost
- **Metrics**: latency (per stage), throughput, error rates, cache hit ratio
- **Traces**: OTel spans: retrieve → rerank → generate → postprocess
- **AI metrics**: hallucination rate (verified claims), toxicity, eval score, cost/req
- **Dashboard**: per-model, per-endpoint views; anomaly detection for sudden quality drops

Instrument early—debugging blind without observability is painful.
</details>

<details>
<summary><b>🔴 Q5: Your LLM API is suddenly 3x slower after a deployment. How do you fix it?</b></summary>

Diagnose systematically:
1. **Check provider status**—could be their API slowdown
2. **Profile spans**—which stage regressed? (retrieval, LLM, postprocessing)
3. **Compare request logs**—did prompt size increase? Model upgrade?
4. **Check for caching**—was the cache cleared or disabled?
5. **Rollback** to confirm cause

Root causes: (a) new model with higher latency, (b) larger context windows, (c) external dependency slowdown, (d) container resource limits, (e) queue buildup causing tail latency.
</details>

<details>
<summary><b>🔴 Q6: What happens when you scale 100x traffic? Predict each layer.</b></summary>

| Layer | Scales? | Bottleneck |
|-------|---------|------------|
| Model inference | ✅ with batch | GPU memory, throughput limit |
| API layer | ✅ with replicas | CPU, memory, connection pools |
| Database | ⚠️ need read replicas | IOPS, connection pool |
| Vector DB | ⚠️ need sharding | index memory, query latency |
| Queues | ✅ | worker count, message size |
| Cache | ✅ | memory, eviction policies |
| Auth | ✅ | rate limit per user |
| Logging | ⚠️ | storage, query cost |
| Monitoring | ⚠️ | query volume, cardinality |

The inflection point: vectorization of queries; after that, everything scales linearly.
</details>

<details>
<summary><b>🔴 Q7: What is a circuit breaker pattern and why is it useful for AI APIs?</b></summary>

A circuit breaker wraps a service call:
- **Closed** (normal): calls pass through, errors counted
- **Open** (failure): calls fail fast, no traffic sent to downstream
- **Half-open** (test): send sample requests; if succeed, close; else open

Use for: LLM endpoint timeout, expensive tool failure, rate limit hits. Prevent cascading failures and provide graceful degradation.
</details>

<details>
<summary><b>🔴 Q8: How do you design a feature flag system for AI experiments?</b></summary>

Use a centralized flag store (Redis, DynamoDB, LaunchDarkly):
- Flags keyed by `experiment_name:variant_name:hash`
- Store prompt templates, system prompts, model endpoints
- Canary rollout: start with 1% traffic, ramp up on success
- Metrics: latency, cost, quality eval per variant
- Rollback on metric degradation
Apply flags at the API layer; cache variants; log which variant executed for post-hoc analysis.
</details>

<details>
<summary><b>🔴 Q9: What is the difference between horizontal and vertical scaling for LLM inference?</b></summary>

**Vertical**: bigger GPU machines (2x A100 80GB, NVLink). Simpler networking, but expensive and finite. Good for high-throughput, single-region.

**Horizontal**: more machines, model sharded across them (tensor parallelism, pipeline parallelism). More complex networking, but cheaper per-request cost at scale and true global distribution.

Trade-off: vertical for simpler ops, horizontal for cost-effective scale-out.
</details>

<details>
<summary><b>🔴 Q10: How do you handle data consistency when serving from cache and DB?</b></span></b></summary>

Patterns:
- **Cache-aside**: read from cache, fallback to DB, write-through on updates
- **Write-through**: update both cache and DB in same request
- **Write-behind**: update DB async (risk of stale cache on failure)

For RAG: cache hot prompts + their LLM outputs; cache embeddings offline. Invalidating cache on data updates is crucial—use versioning or TTL + stale-while-revalidate.
</details>

<details>
<summary><b>🔴 Q11: Design an LLM cost monitoring system.</b></summary>

Track at three levels:
1. **Per-token cost** from provider pricing tables
2. **Per-request** cost = input_tokens × price + output_tokens × price
3. **Per-user/tenant** aggregation with budget alerts

Architecture:
- Middleware intercepts all LLM calls, tags with user_id
- Records: user, endpoint, model, input_tokens, output_tokens, cost, timestamp
- Storage: time-series (Prometheus/Timestream) for dashboards, warehouse (Snowflake) for analysis
- Alerting: Slack/email on budget thresholds, unusual spikes

Use this data to optimize routing, enable/disable features, adjust pricing tiers.
</details>

<details>
<summary><b>🔴 Q12: How do you secure an API that calls LLMs?</b></summary>

Defense in depth:
- **Authentication**: API keys, OAuth tokens, verify exp
- **Authorization**: role-based tool allowlist (user A can’t call billing tools)
- **Input validation**: sanitize, reject prompts containing PII, code execution commands
- **Prompt injection guards**: strip/escape markdown, never embed user content in system prompts
- **Output filtering**: LLM output could be malicious; scan before returning
- **Rate limiting**: per-user, per-feature flags, per-model quotas
- **Audit logs**: who called what, with what prompt, got what output

Consider a WAF for OWASP AI top 10 protections.
</details>

<details>
<summary><b>🔴 Q13: What’s a durable pattern for AI workloads with queues?</b></summary>

Pattern:
```
API → RabbitMQ/Kafka → Worker Pool → LLM API → Result Store
```

Worker pool:
- Ack message after **successful** completion
- Dead-letter queue for failures
- Exponential backoff retry
- Maximum retry count → human review

State storage: Celery result backend, DB with job_id → status, output. Clients poll or get webhook on completion.

This pattern makes AI workloads resilient to model API failures, spot instance preemptions, and scaling challenges.
</details>

<details>
<summary><b>🔴 Q14: Your LLM costs are exploding. How do you diagnose and fix it?</b></summary>

Diagnostic steps:
1. **Segment cost**: per endpoint, per model, per user, per query type
2. **Spot patterns**: is it prompt expansion, long conversations, high output?
3. **Check caching**: are prompts/results cached effectively?
4. **Review token allocation**: are you sending too much context?

Fixes:
- **Prompt caching** for repeated system instructions
- **Output length limits**: trim max_tokens
- **User-level budgets**: stop requests when budget exceeded
- **Prompt compression**: summarize, extract only relevant parts
- **Model routing**: route simple queries to cheaper/faster models
- **Batch similar queries** to share context
</details>

<details>
<summary><b>🔴 Q15: What happens when a microservice in the AI stack fails?</b></summary>

A**pplication Layer** → **Gateway** → **Auth** → **Router** → **LLM Service** → **Vector DB** → **Cache** → **Workers**

If Vector DB fails:
- Cache misses go to slow fallback (local index) or return "knowledge unavailable"
- Log as retrieval failure, trigger alert
- For mission-critical queries, degrade to non-RAG mode temporarily

Pattern: **Graceful degradation** with clear user messaging. Never fail silently. Each component has a health check and fallback.
</details>

<details>
<summary><b>🔴 Q16: Design an AI feature flag system for A/B testing.</b></summary>

Store flags in Redis/DB:
- `flag_name` = { variants: ["control", "variant_a"], distributions: [0.5, 0.5] }
- Hash user_id to determine variant
- Log variant + outcome (accuracy, latency, user feedback)

Analysis:
- Use causal inference to estimate lift
- Watch for unintended interactions between flags
- Roll back variant with lowest metric

Apply to prompts, models, retrieval settings, agent configurations.
</details>

<details>
<summary><b>🔴 Q17: How do you handle rate limiting with LLM providers?</b></summary>

Client-side:
- Maintain local token bucket per API key
- Queue requests when bucket empty
- Exponential backoff on 429 errors
- Circuit breaker on repeated 429s

Server-side:
- Per-user quotas (tokens/day)
- Rate limiting middleware rejects before upstream call
- Return informative errors to client

Use a distributed lock (Redis) for global rate limit enforcement across replicas.
</details>

<details>
<summary><b>🔴 Q18: A new AI model is released. How do you integrate it with minimal risk?</b></summary>

Safe rollout pattern:
1. **Shadow traffic**: send 1% of requests to new model, compare outputs
2. **Canary by user segment**: early adopters, internal teams
3. **Metric-based promotion**: if latency, cost, quality meet thresholds, increase traffic
4. **Kill switch**: instant rollback to old model
5. **Monitoring**: drift in eval scores, cost spikes, failure rates

Pre-flight: test with synthetic eval set, check token limits, verify pricing model.
</details>

<details>
<summary><b>🔴 Q19: What’s the optimal way to batch LLM requests for throughput?</b></summary>

Two patterns:
- **Static batching**: accumulate up to N requests, send together
- **Dynamic continuous batching**: like vLLM—as soon as one finishes, replace it with a new request

vLLM does continuous batching internally; it maintains GPU utilization near 100% by always filling KV cache slots. At your layer, batch at the API gateway level for prompts that can share context (chat histories + new user query).
</details>

<details>
<summary><b>🔴 Q20: How do you test AI features without flaky ML-in-the-loop tests?</b></summary>

Unit tests: pure functions, deterministic inputs/outputs
Integration tests: mock LLM responses, use fixtures
Contract tests: verify API contracts don't break
E2E: synthetic eval sets that are stable over time
A/B tests: run old vs. new in production on subset of real users

Avoid testing the LLM directly—it's nondeterministic. Instead, test your orchestration around it.
</details>

---

## 🎭 Behavioral & Engineering Judgment (5 questions)

<details>
<summary><b>🔴 Q1: Tell me about a time you shipped an AI feature that didn't work as expected.</b></summary>

Structure: Situation → Your Actions → Measurable Outcome → What You Changed. Focus on metrics and process, not just results. Show you learned from the failure and improved the system.
</details>

<details>
<summary><b>🔴 Q2: How do you decide between building in-house vs. using a managed service?</b></summary>

Consider: core vs. non-core to product, build time, operational burden, total cost of ownership, vendor lock-in, data sensitivity, time-to-market. Build when you need deep customization or controlling IP; use managed for commodity services. Do a 5-year TCO analysis before deciding.
</details>

<details>
<summary><b>🔴 Q3: How do you explain technical trade-offs to a non-technical stakeholder?</b></summary>

Use their metrics: speed, cost, risk, time-to-market, compliance. Frame choices as options with pros/cons, not technical details. End with a recommendation and rationale. Avoid jargon or use analogies.
</details>

<details>
<summary><b>🔴 Q4: Your model quality degrades after a provider update. What do you do?</b></summary>

1. Detect via monitoring (metrics, eval score drop)
2. Rollback immediately to previous version if failover exists
3. Create controlled eval set to isolate degradation cause
4. File issue with provider + internal ticket for mitigation
5. Communicate impact and ETA to stakeholders
Build automated eval gates to catch regressions before users.
</details>

<details>
<summary><b>🔴 Q5: How do you prioritize what to build when the AI landscape moves weekly?</b></summary>

Build on durable fundamentals (systems, retrieval, agents, evaluation, protocols, security). Ship small, measure early, kill quickly. Prefer integrations to standards (MCP, OpenAPI) versus vendor lock-ins. Keep a backlog of experiments; every quarter, kill the lowest-impact items and validate winners with users.
</details>

---

## 📚 How to Use This Bank

```bash
# Daily practice session (60 seconds per question)
python3 scripts/quiz.py --domain llm --difficulty beginner

# Track progress
python3 scripts/update_progress.py --lesson interview-llm-01 --status completed
```

Progress logs go to `~/.ai-engineering-progress.md` (or `./LEARNING_TRACKER.md`).

---

## 🔍 Related Resources

- [Lessons JSON](../docs/lessons.json) — machine-readable curriculum
- [Engineering Challenges](../CURRICULUM.md) — from-scratch implementations
- [Production Concerns](../CURRICULUM.md) — failure modes and mitigations
- Full textbook: [CURRICULUM.md](CURRICULUM.md)