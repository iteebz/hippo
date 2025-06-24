"""Base classes for memory storage backends."""
from abc import ABC, abstractmethod
from typing import List

from ..models import Artifact


class MemoryStore(ABC):
    """Abstract base class for memory storage backends.
    
    Note: Implementations are not guaranteed to be thread-safe by default.
    If thread safety is required, it should be implemented by the concrete class.
    """
    
    @abstractmethod
    def save(self, artifact: Artifact) -> None:
        """Save an artifact to the store.
        
        Args:
            artifact: The artifact to save
        """
        pass
    
    @abstractmethod
    def search(self, query: str) -> List[Artifact]:
        """Search for artifacts matching the query.
        
        Args:
            query: Search term to match against artifact text and tags
            
        Returns:
            List of matching Artifacts, ordered by most recent first
        """
        pass
    
    def clear(self) -> None:
        """Clear all artifacts from the store.
        
        This is an optional method that concrete implementations can override
        for better test isolation.
        """
        raise NotImplementedError("clear() not implemented for this store")
