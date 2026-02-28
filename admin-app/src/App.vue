<template>
  <div class="admin-shell">
    <div class="admin-bg-grid" aria-hidden="true"></div>
    <div class="admin-bg-glow" aria-hidden="true"></div>
    <div class="admin-content">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
</script>

<style scoped>
.admin-shell {
  min-height: 100vh;
  padding: 24px 0 60px;
  position: relative;
  overflow-x: hidden;
}

.admin-bg-grid {
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(59, 130, 246, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59, 130, 246, 0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
  z-index: 0;
}

.admin-bg-glow {
  position: fixed;
  top: -30%;
  right: -20%;
  width: 60%;
  height: 80%;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
  animation: admin-glow-drift 12s ease-in-out infinite;
}

.admin-content {
  position: relative;
  z-index: 1;
}

@keyframes admin-glow-drift {
  0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.6; }
  50% { transform: translate(-5%, -10%) scale(1.1); opacity: 1; }
}
</style>
