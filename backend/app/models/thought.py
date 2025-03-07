from typing import Any
import uuid
import datetime

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON, Index


def now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def generate_uuid() -> str:
    return str(uuid.uuid4())


class ThoughtBase(SQLModel):
    """Base model with shared fields"""
    pass


class ThoughtVersion(SQLModel, table=True):
    __tablename__: str = "thought_versions"  # type: ignore

    id: str = Field(default_factory=generate_uuid, primary_key=True)
    thought_id: str = Field(foreign_key="thoughts.id")
    created_at: datetime.datetime = Field(default_factory=now)
    content: str
    version_number: int
    annotations: dict[str, Any] | None = Field(default=None, sa_column=Column(JSON))

    thought: "Thought" = Relationship(
        back_populates="versions",
        sa_relationship_kwargs={"uselist": False},
    )

    # Custom index
    __table_args__ = (
        Index(
            'ix_thought_versions_thought_id_version_number',
            'thought_id',
            'version_number'
        ),
    )


class CurrentThoughtVersion(SQLModel, table=True):
    __tablename__: str = "current_thought_versions"  # type: ignore

    thought_id: str = Field(foreign_key="thoughts.id", primary_key=True)
    version_id: str = Field(foreign_key="thought_versions.id")

    # Complex relationships that need SQLAlchemy's full API
    thought: "Thought" = Relationship(
        back_populates="current_version_association",
        sa_relationship_kwargs={"uselist": False},
    )

    version: "ThoughtVersion" = Relationship(
        sa_relationship_kwargs={"uselist": False},
    )


class Thought(SQLModel, table=True):
    __tablename__: str = "thoughts"  # type: ignore

    id: str = Field(default_factory=generate_uuid, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=now)

    # Relationships 
    versions: list["ThoughtVersion"] = Relationship(back_populates="thought")
    
    current_version_association: "CurrentThoughtVersion | None" = Relationship(
        back_populates="thought",
        sa_relationship_kwargs={"uselist": False},
    )

    @property
    def current_version(self) -> "ThoughtVersion | None":
        """Get the current version of this thought"""
        if self.current_version_association:
            return self.current_version_association.version
        return None