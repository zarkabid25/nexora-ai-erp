# Nexora Ai ERP

Nexora Ai ERP is a simple backend service built with FastAPI to support enterprise resource planning operations. It provides a basic API for health checks, version information, and company metadata.

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Folder Structure

- `backend/` - Backend application source code and dependencies
  - `main.py` - FastAPI application entrypoint
  - `requirements.txt` - Python dependencies for the backend
  - `app/` - Backend application package (future expansion)
  - `tests/` - Backend tests
- `frontend/` - Frontend application code
- `docs/` - Project documentation

## How to run the backend

1. Create and activate a Python virtual environment in the `backend` folder:

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
pip install fastapi uvicorn
```

3. Start the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Open the API documentation in your browser:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`
