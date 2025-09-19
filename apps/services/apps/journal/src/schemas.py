# Journal Service Schemas
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from .models import Mood 

# Schema for creating/updating journal entries
class JournalEntryCreate(BaseModel):
    user_id: UUID
    title: str
    content: str
    tags: Optional[str] = None
    mood: Mood

    class Config:
        orm_mode = True

# Schema for reading journal entries
class JournalEntry(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    content: str
    tags: Optional[str] = None
    mood: Mood
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True