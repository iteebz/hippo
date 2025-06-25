# MAP-2: Storage Persistence

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25

---

## Motivation

Mnemos requires a reliable, pluggable persistence layer to store memory primitives durably beyond runtime. Storage is fundamental to continuity, traceability, and inspection—without it, memory is ephemeral and non-agentic.

To ensure adaptability and low coupling, storage must be abstracted through a consistent interface, allowing support for various backends (e.g., in-memory, SQLite, future databases) while maintaining consistent behavior.

---

## Proposal

Define storage persistence as an adapter pattern that encapsulates:

- **Durability:** Ensure primitives persist across sessions  
- **Schema enforcement:** Minimal, stable schemas for all primitives  
- **Transactional integrity:** Support atomic, consistent operations  
- **Query interface:** Enable lookup by id, tags, keywords, or embeddings  
- **Metadata support:** Store timestamps, source relationships, and versions  

Storage persistence is not just infrastructure—it is the vessel through which memory becomes reliable and evolvable.

---

## Core Responsibilities

1. **Primitive Persistence:** Store validated `Message`, `Summary`, and `Artifact` objects.  
2. **Efficient Retrieval:** Support lookups by id, tags, and free text—delegating semantic search to embedding adapters.  
3. **Schema Enforcement:** Maintain a clear, inspectable schema, with provisions for evolution over time.  
4. **Traceability:** Store lineage data (e.g., source IDs, timestamps, versions) to support inspection and debugging.  
5. **Backend Abstraction:** Provide a unified interface over varied backend implementations.

---

## Example Interface (Conceptual)

```python
from abc import ABC, abstractmethod
from typing import List, Optional, Any

class StorageAdapter(ABC):

    @abstractmethod
    def save(self, primitive: Any) -> None:
        """Persist a memory primitive."""

    @abstractmethod
    def fetch_by_id(self, id: str) -> Optional[Any]:
        """Retrieve a primitive by its unique identifier."""

    @abstractmethod
    def query(self, query_text: str, tags: Optional[List[str]] = None, top_k: int = 5) -> List[Any]:
        """Query primitives by text and optional tags."""

    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete a primitive from storage."""
```

---

## Rationale

Persistence is central to Mnemos’s identity as a memory substrate:

- Ensures continuity of memory beyond agent runtime  
- Allows agents to reflect, revise, and evolve thought over time  
- Supports debugging, transparency, and inspection  
- Provides stability and confidence to adapter implementers and contributors

---

## Future Considerations

- **Consistency:** Favor transactional consistency (atomic writes) via immutability; eventual consistency deferred  
- **Schema Evolution:** Lightweight migration paths as primitives evolve  
- **Search Composition:** Embedding adapter integration for hybrid search  
- **Scalability:** Sharding or replication may be revisited in later MAPs  

---

## Next Steps

- Implement SQLite-backed `StorageAdapter`  
- Define and document minimal schema for each primitive  
- Link this MAP in relevant commits and contributor docs  
- Benchmark for speed, durability, and developer experience