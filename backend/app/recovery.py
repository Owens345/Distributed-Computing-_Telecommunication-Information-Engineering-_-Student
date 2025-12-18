# recovery.py
from database import get_db
from models import TransactionLog, TransactionStatus
from sqlalchemy.orm import Session

def recover_node(node_id: str):
    db: Session = next(get_db())
    pending_logs = db.query(TransactionLog).filter(
        TransactionLog.node_id == node_id,
        TransactionLog.status == TransactionStatus.PREPARED
    ).all()
    
    for log in pending_logs:
        # Rollback any prepared transactions
        log.status = TransactionStatus.ROLLED_BACK
        # Remove leases if CREATE operation
        if log.operation == "CREATE" and log.lease_id:
            lease = db.query(Lease).filter_by(lease_id=log.lease_id).first()
            if lease:
                db.delete(lease)
    db.commit()
