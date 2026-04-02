<template>
  <div class="page">
    <Transition name="nav-video-fade">
      <div
        v-if="showNavVideo"
        class="nav-video-overlay"
        role="dialog"
        aria-modal="true"
        aria-live="assertive"
        aria-label="Transition de page"
      >
        <video
          :key="navVideoFilename"
          ref="navVideoRef"
          class="nav-video"
          :src="navVideoUrl"
          playsinline
          webkit-playsinline
          preload="auto"
        />
      </div>
    </Transition>
    <Transition name="nav-video-fade">
      <div
        v-if="showWelcomeOverlay"
        class="nav-video-overlay welcome-lightning-overlay"
        role="dialog"
        aria-modal="true"
        aria-live="polite"
        aria-label="Bienvenus"
      >
        <div class="welcome-flash-layer" aria-hidden="true" />
        <div class="welcome-bolts" aria-hidden="true">
          <svg class="bolt bolt--a" viewBox="0 0 80 200" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="welcomeBoltGradA" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f0f9ff" />
                <stop offset="50%" stop-color="#38bdf8" />
                <stop offset="100%" stop-color="#0284c7" />
              </linearGradient>
            </defs>
            <path
              class="bolt-path"
              d="M48 0 L28 72 L42 68 L18 128 L52 52 L38 58 L62 200 L44 88 L58 92 L48 0Z"
              fill="none"
              stroke="url(#welcomeBoltGradA)"
              stroke-width="3"
              stroke-linejoin="round"
            />
          </svg>
          <svg class="bolt bolt--b" viewBox="0 0 80 200" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="welcomeBoltGradB" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#fef9c3" />
                <stop offset="100%" stop-color="#38bdf8" />
              </linearGradient>
            </defs>
            <path
              class="bolt-path"
              d="M32 8 L52 80 L38 76 L58 140 L24 60 L40 64 L18 192 L36 96 L22 100 L32 8Z"
              fill="none"
              stroke="url(#welcomeBoltGradB)"
              stroke-width="2.5"
              stroke-linejoin="round"
            />
          </svg>
          <svg class="bolt bolt--c" viewBox="0 0 80 200" xmlns="http://www.w3.org/2000/svg">
            <path
              class="bolt-path bolt-path--fill"
              d="M44 4 L26 68 L38 62 L20 118 L46 48 L34 54 L54 188 L40 84 L50 88 L44 4Z"
              fill="rgba(56,189,248,0.4)"
              stroke="#bae6fd"
              stroke-width="1.5"
            />
          </svg>
        </div>
        <div class="welcome-content">
          <h2 class="welcome-title">Bienvenus</h2>
        </div>
      </div>
    </Transition>
    <header class="header">
      <div class="container header-content">
        <RouterLink to="/" class="logo" @click.prevent="(e) => onNavPageClick('/', e)">
          <img class="logo-avatar" :src="logoAvatar" alt="Profil" />
          Portfolio
        </RouterLink>
        <nav class="nav">
          <RouterLink to="/" @click.prevent="(e) => onNavPageClick('/', e)">Accueil</RouterLink>
          <RouterLink to="/a-propos" @click.prevent="(e) => onNavPageClick('/a-propos', e)">À propos</RouterLink>
          <RouterLink to="/competences" @click.prevent="(e) => onNavPageClick('/competences', e)">Compétences</RouterLink>
          <RouterLink to="/mes-projets" @click.prevent="(e) => onNavPageClick('/mes-projets', e)">Mes projets</RouterLink>
          <RouterLink to="/contact" @click.prevent="(e) => onNavPageClick('/contact', e)">Contact</RouterLink>
        </nav>
        <form class="header-actions" @submit.prevent="onSearch">
          <input
            v-model="searchQuery"
            class="search"
            type="search"
            placeholder="Rechercher compétences, projets..."
            aria-label="Recherche"
          />
          <button type="submit" class="button">Rechercher</button>
        </form>
        <button
          class="hamburger"
          :class="{ open: mobileMenuOpen }"
          type="button"
          aria-label="Menu"
          :aria-expanded="mobileMenuOpen"
          @click="toggleMobileMenu"
        >
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
        </button>
      </div>
      <div class="mobile-menu" :class="{ open: mobileMenuOpen }">
        <div class="container mobile-menu-inner">
        <nav class="mobile-nav">
          <RouterLink to="/" @click.prevent="(e) => onNavPageClick('/', e)">Accueil</RouterLink>
          <RouterLink to="/a-propos" @click.prevent="(e) => onNavPageClick('/a-propos', e)">À propos</RouterLink>
          <RouterLink to="/competences" @click.prevent="(e) => onNavPageClick('/competences', e)">Compétences</RouterLink>
          <RouterLink to="/mes-projets" @click.prevent="(e) => onNavPageClick('/mes-projets', e)">Mes projets</RouterLink>
          <RouterLink to="/contact" @click.prevent="(e) => onNavPageClick('/contact', e)">Contact</RouterLink>
        </nav>
        <form class="mobile-actions" @submit.prevent="onSearch">
          <input
            v-model="searchQuery"
            class="search"
            type="search"
            placeholder="Rechercher compétences, projets..."
            aria-label="Recherche"
          />
          <button type="submit" class="button">Rechercher</button>
        </form>
        </div>
      </div>
    </header>
    <main class="container main-content">
      <RouterView v-slot="{ Component, route }">
        <component :is="Component" :key="route.fullPath" />
      </RouterView>
    </main>
    <button
      v-show="showScrollBtn"
      class="scroll-top-btn"
      aria-label="Retour en haut"
      @click="scrollToTop"
    >
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M12 4l-8 8h5v8h6v-8h5L12 4z" fill="currentColor" />
      </svg>
    </button>
    <footer class="footer">
      <div class="container footer-content">
        <div class="footer-brand">
          <h3 class="footer-logo footer-brand-animate">
            <span class="footer-logo-accent">Assiki</span><span class="footer-logo-name">Mawaki</span>
          </h3>
          <p class="footer-slogan">
            Création d'expériences numériques innovantes et captivantes pour transformer vos idées en réalités visuelles.
          </p>
        </div>
        <div class="footer-links">
          <p class="footer-title">Liens Rapides</p>
          <RouterLink to="/" @click.prevent="(e) => onNavPageClick('/', e)">Accueil</RouterLink>
          <RouterLink to="/a-propos" @click.prevent="(e) => onNavPageClick('/a-propos', e)">À propos</RouterLink>
          <RouterLink to="/competences" @click.prevent="(e) => onNavPageClick('/competences', e)">Compétences</RouterLink>
          <RouterLink to="/mes-projets" @click.prevent="(e) => onNavPageClick('/mes-projets', e)">Mes projets</RouterLink>
          <RouterLink to="/contact" @click.prevent="(e) => onNavPageClick('/contact', e)">Contact</RouterLink>
        </div>
        <div class="footer-socials">
          <p class="footer-title">Réseaux sociaux</p>
          <div class="footer-socials-row">
            <a
              href="https://x.com/tony_kemzy?t=hdJksj-aYSVvpryViuC87Q"
              class="footer-social-pill"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="X"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M5 4l7.2 8.5L6 20h3l5-5.4L18.8 20H21l-7.6-9L19.5 4h-3l-4.4 4.8L8 4H5z" fill="currentColor" />
              </svg>
            </a>
            <a
              href="https://www.linkedin.com/in/mawaki-assiki/"
              class="footer-social-pill"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z" fill="currentColor" />
              </svg>
            </a>
            <a
              href="https://www.instagram.com/tony.assiki"
              class="footer-social-pill"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Instagram"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M7 4h10a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3z" fill="none" stroke="currentColor" stroke-width="1.6" />
                <circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.6" />
                <circle cx="17.5" cy="6.5" r="1" fill="currentColor" />
              </svg>
            </a>
            <a
              href="https://wa.me/70546096"
              class="footer-social-pill"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="WhatsApp"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.865 9.865 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" fill="currentColor" />
              </svg>
            </a>
            <a
              href="https://github.com/mawakitony"
              class="footer-social-pill"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.3-3.4-1.3-.5-1.1-1.1-1.4-1.1-1.4-.9-.6.1-.6.1-.6 1 .1 1.6 1 1.6 1 .9 1.6 2.4 1.1 3 .8.1-.7.4-1.1.7-1.4-2.2-.2-4.5-1.1-4.5-4.9 0-1.1.4-2 1-2.7-.1-.2-.4-1.2.1-2.5 0 0 .8-.3 2.7 1a9.3 9.3 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.3.2 2.3.1 2.5.6.7 1 1.6 1 2.7 0 3.8-2.3 4.7-4.5 4.9.4.3.8.9.8 1.9v2.8c0 .3.2.6.7.5A10 10 0 0 0 12 2z" fill="currentColor" />
              </svg>
            </a>
          </div>
        </div>
        <div class="footer-newsletter">
          <p class="footer-title">Newsletter</p>
          <p class="footer-newsletter-desc">
            Abonnez-vous pour recevoir mes derniers articles et actualités.
          </p>
          <form class="newsletter-form" @submit.prevent="onNewsletterSubmit">
            <input
              v-model="newsletterEmail"
              type="email"
              placeholder="Votre email"
              class="newsletter-input"
              required
            />
            <button type="submit" class="newsletter-btn">OK</button>
          </form>
        </div>
      </div>
      <div class="footer-bar">
        <span class="footer-copyright">© {{ currentYear }} Assiki Mawaki. Tous droits réservés.</span>
        <div class="footer-legal">
          <a href="#" class="footer-legal-link">Mentions légales</a>
          <a href="#" class="footer-legal-link">Politique de confidentialité</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch, computed, provide } from "vue";
import { RouterLink, RouterView, useRouter, useRoute } from "vue-router";
import logoAvatar from "./assets/logo-avatar.png";

const NAV_VIDEO_MS = 2000;
const DEFAULT_NAV_VIDEO = "banniere-competence.mp4";

/** Pas de vidéo avant l’affichage de ces pages (navigation immédiate) */
const PATHS_WITHOUT_NAV_VIDEO = ["/a-propos", "/competences", "/contact"];

/** Message « Bienvenue » + effets foudre : 3 s après l’arrivée, affichage 2 s */
const WELCOME_OVERLAY_DELAY_MS = 3000;
const WELCOME_OVERLAY_DURATION_MS = 2000;

const router = useRouter();
const route = useRoute();
const currentYear = new Date().getFullYear();
const newsletterEmail = ref("");
const searchQuery = ref("");
const showScrollBtn = ref(false);
const mobileMenuOpen = ref(false);
const showNavVideo = ref(false);
const navVideoRef = ref(null);
let navVideoTimer = null;
let pendingNavPath = null;

const showWelcomeOverlay = ref(false);
let welcomeDelayTimer = null;
let welcomeHideTimer = null;
let welcomeRetryTimer = null;

const navVideoFilename = ref(DEFAULT_NAV_VIDEO);
const navDurationMs = ref(NAV_VIDEO_MS);

const navVideoUrl = computed(() => {
  const b = import.meta.env.BASE_URL || "/";
  const base = b.endsWith("/") ? b : `${b}/`;
  return `${base}videos/${navVideoFilename.value}`;
});

function prefersReducedMotionNav() {
  if (typeof window === "undefined") return false;
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function clearNavVideoTimer() {
  if (navVideoTimer != null) {
    clearTimeout(navVideoTimer);
    navVideoTimer = null;
  }
}

function finishNavVideo() {
  clearNavVideoTimer();
  showNavVideo.value = false;
  navVideoFilename.value = DEFAULT_NAV_VIDEO;
  navDurationMs.value = NAV_VIDEO_MS;
  if (pendingNavPath != null) {
    router.push(pendingNavPath);
    pendingNavPath = null;
  }
  closeMobileMenu();
}

/**
 * Transition vidéo puis navigation (utilisée par le menu et par « Contactez-moi » sur l’accueil).
 * @param targetPath ex. "/contact"
 * @param options.videoFile fichier dans public/videos/
 * @param options.durationMs durée avant navigation
 */
async function openNavTransition(targetPath, options = {}) {
  const videoFile = options.videoFile ?? DEFAULT_NAV_VIDEO;
  const durationMs = options.durationMs ?? NAV_VIDEO_MS;

  if (route.path === targetPath) {
    closeMobileMenu();
    return;
  }
  if (PATHS_WITHOUT_NAV_VIDEO.includes(targetPath)) {
    router.push(targetPath);
    closeMobileMenu();
    return;
  }
  if (prefersReducedMotionNav()) {
    router.push(targetPath);
    closeMobileMenu();
    return;
  }

  pendingNavPath = targetPath;
  navVideoFilename.value = videoFile;
  navDurationMs.value = durationMs;
  clearNavVideoTimer();
  showNavVideo.value = true;
  await nextTick();
  const v = navVideoRef.value;
  if (v) {
    v.currentTime = 0;
    try {
      await v.play();
    } catch {
      finishNavVideo();
      return;
    }
  }
  navVideoTimer = window.setTimeout(finishNavVideo, navDurationMs.value);
}

provide("openNavTransition", openNavTransition);

async function onNavPageClick(targetPath, e) {
  e?.preventDefault?.();
  await openNavTransition(targetPath, {
    videoFile: DEFAULT_NAV_VIDEO,
    durationMs: NAV_VIDEO_MS,
  });
}

function clearWelcomeTimers() {
  if (welcomeDelayTimer != null) {
    clearTimeout(welcomeDelayTimer);
    welcomeDelayTimer = null;
  }
  if (welcomeHideTimer != null) {
    clearTimeout(welcomeHideTimer);
    welcomeHideTimer = null;
  }
  if (welcomeRetryTimer != null) {
    clearTimeout(welcomeRetryTimer);
    welcomeRetryTimer = null;
  }
}

function runWelcomeOverlay() {
  if (prefersReducedMotionNav()) return;
  if (showNavVideo.value) {
    welcomeRetryTimer = window.setTimeout(() => {
      welcomeRetryTimer = null;
      runWelcomeOverlay();
    }, 400);
    return;
  }
  showWelcomeOverlay.value = true;
  welcomeHideTimer = window.setTimeout(() => {
    welcomeHideTimer = null;
    showWelcomeOverlay.value = false;
  }, WELCOME_OVERLAY_DURATION_MS);
}

watch(
  [showNavVideo, showWelcomeOverlay],
  ([nav, welcome]) => {
    if (typeof document === "undefined") return;
    document.body.style.overflow = nav || welcome ? "hidden" : "";
  },
  { immediate: true }
);

watch(showNavVideo, (on) => {
  if (!on && navVideoRef.value) {
    navVideoRef.value.pause();
  }
});


const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const closeMobileMenu = () => {
  mobileMenuOpen.value = false;
};

const onSearch = () => {
  const q = searchQuery.value?.trim();
  if (!q) return;
  router.push({ path: "/competences", query: { q } });
};

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const onScroll = () => {
  showScrollBtn.value = window.scrollY > 300;
};

onMounted(() => {
  window.addEventListener("scroll", onScroll);
  if (!prefersReducedMotionNav()) {
    welcomeDelayTimer = window.setTimeout(() => {
      welcomeDelayTimer = null;
      runWelcomeOverlay();
    }, WELCOME_OVERLAY_DELAY_MS);
  }
});

onUnmounted(() => {
  window.removeEventListener("scroll", onScroll);
  clearNavVideoTimer();
  clearWelcomeTimers();
  if (typeof document !== "undefined") document.body.style.overflow = "";
});

const onNewsletterSubmit = () => {
  if (newsletterEmail.value) {
    console.log("Newsletter:", newsletterEmail.value);
    newsletterEmail.value = "";
  }
};
</script>

<style scoped>
.nav-video-overlay {
  position: fixed;
  inset: 0;
  z-index: 10000;
  display: grid;
  place-items: center;
  background: #020617;
  padding: 0;
}

.nav-video {
  width: min(100vw, 100%);
  height: min(100vh, 100%);
  max-height: 100vh;
  object-fit: cover;
}

.welcome-lightning-overlay {
  z-index: 10001;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 24px;
  gap: 0;
  background: radial-gradient(ellipse 80% 60% at 50% 40%, rgba(15, 23, 42, 0.97), #020617);
  overflow: hidden;
}

.welcome-flash-layer {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(circle at 50% 30%, rgba(255, 255, 255, 0.22), transparent 45%);
  animation: welcome-sky-flash 2s ease-in-out infinite;
  mix-blend-mode: screen;
}

@keyframes welcome-sky-flash {
  0%,
  100% {
    opacity: 0;
  }
  4% {
    opacity: 0.85;
  }
  5% {
    opacity: 0.15;
  }
  8% {
    opacity: 0.55;
  }
  10% {
    opacity: 0;
  }
  45% {
    opacity: 0;
  }
  48% {
    opacity: 0.7;
  }
  50% {
    opacity: 0;
  }
  72% {
    opacity: 0;
  }
  74% {
    opacity: 0.45;
  }
  76% {
    opacity: 0;
  }
}

.welcome-bolts {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.bolt {
  position: absolute;
  width: min(22vw, 140px);
  height: min(55vh, 360px);
  filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.9)) drop-shadow(0 0 28px rgba(14, 165, 233, 0.5));
}

.bolt--a {
  left: 8%;
  top: 18%;
  transform: rotate(-8deg);
  animation: bolt-flicker-a 1.8s ease-in-out infinite;
}

.bolt--b {
  right: 10%;
  top: 22%;
  transform: rotate(12deg);
  animation: bolt-flicker-b 2.1s ease-in-out infinite;
}

.bolt--c {
  left: 42%;
  top: 0;
  width: min(18vw, 110px);
  height: min(48vh, 300px);
  transform: rotate(4deg);
  opacity: 0.75;
  animation: bolt-flicker-c 1.4s ease-in-out infinite;
}

.bolt-path {
  stroke-linecap: round;
}

@keyframes bolt-flicker-a {
  0%,
  100% {
    opacity: 0;
    filter: drop-shadow(0 0 4px rgba(56, 189, 248, 0.3));
  }
  3% {
    opacity: 1;
    filter: drop-shadow(0 0 20px rgba(56, 189, 248, 1));
  }
  6% {
    opacity: 0.35;
  }
  9% {
    opacity: 0.95;
  }
  14% {
    opacity: 0;
  }
  50% {
    opacity: 0;
  }
  52% {
    opacity: 0.85;
  }
  56% {
    opacity: 0;
  }
}

@keyframes bolt-flicker-b {
  0%,
  100% {
    opacity: 0;
  }
  12% {
    opacity: 0;
  }
  14% {
    opacity: 1;
  }
  18% {
    opacity: 0.2;
  }
  21% {
    opacity: 0.9;
  }
  25% {
    opacity: 0;
  }
  60% {
    opacity: 0;
  }
  63% {
    opacity: 0.75;
  }
  66% {
    opacity: 0;
  }
}

@keyframes bolt-flicker-c {
  0%,
  100% {
    opacity: 0;
    transform: rotate(4deg) scaleY(0.92);
  }
  5% {
    opacity: 0.55;
    transform: rotate(4deg) scaleY(1);
  }
  7% {
    opacity: 0;
  }
  35% {
    opacity: 0;
  }
  37% {
    opacity: 0.85;
  }
  40% {
    opacity: 0.15;
  }
  43% {
    opacity: 0.65;
  }
  46% {
    opacity: 0;
  }
}

.welcome-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 24px 32px;
}

.welcome-title {
  margin: 0;
  font-size: clamp(2.2rem, 8vw, 3.8rem);
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: none;
  background: linear-gradient(120deg, #f8fafc 0%, #e0f2fe 35%, #38bdf8 55%, #7dd3fc 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: welcome-title-shimmer 2s ease-in-out infinite, welcome-title-glow 2s ease-in-out infinite;
  text-shadow: 0 0 40px rgba(56, 189, 248, 0.35);
}

@keyframes welcome-title-shimmer {
  0%,
  100% {
    background-position: 0% center;
  }
  50% {
    background-position: 100% center;
  }
}

@keyframes welcome-title-glow {
  0%,
  100% {
    filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.4));
  }
  5%,
  48%,
  74% {
    filter: drop-shadow(0 0 22px rgba(250, 250, 250, 0.55)) drop-shadow(0 0 36px rgba(56, 189, 248, 0.9));
  }
  10%,
  52%,
  78% {
    filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.5));
  }
}

@media (prefers-reduced-motion: reduce) {
  .welcome-flash-layer,
  .bolt--a,
  .bolt--b,
  .bolt--c,
  .welcome-title {
    animation: none;
  }

  .welcome-flash-layer {
    opacity: 0;
  }

  .bolt--a,
  .bolt--b,
  .bolt--c {
    opacity: 0.5;
  }
}

.nav-video-fade-enter-active,
.nav-video-fade-leave-active {
  transition: opacity 0.35s ease;
}

.nav-video-fade-enter-from,
.nav-video-fade-leave-to {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .nav-video-fade-enter-active,
  .nav-video-fade-leave-active {
    transition-duration: 0.01ms;
  }
}

.header {
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 28px 0 10px;
  background: linear-gradient(180deg, #0f172a 0%, rgba(15, 23, 42, 0.98) 100%);
  backdrop-filter: blur(8px);
}

.header::after {
  content: "";
  display: block;
  height: 1px;
  margin-top: 16px;
  background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.35), transparent);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}

.logo {
  font-weight: 700;
  font-size: 18px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: #e2e8f0;
  text-decoration: none;
  transition: color 0.2s ease, opacity 0.2s ease;
}

.logo:hover {
  color: #bfdbfe;
  opacity: 0.95;
}

.logo-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid rgba(148, 163, 184, 0.4);
  box-shadow: 0 0 12px rgba(59, 130, 246, 0.35);
}

.nav {
  display: flex;
  gap: 16px;
}

.nav a {
  padding: 6px 10px;
  border-radius: 999px;
  color: rgba(226, 232, 240, 0.8);
}

.nav a.router-link-active {
  color: #bfdbfe;
  background: rgba(59, 130, 246, 0.2);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search {
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: inherit;
  border-radius: 999px;
  padding: 8px 14px;
  width: 180px;
}

.header-actions .button {
  animation: pulse-glow 6s ease-in-out infinite;
}

.main-content {
  padding: 32px 0 60px;
  position: relative;
}

/* Hamburger - visible only on mobile */
.hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 40px;
  height: 40px;
  padding: 8px;
  background: transparent;
  border: 1px solid rgba(148, 163, 184, 0.3);
  border-radius: 8px;
  cursor: pointer;
  color: #e2e8f0;
  transition: background 0.2s ease, border-color 0.2s ease;
}

.hamburger:hover {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.4);
}

.hamburger-line {
  display: block;
  width: 100%;
  height: 2px;
  background: currentColor;
  border-radius: 1px;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.hamburger.open .hamburger-line:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.hamburger.open .hamburger-line:nth-child(2) {
  opacity: 0;
}

.hamburger.open .hamburger-line:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

/* Mobile menu dropdown */
.mobile-menu-inner {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.mobile-menu {
  display: none;
  flex-direction: column;
  padding: 20px 0;
  background: rgba(15, 23, 42, 0.98);
  border-top: 1px solid rgba(148, 163, 184, 0.15);
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.3s ease, opacity 0.3s ease;
}

.mobile-menu.open {
  max-height: 400px;
  opacity: 1;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.mobile-nav a {
  padding: 12px 16px;
  border-radius: 8px;
  color: rgba(226, 232, 240, 0.9);
  font-weight: 500;
  transition: background 0.2s ease, color 0.2s ease;
}

.mobile-nav a:hover,
.mobile-nav a.router-link-active {
  color: #bfdbfe;
  background: rgba(59, 130, 246, 0.2);
}

.mobile-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.mobile-actions .search {
  width: 100%;
}

@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav,
  .header-actions {
    display: none;
  }

  .header-content {
    flex-wrap: nowrap;
  }

  .mobile-menu {
    display: flex;
  }
}

@media (min-width: 769px) {
  .mobile-menu {
    display: none !important;
  }
}

@media (max-width: 900px) {
  .header-content {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }
}

@media (max-width: 600px) {
  .header-actions {
    width: 100%;
    flex-direction: column;
    align-items: stretch;
  }

  .search {
    width: 100%;
  }
}

.footer {
  margin-top: 60px;
  padding: 48px 0 0;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.98), rgba(2, 6, 23, 0.99));
  border-top: 1px solid rgba(148, 163, 184, 0.15);
  position: relative;
  overflow: hidden;
}

.footer-content {
  display: grid;
  gap: 40px;
  grid-template-columns: 1fr auto auto auto;
  position: relative;
  z-index: 1;
  padding-bottom: 32px;
}

.footer-brand {
  max-width: 360px;
}

.footer-logo {
  font-family: var(--font-brand);
  font-size: 24px;
  font-weight: 700;
  margin: 0 0 12px;
  letter-spacing: 0.02em;
}

.footer-logo-accent {
  color: #818cf8;
}

.footer-brand-animate .footer-logo-accent {
  background: linear-gradient(135deg, #93c5fd, #60a5fa, #818cf8);
  background-size: 200% auto;
  background-position: 0% center;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: footer-shimmer 6s ease-in-out infinite;
}

@keyframes footer-shimmer {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}

.footer-logo-name {
  color: rgba(226, 232, 240, 0.85);
  letter-spacing: 0.05em;
}

.footer-slogan {
  color: rgba(226, 232, 240, 0.7);
  font-size: 14px;
  line-height: 1.6;
  margin: 0;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-width: 140px;
}

.footer-title {
  font-weight: 700;
  letter-spacing: 0.5px;
  font-size: 13px;
  color: #818cf8;
  margin: 0 0 4px;
}

.footer-links a {
  color: rgba(226, 232, 240, 0.75);
  font-size: 14px;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: #e2e8f0;
}

.footer-socials .footer-title {
  margin-bottom: 12px;
}

.footer-socials-row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.footer-social-pill {
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  background: rgba(30, 41, 59, 0.9);
  color: #fff;
  border: 1px solid rgba(59, 130, 246, 0.35);
  box-shadow: 0 0 12px rgba(59, 130, 246, 0.15);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.footer-social-pill:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
  border-color: rgba(59, 130, 246, 0.5);
}

.footer-social-pill svg {
  width: 18px;
  height: 18px;
}

.footer-newsletter {
  min-width: 260px;
}

.footer-newsletter-desc {
  color: rgba(226, 232, 240, 0.7);
  font-size: 13px;
  line-height: 1.5;
  margin: 0 0 14px;
}

.newsletter-form {
  display: flex;
  gap: 0;
  border-radius: 8px;
  overflow: hidden;
}

.newsletter-input {
  flex: 1;
  padding: 10px 14px;
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  font-size: 14px;
  outline: none;
}

.newsletter-input::placeholder {
  color: rgba(226, 232, 240, 0.5);
}

.newsletter-input:focus {
  border-color: rgba(129, 140, 248, 0.5);
}

.newsletter-btn {
  padding: 10px 20px;
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  color: #fff;
  font-weight: 600;
  font-size: 14px;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.newsletter-btn:hover {
  opacity: 0.9;
}

.footer-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 18px 0 24px;
  border-top: 1px solid rgba(148, 163, 184, 0.12);
  position: relative;
  z-index: 1;
  flex-wrap: wrap;
}

.footer-copyright {
  color: rgba(226, 232, 240, 0.7);
  font-size: 13px;
}

.footer-legal {
  display: flex;
  gap: 20px;
}

.footer-legal-link {
  color: rgba(226, 232, 240, 0.7);
  font-size: 13px;
  transition: color 0.2s ease;
}

.footer-legal-link:hover {
  color: #e2e8f0;
}

@media (max-width: 900px) {
  .footer-content {
    grid-template-columns: 1fr;
  }

  .footer-brand {
    max-width: none;
  }

  .footer-newsletter {
    min-width: auto;
  }

  .footer-socials-row {
    justify-content: flex-start;
  }
}

.scroll-top-btn {
  position: fixed;
  bottom: 28px;
  right: 28px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: #fff;
  border: none;
  cursor: pointer;
  display: grid;
  place-items: center;
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.45);
  z-index: 90;
  transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.3s ease;
}

.scroll-top-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 28px rgba(59, 130, 246, 0.55);
}

.scroll-top-btn svg {
  width: 22px;
  height: 22px;
}

@media (max-width: 600px) {
  .scroll-top-btn {
    bottom: 20px;
    right: 20px;
    width: 44px;
    height: 44px;
  }

  .scroll-top-btn svg {
    width: 20px;
    height: 20px;
  }
}
</style>
