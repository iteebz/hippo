# 🧠 Mnemos

**Memory for Agentic AI. Inspired by the brain. Built for the future.**

Mnemos is a lightweight, extensible memory system for agentic AI.  
It helps agents **remember what matters**—not just store data.

## ✨ What is Mnemos?

Mnemos is a memory-as-a-service toolkit that enables developers to add persistent, structured, and salience-aware memory to AI agents and LLM apps.

Think of it like a hippocampus for your agents:
- Clean API for memory ingestion and recall
- Supports session, semantic, and artifact-level memory
- Optimized for context relevance, traceability, and long-term coherence
- Built on familiar tools like Postgres and pgvector
- Designed for composability and open-source contribution

## 🧪 Example Usage

```python
import mnemos

# Ingest a memory (e.g., from a chat session or document)
mnemos.ingest(session_id="abc123", content="The user prefers minimalist interfaces.")

# Recall relevant memories
results = mnemos.recall(query="What does the user like?")
print(results)
```

## 🧱 Key Features
- 🧠 Structured memory: episodic, semantic, and artifact tiers
- 🔍 Vector search + SQL filtering via Supabase/Postgres
- 🧰 Opinionated defaults, extensible for custom agents
- 🔄 Daemon-ready for consolidation and pruning cycles
- 🧾 Traceable & versioned memory objects for auditability

## 📦 Installation

Coming soon via PyPI:
```bash
pip install mnemos
```

## 🌱 Project Status

Mnemos is in early development. Contributions, ideas, and feedback are welcome.

We’re building in the open: github.com/iteebz/mnemos

## 📜 License

MIT
