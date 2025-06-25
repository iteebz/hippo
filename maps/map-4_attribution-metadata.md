# MAP-4: Attribution Metadata

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25

---

## Motivation

In a multi-agent or multi-user environment, understanding the origin of memory entries is essential for trust, traceability, and informed decision-making.

Attribution metadata records who created or modified a memory, when, and under what context. This allows agents to reason about reliability, identity, and lineage—reinforcing Mnemos’s core principles of clarity and continuity.

---

## Proposal

Introduce an `Attribution` schema shared across all memory primitives (`Message`, `Summary`, `Artifact`) containing:

- `creator_id`: Unique identifier for the user or agent who authored the memory  
- `created_at`: Timestamp of creation  
- `source_context`: Optional contextual reference (e.g. session, environment)  
- `modifiers`: Optional list of agents or systems that altered or verified the memory  
- `version`: Integer for versioning—primarily applicable to evolving artifacts  

This metadata is stored as a structured JSON blob, with recommended fields but extensibility for custom implementations.

---

## Example Extension to Primitives

```python
@dataclass
class Attribution:
    creator_id: str
    created_at: datetime
    source_context: Optional[str] = None
    modifiers: List[str] = field(default_factory=list)
    version: int = 1

@dataclass
class Message:
    id: str
    content: str
    attribution: Attribution
    tags: List[str] = field(default_factory=list)
```

---

## Rationale

- Attribution reinforces inspectability and trust, especially in collaborative or autonomous systems  
- Enables auditing, debugging, and lineage tracking for memory evolution  
- Establishes groundwork for future features such as memory permissioning or shared workspaces  
- JSON-based schema with suggested defaults allows flexibility without rigid enforcement

---

## Future Considerations

- Define default attribution format and schema recommendations  
- Support for anonymization, pseudonyms, or privacy-respecting identifiers  
- Enable memory filtering or search by attribution metadata  
- Explore cryptographic signatures for verifiable provenance (future MAP)  
- Integrate with version control strategies for evolving artifacts

---

## Next Steps

- Implement attribution field in core memory primitives  
- Update serialization and storage adapters to persist and query attribution metadata  
- Extend developer documentation with attribution examples and use cases  
- Ensure test coverage for attribution-specific behaviors