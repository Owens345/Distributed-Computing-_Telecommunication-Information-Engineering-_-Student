<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Tenant</th>
          <th>Property</th>
          <th>Amount</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="lease in leases" :key="lease.lease_id">
          <td>{{ lease.lease_id ?? '-' }}</td>
          <td>{{ lease.tenant_name ?? '-' }}</td>
          <td>{{ lease.property_name ?? '-' }}</td>
          <td>{{ lease.amount ?? '-' }}</td>
          <td>{{ lease.status ?? 'ACTIVE' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "LeaseTable",
  props: {
    leases: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

h2 {
  font-family: Arial, sans-serif;
  color: #2c3e50;
  margin-bottom: 10px;
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
</style>


