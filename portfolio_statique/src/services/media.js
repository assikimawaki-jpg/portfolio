export const resolveMediaUrl = (url) => {
  if (!url) return "";
  if (url.startsWith("http")) return url;
  const apiBase = import.meta.env.VITE_API_URL || "http://localhost:8000/api/";
  const mediaBase = apiBase.replace(/\/api\/?$/, "/");
  return `${mediaBase}${url.replace(/^\//, "")}`;
};
