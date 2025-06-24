# 🧠 Mnemos

A minimal, extensible memory layer for agentic AI.

[![PyPI version](https://badge.fury.io/py/mnemos.svg)](https://badge.fury.io/py/mnemos)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

## 🚀 Features

- 🧠 `remember()`, `recall()` - simple, intuitive API
- 🏷️ Tag + keyword search
- 🧩 Pluggable storage backends (in-memory included)
- 🧪 Fully typed and test-covered

## 🛠️ Usage

```python
from mnemos import remember, recall

remember("Memory is all you need.", tags=["mnemos", "focus"])

results = recall("memory")
print(results[0].text)  # "Memory is all you need."
```

## 📦 Installation

Install with pip:

```bash
pip install mnemos
```

## 🧪 Testing

```bash
pytest tests/
```

## 🌱 Status

Mnemos is in early development. This initial version provides an in-memory implementation with a clean API. Future versions will add persistent storage and more advanced search capabilities.

Contributions, ideas, and feedback are welcome at [github.com/iteebz/mnemos](https://github.com/iteebz/mnemos)

## 📜 License

[MIT](./LICENSE)
