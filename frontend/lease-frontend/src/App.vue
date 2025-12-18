<template>
  <div id="app">
    <!-- Navigation Bar -->
    <nav class="navbar">
      <ul class="nav-links">
        <li><router-link to="/" exact>Dashboard</router-link></li>
        <li><router-link to="/create">Create Lease</router-link></li>
        <li><router-link to="/logs">Transaction Logs</router-link></li>
        <li><router-link to="/leases">Lease Table</router-link></li>
      </ul>
    </nav>

    <!-- Main content area -->
    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.navbar {
  background-color: #2c3e50;
  padding: 10px 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: #ecf0f1;
  text-decoration: none;
  font-weight: bold;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nav-links a:hover {
  background-color: #34495e;
}

.nav-links a.router-link-exact-active {
  text-decoration: underline;
  background-color: #1abc9c;
  color: white;
}

.main-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>


