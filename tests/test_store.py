"""Tests for the memory store implementations."""
import pytest
from datetime import datetime, UTC, timedelta

from mnemos import Artifact
from mnemos.store.base import MemoryStore
from mnemos.store.memory import InMemoryStore


import abc

class TestMemoryStore(abc.ABC):
    """Base tests for all MemoryStore implementations."""
    
    @pytest.fixture
    @abc.abstractmethod
    def store(self) -> MemoryStore:
        """Return a fresh store instance for testing."""
        pass
    
    def test_save_and_retrieve(self, store: MemoryStore):
        """Test basic save and retrieve functionality."""
        artifact = Artifact(text="Test artifact")
        store.save(artifact)
        
        results = store.search("test")
        assert len(results) == 1
        assert results[0].text == "Test artifact"
    
    def test_search_by_tag(self, store: MemoryStore):
        """Test searching by tag."""
        artifact = Artifact(text="Test artifact", tags=["important"])
        store.save(artifact)
        
        results = store.search("important")
        assert len(results) == 1
        assert results[0].text == "Test artifact"
    
    def test_search_not_found(self, store: MemoryStore):
        """Test searching for non-existent items."""
        store.save(Artifact(text="Test artifact"))
        
        results = store.search("nonexistent")
        assert len(results) == 0
    
    def test_ordering(self, store: MemoryStore):
        """Test that results are ordered by most recent first."""
        now = datetime.now(UTC)
        
        # Create artifacts with different timestamps
        old = Artifact(
            text="Old artifact",
            created_at=now - timedelta(days=1)
        )
        
        new = Artifact(
            text="New artifact",
            created_at=now
        )
        
        store.save(old)
        store.save(new)
        
        results = store.search("artifact")
        assert len(results) == 2
        assert results[0].text == "New artifact"
        assert results[1].text == "Old artifact"


class TestInMemoryStore(TestMemoryStore):
    """Tests specific to the InMemoryStore implementation."""
    
    @pytest.fixture
    def store(self) -> InMemoryStore:
        """Return a fresh InMemoryStore instance."""
        return InMemoryStore()
    
    def test_clear(self, store: InMemoryStore):
        """Test the clear() method."""
        artifact = Artifact(text="Test artifact")
        store.save(artifact)
        assert len(store.search("artifact")) == 1
        
        store.clear()
        assert len(store.search("artifact")) == 0
