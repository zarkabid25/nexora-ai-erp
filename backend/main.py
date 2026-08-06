from python_basics import calculate_profit
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "name": "Nexora Ai ERP",
            "version": "1.0.0",
            "status": "running"
        }
    }

@app.get("/health")
def health() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "status": "Healthy"
        }
    }

@app.get("/version")
def version() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "version": "1.0.0"
        }
    }

@app.get("/company")
def company() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "name": "Nexora Ai ERP",
            "company": "Nexora Ai",
            "product": "ERP"
        }
    }

@app.get("/stats")
def stats() -> dict[str, bool | dict[str, int | float]]:
    revenue = 250000
    expenses = 150000

    return {
        "success": True,
        "data": {
            "customers": 15,
            "employees": 8,
            "projects": 5,
            "revenue": revenue,
            "expenses": expenses,
            "profit": calculate_profit(revenue, expenses)
        }
    }