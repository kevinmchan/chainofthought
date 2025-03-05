from sqlalchemy.orm import Session
import uuid

from app.models.thought import Thought, ThoughtVersion, CurrentThoughtVersion
from app.schemas.thought import ThoughtCreate


def create_thought(db: Session, thought_data: ThoughtCreate) -> Thought:
    """Create a new thought with its first version"""
    # Create thought record
    thought_id = str(uuid.uuid4())
    db_thought = Thought(id=thought_id)
    db.add(db_thought)
    db.flush()
    
    # Create first version
    version_id = str(uuid.uuid4())
    db_version = ThoughtVersion(
        id=version_id,
        thought_id=thought_id,
        content=thought_data.content,
        metadata=thought_data.annotations,
        version_number=1
    )
    db.add(db_version)
    
    # Set current version
    db_current = CurrentThoughtVersion(
        thought_id=thought_id,
        version_id=version_id
    )
    db.add(db_current)
    
    db.commit()
    
    # Set current_version for response
    db_thought.current_version = db_version
    
    return db_thought