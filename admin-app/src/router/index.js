import { createRouter, createWebHistory } from "vue-router";
import AdminDashboard from "../pages/AdminDashboard.vue";
import AdminLogin from "../pages/AdminLogin.vue";
import { useAuthStore } from "../stores/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/admin-login" },
    { path: "/admin-login", name: "admin-login", component: AdminLogin },
    {
      path: "/admin-dashboard",
      name: "admin-dashboard",
      component: AdminDashboard,
      meta: { requiresAuth: true },
    },
  ],
});

router.beforeEach((to) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return { name: "admin-login" };
  }
  return true;
});

export default router;
