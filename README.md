# 🧠 Mnemos

**Structured memory for agentic systems.**  
Built for continuity — not just retrieval.

Mnemos is a minimal, extensible memory layer that gives AI agents the ability to remember with structure, coherence, and traceability.

It stores messages, builds summaries, and evolves knowledge artifacts over time — just like you.

[![PyPI version](https://badge.fury.io/py/mnemos.svg)](https://badge.fury.io/py/mnemos)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

## 🚀 Features

- 🧠 Simple, inspectable API: `remember()`, `recall()`, `trace()`
- 🏷️ Semantic + tag-based search
- 🧩 Pluggable storage backends (in-memory, SQLite)
- 🧪 Fully typed and test-covered
- ⚡️ DX-first install and invocation

## 🛠️ Quickstart

```bash
pip install mnemos
```

```python
from mnemos import remember, recall

remember("Memory is all you need.", tags=["mnemos", "focus"])
results = recall("memory")
print(results[0].text)  # "Memory is all you need."
```

→ Full example: [`examples/basic.py`](./examples/basic.py)  
→ Learn more in [`docs/getting-started.md`](./docs/getting-started.md)

## 🧠 Philosophy

Mnemos isn’t retrieval infrastructure.  

It’s a substrate of memory — structured, inspectable, and intentional.

Built for agents that think, not APIs that fetch.

Explore our architecture: [`maps/map-0_memory-primitives.md`](./maps/map-0_memory-primitives.md)

## 📚 Documentation

- [`docs/getting-started.md`](./docs/getting-started.md) — install + first memory
- [`docs/roadmap.md`](./docs/roadmap.md) — current scope + future releases
- [`docs/principles.md`](./docs/principles.md) — core values + DX decisions
- [`docs/contributing.md`](./docs/contributing.md) — how to get involved
- [`maps/README.md`](./maps/README.md) — design MAPs and architectural decisions

## 🧪 Development

### Requirements

- Python 3.12.10 (see `.python-version`)
- Poetry for dependency management

### Setup

Install dependencies:

```bash
poetry install
```

### Testing

Run the full test suite with:

```bash
poetry run pytest tests/
```

### Commands

Use the included justfile for common tasks:

```bash
just # lists available commands
```

## 💡 Contributions

Contributions, ideas, and feedback are welcome! Please see [docs/contributing.md](./docs/contributing.md) for guidelines.

## 📜 License

[MIT](./LICENSE)

---

> **Mnemos is built for clarity, continuity, and agency.**
> _Memory isn’t just storage — it’s structure, intent, and traceable thought._