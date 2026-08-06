from pydantic import BaseModel

class CompanyData(BaseModel):
    name: str
    company: str
    product: str

class CompanyResponse(BaseModel):
    success: bool
    data: CompanyData