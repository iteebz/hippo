"""Mnemos - Simple in-memory storage for AI agents.

Provides remember() and recall() functions for basic memory operations,
with support for pluggable storage backends.
"""
from .core import Mnemos
from .models import Artifact
from .store.memory import InMemoryStore

# Create a default instance for the simple API
_default_mnemos = Mnemos(store=InMemoryStore())

# Public API
remember = _default_mnemos.remember
recall = _default_mnemos.recall

__version__ = "0.1.1"
__all__ = ['remember', 'recall', 'Artifact', 'Mnemos', 'InMemoryStore']