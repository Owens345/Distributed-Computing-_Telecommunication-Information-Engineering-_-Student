import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const getLeases = async () => {
  return API.get("/leases");
};

export const createLease = async (leaseData) => {
  return API.post("/create_lease", leaseData);
};

export const getTransactionLogs = async () => {
  return API.get("/transaction_logs");
};

