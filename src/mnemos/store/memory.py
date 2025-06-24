"""In-memory implementation of the memory store."""
from typing import Dict, List

from .base import MemoryStore
from ..models import Artifact


class InMemoryStore(MemoryStore):
    """In-memory implementation of the memory store.
    
    This implementation is not thread-safe. For concurrent access, external
    synchronization is required.
    """
    
    def __init__(self):
        """Initialize a new in-memory store."""
        self._store: Dict[str, Artifact] = {}
    
    def save(self, artifact: Artifact) -> None:
        """Save an artifact to the in-memory store."""
        self._store[str(artifact.id)] = artifact
    
    def search(self, query: str) -> List[Artifact]:
        """Search for artifacts matching the query."""
        if not query:
            return []
            
        query = query.lower()
        results = []
        
        for artifact in self._store.values():
            if query in artifact.text.lower():
                results.append(artifact)
                continue
                
            if any(query in tag.lower() for tag in artifact.tags):
                results.append(artifact)
        
        # Sort by most recent first
        return sorted(results, key=lambda x: x.created_at, reverse=True)
    
    def clear(self) -> None:
        """Clear all artifacts from the store."""
        self._store.clear()
