from fastapi import APIRouter
from python_basics import calculate_profit
from app.schemas.company import CompanyResponse
from app.services.company_service import get_company
from app.services.about_service import get_about
from app.schemas.about import AboutResponse

router = APIRouter()

@router.get("/")
def root() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "name": "Nexora Ai ERP",
            "version": "1.0.0",
            "status": "running"
        }
    }

@router.get("/health")
def health() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "status": "Healthy"
        }
    }

@router.get("/version")
def version() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "version": "1.0.0"
        }
    }

@router.get("/company", response_model=CompanyResponse)
def company():
    return get_company()

@router.get("/about", response_model=AboutResponse)
def about():
    return get_about()

@router.get("/stats")
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