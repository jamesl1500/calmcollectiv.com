from fastapi import FastAPI, HTTPException, status
from typing import List
from datetime import datetime
from uuid import UUID, uuid4

app = FastAPI(title="Journal Service")

# Models
from backend.services.journal.src.models import JournalEntry, JournalEntryCreate

# In-memory storage
journal_entries = {
    UUID('12345678-1234-5678-1234-567812345678'): JournalEntry(
        id=UUID('12345678-1234-5678-1234-567812345678'),
        title="First Journal Entry",
        content="This is my first journal entry content.",
        mood="happy",
        tags=["first", "happy"],
        created_at=datetime(2025, 9, 15, 10, 0),
        updated_at=datetime(2025, 9, 15, 10, 0)
    ),
    UUID('87654321-4321-8765-4321-876543210987'): JournalEntry(
        id=UUID('87654321-4321-8765-4321-876543210987'),
        title="Second Journal Entry",
        content="This is my second journal entry content.",
        mood="relaxed",
        tags=["second", "relaxed"],
        created_at=datetime(2025, 9, 15, 11, 0),
        updated_at=datetime(2025, 9, 15, 11, 0)
    )
}

@app.post("/journals/", response_model=JournalEntry, status_code=status.HTTP_201_CREATED)
async def create_journal_entry(entry: JournalEntryCreate):
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
async def list_journal_entries():
    return list(journal_entries.values())

@app.get("/journals/{entry_id}", response_model=JournalEntry)
async def get_journal_entry(entry_id: UUID):
    if entry_id not in journal_entries:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return journal_entries[entry_id]

@app.put("/journals/{entry_id}", response_model=JournalEntry)
async def update_journal_entry(entry_id: UUID, entry: JournalEntryCreate):
    if entry_id not in journal_entries:
        raise HTTPException(status_code=404, detail="Journal entry not found")

    current_entry = journal_entries[entry_id]
    updated_entry = JournalEntry(
        id=entry_id,
        created_at=current_entry.created_at,
        updated_at=datetime.now(),
        **entry.dict()
    )
    journal_entries[entry_id] = updated_entry
    return updated_entry

@app.delete("/journals/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_entry(entry_id: UUID):
    if entry_id not in journal_entries:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    del journal_entries[entry_id]
