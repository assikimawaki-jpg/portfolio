import { defineStore } from "pinia";
import api from "../services/api";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    accessToken: localStorage.getItem("access_token") || "",
    refreshToken: localStorage.getItem("refresh_token") || "",
    loginError: "",
  }),
  getters: {
    isAuthenticated: (state) => Boolean(state.accessToken),
  },
  actions: {
    async login(username, password) {
      this.loginError = "";
      try {
        const response = await api.post("token/", { username, password });
        this.accessToken = response.data.access;
        this.refreshToken = response.data.refresh;
        localStorage.setItem("access_token", this.accessToken);
        localStorage.setItem("refresh_token", this.refreshToken);
        return true;
      } catch (error) {
        this.loginError = "Identifiants invalides.";
        return false;
      }
    },
    logout() {
      this.accessToken = "";
      this.refreshToken = "";
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
    },
  },
});
