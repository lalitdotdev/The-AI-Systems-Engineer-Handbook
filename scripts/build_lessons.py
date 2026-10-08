#!/usr/bin/env python3
"""Generate the interactive lesson scaffold for every topic in the curriculum.

Run from repo root:

    python3 scripts/build_lessons.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (volume_dir, number, slug, title, difficulty)
LESSONS = [
    # ── Volume I ────────────────────────────────────────────────────────────
    ("01-computer-science-python", "01", "python-fundamentals", "Python Fundamentals", "beginner"),
    ("01-computer-science-python", "02", "python-type-system", "Python Type System", "beginner"),
    ("01-computer-science-python", "03", "object-oriented-programming", "Object-Oriented Programming", "beginner"),
    ("01-computer-science-python", "04", "advanced-python", "Advanced Python", "intermediate"),
    ("01-computer-science-python", "05", "async-python", "Async Python", "intermediate"),
    ("01-computer-science-python", "06", "concurrency", "Concurrency", "intermediate"),
    ("01-computer-science-python", "07", "memory-management", "Memory Management", "intermediate"),
    ("01-computer-science-python", "08", "data-structures", "Data Structures", "beginner"),
    ("01-computer-science-python", "09", "algorithms", "Algorithms", "beginner"),
    ("01-computer-science-python", "10", "complexity", "Complexity & Big-O", "beginner"),
    ("01-computer-science-python", "11", "operating-systems", "Operating Systems", "intermediate"),
    ("01-computer-science-python", "12", "linux", "Linux", "beginner"),
    ("01-computer-science-python", "13", "networking", "Networking", "intermediate"),
    ("01-computer-science-python", "14", "databases", "Databases", "intermediate"),
    ("01-computer-science-python", "15", "transactions", "Transactions", "intermediate"),
    ("01-computer-science-python", "16", "redis", "Redis", "intermediate"),
    ("01-computer-science-python", "17", "software-engineering", "Software Engineering", "intermediate"),
    ("01-computer-science-python", "18", "testing", "Testing", "intermediate"),
    ("01-computer-science-python", "19", "git", "Git", "beginner"),
    ("01-computer-science-python", "20", "docker", "Docker", "intermediate"),
    # ── Volume II ───────────────────────────────────────────────────────────
    ("02-machine-learning", "21", "mathematics", "Mathematics for ML", "intermediate"),
    ("02-machine-learning", "22", "numpy", "NumPy", "intermediate"),
    ("02-machine-learning", "23", "classical-machine-learning", "Classical ML", "intermediate"),
    ("02-machine-learning", "24", "ml-evaluation", "ML Evaluation", "intermediate"),
    ("02-machine-learning", "25", "pytorch", "PyTorch", "intermediate"),
    ("02-machine-learning", "26", "neural-networks", "Neural Networks", "intermediate"),
    ("02-machine-learning", "27", "computer-vision", "Computer Vision", "advanced"),
    ("02-machine-learning", "28", "nlp-foundations", "NLP Foundations", "intermediate"),
    ("02-machine-learning", "29", "rnns-and-lstms", "RNNs & LSTMs", "advanced"),
    ("02-machine-learning", "30", "attention", "Attention", "advanced"),
    ("02-machine-learning", "31", "transformers", "Transformers", "advanced"),
    # ── Volume III ──────────────────────────────────────────────────────────
    ("03-llm-engineering", "32", "tokenization", "Tokenization", "intermediate"),
    ("03-llm-engineering", "33", "embeddings", "Embeddings", "intermediate"),
    ("03-llm-engineering", "34", "llm-architecture", "LLM Architecture", "intermediate"),
    ("03-llm-engineering", "35", "next-token-prediction", "Next-Token Prediction", "intermediate"),
    ("03-llm-engineering", "36", "context-windows", "Context Windows", "intermediate"),
    ("03-llm-engineering", "37", "prompt-engineering", "Prompt Engineering", "intermediate"),
    ("03-llm-engineering", "38", "structured-outputs", "Structured Outputs", "advanced"),
    ("03-llm-engineering", "39", "function-tool-calling", "Function / Tool Calling", "advanced"),
    ("03-llm-engineering", "40", "llm-evaluation", "LLM Evaluation", "advanced"),
    ("03-llm-engineering", "41", "fine-tuning", "Fine-Tuning", "advanced"),
    ("03-llm-engineering", "42", "quantization", "Quantization", "advanced"),
    ("03-llm-engineering", "43", "inference", "Inference Optimization", "advanced"),
    # ── Volume IV ───────────────────────────────────────────────────────────
    ("04-rag", "44", "why-rag", "Why RAG?", "intermediate"),
    ("04-rag", "45", "document-processing", "Document Processing", "intermediate"),
    ("04-rag", "46", "chunking", "Chunking Strategies", "intermediate"),
    ("04-rag", "47", "embedding-models", "Embedding Models", "intermediate"),
    ("04-rag", "48", "vector-databases", "Vector Databases", "advanced"),
    ("04-rag", "49", "bm25", "BM25 & Lexical Search", "intermediate"),
    ("04-rag", "50", "hybrid-search", "Hybrid Search", "advanced"),
    ("04-rag", "51", "reranking", "Reranking", "advanced"),
    ("04-rag", "52", "context-compression", "Context Compression", "advanced"),
    ("04-rag", "53", "query-transformation", "Query Transformation", "advanced"),
    ("04-rag", "54", "advanced-rag", "Advanced RAG", "advanced"),
    ("04-rag", "55", "rag-evaluation", "RAG Evaluation", "advanced"),
    ("04-rag", "56", "production-rag-architecture", "Production RAG", "advanced"),
    # ── Volume V ────────────────────────────────────────────────────────────
    ("05-agents", "57", "what-is-an-agent", "What Is an Agent?", "intermediate"),
    ("05-agents", "58", "agent-architecture", "Agent Architecture", "intermediate"),
    ("05-agents", "59", "tool-calling", "Tool Calling", "intermediate"),
    ("05-agents", "60", "agent-state", "Agent State", "intermediate"),
    ("05-agents", "61", "agent-memory", "Agent Memory", "advanced"),
    ("05-agents", "62", "planning", "Planning", "advanced"),
    ("05-agents", "63", "reflection", "Reflection", "advanced"),
    ("05-agents", "64", "human-in-the-loop", "Human-in-the-Loop", "advanced"),
    ("05-agents", "65", "multi-agent-systems", "Multi-Agent Systems", "advanced"),
    ("05-agents", "66", "multi-agent-communication", "Multi-Agent Communication", "advanced"),
    ("05-agents", "67", "agent-reliability", "Agent Reliability", "advanced"),
    ("05-agents", "68", "agent-evaluation", "Agent Evaluation", "advanced"),
    # ── Volume VI ───────────────────────────────────────────────────────────
    ("06-mcp", "69", "mcp-fundamentals", "MCP Fundamentals", "intermediate"),
    ("06-mcp", "70", "mcp-architecture", "MCP Architecture", "intermediate"),
    ("06-mcp", "71", "build-an-mcp-server", "Build an MCP Server", "advanced"),
    ("06-mcp", "72", "mcp-security", "MCP Security", "advanced"),
    ("06-mcp", "73", "mcp-production-architecture", "MCP Production Architecture", "advanced"),
    # ── Volume VII ──────────────────────────────────────────────────────────
    ("07-production", "74", "api-architecture", "API Architecture", "intermediate"),
    ("07-production", "75", "fastapi", "FastAPI", "intermediate"),
    ("07-production", "76", "caching", "Caching", "intermediate"),
    ("07-production", "77", "message-queues", "Message Queues", "advanced"),
    ("07-production", "78", "event-driven-architecture", "Event-Driven Architecture", "advanced"),
    ("07-production", "79", "distributed-systems", "Distributed Systems", "advanced"),
    ("07-production", "80", "kubernetes", "Kubernetes", "advanced"),
    ("07-production", "81", "ai-inference-infrastructure", "AI Inference Infrastructure", "advanced"),
    ("07-production", "82", "llm-gateway", "LLM Gateway", "advanced"),
    ("07-production", "83", "observability", "Observability", "advanced"),
    ("07-production", "84", "ai-observability", "AI Observability", "advanced"),
    ("07-production", "85", "reliability", "Reliability", "advanced"),
    ("07-production", "86", "security", "Security", "advanced"),
    ("07-production", "87", "ai-security", "AI Security", "advanced"),
    ("07-production", "88", "cost-engineering", "Cost Engineering", "advanced"),
    # ── Volume VIII ─────────────────────────────────────────────────────────
    ("08-system-design", "89", "system-design-fundamentals", "System Design Fundamentals", "advanced"),
    ("08-system-design", "90", "ai-system-design-framework", "AI System Design Framework", "advanced"),
    ("08-system-design", "91", "system-design-rag", "Design: RAG System", "advanced"),
    ("08-system-design", "92", "system-design-ai-search", "Design: AI Search", "advanced"),
    ("08-system-design", "93", "system-design-coding-agent", "Design: Coding Agent", "advanced"),
    ("08-system-design", "94", "system-design-customer-support", "Design: Customer Support AI", "advanced"),
    ("08-system-design", "95", "system-design-ai-analytics", "Design: AI Analytics Platform", "advanced"),
    ("08-system-design", "96", "system-design-multi-agent-platform", "Design: Multi-Agent Platform", "advanced"),
]

DIFFICULTY_EMOJI = {
    "beginner": "🟢",
    "intermediate": "🟡",
    "advanced": "🔴",
}

def lesson_readme(vol_dir, num, slug, title, difficulty):
    vol_label = {
        "01-computer-science-python": "📘 Volume I",
        "02-machine-learning": "📗 Volume II",
        "03-llm-engineering": "📙 Volume III",
        "04-rag": "📕 Volume IV",
        "05-agents": "📒 Volume V",
        "06-mcp": "📓 Volume VI",
        "07-production": "📔 Volume VII",
        "08-system-design": "📖 Volume VIII",
    }[vol_dir]
    emoji = DIFFICULTY_EMOJI[difficulty]

    return f"""\
# {num}. {title}

> {vol_label} · {emoji} {difficulty.capitalize()}

---

## 📋 Learning outcome

By the end of this lesson you should be able to:

- [ ] **Explain** the core concept in your own words
- [ ] **Implement** a from-scratch version (no frameworks)
- [ [ ]**Run** the code and verify the output matches the expected result
- [ ] **Build** a small project that uses this concept
- [ ] **Debug** a common failure mode
- [ ] **Measure** one performance or quality metric
- [ ] **Answer** the checkpoint interview questions

---

## 📚 Learn — Concepts

<!-- TODO: fill in the core concepts -->

---

## 🔬 Understand — Mental models

<!-- TODO: add diagrams and intuition -->

---

## 💻 Implement — Build it from scratch

Run the starter and complete the implementation:

```bash
python3 code/starter.py        # skeleton with tests
python3 -m pytest code/test_starter.py -v
```

Expected output:

```text
<!-- TODO: paste expected output here -->
```

---

## 🧪 Practice — Exercises

1. <!-- TODO -->
2. <!-- TODO -->
3. <!-- TODO -->

---

## 🏗️ Project

Build:

<!-- TODO: project spec -->

**Definition of done:**

- [ ] <!-- TODO -->
- [ ] <!-- TODO -->

---

## 🚀 Production

Consider:

<!-- TODO: production concerns -->

---

## 🎯 Checkpoint — Self-assessment (click to reveal)

<details>
<summary>Checkpoint 1</summary>

<!-- TODO: question + answer -->

</details>

<details>
<summary>Checkpoint 2</summary>

<!-- TODO: question + answer -->

</details>

<details>
<summary>Checkpoint 3</summary>

<!-- TODO: question + answer -->

</details>

---

## 💬 Discussion questions

1. <!-- TODO -->
2. <!-- TODO -->

---

*← [Curriculum index](https://github.com/lalitdotdev/-The-AI-Systems-Engineer-Handbook/blob/main/CURRICULUM.md)*
"""

def starter_py(title):
    return f'''\
"""Lesson {title} — starter skeleton.

Delete this placeholder docstring and implement.
"""
from __future__ import annotations


def hello() -> str:
    """Return a greeting."""
    return "TODO"


if __name__ == "__main__":
    print(hello())
'''

def test_starter_py():
    return '''\
"""Tests for the lesson starter. Replace or extend freely."""
import pytest

from starter import hello


def test_hello_not_todo():
    assert "TODO" not in hello()


def test_hello_returns_string():
    assert isinstance(hello(), str)
'''

def __main__():
    created = 0
    for vol_dir, num, slug, title, difficulty in LESSONS:
        lesson_dir = ROOT / vol_dir / f"{num}-{slug}"
        (lesson_dir / "code").mkdir(parents=True, exist_ok=True)
        (lesson_dir / "docs").mkdir(parents=True, exist_ok=True)
        (lesson_dir / "exercises").mkdir(parents=True, exist_ok=True)
        (lesson_dir / "project").mkdir(parents=True, exist_ok=True)

        (lesson_dir / "README.md").write_text(
            lesson_readme(vol_dir, num, slug, title, difficulty), encoding="utf-8"
        )
        (lesson_dir / "code" / "starter.py").write_text(
            starter_py(title), encoding="utf-8"
        )
        (lesson_dir / "code" / "test_starter.py").write_text(
            test_starter_py(), encoding="utf-8"
        )
        (lesson_dir / "docs" / "en.md").write_text(
            f"# {title}\n\n> Lesson narrative — fill me in.\n", encoding="utf-8"
        )
        (lesson_dir / "exercises" / "README.md").write_text(
            f"# Exercises — {title}\n\nPractice problems go here.\n", encoding="utf-8"
        )
        (lesson_dir / "project" / "README.md").write_text(
            f"# Project — {title}\n\nA larger project combining this lesson's concepts.\n",
            encoding="utf-8",
        )
        created += 1

    # Write a catalog of lessons as JSON (handy for tooling / quizzes)
    catalog = [
        {"volume": vol, "number": n, "slug": s, "title": t, "difficulty": d}
        for vol, n, s, t, d in LESSONS
    ]
    (ROOT / "docs" / "lessons.json").write_text(
        json.dumps(catalog, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Created {created} lessons + docs/lessons.json")


if __name__ == "__main__":
    __main__()
