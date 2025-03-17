import { createWebHistory, createRouter } from "vue-router";
import Layout from "@/layouts/Layout.vue";
import Home from "@/views/Home.vue";
import Thoughts from "@/views/Thoughts.vue";
import Daily from "@/views/Daily.vue";
import Orientation from "@/views/Orientation.vue";

const routes = [
  {
    path: "/",
    component: Layout,
    children: [
      { path: "", name: "Orientation", component: Orientation },
      { path: "daily", name: "Daily", component: Daily},
      { path: "thoughts", name: "Thoughts", component: Thoughts},
      { path: "actions", name: "Actions", component: Home},
      { path: "progress", name: "Progress", component: Home},
      { path: "analysis", name: "Analysis", component: Home},
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;