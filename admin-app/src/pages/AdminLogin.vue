<template>
  <section class="login-wrapper">
    <div class="login-glow"></div>
    <section class="card login login-futuristic">
      <div class="login-accent"></div>
      <h2 class="login-title">Admin - Connexion</h2>
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
          <span class="btn-text">{{ loading ? "Connexion..." : "Se connecter" }}</span>
        </button>
        <p v-if="authStore.loginError" class="error">{{ authStore.loginError }}</p>
      </form>
    </section>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const authStore = useAuthStore();
const username = ref("");
const password = ref("");
const loading = ref(false);

const handleLogin = async () => {
  loading.value = true;
  const success = await authStore.login(username.value, password.value);
  loading.value = false;
  if (success) {
    router.push({ name: "admin-dashboard" });
  }
};
</script>

<style scoped>
.login-wrapper {
  position: relative;
  min-height: 80vh;
  display: grid;
  place-items: center;
  padding: 24px;
}

.login-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120%;
  height: 120%;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.12) 0%, transparent 60%);
  pointer-events: none;
  animation: login-glow-pulse 6s ease-in-out infinite;
}

@keyframes login-glow-pulse {
  0%, 100% { opacity: 0.6; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 1; transform: translate(-50%, -50%) scale(1.05); }
}

.login {
  max-width: 440px;
  width: 100%;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
  animation: login-card-in 0.6s cubic-bezier(0.22, 1, 0.36, 1);
}

@keyframes login-card-in {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-accent {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #60a5fa, #38bdf8);
  animation: accent-shine 3s ease-in-out infinite;
}

@keyframes accent-shine {
  0%, 100% { opacity: 0.9; }
  50% { opacity: 1; }
}

.login-title {
  margin: 0 0 24px;
  font-size: 24px;
  font-weight: 700;
  background: linear-gradient(135deg, #e2e8f0, #93c5fd);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.form {
  display: grid;
  gap: 20px;
}

.input-label {
  display: block;
}

.input-label input {
  width: 100%;
  margin-top: 8px;
  padding: 12px 16px;
  border-radius: 12px;
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
