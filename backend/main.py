from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "name": "Nexora Ai ERP",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

@app.get("/company")
def company():
    return {
        "name": "Nexora Ai ERP",
        "company": "Nexora Ai",
        "product": "ERP"
    }