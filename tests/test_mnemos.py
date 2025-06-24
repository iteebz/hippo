"""Tests for the Mnemos memory service."""
import uuid
from datetime import datetime, timedelta, UTC
from unittest.mock import patch

import pytest

from mnemos import Artifact, MnemosCore, remember, recall


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


class TestMnemosCore:
    """Tests for the MnemosCore class."""
    
    @pytest.fixture
    def core(self):
        """Return a fresh MnemosCore instance for each test."""
        return MnemosCore()
    
    def test_remember_creates_artifact(self, core):
        """Test that remember() creates and stores an artifact."""
        artifact = core.remember("Test memory", tags=["test"])
        
        assert isinstance(artifact, Artifact)
        assert artifact.text == "Test memory"
        assert artifact.tags == ["test"]
    
    def test_recall_finds_matching_artifacts(self, core):
        """Test that recall() finds artifacts matching the query."""
        # Add test artifacts
        core.remember("The quick brown fox", ["animal", "fox"])
        core.remember("Lazy dog jumps over", ["animal", "dog"])
        core.remember("Irrelevant memory", ["other"])
        
        # Search in text
        results = core.recall("brown")
        assert len(results) == 1
        assert results[0].text == "The quick brown fox"
        
        # Search in tags
        results = core.recall("dog")
        assert len(results) == 1
        assert results[0].text == "Lazy dog jumps over"
    
    def test_recall_returns_all_matches(self, core):
        """Test that recall() returns all matching artifacts."""
        core.remember("Memory 1")
        core.remember("Memory 2")
        
        results = core.recall("memory")
        assert len(results) == 2
    
    def test_recall_orders_by_most_recent(self, core):
        """Test that recall() returns artifacts ordered by most recent first."""
        now = datetime.now(UTC)
        
        with patch('mnemos.models.datetime') as mock_datetime:
            mock_datetime.now.return_value = now - timedelta(days=1)
            core.remember("Old memory")
            
            mock_datetime.now.return_value = now
            core.remember("Recent memory")
        
        results = core.recall("memory")
        assert len(results) == 2
        assert results[0].text == "Recent memory"
        assert results[1].text == "Old memory"


class TestPublicAPI:
    """Tests for the public API functions."""
    
    def test_remember_function(self, monkeypatch):
        """Test the top-level remember() function."""
        # Create a fresh core for testing
        test_core = MnemosCore()
        monkeypatch.setattr('mnemos._memory', test_core)
        
        artifact = remember("Test memory", ["test"])
        assert artifact.text == "Test memory"
        assert artifact.tags == ["test"]
    
    def test_recall_function(self, monkeypatch):
        """Test the top-level recall() function."""
        # Create a fresh core for testing
        test_core = MnemosCore()
        monkeypatch.setattr('mnemos._memory', test_core)
        
        # Add test data
        remember("Test memory 1", ["test"])
        remember("Test memory 2", ["test"])
        
        results = recall("memory")
        assert len(results) == 2
        assert all(isinstance(a, Artifact) for a in results)
