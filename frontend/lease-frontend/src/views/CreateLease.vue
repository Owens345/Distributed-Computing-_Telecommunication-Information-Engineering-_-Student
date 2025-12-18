<template>
  <div class="create-lease-container">
    <h1>Create Lease</h1>
    <form @submit.prevent="submitLease" class="lease-form">
      <input v-model="tenant_name" placeholder="Tenant Name" required />
      <input v-model="property_name" placeholder="Property Name" required />
      <input v-model="amount" type="number" placeholder="Amount" required />
      <button type="submit">Create Lease</button>
    </form>
    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<script>
import { ref } from 'vue'
import { createLease } from '../api'

export default {
  setup() {
    const tenant_name = ref('')
    const property_name = ref('')
    const amount = ref(0)
    const message = ref('')

    async function submitLease() {
      try {
        const response = await createLease({
          tenant_name: tenant_name.value,
          property_name: property_name.value,
          amount: amount.value
        })
        message.value = response.data.status
      } catch (err) {
        message.value = err.response?.data?.detail || 'Transaction failed'
      }
    }

    return { tenant_name, property_name, amount, message, submitLease }
  }
}
</script>

<style scoped>
.create-lease-container {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  font-family: Arial, sans-serif;
}

.create-lease-container h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.lease-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.lease-form input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.lease-form button {
  padding: 10px;
  background-color: #2c3e50;
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.lease-form button:hover {
  background-color: #1a252f;
}

.message {
  margin-top: 15px;
  text-align: center;
  color: #e74c3c; /* red for error messages */
}
</style>

