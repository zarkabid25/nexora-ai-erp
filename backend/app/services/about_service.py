from app.core.config import APP_NAME, APP_VERSION, ENVIRONMENT
def get_about() -> dict[str, bool | dict[str, str]]:
    return {
        "success": True,
        "data": {
            "application": APP_NAME,
            "version": APP_VERSION,
            "environment": ENVIRONMENT,
            "developer": "Zark Abid"
        }
    }