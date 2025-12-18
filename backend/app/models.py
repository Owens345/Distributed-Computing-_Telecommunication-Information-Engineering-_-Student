# models.py
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from app.database import Base

import enum

# Lease status enum
class LeaseStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Lease(Base):
    __tablename__ = "leases"

    lease_id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(String, nullable=False)
    property_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(LeaseStatus), default=LeaseStatus.ACTIVE)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Node transaction logs
class TransactionStatus(str, enum.Enum):
    PREPARED = "PREPARED"
    COMMITTED = "COMMITTED"
    ROLLED_BACK = "ROLLED_BACK"

class TransactionLog(Base):
    __tablename__ = "transaction_logs"

    log_id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, nullable=False)
    node_id = Column(String, nullable=False)
    lease_id = Column(Integer, ForeignKey("leases.lease_id"), nullable=True)
    operation = Column(String, nullable=False)  # e.g., CREATE, UPDATE
    status = Column(Enum(TransactionStatus), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
