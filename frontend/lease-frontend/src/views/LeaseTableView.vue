<template>
  <div class="dashboard-container">
    <h1>Lease Table</h1>
    <LeaseTable :leases="leases" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import LeaseTable from './LeaseTable.vue'
import { getLeases } from '../api/index.js'

export default {
  name: "LeaseTableView",
  components: { LeaseTable },
  setup() {
    const leases = ref([])

    async function loadLeases() {
      try {
        const response = await getLeases()
        leases.value = response.data
        console.log("Loaded leases:", leases.value)
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
  padding: 20px;
  background: #fafafa;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style>
