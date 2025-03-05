import uuid
import datetime

from sqlalchemy import Column, String, DateTime, JSON, ForeignKey, Integer, Index
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


def now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Thought(Base):
    __tablename__ = 'thoughts'

    id = Column(String, primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, default=now)

    versions = relationship("ThoughtVersion", back_populates="thought")
    current_version_association = relationship(
        "CurrentThoughtVersion",
        back_populates="thought",
        uselist=False,
    )

    @property
    def current_version(self) -> "ThoughtVersion | None":
        if self.current_version_association:
            return self.current_version_association.version
        return None

class ThoughtVersion(Base):
    __tablename__ = 'thought_versions'

    id = Column(String, primary_key=True, default=generate_uuid)
    thought_id = Column(String, ForeignKey('thoughts.id'), nullable=False)
    created_at = Column(DateTime, default=now)
    content = Column(String, nullable=False)
    version_number = Column(Integer, nullable=False)
    annotations = Column(JSON)

    thought = relationship("Thought", back_populates="versions", uselist=False)

    __table_args__ = (
        Index('ix_thought_versions_thought_id_version_number', 'thought_id', 'version_number'),
    )


class CurrentThoughtVersion(Base):
    __tablename__ = 'current_thought_versions'

    thought_id = Column(String, ForeignKey('thoughts.id'), primary_key=True)
    version_id = Column(String, ForeignKey('thought_versions.id'), nullable=False)

    thought = relationship(
        "Thought",
        back_populates="current_version_association",
        uselist=False,
    )
    version = relationship("ThoughtVersion", uselist=False)