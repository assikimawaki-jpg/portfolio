<template>
  <section class="skills-shell">
    <div class="skills-hero skills-hero--video">
      <div class="skills-hero-media" aria-hidden="true">
        <video
          class="skills-hero-video"
          :src="skillsHeroVideoUrl"
          autoplay
          muted
          loop
          playsinline
          webkit-playsinline
        />
        <div class="skills-hero-scrim" />
      </div>
      <div class="skills-hero-content">
        <span class="pill">Compétences</span>
        <h2 class="title">Outils & Technologies</h2>
        <p class="muted skills-hero-intro">
          Les logiciels et technologies que j'utilise quotidiennement pour créer
          des expériences numériques exceptionnelles.
        </p>
      </div>
    </div>

    <div
      v-if="searchQuery"
      class="filter-chip"
      role="status"
    >
      <span class="filter-chip-label">Filtre actif</span>
      <span class="filter-chip-q">« {{ route.query.q }} »</span>
      <RouterLink
        :to="{ path: '/competences', query: {} }"
        class="filter-chip-clear"
      >
        Réinitialiser
      </RouterLink>
    </div>

    <div class="skills-tools-shell">
      <div class="skills-tools-aurora" aria-hidden="true" />
      <div class="skills-tools-noise" aria-hidden="true" />

      <div
        class="tabs"
        :style="{ '--active-tab': activeTabIndex }"
        role="tablist"
        aria-label="Catégories de compétences"
      >
        <button
          v-for="tab in tabs"
          :key="tab"
          type="button"
          class="tab"
          role="tab"
          :class="{ active: activeTab === tab }"
          :aria-selected="activeTab === tab"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>

      <p v-if="searchQuery && !filteredActiveTools.length" class="projects-empty">
        Aucun outil ne correspond à « {{ route.query.q }} » dans cette catégorie.
      </p>
      <TransitionGroup
        v-else
        name="list-stagger"
        tag="div"
        class="tool-grid"
      >
        <div
          v-for="(tool, idx) in filteredActiveTools"
          :key="`${activeTab}-${tool.name}`"
          class="tool-card"
          :class="`tool-accent-${(idx % 4) + 1}`"
          :style="{ '--stagger': idx }"
        >
          <div class="tool-card-glow" aria-hidden="true" />
          <div class="tool-header">
            <div class="tool-icon" :class="{ 'tool-icon-light': tool.iconBg }">
              <img :src="tool.icon" :alt="tool.name" loading="lazy" />
            </div>
            <div class="tool-circle-progress">
              <svg viewBox="0 0 36 36">
                <path
                  class="circle-bg"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  class="circle-fill"
                  :stroke-dasharray="`${displayLevel(tool.level)} 100`"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <span class="circle-value">{{ Math.round(tool.level * levelAnimProgress) }}%</span>
            </div>
          </div>
          <h3>{{ tool.name }}</h3>
          <div class="tool-progress">
            <div class="progress">
              <div
                class="progress-bar"
                :style="{ width: `${displayLevel(tool.level)}%` }"
              />
            </div>
          </div>
        </div>
      </TransitionGroup>
    </div>

    <div class="projects-section">
      <span class="pill">Portfolio</span>
      <h2 class="projects-title">Projets récents</h2>
      <p class="muted projects-subtitle">
        Projets web et créations graphiques (affiches, print) — un aperçu de mon travail.
      </p>
      <p class="projects-see-all">
        <RouterLink to="/mes-projets" class="link-all-projects">Voir tous les projets →</RouterLink>
      </p>
      <TransitionGroup
        name="list-stagger"
        tag="div"
        class="project-grid"
      >
        <article
          v-for="(project, idx) in filteredProjects"
          :key="project.id"
          class="project-card"
          :class="[
            `project-accent-${(idx % 4) + 1}`,
            { 'project-card--affiche': project.kind === 'graphisme' },
          ]"
        >
          <div
            class="project-image-wrap"
            :class="{ 'project-image-wrap--affiche': project.kind === 'graphisme' }"
          >
            <img
              v-if="project.image"
              :src="resolveImg(project.image)"
              :alt="project.titre"
              class="project-image"
              loading="lazy"
            />
            <div v-else class="project-image-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="3" width="18" height="18" rx="2" />
                <circle cx="8.5" cy="8.5" r="1.5" />
                <path d="M21 15l-5-5L5 21" />
              </svg>
              <span>Projet</span>
            </div>
          </div>
          <div class="project-body">
            <h3 class="project-title">{{ project.titre }}</h3>
            <p class="project-desc">{{ truncateDesc(project.description) }}</p>
            <div class="project-actions">
              <a
                v-if="project.lien_demo"
                :href="project.lien_demo"
                target="_blank"
                rel="noopener noreferrer"
                class="project-btn"
              >
                Voir la démo
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                  <polyline points="15 3 21 3 21 9" />
                  <line x1="10" y1="14" x2="21" y2="3" />
                </svg>
              </a>
              <a
                v-if="project.lien_github"
                :href="project.lien_github"
                target="_blank"
                rel="noopener noreferrer"
                class="project-btn secondary"
              >
                GitHub
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.3-3.4-1.3-.5-1.1-1.1-1.4-1.1-1.4-.9-.6.1-.6.1-.6 1 .1 1.6 1 1.6 1 .9 1.6 2.4 1.1 3 .8.1-.7.4-1.1.7-1.4-2.2-.2-4.5-1.1-4.5-4.9 0-1.1.4-2 1-2.7-.1-.2-.4-1.2.1-2.5 0 0 .8-.3 2.7 1a9.3 9.3 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.3.2 2.3.1 2.5.6.7 1 1.6 1 2.7 0 3.8-2.3 4.7-4.5 4.9.4.3.8.9.8 1.9v2.8c0 .3.2.6.7.5A10 10 0 0 0 12 2z" />
                </svg>
              </a>
              <a
                v-if="project.kind === 'graphisme' && project.image"
                :href="resolveImg(project.image)"
                class="project-btn secondary"
                :download="fichierImage(project)"
              >
                Télécharger l’image
              </a>
            </div>
          </div>
        </article>
      </TransitionGroup>
      <p v-if="!filteredProjects.length" class="projects-empty">
        {{ searchQuery ? "Aucun projet ne correspond à votre recherche." : "Aucun projet pour le moment. (Version statique)" }}
      </p>
    </div>
  </section>
</template>

<script setup>
import {
  computed,
  ref,
  watch,
  onMounted,
  onUnmounted,
  nextTick,
} from "vue";
import { useRoute, RouterLink } from "vue-router";
import { competences, projets, projetsGraphisme } from "../data/static";

const route = useRoute();

const skillsHeroVideoUrl = computed(() => {
  const b = import.meta.env.BASE_URL || "/";
  const base = b.endsWith("/") ? b : `${b}/`;
  return `${base}videos/au-cli.mp4`;
});
const tabs = ["Design", "Développement", "Motion & 3D"];
const activeTab = ref("Design");
/** 0 → 1 : remplit cercles et barres (ease-out) */
const levelAnimProgress = ref(0);

let levelAnimFrame = null;

function prefersReducedMotion() {
  if (typeof window === "undefined") return false;
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function displayLevel(level) {
  return Math.round(level * levelAnimProgress.value * 100) / 100;
}

function runToolsLevelAnimation() {
  if (prefersReducedMotion()) {
    levelAnimProgress.value = 1;
    return;
  }
  levelAnimProgress.value = 0;
  if (levelAnimFrame != null) cancelAnimationFrame(levelAnimFrame);
  const start = performance.now();
  const duration = 1150;
  function easeOutCubic(t) {
    return 1 - (1 - t) ** 3;
  }
  function tick(now) {
    const raw = Math.min(1, (now - start) / duration);
    levelAnimProgress.value = easeOutCubic(raw);
    if (raw < 1) levelAnimFrame = requestAnimationFrame(tick);
    else levelAnimFrame = null;
  }
  levelAnimFrame = requestAnimationFrame(tick);
}

onMounted(() => {
  nextTick(() => runToolsLevelAnimation());
});

onUnmounted(() => {
  if (levelAnimFrame != null) cancelAnimationFrame(levelAnimFrame);
});

watch(activeTab, () => {
  nextTick(() => runToolsLevelAnimation());
});

watch(
  () => route.query.q,
  () => {
    nextTick(() => runToolsLevelAnimation());
  }
);

const activeTabIndex = computed(() => {
  const i = tabs.indexOf(activeTab.value);
  return i >= 0 ? i : 0;
});

const base = import.meta.env.BASE_URL || "/";

const resolveImg = (path) => {
  if (!path) return "";
  if (path.startsWith("http")) return path;
  const b = base.endsWith("/") ? base : `${base}/`;
  return `${b}${path.replace(/^\//, "")}`;
};

const fichierImage = (project) => {
  const fromPath = project.image?.split("/").pop();
  return fromPath || "image.png";
};

const truncateDesc = (text, max = 120) => {
  if (!text) return "";
  return text.length > max ? text.slice(0, max).trim() + "…" : text;
};

const activeTools = computed(() => {
  return competences.find((t) => t.category === activeTab.value)?.items || [];
});

const searchQuery = computed(() => (route.query.q || "").trim().toLowerCase());

const filteredActiveTools = computed(() => {
  const list = activeTools.value;
  const q = searchQuery.value;
  if (!q) return list;
  return list.filter((t) => t.name.toLowerCase().includes(q));
});

const portfolioListe = computed(() => [
  ...projets.map((p) => ({ ...p, kind: "web" })),
  ...projetsGraphisme.map((p) => ({ ...p, kind: "graphisme" })),
]);

function projectSearchBlob(p) {
  return [
    p.titre,
    p.description,
    p.contexte,
    p.probleme,
    p.solution,
    p.resultat,
  ]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
}

const filteredProjects = computed(() => {
  const list = portfolioListe.value;
  const q = searchQuery.value;
  if (!q) return list;
  return list.filter((p) => projectSearchBlob(p).includes(q));
});
</script>

<style scoped>
.skills-shell {
  display: grid;
  gap: 28px;
  padding: 32px;
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(10, 19, 46, 0.85), rgba(7, 14, 36, 0.95));
  border: 1px solid rgba(59, 130, 246, 0.15);
}

.skills-hero {
  margin-bottom: 8px;
}

.skills-hero--video {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  border: 1px solid rgba(59, 130, 246, 0.25);
  box-shadow: 0 24px 48px rgba(2, 6, 23, 0.45);
  min-height: min(48vh, 380px);
  display: grid;
  align-items: center;
  justify-items: center;
}

.skills-hero-media {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.skills-hero-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.skills-hero-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(2, 6, 23, 0.45) 0%,
    rgba(15, 23, 42, 0.72) 45%,
    rgba(2, 6, 23, 0.88) 100%
  );
  pointer-events: none;
}

.skills-hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 640px;
  margin: 0 auto;
  padding: clamp(24px, 5vw, 40px) clamp(18px, 3vw, 28px);
}

.skills-hero--video .pill {
  margin-bottom: 10px;
  background: rgba(15, 23, 42, 0.55);
  border-color: rgba(147, 197, 253, 0.45);
  backdrop-filter: blur(8px);
}

.skills-hero--video .title {
  text-shadow: 0 2px 24px rgba(0, 0, 0, 0.45);
}

.skills-hero--video .skills-hero-intro {
  text-shadow: 0 1px 12px rgba(0, 0, 0, 0.35);
  color: rgba(241, 245, 249, 0.92);
  margin: 0;
}

@media (prefers-reduced-motion: reduce) {
  .skills-hero-video {
    display: none;
  }

  .skills-hero--video {
    background: linear-gradient(145deg, #1e293b 0%, #0f172a 55%, #020617 100%);
    min-height: 260px;
  }

  .skills-hero-scrim {
    opacity: 0.35;
  }
}

.pill {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(59, 130, 246, 0.18);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.35);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1px;
}

.title {
  margin: 10px 0 12px;
}

.skills-tools-shell {
  position: relative;
  padding: 28px 16px 8px;
  margin: 8px -8px 0;
  border-radius: 22px;
  overflow: hidden;
  isolation: isolate;
}

.skills-tools-aurora {
  position: absolute;
  inset: -45%;
  pointer-events: none;
  z-index: 0;
  background:
    radial-gradient(ellipse 50% 42% at 18% 32%, rgba(99, 102, 241, 0.5), transparent 58%),
    radial-gradient(ellipse 48% 48% at 88% 68%, rgba(14, 165, 233, 0.4), transparent 58%),
    radial-gradient(ellipse 38% 38% at 48% 95%, rgba(236, 72, 153, 0.28), transparent 55%);
  filter: blur(32px);
  opacity: 0.75;
  animation: skillsAurora 16s ease-in-out infinite alternate;
}

.skills-tools-noise {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
  opacity: 0.055;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  mix-blend-mode: overlay;
}

@keyframes skillsAurora {
  0% {
    transform: translate(0, 0) scale(1);
    filter: blur(32px) hue-rotate(0deg) saturate(1.15);
  }
  100% {
    transform: translate(4%, -3%) scale(1.1);
    filter: blur(42px) hue-rotate(55deg) saturate(1.45);
  }
}

.skills-tools-shell .tabs,
.skills-tools-shell > .tool-grid,
.skills-tools-shell > .projects-empty {
  position: relative;
  z-index: 2;
}

.tabs {
  --active-tab: 0;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  align-items: stretch;
  gap: 0;
  position: relative;
  background: rgba(12, 24, 60, 0.9);
  padding: 6px;
  border-radius: 12px;
  border: 1px solid rgba(59, 130, 246, 0.25);
  justify-self: center;
  max-width: min(100%, 520px);
  width: 100%;
}

.tabs::before {
  content: "";
  position: absolute;
  top: 6px;
  left: 6px;
  width: calc((100% - 12px) / 3);
  height: calc(100% - 12px);
  border-radius: 8px;
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  box-shadow: 0 8px 22px rgba(79, 70, 229, 0.4);
  transform: translateX(calc(var(--active-tab) * 100%));
  transition: transform 0.42s cubic-bezier(0.34, 1.25, 0.64, 1);
  z-index: 0;
  pointer-events: none;
}

.tab {
  position: relative;
  z-index: 1;
  background: transparent;
  color: rgba(226, 232, 240, 0.72);
  border: none;
  padding: 10px 12px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: clamp(12px, 2.8vw, 14px);
  transition: color 0.25s ease, transform 0.2s ease;
}

.tab:hover {
  color: #f1f5f9;
}

.tab.active {
  color: #fff;
  background: transparent;
  box-shadow: none;
}

.tool-grid {
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  position: relative;
  z-index: 2;
}

.tool-card {
  background: rgba(15, 23, 42, 0.78);
  border-radius: 16px;
  padding: 20px;
  border: 1px solid rgba(148, 163, 184, 0.15);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  display: grid;
  gap: 14px;
  transition: transform 0.45s cubic-bezier(0.34, 1.25, 0.64, 1),
    box-shadow 0.4s ease,
    border-color 0.3s ease,
    filter 0.35s ease;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(12px) saturate(1.15);
  z-index: 2;
  animation: toolCardPop 0.75s cubic-bezier(0.34, 1.3, 0.64, 1) backwards;
  animation-delay: calc(var(--stagger, 0) * 65ms);
}

@keyframes toolCardPop {
  from {
    opacity: 0;
    transform: translateY(28px) scale(0.92) rotateX(8deg);
    filter: blur(8px) brightness(0.85);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1) rotateX(0);
    filter: blur(0) brightness(1);
  }
}

.tool-card-glow {
  position: absolute;
  inset: -1px;
  border-radius: 17px;
  pointer-events: none;
  opacity: 0;
  background: conic-gradient(
    from 180deg at 50% 50%,
    rgba(99, 102, 241, 0.35),
    rgba(14, 165, 233, 0.25),
    rgba(236, 72, 153, 0.2),
    rgba(99, 102, 241, 0.35)
  );
  filter: blur(14px);
  transition: opacity 0.45s ease;
  z-index: 0;
}

.tool-card:hover .tool-card-glow {
  opacity: 0.95;
}

.tool-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.tool-card.tool-accent-1::before { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
.tool-card.tool-accent-2::before { background: linear-gradient(90deg, #fb923c, #ea580c); }
.tool-card.tool-accent-3::before { background: linear-gradient(90deg, #38bdf8, #0ea5e9); }
.tool-card.tool-accent-4::before { background: linear-gradient(90deg, #3b82f6, #2563eb); }

.tool-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow:
    0 24px 56px rgba(0, 0, 0, 0.55),
    0 0 48px rgba(99, 102, 241, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.08);
  border-color: rgba(129, 140, 248, 0.55);
  filter: saturate(1.2) contrast(1.06) drop-shadow(0 0 22px rgba(99, 102, 241, 0.4));
}

.tool-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  position: relative;
  z-index: 1;
}

.tool-icon {
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.25);
}

.tool-icon-light {
  background: rgba(255, 255, 255, 0.95);
  border-color: rgba(148, 163, 184, 0.3);
}

.tool-icon img {
  width: 28px;
  height: 28px;
  object-fit: contain;
  transition: transform 0.5s cubic-bezier(0.34, 1.4, 0.64, 1), filter 0.4s ease;
}

.tool-icon-light img {
  width: 32px;
  height: 32px;
}

.tool-card:hover .tool-icon img {
  transform: scale(1.14) rotate(-5deg);
  filter: drop-shadow(0 0 16px rgba(165, 180, 252, 0.85)) saturate(1.25);
}

.tool-circle-progress {
  position: relative;
  width: 56px;
  height: 56px;
}

.tool-circle-progress svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.circle-bg {
  fill: none;
  stroke: rgba(148, 163, 184, 0.2);
  stroke-width: 3;
}

.circle-fill {
  fill: none;
  stroke-width: 3;
  stroke-linecap: round;
  transition: none;
  filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.15));
}

.tool-accent-1 .circle-fill { stroke: #f59e0b; }
.tool-accent-2 .circle-fill { stroke: #ea580c; }
.tool-accent-3 .circle-fill { stroke: #0ea5e9; }
.tool-accent-4 .circle-fill { stroke: #3b82f6; }

.circle-value {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 12px;
  font-weight: 700;
  color: #e2e8f0;
}

.tool-card h3 {
  font-size: 15px;
  font-weight: 700;
  color: #e2e8f0;
  margin: 0;
  position: relative;
  z-index: 1;
}

.tool-progress {
  display: grid;
  gap: 6px;
  position: relative;
  z-index: 1;
}

.progress {
  height: 7px;
  background: rgba(148, 163, 184, 0.12);
  border-radius: 999px;
  overflow: hidden;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.35);
}

.progress-bar {
  height: 100%;
  border-radius: 999px;
  transition: none;
  position: relative;
  box-shadow: 0 0 14px rgba(255, 255, 255, 0.12);
}

.progress-bar::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    105deg,
    transparent 0%,
    rgba(255, 255, 255, 0.45) 48%,
    transparent 52%
  );
  transform: translateX(-120%);
  animation: progressShine 2.8s ease-in-out infinite;
}

@keyframes progressShine {
  0%,
  40% {
    transform: translateX(-120%);
  }
  60%,
  100% {
    transform: translateX(220%);
  }
}

.tool-card:hover .progress-bar::after {
  animation-duration: 1.4s;
}

.tool-accent-1 .progress-bar { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
.tool-accent-2 .progress-bar { background: linear-gradient(90deg, #fb923c, #ea580c); }
.tool-accent-3 .progress-bar { background: linear-gradient(90deg, #38bdf8, #0ea5e9); }
.tool-accent-4 .progress-bar { background: linear-gradient(90deg, #60a5fa, #3b82f6); }

/* Projects section */
.projects-section {
  margin-top: 48px;
  padding-top: 36px;
  border-top: 1px solid rgba(148, 163, 184, 0.15);
}

.projects-title {
  margin: 10px 0 8px;
}

.projects-subtitle {
  margin-bottom: 8px;
}

.projects-see-all {
  margin: 0 0 20px;
}

.link-all-projects {
  display: inline-block;
  font-size: 14px;
  font-weight: 600;
  color: #93c5fd;
  text-decoration: none;
  transition: color 0.2s ease, transform 0.2s ease;
}

.link-all-projects:hover {
  color: #bfdbfe;
  transform: translateX(4px);
}

.project-grid {
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  position: relative;
}

.project-card {
  background: rgba(15, 23, 42, 0.82);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(148, 163, 184, 0.15);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.35s cubic-bezier(0.34, 1.15, 0.64, 1),
    box-shadow 0.35s ease,
    border-color 0.25s ease;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(8px);
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 22px 48px rgba(0, 0, 0, 0.48);
  border-color: rgba(96, 165, 250, 0.28);
}

.project-image-wrap {
  aspect-ratio: 16 / 10;
  background: rgba(30, 41, 59, 0.6);
  overflow: hidden;
  isolation: isolate;
}

.project-image-wrap--affiche {
  aspect-ratio: 4 / 3;
  background: linear-gradient(145deg, #1e293b, #0f172a);
}

.project-image-wrap--affiche .project-image {
  object-fit: contain;
  padding: 8px;
}

.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.55s cubic-bezier(0.4, 0, 0.2, 1),
    filter 0.45s ease;
  will-change: transform;
}

.project-card:hover .project-image {
  transform: scale(1.05);
  filter: brightness(1.08) saturate(1.12) contrast(1.03);
}

.project-image-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: rgba(148, 163, 184, 0.5);
}

.project-image-placeholder svg {
  width: 48px;
  height: 48px;
}

.project-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.project-title {
  font-size: 17px;
  font-weight: 700;
  color: #e2e8f0;
  margin: 0;
}

.project-desc {
  font-size: 14px;
  color: rgba(226, 232, 240, 0.75);
  line-height: 1.5;
  margin: 0;
  flex: 1;
}

.project-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.project-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  color: #fff;
  border: none;
}

.project-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

.project-btn.secondary {
  background: rgba(30, 41, 59, 0.9);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.35);
}

.project-btn.secondary:hover {
  background: rgba(59, 130, 246, 0.2);
}

.project-btn svg {
  width: 16px;
  height: 16px;
}

.projects-empty {
  text-align: center;
  color: rgba(226, 232, 240, 0.6);
  padding: 32px;
}

@media (max-width: 700px) {
  .skills-shell {
    padding: 24px;
  }

  .tabs {
    max-width: 100%;
    grid-template-columns: 1fr;
    gap: 6px;
  }

  .tabs::before {
    display: none;
  }

  .tab {
    text-align: center;
  }

  .tab.active {
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    box-shadow: 0 8px 18px rgba(79, 70, 229, 0.35);
  }

  .projects-section {
    margin-top: 36px;
    padding-top: 28px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tabs::before {
    transition: none;
  }

  .skills-tools-aurora {
    animation: none;
    filter: blur(28px) hue-rotate(0deg);
  }

  .tool-card {
    animation: none;
  }

  .progress-bar::after {
    animation: none;
  }

  .tool-card:hover {
    filter: none;
    transform: translateY(-4px);
  }

  .tool-card:hover .tool-icon img {
    transform: none;
    filter: none;
  }

  .project-card:hover .project-image {
    transform: none;
    filter: none;
  }
}
</style>
