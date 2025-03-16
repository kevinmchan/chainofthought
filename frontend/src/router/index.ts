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
      { path: "actions", name: "Actions", component: Home},
      { path: "progress", name: "Progress", component: Home},
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;