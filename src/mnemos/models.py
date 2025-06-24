from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import uuid4, UUID


@dataclass
class Artifact:
    """A memory artifact stored in Mnemos.
    
    Attributes:
        text: The content to remember
        id: Unique identifier (auto-generated)
        tags: List of tags for categorization
        created_at: Timestamp of creation (auto-generated)
    """
    text: str
    id: UUID = field(default_factory=uuid4)
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __str__(self) -> str:
        return f"Artifact(id={self.id}, text='{self.text[:50]}...', tags={self.tags})"
