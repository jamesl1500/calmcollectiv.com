from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from uuid import UUID, uuid4
from .schemas import JournalEntryCreate, JournalEntry
from database import Base, engine, SessionLocal

app = FastAPI(title="Journal Service")

# Models
from .models import JournalEntryModel, Mood

# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Saving journal entries in memory for simplicity
journal_entries = {}

@app.post("/journals/", response_model=JournalEntry, status_code=status.HTTP_201_CREATED)
async def create_journal_entry(entry: JournalEntryCreate, db: Session = Depends(get_db)):
    entry_id = uuid4()
    current_time = datetime.now()
    journal_entry = JournalEntry(
        id=entry_id,
        created_at=current_time,
        updated_at=current_time,
        **entry.dict()
    )
    journal_entries[entry_id] = journal_entry
    return journal_entry

@app.get("/journals/", response_model=List[JournalEntry])
async def list_journal_entries(db: Session = Depends(get_db)):
    return db.query(JournalEntryModel).all()

@app.get("/journals/{entry_id}", response_model=JournalEntry)
async def get_journal_entry(entry_id: UUID, db: Session = Depends(get_db)):
    entry = db.query(JournalEntryModel).filter(JournalEntryModel.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return entry

@app.put("/journals/{entry_id}", response_model=JournalEntry)
async def update_journal_entry(entry_id: UUID, entry: JournalEntryCreate, db: Session = Depends(get_db)):
    current_entry = db.query(JournalEntryModel).filter(JournalEntryModel.id == entry_id).first()
    if not current_entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")

    for key, value in entry.dict().items():
        setattr(current_entry, key, value)
    db.commit()
    db.refresh(current_entry)
    return current_entry

@app.delete("/journals/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_entry(entry_id: UUID, db: Session = Depends(get_db)):
    current_entry = db.query(JournalEntryModel).filter(JournalEntryModel.id == entry_id).first()
    if not current_entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")

    db.delete(current_entry)
    db.commit()
