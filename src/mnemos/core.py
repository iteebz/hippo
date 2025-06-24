"""Core Mnemos functionality with pluggable storage backends."""
from __future__ import annotations

from typing import List, Optional

from .models import Artifact
from .store.base import MemoryStore
from .store.memory import InMemoryStore


class Mnemos:
    """Main class for Mnemos memory operations with pluggable storage.
    
    This class provides a high-level interface for storing and retrieving
    memories using a pluggable storage backend.
    """
    
    def __init__(self, store: Optional[MemoryStore] = None):
        """Initialize Mnemos with an optional store backend.
        
        Args:
            store: The storage backend to use. Defaults to InMemoryStore.
        """
        self.store = store if store is not None else InMemoryStore()
    
    def remember(self, text: str, tags: Optional[List[str]] = None) -> Artifact:
        """Store a new memory artifact.
        
        Args:
            text: The content to remember
            tags: Optional list of tags for categorization
            
        Returns:
            The created Artifact
        """
        artifact = Artifact(
            text=text,
            tags=tags or []
        )
        
        self.store.save(artifact)
        return artifact
    
    def recall(self, query: str) -> List[Artifact]:
        """Search for memory artifacts matching the query.
        
        Performs a case-insensitive substring match on:
        - Artifact text
        - Any of the artifact's tags
        
        Args:
            query: Search term to match against artifact text and tags
            
        Returns:
            List of matching Artifacts, ordered by most recent first
        """
        return self.store.search(query)
    
    def clear(self) -> None:
        """Clear all artifacts from the store.
        
        This is a convenience method that delegates to the store's clear() method.
        Not all stores may support this operation.
        """
        self.store.clear()
