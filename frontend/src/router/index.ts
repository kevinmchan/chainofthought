import { createWebHistory, createRouter } from "vue-router";
import Layout from "@/layouts/Layout.vue";
import Home from "@/views/Home.vue";
import Notes from "@/views/Notes.vue";

const routes = [
  {
    path: "/",
    component: Layout,
    children: [
      { path: "", name: "Home", component: Home },
      { path: "notes", name: "Notes", component: Notes},
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;