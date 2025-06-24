# 🧠 Mnemos

**Memory for Agentic AI. Inspired by minds. Engineered for longevity.**

Mnemos is a lightweight, extensible memory system for agentic AI.  
It helps agents **remember what matters** — not just store data.

## ✨ What is Mnemos?

Mnemos is a memory-as-a-service toolkit that enables developers to add persistent, structured, and coherent memory to AI agents and LLM apps.

Think of it like a hippocampus for your agents:
- Clean API for memory storage and recall
- Optimized for simplicity and developer experience
- Designed for extensibility with pluggable storage backends

## 🧪 Example Usage

```python
import mnemos

# Store a memory
mnemos.remember("The user prefers minimalist interfaces.", tags=["ui", "preference"])

# Recall related memories
results = mnemos.recall("user interface")
print(results[0].text)  # "The user prefers minimalist interfaces."
```

## 🧱 Key Features
- 🧠 Simple, intuitive API with `remember()` and `recall()`
- 🔍 Basic text and tag-based search
- 🧪 Fully typed with Python type hints
- 🧰 Extensible storage backends (in-memory included)

## 📦 Installation

Install with pip:

```bash
pip install mnemos
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 🌱 Project Status

Mnemos is in early development. This initial version provides an in-memory implementation with a clean API. Future versions will add persistent storage and more advanced search capabilities.

Contributions, ideas, and feedback are welcome at [github.com/iteebz/mnemos](https://github.com/iteebz/mnemos)

## 📜 License

MIT
