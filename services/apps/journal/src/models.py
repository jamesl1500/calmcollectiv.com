# Journal Services Models
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4

class JournalEntryBase(BaseModel):
    title: str
    content: str
    mood: Optional[str] = None
    tags: List[str] = []

class JournalEntryCreate(JournalEntryBase):
    pass

class JournalEntry(JournalEntryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
