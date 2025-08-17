from fastapi import FastAPI
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    content: str
    done: bool

class NoteUpdate(BaseModel):
    content: str

app = FastAPI()

notes = []

@app.post("/notes")
async def create_note(request: Note):
    notes.append({
        "title": request.title,
        "content": request.content,
        "done": False
    })

@app.get("/notes", response_model=list[Note])
async def read_notes():
    return notes

@app.get("/notes/{id}")
async def read_note(id: int):
    return notes[id-1]

@app.put("/notes/{id}")
async def update_note(id: int, request: NoteUpdate):
    notes[id-1]["content"] = request.content

@app.delete("/notes/{id}")
async def delete_note(id: int):
    notes.remove(notes[id-1])