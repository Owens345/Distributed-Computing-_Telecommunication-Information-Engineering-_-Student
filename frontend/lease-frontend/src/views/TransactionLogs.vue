<template>
  <div class="table-container">
    <h1>Transaction Logs</h1>
    <table>
      <thead>
        <tr>
          <th>Transaction ID</th>
          <th>Node ID</th>
          <th>Lease ID</th>
          <th>Operation</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="log in logs" :key="log.transaction_id + log.node_id">
          <td>{{ log.transaction_id || 'N/A' }}</td>
          <td>{{ log.node_id || 'N/A' }}</td>
          <td>{{ log.lease_id ?? '-' }}</td>
          <td>{{ log.operation || '-' }}</td>
          <td>{{ log.status || '-' }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="logs.length === 0" class="no-logs">No transaction logs found.</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getTransactionLogs } from '../api/index.js'

export default {
  name: "TransactionLogs",
  setup() {
    const logs = ref([])

    const loadLogs = async () => {
      try {
        const response = await getTransactionLogs()
        logs.value = response.data.map(log => ({
          transaction_id: log.transaction_id,
          node_id: log.node_id,
          lease_id: log.lease_id,
          operation: log.operation,
          status: log.status
        }))
      } catch (err) {
        console.error("Failed to load transaction logs:", err)
      }
    }

    onMounted(loadLogs)

    return { logs }
  }
}
</script>

<style scoped>
.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

h1 {
  font-family: Arial, sans-serif;
  margin-bottom: 10px;
  color: #2c3e50;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

th, td {
  padding: 12px 15px;
  border: 1px solid #ddd;
  text-align: left;
}

thead {
  background-color: #2c3e50;
  color: white;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #f1f1f1;
}

.no-logs {
  margin-top: 10px;
  color: #888;
  font-style: italic;
}
</style>


