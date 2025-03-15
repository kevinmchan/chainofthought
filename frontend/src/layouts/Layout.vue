<template>
  <div class="layout">
    <nav class="navbar">
      <div class="logo-container">
        <div class="logo">chainofthought</div>
      </div>
      <div class="links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/notes" class="nav-link">Notes</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-link {
  margin: 0.5em;
  color: grey;
  text-decoration: none;
}

.nav-link.router-link-exact-active {
  font-weight: bold;
}

.logo {
  font-size: 1.5em;
  font-weight: 100;
}
</style>