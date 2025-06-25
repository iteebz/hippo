# MAP-0: Memory Primitives

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25  

---

## Motivation

Mnemos exists to provide persistent, structured memory for agents—not just a search engine but a continuity layer for thought and reflection.

To do this effectively, memory must be structured, inspectable, and evolvable. This MAP defines the core memory primitives that form Mnemos’s foundation.

---

## Proposal

Define three core memory primitives:

### 1. `Message`

Raw input—text or interaction data, timestamped and optionally tagged.

```python
@dataclass
class Message:
    id: str
    user_id: str
    session_id: Optional[str] = None
    timestamp: datetime
    content: str
    tags: list[str] = field(default_factory=list)
```

### 2. `Summary`

A distilled abstraction over one or more messages. Used for compression and high-level review.

```python
@dataclass
class Summary:
    id: str
    user_id: str
    session_id: Optional[str] = None
    source_ids: list[str]
    content: str
    created_at: datetime
    tags: list[str] = field(default_factory=list)
```

### 3. `Artifact`

Persistent, versionable knowledge units—facts, beliefs, or decisions.

```python
@dataclass
class Artifact:
    id: str
    user_id: str
    session_id: Optional[str] = None
    content: str
    created_at: datetime
    source_ids: list[str]
    version: int = 1
    tags: list[str] = field(default_factory=list)


Artifacts are immutable. New versions should be created by appending a new entry with an incremented version number. A `"latest"` flag may be used to simplify retrieval.
```

---

## Relationships

- Typical progression: `Message` → `Summary` → `Artifact`
- Traceability maintained via `source_ids`
- All primitives support optional tagging
- Immutability ensures a stable memory trail

---

## Future Considerations

- Advanced artifact versioning (conflict resolution, branching)
- Tagging strategy: agent-generated with optional manual override
- Meta-primitives and hierarchical memory structure
- Attribution metadata (see MAP-4)
- Memory lifespan and eviction (see MAP-5)

---

## Rationale

These primitives mirror human memory stages:

- Messages represent raw experience  
- Summaries provide abstraction and compression  
- Artifacts encode stable knowledge and beliefs

This model balances simplicity, extensibility, and narrative coherence.

By defining structured, inspectable memory primitives, Mnemos affirms its philosophy: memory is not a blob to be indexed, but a coherent sequence of thought. Immutability reinforces transparency and avoids caching concerns. Each unit holds purpose, provenance, and position in the memory trail.

---

## Next Steps

- Accept MAP-0  
- Implement primitives in code  
- Integrate with core APIs (`remember()`, `recall()`)  
- Reference MAP-0 in commits and PRs