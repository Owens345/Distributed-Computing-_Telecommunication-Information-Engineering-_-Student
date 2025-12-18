<template>
  <div class="dashboard-container">
    <h1>Lease Dashboard</h1>
    <LeaseTable :leases="leases" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import LeaseTable from './LeaseTable.vue'
import { getLeases } from '../api/index.js'

export default {
  name: "Dashboard",
  components: { LeaseTable },
  setup() {
    const leases = ref([])

    async function loadLeases() {
  try {
    const response = await getLeases()
    console.log(response.data)  // <--- Check lease_id here
    leases.value = response.data
  } catch (err) {
    console.error("Failed to load leases:", err)
  }
}

    onMounted(loadLeases)

    return { leases }
  }
}
</script>

<style scoped>
.dashboard-container {
  max-width: 900px;
  margin: 40px auto;
  padding: 25px;
  background-color: #fafafa;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.dashboard-container h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}
</style>


