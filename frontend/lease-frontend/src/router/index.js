import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import CreateLease from '../views/CreateLease.vue'
import TransactionLogs from '../views/TransactionLogs.vue'
import LeaseTableView from '../views/LeaseTableView.vue'

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/create', name: 'CreateLease', component: CreateLease },
  { path: '/logs', name: 'TransactionLogs', component: TransactionLogs },
  { path: '/leases', name: 'LeaseTable', component: LeaseTableView }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
