# Virtuelle Umgebung einrichten
```bash
python -m venv venv
venv/Scripts/activate
```

# Programme installieren
```bash
pip install -r requirements.txt
```

# Server starten
```bash
uvicorn main:app --reload
```

# Endpoints
- create note
- read notes
- read note
- update note
- delete note