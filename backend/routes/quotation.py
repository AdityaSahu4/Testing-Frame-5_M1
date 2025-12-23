from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas.quotation import QuotationCreate, QuotationResponse
from backend.models.quotation import QuotationRequest
from backend.core.database import SessionLocal

router = APIRouter(
    prefix="/api/quotation",
    tags=["Quotation"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=QuotationResponse)
def create_quotation(
    payload: QuotationCreate,
    db: Session = Depends(get_db)
):
    if not payload.selected_labs:
        raise HTTPException(
            status_code=400,
            detail="At least one lab must be selected"
        )

    quotation = QuotationRequest(
        eut_name=payload.eut_name,
        state=payload.state,
        city=payload.city,
        selected_labs=payload.selected_labs,
        testing_requirements=payload.testing_requirements,
        testing_standards=payload.testing_standards,
        estimated_time="24–48 hrs",
        estimated_price=400
    )

    db.add(quotation)
    db.commit()
    db.refresh(quotation)

    return {
        "quotation_id": quotation.id,
        "estimated_time": quotation.estimated_time,
        "estimated_price": quotation.estimated_price,
        "status": quotation.status
    }
