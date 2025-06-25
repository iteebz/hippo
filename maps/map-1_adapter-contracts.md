# MAP-1: Adapter Contracts

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25

---

## Motivation

Mnemos is built around modular, pluggable components—adapters—that encapsulate storage, embeddings, and future integrations. Defining clear contracts (abstract base classes, or ABCs) ensures consistency, extensibility, and clean separation of concerns.

Without these contracts, adapter implementations may diverge in structure and behavior, leading to fragility, coupling, and poor developer ergonomics.

---

## Proposal

Introduce formal contracts as Python ABCs for all core adapters, including but not limited to:

- **Storage Adapter**: Abstracts persistence (in-memory, SQLite, etc.)
- **Embedding Adapter**: Abstracts vectorization backends (e.g., Nomic, OpenAI, HuggingFace)
- **(Future) Search Adapter**: Enables hybrid or custom retrieval strategies

Each contract will define:

- Required method names and signatures  
- Return types and expected behavior  
- Typing and docstrings for readability and enforcement

These contracts are the stable public API surface for all adapter integrations—first-party and community-maintained alike.

---

## Contract Sketch: Storage Adapter

```python
from abc import ABC, abstractmethod
from typing import List, Optional, Any

class StorageAdapter(ABC):

    @abstractmethod
    def store(self, primitive: Any) -> None:
        """Store a memory primitive (Message, Summary, Artifact)."""

    @abstractmethod
    def retrieve(self, query: str, top_k: int = 5) -> List[Any]:
        """Retrieve matching primitives based on query."""
    
    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete a primitive by id."""
```

---

## Contract Sketch: Embedding Adapter

```python
from abc import ABC, abstractmethod
from typing import List

class EmbeddingAdapter(ABC):

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate vector embeddings for a list of texts."""
```

---

## Rationale

Adapter contracts are foundational to Mnemos’s architectural clarity. They:

- Ensure consistent behavior across all adapters  
- Allow adapters to evolve independently while remaining interoperable  
- Make it easy to onboard new contributors or plug in external providers  
- Support testability by enabling mock or dummy adapters  

---

## Future Considerations

- Define contracts for additional layers (Search Adapter, Serialization Adapter, etc.)  
- Add support for versioned contracts to manage evolution gracefully  
- Explore adapter-specific hooks for lifecycle or observability (out of scope for MAP-1)  
- Determine how async methods may be integrated cleanly in a future MAP  
- Provide test harnesses to validate adapter compliance

---

## Next Steps

- Implement `StorageAdapter` and `EmbeddingAdapter` ABCs  
- Refactor current adapters to conform  
- Add developer docs with adapter scaffolding examples  
- Reference MAP-1 in adapter-related commits and PRs