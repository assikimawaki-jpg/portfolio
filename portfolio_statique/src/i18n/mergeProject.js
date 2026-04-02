import { PROJECT_EN_BY_ID } from "./projectEn.js";

export function mergeProjectLocale(p, locale) {
  if (locale !== "en") return p;
  const ov = PROJECT_EN_BY_ID[p.id];
  if (!ov) return p;
  return { ...p, ...ov };
}
