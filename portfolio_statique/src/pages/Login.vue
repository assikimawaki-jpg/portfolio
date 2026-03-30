<template>
  <section class="login-section">
    <div class="login-glow"></div>
    <section class="card login-card">
      <div class="login-accent"></div>
      <h2 class="login-title">Version statique</h2>
      <p class="login-desc">
        Ce portfolio est une version statique sans backend. L'administration n'est pas disponible.
        Pour la version complète avec tableau de bord, utilisez le projet principal.
      </p>
      <RouterLink to="/" class="button login-btn">Retour à l'accueil</RouterLink>
    </section>
  </section>
</template>

<script setup>
import { RouterLink } from "vue-router";
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
  line-height: 1.6;
}

.login-btn {
  display: inline-block;
  margin-top: 8px;
  padding: 14px 24px;
  font-size: 16px;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
}
</style>
