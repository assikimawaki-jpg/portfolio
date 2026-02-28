<template>
  <section class="hero hero-shell">
    <div class="hero-grid">
      <div class="hero-info">
        <p class="hero-eyebrow animate-in">Bonjour, je suis</p>
        <h1 class="hero-title hero-brand-name animate-in" style="--delay: 0.05s">
          {{ displayedName }}
        </h1>
        <p class="hero-role animate-in" style="--delay: 0.1s">
          {{ profil?.titre_professionnel || "Designer UI/UX & Créateur web" }}
        </p>
        <p class="hero-tag animate-in" style="--delay: 0.15s">
          pour le web design et l'automatisation digitale
        </p>
        <p class="hero-copy animate-in" style="--delay: 0.2s">
          {{ profil?.bio || "Je conçois des expériences visuelles immersives et des interfaces modernes avec une touche futuriste." }}
        </p>
        <div class="hero-actions animate-in" style="--delay: 0.25s">
          <RouterLink class="button" to="/contact">Contactez-moi</RouterLink>
          <a
            v-if="profil?.cv"
            class="button secondary"
            :href="resolveMediaUrl(profil.cv)"
            target="_blank"
            rel="noopener noreferrer"
          >
            CV
          </a>
        </div>
        <div class="hero-socials animate-in" style="--delay: 0.3s">
          <a
            href="https://x.com/tony_kemzy?t=hdJksj-aYSVvpryViuC87Q"
            class="social-pill"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="X"
          >
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M5 4l7.2 8.5L6 20h3l5-5.4L18.8 20H21l-7.6-9L19.5 4h-3l-4.4 4.8L8 4H5z"
                fill="currentColor"
              />
            </svg>
          </a>
          <a
            href="https://www.linkedin.com/in/mawaki-assiki/"
            class="social-pill"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="LinkedIn"
          >
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"
                fill="currentColor"
              />
            </svg>
          </a>
          <a
            href="https://www.instagram.com/tony.assiki"
            class="social-pill"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Instagram"
          >
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M7 4h10a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3z"
                fill="none"
                stroke="currentColor"
                stroke-width="1.6"
              />
              <circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.6" />
              <circle cx="17.5" cy="6.5" r="1" fill="currentColor" />
            </svg>
          </a>
          <a
            href="https://wa.me/70546096"
            class="social-pill"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="WhatsApp"
          >
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.865 9.865 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"
                fill="currentColor"
              />
            </svg>
          </a>
          <a
            href="https://github.com/mawakitony"
            class="social-pill"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="GitHub"
          >
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.3-3.4-1.3-.5-1.1-1.1-1.4-1.1-1.4-.9-.6.1-.6.1-.6 1 .1 1.6 1 1.6 1 .9 1.6 2.4 1.1 3 .8.1-.7.4-1.1.7-1.4-2.2-.2-4.5-1.1-4.5-4.9 0-1.1.4-2 1-2.7-.1-.2-.4-1.2.1-2.5 0 0 .8-.3 2.7 1a9.3 9.3 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.3.2 2.3.1 2.5.6.7 1 1.6 1 2.7 0 3.8-2.3 4.7-4.5 4.9.4.3.8.9.8 1.9v2.8c0 .3.2.6.7.5A10 10 0 0 0 12 2z"
                fill="currentColor"
              />
            </svg>
          </a>
        </div>
      </div>
      <div class="hero-visual animate-in" style="--delay: 0.15s">
        <div class="ring"></div>
        <div class="ring ring-glow"></div>
        <div class="photo-frame">
          <img :src="heroImage" alt="Photo profil" />
        </div>
      </div>
    </div>
    <div class="hero-glow"></div>
  </section>

  <section class="services">
    <p class="hero-eyebrow">Mes services</p>
    <h2 class="glow-text">Ce que je fais</h2>
    <div class="grid three service-grid">
      <div class="card service-card step-service-1">
        <div class="service-step-badge">01</div>
        <div class="service-icon">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M4 6h16v8H4zM8 18h8"
              fill="none"
              stroke="currentColor"
              stroke-width="1.6"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
        <h3>Designer UI/UX</h3>
        <p class="muted">Design d'interfaces modernes et centrées utilisateur.</p>
        <RouterLink to="/competences" class="link">Voir plus</RouterLink>
      </div>
      <div class="card service-card step-service-2">
        <div class="service-step-badge">02</div>
        <div class="service-icon">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M4 20h16M7 17l5-10 5 10"
              fill="none"
              stroke="currentColor"
              stroke-width="1.6"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
        <h3>Graphisme</h3>
        <p class="muted">Identité visuelle, branding, et supports marketing.</p>
        <RouterLink to="/competences" class="link">Voir plus</RouterLink>
      </div>
      <div class="card service-card step-service-3">
        <div class="service-step-badge">03</div>
        <div class="service-icon">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M4 5h16v14H4zM4 9h16"
              fill="none"
              stroke="currentColor"
              stroke-width="1.6"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
        <h3>Web Design</h3>
        <p class="muted">Sites vitrines élégants et performants.</p>
        <RouterLink to="/competences" class="link">Voir plus</RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { RouterLink } from "vue-router";
import api from "../services/api";
import { resolveMediaUrl } from "../services/media";
import heroProfileImage from "../assets/hero-profile.png";

const profil = ref(null);
const heroImage = heroProfileImage;
const displayedName = computed(() => profil.value?.nom || "Assiki Mawaki");

const loadProfil = async () => {
  const response = await api.get("profil/");
  profil.value = response.data?.results?.[0] || response.data?.[0] || null;
};

onMounted(loadProfil);
</script>

<style scoped>
.hero-shell {
  position: relative;
  padding: 48px;
  width: 100%;
  border-radius: 20px;
  background: radial-gradient(ellipse 80% 60% at 70% 20%, rgba(59, 130, 246, 0.2), transparent 50%),
    radial-gradient(circle at top right, rgba(59, 130, 246, 0.12), transparent 45%),
    linear-gradient(160deg, rgba(15, 23, 42, 0.9), rgba(2, 6, 23, 0.98));
  border: 1px solid rgba(148, 163, 184, 0.18);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.hero-grid {
  display: grid;
  gap: 32px;
  align-items: center;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  position: relative;
  z-index: 2;
}

.animate-in {
  animation: fade-slide-in 0.6s ease-out forwards;
  animation-delay: var(--delay, 0s);
  opacity: 0;
}

@keyframes fade-slide-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-eyebrow {
  color: #93c5fd;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 2px;
  font-size: 12px;
}

.hero-title {
  font-family: var(--font-brand);
  font-size: clamp(32px, 5vw, 64px);
  letter-spacing: 8px;
  text-transform: capitalize;
  margin: 12px 0 2px;
  font-weight: 700;
}

.hero-brand-name {
  font-family: "Dream Avenue", serif;
  background: linear-gradient(
    120deg,
    #f8fafc 0%,
    #e2e8f0 20%,
    #bfdbfe 40%,
    #93c5fd 60%,
    #60a5fa 80%,
    #bfdbfe 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 0 28px rgba(59, 130, 246, 0.35));
  animation: shimmer-text 5s ease-in-out infinite, brand-reveal 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  animation-delay: var(--delay, 0s), var(--delay, 0s);
}

@keyframes brand-reveal {
  from {
    opacity: 0;
    transform: translateY(24px);
    letter-spacing: 2px;
  }
  to {
    opacity: 1;
    transform: translateY(0);
    letter-spacing: 8px;
  }
}

@keyframes shimmer-text {
  0%, 100% {
    background-position: 0% center;
  }
  50% {
    background-position: 100% center;
  }
}

.hero-role {
  font-size: 20px;
  color: #93c5fd;
  letter-spacing: 1px;
  font-weight: 700;
  text-transform: uppercase;
}

.hero-tag {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: rgba(226, 232, 240, 0.6);
  margin-top: 6px;
}

.hero-copy {
  margin-top: 16px;
  color: rgba(226, 232, 240, 0.8);
  max-width: 520px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 12px;
  margin: 24px 0 18px;
  flex-wrap: wrap;
}

.hero-actions .button {
  padding: 12px 24px;
  font-size: 15px;
  border-radius: 10px;
}

.hero-actions .button:not(.secondary) {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
}

.hero-actions .button:not(.secondary):hover {
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.5);
}

.hero-actions .button.secondary {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.4);
  color: #93c5fd;
}

.hero-actions .button.secondary:hover {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.6);
}

.hero-socials {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 20px;
}

.social-pill {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: rgba(59, 130, 246, 0.15);
  color: #bfdbfe;
  font-weight: 600;
  border: 1px solid rgba(59, 130, 246, 0.3);
  transition: transform 0.2s ease, background 0.2s ease, color 0.2s ease, box-shadow 0.2s ease;
}

.social-pill:hover {
  transform: translateY(-3px) scale(1.05);
  background: rgba(59, 130, 246, 0.3);
  color: #fff;
  box-shadow: 0 6px 16px rgba(59, 130, 246, 0.35);
}

.social-pill svg {
  width: 18px;
  height: 18px;
}

.hero-visual.animate-in {
  animation: fade-scale-in 0.8s ease-out forwards;
  animation-delay: var(--delay, 0s);
}

@keyframes fade-scale-in {
  from {
    opacity: 0;
    transform: scale(0.92);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.hero-visual {
  display: grid;
  place-items: center;
  position: relative;
  min-height: 320px;
}

.ring {
  position: absolute;
  width: min(320px, 70vw);
  height: min(320px, 70vw);
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 0 40px rgba(59, 130, 246, 0.4), inset 0 0 20px rgba(59, 130, 246, 0.08);
  animation: float-slow 7s ease-in-out infinite;
}

.ring-glow {
  border: 2px solid rgba(59, 130, 246, 0.6);
  filter: blur(0.2px);
  animation-delay: 1.2s;
}

.photo-frame {
  width: min(300px, 68vw);
  aspect-ratio: 1 / 1;
  display: grid;
  place-items: center;
  position: relative;
  z-index: 2;
}

.photo-frame img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 20px 40px rgba(2, 6, 23, 0.6));
}

.hero-glow {
  position: absolute;
  inset: -40%;
  background: radial-gradient(ellipse 60% 50% at 80% 30%, rgba(59, 130, 246, 0.2), transparent 50%);
  opacity: 0.5;
  z-index: 1;
  pointer-events: none;
}

@media (max-width: 900px) {
  .hero-shell {
    padding: 36px;
  }

  .hero-title {
    letter-spacing: 3px;
  }
}

@media (max-width: 600px) {
  .hero-shell {
    padding: 28px;
  }

  .hero-title {
    font-size: clamp(26px, 8vw, 42px);
    letter-spacing: 2px;
  }

  .hero-visual {
    min-height: 240px;
  }

  .ring {
    width: min(240px, 70vw);
    height: min(240px, 70vw);
  }
}

.services {
  margin-top: 56px;
  padding-top: 48px;
  border-top: 1px solid rgba(148, 163, 184, 0.12);
}

.services .hero-eyebrow {
  margin-bottom: 4px;
}

.services .glow-text {
  font-size: clamp(24px, 4vw, 32px);
  font-weight: 700;
  margin-bottom: 28px;
}

.service-card {
  display: grid;
  gap: 14px;
  padding: 24px;
  transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
  position: relative;
  overflow: hidden;
}

.service-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.step-service-1::before { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
.step-service-2::before { background: linear-gradient(90deg, #fb923c, #ea580c); }
.step-service-3::before { background: linear-gradient(90deg, #38bdf8, #0ea5e9); }

.service-step-badge {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 2px;
  width: fit-content;
  padding: 4px 10px;
  border-radius: 6px;
}

.step-service-1 .service-step-badge { background: rgba(251, 191, 36, 0.25); color: #fbbf24; }
.step-service-2 .service-step-badge { background: rgba(251, 146, 60, 0.25); color: #fb923c; }
.step-service-3 .service-step-badge { background: rgba(56, 189, 248, 0.25); color: #38bdf8; }

.service-card:hover {
  border-color: rgba(59, 130, 246, 0.35);
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
}

.service-card h3 {
  font-size: 18px;
  font-weight: 700;
  color: #e2e8f0;
  margin: 0;
}

.service-card .muted {
  font-size: 14px;
  line-height: 1.6;
}

.service-card .link {
  display: inline-block;
  background: none;
  border: none;
  color: #93c5fd;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  padding: 0;
  margin-top: 4px;
  text-align: left;
  text-decoration: none;
  transition: color 0.2s ease, transform 0.2s ease;
}

.service-card .link:hover {
  color: #bfdbfe;
  transform: translateX(4px);
}

.service-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: rgba(59, 130, 246, 0.2);
  color: #bfdbfe;
  font-weight: 700;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.service-icon svg {
  width: 24px;
  height: 24px;
}

.service-grid .card {
  animation: fade-slide-in 0.5s ease-out forwards;
  opacity: 0;
}

.service-grid .card:nth-child(1) { animation-delay: 0.1s; }
.service-grid .card:nth-child(2) { animation-delay: 0.2s; }
.service-grid .card:nth-child(3) { animation-delay: 0.3s; }
</style>
