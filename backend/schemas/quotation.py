from pydantic import BaseModel
from typing import List, Optional

class QuotationCreate(BaseModel):
    eut_name: str
    state: str
    city: str
    selected_labs: List[str]
    testing_requirements: Optional[str] = None
    testing_standards: Optional[str] = None

class QuotationResponse(BaseModel):
    quotation_id: int
    estimated_time: str
    estimated_price: int
    status: str
