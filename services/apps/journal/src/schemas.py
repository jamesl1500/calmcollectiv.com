# Journal Service Schemas
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from .models import Mood

def JournalEntryCreate(BaseModel):
    user_id: UUID
    content: str
    mood: Mood