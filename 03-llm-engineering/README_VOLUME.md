# 📙 Volume III — LLM Engineering

Move from ML to modern language-model systems and engineering.

## 🎯 Learning Objectives

By the end of this volume you should understand:

1. **Tokenization** - BPE, WordPiece, SentencePiece, vocab building
2. **Embeddings** - dense vectors, semantic similarity
3. **LLM Architecture** - decoder-only, causal masking, KV cache
4. **Next-Token Prediction** - sampling, temperature, top-k/p
5. **Context Windows** - prompt budget, context management
6. **Prompt Engineering** - templates, few-shot, chain-of-thought
7. **Structured Outputs** - JSON mode, constrained generation
8. **Function/Tool Calling** - schemas, validation, multi-tool
9. **LLM Evaluation** - automated evals, LLM-as-judge, hallucination
10. **Fine-Tuning** - SFT, LoRA, QLoRA, DPO
11. **Quantization** - int8/4, GGUF, memory-accuracy tradeoffs
12. **Inference** - batching, streaming, speculative decoding

## 📚 Lesson Map

| # | Lesson | Status | Difficulty | Project |
|---|--------|--------|------------|---------|
| 32 | Tokenization | 🟡 | 🟡 Intermediate | Tokenizer from Scratch |
| 33 | Embeddings | 🟡 | 🟡 Intermediate | Semantic Search Core |
| 34 | LLM Architecture | 🟡 | 🟡 Intermediate | Inference from Weights |
| 35 | Next-Token Prediction | 🟡 | 🟡 Intermediate | Sampling Controller |
| 36 | Context Windows | 🟡 | 🟡 Intermediate | Context Optimizer |
| 37 | Prompt Engineering | 🟡 | 🟡 Intermediate | Prompt Library |
| 38 | Structured Outputs | 🟡 | 🔴 Advanced | JSON Extractor |
| 39 | Function/Tool Calling | 🟡 | 🔴 Advanced | Tool Dispatcher |
| 40 | LLM Evaluation | 🟡 | 🔴 Advanced | Evals for RAG System |
| 41 | Fine-Tuning | 🟡 | 🔴 Advanced | Fine-tune Small Model |
| 42 | Quantization | 🟡 | 🔴 Advanced | Quantize & Compare |
| 43 | Inference | 🟡 | 🔴 Advanced | Inference Server |

## 🏗️ Capstone Projects

1. **AI Chatbot** - Streaming, sessions, structured outputs
2. **LLM Gateway** - Multi-model routing, fallbacks, cost tracking
3. **Structured Data Extraction API** - Pydantic + LLM + validation

## 📖 Quick Links

- [Start at Tokenization](32-tokenization)
- [View All Lessons JSON](../docs/lessons.json)
- [Previous Volume](#) → [Volume II (ML)](../02-machine-learning/README_VOLUME.md) | Next Volume → [Volume IV (RAG)](../04-rag/README_VOLUME.md)