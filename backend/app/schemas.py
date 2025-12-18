# schemas.py
from pydantic import BaseModel
from typing import Optional
from models import LeaseStatus

class LeaseCreate(BaseModel):
    tenant_name: str
    property_name: str
    amount: float

class LeaseResponse(BaseModel):
    lease_id: int
    tenant_name: str
    property_name: str
    amount: float
    status: LeaseStatus

    class Config:
        orm_mode = True

class TransactionLogResponse(BaseModel):
    transaction_id: str
    node_id: str
    lease_id: Optional[int]
    operation: str
    status: str
