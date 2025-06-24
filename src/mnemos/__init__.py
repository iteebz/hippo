"""Mnemos - Simple in-memory storage for AI agents.

Provides remember() and recall() functions for basic memory operations.
"""
from typing import List, Optional

from .core import MnemosCore
from .models import Artifact

# Create a single instance for the module
_memory = MnemosCore()

__version__ = "0.1.0"
__all__ = ['remember', 'recall', 'Artifact']


def remember(
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
        
    Example:
        >>> remember("The fire rises", ["dark_knight", "bane"], "org-123")
    """
    return _memory.remember(text, tags=tags)


def recall(
    query: str
) -> List[Artifact]:
    """Search for memory artifacts matching the query.
    
    Performs a simple substring match on artifact text and tags.
    
    Args:
        query: Search term to match against artifact text and tags
        org_id: Optional organization identifier to scope the search
        
    Returns:
        List of matching Artifacts, ordered by most recent first
        
    Example:
        >>> results = recall("fire", org_id="org-123")
    """
    return _memory.recall(query)


# Make the core types available for advanced usage
__all__ = ['Artifact', 'MnemosCore', 'remember', 'recall']