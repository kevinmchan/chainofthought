<template>
  <div class="layout">
    <nav class="navbar">
      <div class="logo-container">
        <div class="logo">chainofthought</div>
      </div>
      <div class="links">
        <router-link to="/" class="nav-link">Orientation</router-link>
        <router-link to="/progress" class="nav-link">Progress</router-link>
        <router-link to="/actions" class="nav-link">Actions</router-link>
        <router-link to="/thoughts" class="nav-link">Thoughts</router-link>
        <router-link to="/analysis" class="nav-link">Analysis</router-link>
      </div>
    </nav>
    <router-view class="view"/>
  </div>
</template>

<style scoped>
.view {
  height: 100%;
  margin: 1em 0;
}

.layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
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