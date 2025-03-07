from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.thought import ThoughtCreate, ThoughtWithCurrentVersion
from app.crud.thoughts import create_thought, read_thought
from app.db.session import get_db


router = APIRouter(prefix="/thoughts", tags=["thoughts"])

@router.post("/", response_model=ThoughtWithCurrentVersion)
def create_thought_endpoint(
    thought: ThoughtCreate, 
    db: Session = Depends(get_db)
):
    """Create a new thought with its first version"""
    return create_thought(db, thought)

@router.get("/{id}", response_model=ThoughtWithCurrentVersion)
def read_thought_endpoint(id: str, db: Session = Depends(get_db)):
    """Read a thought by ID"""
    thought = read_thought(db, id)
    if thought is None:
        raise HTTPException(status_code=404, detail="Thought not found")
    return thought