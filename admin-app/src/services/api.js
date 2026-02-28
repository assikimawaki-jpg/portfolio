import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/api/",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const refreshToken = localStorage.getItem("refresh_token");
    const originalRequest = error.config || {};
    if (
      error.response?.status === 401 &&
      refreshToken &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;
      try {
        const response = await axios.post(
          `${api.defaults.baseURL}token/refresh/`,
          { refresh: refreshToken }
        );
        localStorage.setItem("access_token", response.data.access);
        originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
        return api(originalRequest);
      } catch (refreshError) {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export default api;
