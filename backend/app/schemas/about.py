from pydantic import BaseModel

class AboutData(BaseModel):
    application: str
    version: str
    environment: str
    developer: str

class AboutResponse(BaseModel):
    success: bool
    data: AboutData