from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from backend.core.database import Base

class QuotationRequest(Base):
    __tablename__ = "quotation_requests"

    id = Column(Integer, primary_key=True, index=True)

    eut_name = Column(String(255), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)

    selected_labs = Column(JSON, nullable=False)

    testing_requirements = Column(Text, nullable=True)
    testing_standards = Column(Text, nullable=True)

    estimated_time = Column(String(50), nullable=False)
    estimated_price = Column(Integer, nullable=False)

    status = Column(String(50), default="created", nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
