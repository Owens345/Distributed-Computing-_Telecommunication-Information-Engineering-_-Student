# main.py
import os
from fastapi import FastAPI

# Decide role via environment variable
ROLE = os.environ.get("ROLE", "COORDINATOR")  # "NODE" or "COORDINATOR"

if ROLE == "COORDINATOR":
    from app.coordinator import app as app
else:
    from app.node import app as app

