"""Tests for the Mnemos package."""
import uuid
from datetime import datetime, timedelta, UTC
from unittest.mock import patch

import pytest

from mnemos import Artifact, remember, recall, Mnemos, InMemoryStore


class TestArtifact:
    """Tests for the Artifact model."""
    
    def test_artifact_creation(self):
        """Test that an Artifact can be created with all fields."""
        artifact_id = uuid.uuid4()
        created_at = datetime.now(UTC)
        artifact = Artifact(
            id=artifact_id,
            text="Test artifact",
            tags=["test", "example"],
            created_at=created_at
        )
        
        assert artifact.id == artifact_id
        assert artifact.text == "Test artifact"
        assert artifact.tags == ["test", "example"]
        assert artifact.created_at == created_at
    
    def test_artifact_defaults(self):
        """Test that an Artifact has sensible defaults."""
        artifact = Artifact(text="Test artifact")

        assert isinstance(artifact.id, uuid.UUID)
        assert artifact.text == "Test artifact"
        assert artifact.tags == []
        assert isinstance(artifact.created_at, datetime)


class TestMnemos:
    """Tests for the Mnemos class."""
    
    @pytest.fixture
    def mnemos(self):
        """Return a fresh Mnemos instance for each test."""
        return Mnemos(store=InMemoryStore())
    
    def test_remember_creates_artifact(self, mnemos):
        """Test that remember() creates and stores an artifact."""
        artifact = mnemos.remember("Test memory", ["test"])
        
        assert artifact.text == "Test memory"
        assert artifact.tags == ["test"]
    
    def test_recall_finds_matching_artifacts(self, mnemos):
        """Test that recall() finds artifacts with matching text."""
        mnemos.remember("Test memory 1")
        mnemos.remember("Test memory 2")
        
        results = mnemos.recall("memory 1")
        assert len(results) == 1
        assert results[0].text == "Test memory 1"
    
    def test_recall_returns_all_matches(self, mnemos):
        """Test that recall() returns all matching artifacts."""
        mnemos.remember("Test memory 1")
        mnemos.remember("Test memory 2")
        
        results = mnemos.recall("memory")
        assert len(results) == 2
    
    def test_recall_orders_by_most_recent(self, mnemos):
        """Test that recall() returns artifacts in most-recent-first order."""
        now = datetime.now(UTC)
        
        with patch('mnemos.models.datetime') as mock_datetime:
            mock_datetime.now.return_value = now - timedelta(days=1)
            mnemos.remember("Older memory")
            
            mock_datetime.now.return_value = now
            mnemos.remember("Newer memory")
        
        results = mnemos.recall("memory")
        assert results[0].text == "Newer memory"
        assert results[1].text == "Older memory"
    
    def test_clear_removes_all_artifacts(self, mnemos):
        """Test that clear() removes all artifacts."""
        mnemos.remember("Test memory 1")
        mnemos.remember("Test memory 2")
        
        mnemos.clear()
        results = mnemos.recall("memory")
        assert len(results) == 0
        
    def test_save_search_clear_flow(self, mnemos):
        """Test the complete memory lifecycle:
        save → search → clear → confirm clear → save again → search."""
        # 1. Save some artifacts
        mnemos.remember("First test artifact", ["test", "smoke"])
        mnemos.remember("Second test artifact", ["test"])
        
        # 2. Verify they can be found
        results = mnemos.recall("test")
        assert len(results) == 2
        assert {a.text for a in results} == {"First test artifact", "Second test artifact"}
        
        # 3. Clear the store
        mnemos.clear()
        
        # 4. Verify the store is empty
        results = mnemos.recall("test")
        assert len(results) == 0
        
        # 5. Add new data and verify it works
        mnemos.remember("Third test artifact", ["test", "after_clear"])
        results = mnemos.recall("test")
        assert len(results) == 1
        assert results[0].text == "Third test artifact"


class TestPublicAPI:
    """Tests for the public API functions."""
    
    def test_remember_function(self, monkeypatch):
        """Test the top-level remember() function."""
        # Create a fresh store just for this test
        store = InMemoryStore()
        mnemos = Mnemos(store=store)
        monkeypatch.setattr('mnemos._default_mnemos', mnemos)
        
        # Clear any existing state
        if hasattr(store, 'clear'):
            store.clear()
            
        artifact = remember("Test memory", ["test"])
        assert artifact.text == "Test memory"
        assert artifact.tags == ["test"]
    
    def test_recall_function(self, monkeypatch):
        """Test the top-level recall() function."""
        # Create a fresh store just for this test
        store = InMemoryStore()
        mnemos = Mnemos(store=store)
        monkeypatch.setattr('mnemos._default_mnemos', mnemos)
        
        # Clear any existing state
        if hasattr(store, 'clear'):
            store.clear()
        
        # Use a unique prefix for this test
        test_prefix = "UNIQUE_TEST_PREFIX_"
            
        # Add test data with unique prefix
        remember(f"{test_prefix} memory 1", ["test"])
        remember(f"{test_prefix} memory 2", ["test"])
        
        # Should only find the two we just added
        results = recall(test_prefix)
        assert len(results) == 2, f"Expected 2 results, got {len(results)}: {results}"
        assert all(isinstance(a, Artifact) for a in results)
        assert all(test_prefix in a.text for a in results)
