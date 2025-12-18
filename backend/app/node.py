from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import threading
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Lease, TransactionLog, TransactionStatus

app = FastAPI(title="Distributed Lease Node")

NODE_ID = os.environ.get("NODE_ID", "NODE1")

# ------------------ Concurrency Control ------------------
transaction_lock = threading.Lock()  # ensures one transaction at a time

class PrepareRequest(BaseModel):
    transaction_id: str
    lease_data: dict
    operation: str  # CREATE, UPDATE

# ------------------ Endpoints ------------------
@app.post("/prepare")
def prepare(req: PrepareRequest):
    with transaction_lock:
        with SessionLocal() as db:
            try:
                lease = None
                if req.operation == "CREATE":
                    lease = Lease(**req.lease_data)
                    db.add(lease)
                    db.flush()  # Ensures lease_id is recorded

                log = TransactionLog(
                    transaction_id=req.transaction_id,
                    node_id=NODE_ID,
                    lease_id=lease.lease_id if lease else None,
                    operation=req.operation,
                    status=TransactionStatus.PREPARED
                )
                db.add(log)
                db.commit()
                return {"status": "PREPARED", "lease_id": lease.lease_id if lease else None}
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=500, detail=str(e))

@app.post("/commit")
def commit(transaction_id: str):
    with transaction_lock:
        with SessionLocal() as db:
            try:
                logs = db.query(TransactionLog).filter(TransactionLog.transaction_id == transaction_id).all()
                for log in logs:
                    log.status = TransactionStatus.COMMITTED
                db.commit()
                return {"status": "COMMITTED"}
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=500, detail=str(e))

@app.post("/rollback")
def rollback(transaction_id: str):
    with transaction_lock:
        with SessionLocal() as db:
            try:
                logs = db.query(TransactionLog).filter(TransactionLog.transaction_id == transaction_id).all()
                for log in logs:
                    log.status = TransactionStatus.ROLLED_BACK
                    if log.operation == "CREATE" and log.lease_id:
                        lease = db.query(Lease).filter(Lease.lease_id == log.lease_id).first()
                        if lease:
                            db.delete(lease)
                db.commit()
                return {"status": "ROLLED_BACK"}
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=500, detail=str(e))

@app.get("/leases")
def get_leases():
    with SessionLocal() as db:
        leases = db.query(Lease).all()
        return [
            {
                "lease_id": lease.lease_id,
                "tenant_name": lease.tenant_name,
                "property_name": lease.property_name,
                "amount": lease.amount,
                "status": lease.status.value if lease.status else "ACTIVE"
            }
            for lease in leases
        ]

@app.get("/transaction_logs")
def get_transaction_logs():
    with SessionLocal() as db:
        logs = db.query(TransactionLog).all()
        return [
            {
                "transaction_id": log.transaction_id,
                "node_id": log.node_id,
                "lease_id": log.lease_id,
                "operation": log.operation,
                "status": log.status.value
            }
            for log in logs
        ]

