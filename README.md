# Nexora AI ERP

Nexora AI ERP is a simple backend service built with FastAPI to support enterprise resource planning operations. It provides a basic API for health checks, version information, and company metadata.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv

## Folder Structure

- [backend](backend/) - Backend application source code and dependencies
  - [backend/main.py](backend/main.py) - FastAPI application entrypoint
  - [backend/requirements.txt](backend/requirements.txt) - Python dependencies for the backend
  - [backend/app](backend/app/) - Backend application package
  - [backend/tests](backend/tests/) - Backend tests
- [frontend](frontend/) - Frontend application code
- [docs](docs/) - Project documentation

## How to run the backend

1. Create and activate a Python virtual environment inside the backend folder:

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Open the API documentation in your browser:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Notes

- Daily learning notes are stored in [docs/day2-notes.md](docs/day2-notes.md).
