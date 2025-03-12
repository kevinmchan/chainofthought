from typing import cast

from sqlalchemy.orm import Session
from app.schemas.thought import ThoughtCreate
from app.crud.thoughts import create_thought, read_thought
from app.models.thought import ThoughtVersion


def test_create_thought(db_session: Session):
    # create a thought object
    thought = ThoughtCreate(
        content="Test thought content",
        annotations={"tag": "test"}
    )
    
    # add thought object to the database
    db_thought = create_thought(db_session, thought)

    # assert that the returned thought object has the correct values
    assert db_thought.id is not None
    assert db_thought.created_at is not None
    assert db_thought.current_version is not None
    assert db_thought.current_version.id is not None
    assert db_thought.current_version.created_at is not None
    assert db_thought.current_version.thought_id == db_thought.id
    assert db_thought.current_version.content == thought.content
    assert db_thought.current_version.annotations == thought.annotations
    assert db_thought.current_version.version_number == 1

def test_read_thought(db_session: Session):
    # create a thought object
    thought = ThoughtCreate(
        content="Test thought content",
        annotations={"tag": "test"}
    )
    
    # add thought object to the database
    db_thought_create = create_thought(db_session, thought)
    db_version_create = db_thought_create.current_version
    db_version_create = cast(ThoughtVersion, db_version_create)   # type narrow to be not None

    # get the thought object from the database by id
    db_thought_read = read_thought(db_session, db_thought_create.id)

    # assert that the returned thought object has the correct values
    assert db_thought_read is not None
    assert db_thought_read.id == db_thought_create.id
    assert db_thought_read.created_at == db_thought_create.created_at
    assert db_thought_read.current_version is not None
    assert db_thought_read.current_version.id == db_version_create.id
    assert db_thought_read.current_version.created_at == db_version_create.created_at
    assert db_thought_read.current_version.thought_id == db_version_create.thought_id
    assert db_thought_read.current_version.content == db_version_create.content
    assert db_thought_read.current_version.annotations == db_version_create.annotations
    assert db_thought_read.current_version.version_number == db_version_create.version_number