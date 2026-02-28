import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import About from "../pages/About.vue";
import Skills from "../pages/Skills.vue";
import Contact from "../pages/Contact.vue";


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: Home },
    { path: "/a-propos", name: "about", component: About },
    { path: "/competences", name: "skills", component: Skills },
    { path: "/contact", name: "contact", component: Contact },
  ],
});

export default router;
