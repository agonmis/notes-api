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
- POST /notes
- GET /notes
- GET /notes/{id}
- PUT /notes/{id}
- DELETE /notes/{id}