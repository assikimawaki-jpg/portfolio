import { createI18n } from "vue-i18n";
import fr from "./fr.js";
import en from "./en.js";

function getInitialLocale() {
  if (typeof localStorage === "undefined") return "fr";
  const s = localStorage.getItem("portfolio-locale");
  return s === "en" || s === "fr" ? s : "fr";
}

export const i18n = createI18n({
  legacy: false,
  locale: getInitialLocale(),
  fallbackLocale: "fr",
  messages: { fr, en },
});
