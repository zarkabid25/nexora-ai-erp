from app.core.config import APP_NAME
def get_company() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "name": APP_NAME,
            "company": "Nexora AI",
            "product": "ERP"
        }
    }