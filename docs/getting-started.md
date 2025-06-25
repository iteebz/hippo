# Getting Started with Mnemos

Welcome to **Mnemos** — a minimal memory layer for AI agents, built for continuity, clarity, and coherence.

This quickstart will help you install Mnemos, initialize your memory system, and store your first memory primitive.

---

## 📦 Installation

Mnemos is available as a Python package. Requires Python 3.12.10 for now.

```bash
pip install mnemos
```

---

## ⚙️ Initialize

Create a local SQLite-backed memory store:

```python
import mnemos

mnemos.init(storage="sqlite", db_path="mnemos.db")
```

This sets up the memory system using idiomatic defaults. No config files required.

---

## 🧠 Store a Memory

Store a simple fact or message:

```python
mnemos.remember("The capital of France is Paris.", tags=["geo", "fact"])
```

Mnemos converts this into a Message primitive and stores it with traceable metadata.

---

## 🔍 Recall a Memory

Query memory by semantic similarity or keyword:

```python
results = mnemos.recall("capital of France", top_k=3)
```

Returns ranked results with metadata. You can inspect, trace, or summarize them.

---

## 🕵️‍♀️ Trace It

Inspect the origin and metadata of recalled memory:

```python
mnemos.trace(results)
```

---

## 📁 File Structure (v0.1)

```bash
project/
├── mnemos.db             ← local SQLite memory
├── your_script.py        ← use Mnemos in any Python script
└── requirements.txt      ← (optional)
```

Mnemos is unopinionated about project structure. Just import and go.

---

## 📚 Next Steps

- Explore memory primitives: [MAP-0](../maps/map-0_memory-primitives.md)
- Review the [guiding principles](./principles.md)
- Read the [roadmap](./roadmap.md) to understand current scope
- Optionally review [contributing guidelines](./contributing.md)

---

## 💬 Questions?

For feedback, ideas, or contributions, open an issue or join the community (Discord link TBA).