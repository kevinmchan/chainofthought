import { createWebHistory, createRouter } from "vue-router";
import Layout from "@/layouts/Layout.vue";
import Home from "@/views/Home.vue";
import Thoughts from "@/views/Thoughts.vue";

const routes = [
  {
    path: "/",
    component: Layout,
    children: [
      { path: "", name: "Home", component: Home },
      { path: "thoughts", name: "Thoughts", component: Thoughts},
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;