from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.thought import ThoughtCreate, ThoughtWithCurrentVersion
from app.crud.thoughts import create_thought
from app.db.session import get_db


router = APIRouter(prefix="/thoughts", tags=["thoughts"])

@router.post("/", response_model=ThoughtWithCurrentVersion)
def create_thought_endpoint(
    thought: ThoughtCreate, 
    db: Session = Depends(get_db)
):
    """Create a new thought with its first version"""
    return create_thought(db, thought)