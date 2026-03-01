<template>
  <section class="login-section">
    <div class="login-glow"></div>
    <section class="card login-card">
      <div class="login-accent"></div>
      <h2 class="login-title">Connexion Admin</h2>
      <p class="login-desc">Accédez au tableau de bord pour gérer votre portfolio.</p>
      <form class="form" @submit.prevent="handleLogin">
        <label class="input-label">
          Nom d'utilisateur
          <input v-model="username" type="text" required placeholder="Entrez votre identifiant" />
        </label>
        <label class="input-label">
          Mot de passe
          <input v-model="password" type="password" required placeholder="••••••••" />
        </label>
        <button class="button login-btn" type="submit" :disabled="loading">
          {{ loading ? "Connexion..." : "Se connecter" }}
        </button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>
    </section>
  </section>
</template>

<script setup>
import { ref, computed } from "vue";
import api from "../services/api";

const username = ref("");
const password = ref("");
const loading = ref(false);
const error = ref("");

const adminDashboardUrl = computed(() => {
  const base = import.meta.env.VITE_ADMIN_URL;
  if (base) return base.replace(/\/$/, "") + "/admin-dashboard";
  if (import.meta.env.DEV) return "http://localhost:5174/admin-dashboard";
  return window.location.origin + "/admin-dashboard";
});

const handleLogin = async () => {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.post("token/", { username: username.value, password: password.value });
    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);
    window.location.href = adminDashboardUrl.value;
  } catch (err) {
    if (err.code === "ERR_NETWORK" || err.message?.includes("Network Error")) {
      error.value = "Impossible de joindre l'API. Vérifiez que le backend est déployé et que VITE_API_URL est configuré sur Vercel.";
    } else if (err.response?.status === 401) {
      error.value = "Identifiants invalides.";
    } else if (err.response?.status === 404) {
      error.value = "API non trouvée. Vérifiez l'URL du backend (VITE_API_URL).";
    } else {
      error.value = err.response?.data?.detail || "Erreur de connexion. Vérifiez la configuration.";
    }
    loading.value = false;
  }
};
</script>

<style scoped>
.login-section {
  position: relative;
  min-height: 60vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
}

.login-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120%;
  height: 120%;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.1) 0%, transparent 60%);
  pointer-events: none;
}

.login-card {
  max-width: 420px;
  width: 100%;
  position: relative;
  overflow: hidden;
  padding: 32px;
  background: linear-gradient(160deg, rgba(15, 23, 42, 0.95), rgba(2, 6, 23, 0.98));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.login-accent {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #60a5fa, #38bdf8);
}

.login-title {
  margin: 0 0 8px;
  font-size: 24px;
  font-weight: 700;
  color: #e2e8f0;
}

.login-desc {
  margin: 0 0 24px;
  font-size: 14px;
  color: rgba(226, 232, 240, 0.7);
}

.form {
  display: grid;
  gap: 20px;
}

.input-label {
  display: block;
  color: rgba(226, 232, 240, 0.9);
  font-size: 14px;
  font-weight: 500;
}

.input-label input {
  width: 100%;
  margin-top: 8px;
  padding: 12px 16px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.25);
  background: rgba(15, 23, 42, 0.8);
  color: #e2e8f0;
  font-size: 15px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.input-label input::placeholder {
  color: rgba(148, 163, 184, 0.5);
}

.input-label input:focus {
  outline: none;
  border-color: rgba(59, 130, 246, 0.5);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}

.login-btn {
  margin-top: 8px;
  padding: 14px 24px;
  font-size: 16px;
  font-weight: 600;
}

.error {
  color: #f87171;
  font-size: 14px;
  margin: 0;
}
</style>
