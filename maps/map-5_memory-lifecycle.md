# MAP-5: Memory Lifecycle

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25

---

## Motivation

Memory in Mnemos is not static; it evolves through stages—from raw experience to stable knowledge—and must be managed accordingly. A well-defined memory lifecycle ensures continuity, consistency, and control over how memory is retained, transformed, or removed.

Without lifecycle awareness, systems risk bloated storage, lost traceability, and incoherent memory states over time.

---

## Proposal

Define the lifecycle stages and management policies for all core memory primitives:

### Lifecycle Stages

- **Creation**: A `Message` is captured from raw input, with attribution and timestamp.  
- **Summarization**: One or more messages are condensed into a `Summary`, often agent-initiated.  
- **Artifact Formation**: A durable `Artifact` is created to reflect distilled knowledge or beliefs.  
- **Versioning**: Artifacts may evolve over time, with each version persisted immutably and traceably.  
- **Eviction or Archival**: Older or redundant memory entries may be soft-deleted (evicted) or moved to long-term archive, based on policy.  

---

### Lifecycle Policies

- **Retention Rules**: Memories can be retained by age, frequency of access, or tag-based relevance.  
- **Eviction Triggers**: When storage thresholds are reached (e.g. memory count, disk size), oldest or least-relevant items are pruned.  
- **Forget vs Delete**:
  - `forget()`: Soft deletion—marks memory as inactive or hidden, preserving trace.
  - `delete()`: Hard deletion—removes memory entirely from the store.  
- **Audit Trail**: All transitions should be recorded for inspection and traceability.

---

## Rationale

- Lifecycle design ensures memory doesn't grow unbounded or become incoherent over time.  
- Aligns with Mnemos's principle of inspectable, intentional memory.  
- Versioning supports long-term agent learning and reflection without overwriting past states.  
- Separation of `forget` vs `delete` allows nuance between reversible and permanent memory actions.  

---

## Future Considerations

- Automate summarization or condensation based on thresholds (e.g. total size, activity decay).  
- Allow configurable retention/eviction strategies per agent or session.  
- Introduce archival storage for cold or infrequently accessed memory.  
- Integrate visual tools (e.g. Mermaid diagrams) to visualize lifecycle flows and transitions.  
- Explore policy enforcement via decorators, middleware, or config-driven rules.

---

## Next Steps

- Define baseline lifecycle rules in v0.1 for in-memory and SQLite stores.  
- Implement `forget()` and `delete()` behavior in storage adapters.  
- Track memory state transitions with metadata and logging.  
- Document lifecycle stages, developer hooks, and API affordances in `docs/lifecycle.md`.  