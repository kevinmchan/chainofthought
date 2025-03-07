from pydantic import BaseModel, ConfigDict
from typing import Any
from datetime import datetime


# Base schemas
class ThoughtVersionBase(BaseModel):
    content: str
    metadata: dict[str, Any] | None = None

# Creation schemas
class ThoughtCreate(ThoughtVersionBase):
    """Schema for creating a new thought (includes first version content)"""
    pass

# Response schemas
class ThoughtVersionRead(ThoughtVersionBase):
    """Schema for reading a thought version"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    thought_id: str
    created_at: datetime
    version_number: int

class ThoughtRead(BaseModel):
    """Schema for reading a thought"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    created_at: datetime
    
class ThoughtWithCurrentVersion(ThoughtRead):
    """Schema for reading a thought with its current version"""
    model_config = ConfigDict(from_attributes=True)
    
    current_version: ThoughtVersionRead