import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import { i18n } from "./i18n";
import "./styles.css";

/** Favicon : chemin aligné sur import.meta.env.BASE_URL (évite une icône cassée avec base "./" ou sous-dossier) */
const faviconVersion = "5";
const base = import.meta.env.BASE_URL || "/";
const baseNorm = base.endsWith("/") ? base : `${base}/`;
const faviconHref = `${baseNorm}favicon.png?v=${faviconVersion}`.replace(/\/{2,}/g, "/");
document.querySelectorAll('link[rel="icon"], link[rel="shortcut icon"], link[rel="apple-touch-icon"]').forEach((el) => {
  el.setAttribute("href", faviconHref);
});

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.use(i18n);
app.mount("#app");
