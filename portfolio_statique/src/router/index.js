import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import About from "../pages/About.vue";
import Skills from "../pages/Skills.vue";
import Contact from "../pages/Contact.vue";
import Login from "../pages/Login.vue";
import Projects from "../pages/Projects.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(_to, _from, savedPosition) {
    if (savedPosition) return savedPosition;
    return { top: 0, left: 0 };
  },
  routes: [
    { path: "/", name: "home", component: Home },
    { path: "/a-propos", name: "about", component: About },
    { path: "/competences", name: "skills", component: Skills },
    { path: "/mes-projets", name: "projects", component: Projects },
    { path: "/contact", name: "contact", component: Contact },
    { path: "/connexion", name: "login", component: Login },
  ],
});

export default router;
