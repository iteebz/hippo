# MAP-3: Embedding Adapter

- **Status**: Draft  
- **Author**: Tyson Chan (iteebz)  
- **Created**: 2025-06-25

---

## Motivation

Semantic search enables Mnemos to recall memory meaningfully—not just by keyword, but by conceptual similarity. Embeddings translate memory content into vector space, enabling flexible, context-aware search.

To support multiple providers and future extensibility, embeddings must be encapsulated within a dedicated adapter layer. This allows Mnemos to remain backend-agnostic and modular across local or external models.

---

## Proposal

Define an `EmbeddingAdapter` interface with responsibilities including:

- Converting memory content or query strings into embedding vectors  
- Indexing and managing those vectors for fast similarity search  
- Providing nearest-neighbor lookup returning relevant memory references  
- Abstracting over multiple embedding providers (e.g., OpenAI, HuggingFace, Nomic, local models)  
- Supporting batch operations for performance and scalability

---

## Core Responsibilities

1. **Embedding Generation:** Transform strings or memory primitives into numerical vectors.  
2. **Index Management:** Store and update embeddings in a search index optimized for fast similarity queries.  
3. **Similarity Search:** Return top-k nearest neighbors for a given vector input.  
4. **Backend Abstraction:** Encapsulate model-specific logic behind a consistent interface.

---

## Example Interface (Conceptual)

```python
class EmbeddingAdapter(ABC):

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate vector embeddings for a list of texts."""

    @abstractmethod
    def add_embeddings(self, ids: List[str], embeddings: List[List[float]]) -> None:
        """Add or update embeddings in the index."""

    @abstractmethod
    def query(self, embedding: List[float], top_k: int) -> List[str]:
        """Query the index using a vector embedding to return matching IDs."""
```

---

## Rationale

- Separating embeddings into an adapter simplifies integration and swapping of providers  
- Semantic recall is core to agentic memory; embedding support ensures more natural interactions  
- Batch operations and provider abstraction improve performance and future flexibility  
- Keeping embedding logic out of the storage adapter ensures clean separation of concerns

---

## Future Considerations

- Support hybrid search (vector + keyword filtering)  
- Allow embedding version tags for backward compatibility or comparison  
- Defer graph/native embeddings until knowledge graphs are introduced  
- Potential caching if embedding generation becomes a bottleneck  
- Robust error handling for third-party embedding APIs

---

## Next Steps

- Implement a basic OpenAI or SentenceTransformer adapter  
- Integrate semantic search into `recall()` API  
- Validate similarity ranking behavior against baseline keyword search  
- Update documentation with embedding adapter guidelines