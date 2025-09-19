# Journal Services Models
from pydantic import BaseModel  # For Pydantic models
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4

# Import DB Configuration
from database import Base, engine

# Mood Enum
from enum import Enum

class Mood(str, Enum):
    HAPPY = "happy"
    SAD = "sad"
    ANXIOUS = "anxious"
    NEUTRAL = "neutral"
    EXCITED = "excited"
    ANGRY = "angry"
    STRESSED = "stressed"
    RELAXED = "relaxed"
    GRATEFUL = "grateful"
    LONELY = "lonely"
    CONFUSED = "confused"
    HOPEFUL = "hopeful"
    TIRED = "tired"
    CONTENT = "content"
    FRUSTRATED = "frustrated"
    OVERWHELMED = "overwhelmed"
    CALM = "calm"
    MOTIVATED = "motivated"
    BORED = "bored"
    CURIOUS = "curious"

# Journal Entry Model
from sqlalchemy import Column, String, DateTime, Text, Enum as SqlEnum

# Journal Entry Table
class JournalEntryModel(Base):
    __tablename__ = "journal_entries"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String(36), index=True, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    mood = Column(SqlEnum(Mood), nullable=False)
    tags = Column(Text)  # Comma-separated tags
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create the tables in the database
Base.metadata.create_all(bind=engine)