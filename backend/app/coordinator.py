from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import uuid
import threading

app = FastAPI(title="Distributed Lease Coordinator")

# ------------------ GLOBAL TRANSACTION LOCK ------------------
transaction_lock = threading.Lock()

# ------------------ CORS ------------------
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ------------------ Node URLs ------------------
NODES = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    "http://127.0.0.1:8003"
]

# ------------------ In-memory storage ------------------
LEASES = []
TRANSACTION_LOGS = []

# ------------------ Models ------------------
class LeaseRequest(BaseModel):
    tenant_name: str
    property_name: str
    amount: float

# ------------------ Endpoints ------------------
@app.post("/create_lease")
def create_lease(req: LeaseRequest):
    # 🔒 SERIALIZE ALL TRANSACTIONS
    with transaction_lock:

        transaction_id = str(uuid.uuid4())
        lease_id = str(uuid.uuid4())  # SINGLE SOURCE OF TRUTH
        lease_data = req.dict()

        prepare_responses = []

        # -------- PHASE 1: PREPARE --------
        for node in NODES:
            try:
                resp = requests.post(
                    f"{node}/prepare",
                    json={
                        "transaction_id": transaction_id,
                        "lease_id": lease_id,
                        "lease_data": lease_data,
                        "operation": "CREATE"
                    },
                    timeout=5
                )
                prepare_responses.append(resp.json())
            except requests.RequestException:
                prepare_responses.append({"status": "FAILED"})

        # -------- DECISION --------
        if all(r.get("status") == "PREPARED" for r in prepare_responses):

            # -------- PHASE 2: COMMIT --------
            for node in NODES:
                try:
                    requests.post(
                        f"{node}/commit",
                        params={"transaction_id": transaction_id},
                        timeout=5
                    )
                except requests.RequestException:
                    pass

                TRANSACTION_LOGS.append({
                    "transaction_id": transaction_id,
                    "node_id": node,
                    "lease_id": lease_id,
                    "operation": "CREATE",
                    "status": "COMMITTED"
                })

            LEASES.append({
                "lease_id": lease_id,
                **lease_data,
                "status": "COMMITTED"
            })

            return {
                "status": "COMMITTED",
                "transaction_id": transaction_id,
                "lease_id": lease_id
            }

        # -------- PHASE 2: ROLLBACK --------
        for node in NODES:
            try:
                requests.post(
                    f"{node}/rollback",
                    params={"transaction_id": transaction_id},
                    timeout=5
                )
            except requests.RequestException:
                pass

            TRANSACTION_LOGS.append({
                "transaction_id": transaction_id,
                "node_id": node,
                "lease_id": lease_id,
                "operation": "CREATE",
                "status": "ROLLED_BACK"
            })

        raise HTTPException(
            status_code=500,
            detail="Transaction rolled back due to node failure"
        )

# ------------------ Get all leases ------------------
@app.get("/leases")
def get_leases():
    return LEASES

# ------------------ Get all transaction logs ------------------
@app.get("/transaction_logs")
def get_transaction_logs():
    return TRANSACTION_LOGS

@app.get("/")
def root():
    return {"status": "Coordinator running"}
