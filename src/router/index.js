import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Main",
    component: () => import("../views/main.vue"),
  },
  {
    path: "/chat",
    name: "Chat",
    component: () => import("../views/chat.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
