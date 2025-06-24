"""Core in-memory storage implementation for Mnemos."""
from __future__ import annotations

from typing import Dict, List, Optional

from .models import Artifact


class MnemosCore:
    """Core in-memory storage for Mnemos memory operations.
    
    This class handles the actual storage and retrieval of memory artifacts
    using simple in-memory data structures.
    """
    
    def __init__(self):
        """Initialize the in-memory storage."""
        self._store: Dict[str, Artifact] = {}
    
    def remember(
        self, 
        text: str, 
        tags: Optional[List[str]] = None
    ) -> Artifact:
        """Store a new memory artifact.
        
        Args:
            text: The content to remember
            tags: Optional list of tags for categorization
            org_id: Optional organization identifier
            
        Returns:
            The created Artifact
        """
        artifact = Artifact(
            text=text,
            tags=tags or []
        )
        
        # Store the artifact
        self._store[str(artifact.id)] = artifact
        return artifact
    
    def recall(
        self, 
        query: str
    ) -> List[Artifact]:
        """Search for memory artifacts matching the query.
        
        Performs a case-insensitive substring match on:
        - Artifact text
        - Any of the artifact's tags
        
        Args:
            query: Search term to match against artifact text and tags
            
        Returns:
            List of matching Artifacts, ordered by most recent first
        """
        if not query:
            return []
            
        query = query.lower()
        results = []
        
        for artifact in self._store.values():
            # Check if query matches text
            if query in artifact.text.lower():
                results.append(artifact)
                continue
                
            # Check if query matches any tag
            if any(query in tag.lower() for tag in artifact.tags):
                results.append(artifact)
        
        # Sort by most recent first
        return sorted(results, key=lambda x: x.created_at, reverse=True)
