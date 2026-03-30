<template>
  <section class="projects-page">
    <div class="projects-hero projects-hero--video">
      <div class="projects-hero-media" aria-hidden="true">
        <video
          class="projects-hero-video"
          :src="heroBannerVideoUrl"
          autoplay
          muted
          loop
          playsinline
          webkit-playsinline
        />
        <div class="projects-hero-scrim" />
      </div>
      <div class="projects-hero-content">
        <span class="pill">Portfolio</span>
        <h1 class="page-title">Mes projets</h1>
        <p class="muted page-intro">
          Chaque projet est présenté sous forme de mini étude : contexte, problème, solution, résultat — avec des textes courts et lisibles.
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
        :to="{ path: '/mes-projets', query: {} }"
        class="filter-chip-clear"
      >
        Réinitialiser
      </RouterLink>
    </div>

    <template v-for="section in projectSections" :key="section.key">
      <div class="projects-block">
        <h2 class="section-heading">{{ section.title }}</h2>
        <p class="section-sub muted">{{ section.subtitle }}</p>
        <TransitionGroup
          name="list-stagger"
          tag="div"
          class="project-grid"
        >
          <article
            v-for="(project, idx) in section.items"
            :key="project.id"
            class="project-card"
            :class="[
              `project-accent-${(idx % 4) + 1}`,
              { 'project-card--affiche': section.key === 'graphisme' },
            ]"
          >
            <div
              class="project-image-wrap"
              :class="{ 'project-image-wrap--affiche': section.key === 'graphisme' }"
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
              <h2 class="project-title">{{ project.titre }}</h2>
              <div v-if="project.contexte" class="project-case">
                <div class="case-block">
                  <span class="case-label">Contexte</span>
                  <p class="case-text">{{ project.contexte }}</p>
                </div>
                <div class="case-block">
                  <span class="case-label">Problème</span>
                  <p class="case-text">{{ project.probleme }}</p>
                </div>
                <div class="case-block">
                  <span class="case-label">Solution</span>
                  <p class="case-text">{{ project.solution }}</p>
                </div>
                <div class="case-block">
                  <span class="case-label">Résultat</span>
                  <p class="case-text">{{ project.resultat }}</p>
                </div>
              </div>
              <p v-else class="project-desc">{{ truncateDesc(project.description, 220) }}</p>
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
                  v-if="section.key === 'graphisme' && project.image"
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
      </div>
    </template>

    <p v-if="!projectSections.length" class="projects-empty">
      {{ searchQuery ? "Aucun projet ne correspond à votre recherche." : "Aucun projet pour le moment." }}
    </p>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { projets, projetsGraphisme } from "../data/static";

const route = useRoute();
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

const searchQuery = computed(() => (route.query.q || "").trim().toLowerCase());

const heroBannerVideoUrl = computed(() => {
  const b = base.endsWith("/") ? base : `${base}/`;
  return `${b}videos/les-projets.mp4`;
});

const truncateDesc = (text, max = 120) => {
  if (!text) return "";
  return text.length > max ? text.slice(0, max).trim() + "…" : text;
};

function projectSearchText(p) {
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

const filterList = (list) => {
  const q = searchQuery.value;
  if (!q) return list;
  return list.filter((p) => projectSearchText(p).includes(q));
};

const projectSections = computed(() => {
  const web = filterList(projets);
  const graph = filterList(projetsGraphisme);
  const out = [];
  if (web.length) {
    out.push({
      key: "web",
      title: "Projets web & digital",
      subtitle: "Sites, applications et interfaces — études de cas synthétiques.",
      items: web,
    });
  }
  if (graph.length) {
    out.push({
      key: "graphisme",
      title: "Graphisme & affiches",
      subtitle: "Logos, affiches et visuels — même structure (contexte à résultat).",
      items: graph,
    });
  }
  return out;
});
</script>

<style scoped>
.projects-page {
  padding: 32px 0 48px;
}

.projects-hero {
  margin-bottom: 36px;
}

.projects-hero--video {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  border: 1px solid rgba(59, 130, 246, 0.25);
  box-shadow: 0 24px 48px rgba(2, 6, 23, 0.55);
  min-height: min(52vh, 420px);
  display: grid;
  align-items: center;
  justify-items: center;
}

.projects-hero-media {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.projects-hero-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.projects-hero-scrim {
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

.projects-hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 640px;
  margin: 0 auto;
  padding: clamp(28px, 6vw, 48px) clamp(20px, 4vw, 32px);
}

.projects-hero--video .pill {
  margin-bottom: 12px;
  background: rgba(15, 23, 42, 0.55);
  border-color: rgba(147, 197, 253, 0.45);
  backdrop-filter: blur(8px);
}

.projects-hero--video .page-title {
  text-shadow: 0 2px 24px rgba(0, 0, 0, 0.45);
}

.projects-hero--video .page-intro {
  text-shadow: 0 1px 12px rgba(0, 0, 0, 0.35);
  color: rgba(241, 245, 249, 0.92);
}

@media (prefers-reduced-motion: reduce) {
  .projects-hero-video {
    display: none;
  }

  .projects-hero--video {
    background: linear-gradient(145deg, #1e293b 0%, #0f172a 55%, #020617 100%);
    min-height: 280px;
  }

  .projects-hero-scrim {
    opacity: 0.35;
  }
}

.projects-block {
  margin-bottom: 48px;
}

.projects-block:last-of-type {
  margin-bottom: 0;
}

.section-heading {
  font-size: clamp(20px, 3vw, 26px);
  font-weight: 700;
  color: #e2e8f0;
  margin: 0 0 6px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.2);
}

.section-sub {
  font-size: 14px;
  margin: 0 0 20px;
}

.pill {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  margin-bottom: 12px;
}

.page-title {
  font-size: clamp(28px, 4vw, 40px);
  font-weight: 700;
  color: #e2e8f0;
  margin: 0 0 12px;
}

.page-intro {
  font-size: 16px;
  line-height: 1.6;
  margin: 0;
}

.muted {
  color: rgba(226, 232, 240, 0.65);
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
  margin: 0 0 2px;
  line-height: 1.25;
}

.project-case {
  display: grid;
  gap: 10px;
  margin-top: 6px;
  flex: 1;
}

.case-block {
  display: grid;
  gap: 3px;
}

.case-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #93c5fd;
}

.case-text {
  font-size: 13px;
  line-height: 1.45;
  color: rgba(226, 232, 240, 0.82);
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
  padding: 48px 24px;
}

@media (max-width: 700px) {
  .projects-page {
    padding: 20px 0 36px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .project-card:hover .project-image {
    transform: none;
    filter: none;
  }
}
</style>
