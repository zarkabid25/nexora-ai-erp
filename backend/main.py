
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Nexora AI ERP",
    version="1.0.0",
    description="AI Native ERP"
)


app.include_router(router)