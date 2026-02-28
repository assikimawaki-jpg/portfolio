<template>
  <section class="skills-shell">
    <div class="skills-header">
      <span class="pill">Compétences</span>
      <h2 class="title">Outils & Technologies</h2>
      <p class="muted">
        Les logiciels et technologies que j'utilise quotidiennement pour créer
        des expériences numériques exceptionnelles.
      </p>
    </div>

    <div class="tabs">
      <button
        v-for="tab in tabs"
        :key="tab"
        class="tab"
        :class="{ active: activeTab === tab }"
        @click="activeTab = tab"
      >
        {{ tab }}
      </button>
    </div>

    <div class="tool-grid">
      <div
        v-for="(tool, idx) in activeTools"
        :key="tool.name"
        class="tool-card"
        :class="`tool-accent-${(idx % 4) + 1}`"
      >
        <div class="tool-header">
          <div class="tool-icon">
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
                :stroke-dasharray="`${tool.level} 100`"
                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              />
            </svg>
            <span class="circle-value">{{ tool.level }}%</span>
          </div>
        </div>
        <h3>{{ tool.name }}</h3>
        <div class="tool-progress">
          <div class="progress">
            <div class="progress-bar" :style="{ width: `${tool.level}%` }"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="projects-section">
      <span class="pill">Portfolio</span>
      <h2 class="projects-title">Projets récents</h2>
      <p class="muted projects-subtitle">
        Découvrez quelques réalisations qui illustrent mon expertise.
      </p>
      <div class="project-grid">
        <article
          v-for="(project, idx) in projects"
          :key="project.id"
          class="project-card"
          :class="`project-accent-${(idx % 4) + 1}`"
        >
          <div class="project-image-wrap">
            <img
              v-if="project.image"
              :src="projectImageUrl(project.image)"
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
            </div>
          </div>
        </article>
      </div>
      <p v-if="!projects.length && !loadingProjects" class="projects-empty">
        Aucun projet pour le moment.
      </p>
    </div>
  </section>
</template>

<script setup>
import { computed, ref, onMounted } from "vue";
import api from "../services/api";
import { resolveMediaUrl } from "../services/media";

const tabs = ["Design", "Développement", "Motion & 3D"];
const activeTab = ref("Design");

const toolsFromApi = ref([]);
const loading = ref(true);
const projects = ref([]);
const loadingProjects = ref(true);

const projectImageUrl = (url) => resolveMediaUrl(url);
const truncateDesc = (text, max = 120) => {
  if (!text) return "";
  return text.length > max ? text.slice(0, max).trim() + "…" : text;
};

const fallbackTools = [
  {
    category: "Design",
    items: [
      { name: "Adobe Photoshop", level: 90, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg" },
      { name: "Adobe Illustrator", level: 95, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg" },
      { name: "Adobe InDesign", level: 85, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/indesign/indesign-plain.svg" },
      { name: "Figma", level: 95, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" },
      { name: "Sketch", level: 80, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sketch/sketch-original.svg" },
    ],
  },
  {
    category: "Développement",
    items: [
      { name: "HTML/CSS", level: 90, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" },
      { name: "JavaScript", level: 85, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" },
      { name: "React", level: 80, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" },
      { name: "WordPress", level: 85, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/wordpress/wordpress-plain.svg" },
      { name: "Git", level: 75, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" },
    ],
  },
  {
    category: "Motion & 3D",
    items: [
      { name: "Adobe After Effects", level: 85, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/aftereffects/aftereffects-plain.svg" },
      { name: "Adobe Premiere Pro", level: 80, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/premierepro/premierepro-plain.svg" },
      { name: "Cinema 4D", level: 70, icon: "https://www.svgrepo.com/show/373543/cinema-4d.svg" },
      { name: "Blender", level: 65, icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/blender/blender-original.svg" },
      { name: "Lottie", level: 85, icon: "https://framerusercontent.com/images/27k5A6CzdmGNNnh9WlkdtSdQfd8.svg" },
    ],
  },
];

const tools = computed(() => {
  if (toolsFromApi.value.length) return toolsFromApi.value;
  return fallbackTools;
});

const activeTools = computed(() => {
  return tools.value.find((t) => t.category === activeTab.value)?.items || [];
});

onMounted(async () => {
  try {
    const res = await api.get("competences/");
    const raw = res.data?.results || res.data || [];
    const byCategory = {};
    for (const c of raw) {
      const cat = c.categorie || "Développement";
      if (!byCategory[cat]) byCategory[cat] = [];
      byCategory[cat].push({
        name: c.nom,
        level: c.pourcentage ?? 0,
        icon: c.icon || "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
      });
    }
    toolsFromApi.value = Object.entries(byCategory).map(([category, items]) => ({ category, items }));
  } catch {
    toolsFromApi.value = [];
  } finally {
    loading.value = false;
  }

  try {
    const projRes = await api.get("projets/");
    projects.value = projRes.data?.results || projRes.data || [];
  } catch {
    projects.value = [];
  } finally {
    loadingProjects.value = false;
  }
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

.skills-header {
  text-align: center;
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

.tabs {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(12, 24, 60, 0.9);
  padding: 6px;
  border-radius: 12px;
  border: 1px solid rgba(59, 130, 246, 0.25);
  justify-self: center;
}

.tab {
  background: transparent;
  color: rgba(226, 232, 240, 0.7);
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.tab.active {
  background: #4f46e5;
  color: #fff;
  box-shadow: 0 8px 18px rgba(79, 70, 229, 0.35);
}

.tool-grid {
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

.tool-card {
  background: rgba(15, 23, 42, 0.8);
  border-radius: 16px;
  padding: 20px;
  border: 1px solid rgba(148, 163, 184, 0.15);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  display: grid;
  gap: 14px;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  position: relative;
  overflow: hidden;
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
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
}

.tool-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
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

.tool-icon img {
  width: 28px;
  height: 28px;
  object-fit: contain;
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
  transition: stroke-dasharray 0.6s ease;
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
}

.tool-progress {
  display: grid;
  gap: 6px;
}

.progress {
  height: 6px;
  background: rgba(148, 163, 184, 0.15);
  border-radius: 999px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  border-radius: 999px;
  transition: width 0.5s ease;
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
  margin-bottom: 24px;
}

.project-grid {
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.project-card {
  background: rgba(15, 23, 42, 0.8);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(148, 163, 184, 0.15);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
}

.project-image-wrap {
  aspect-ratio: 16 / 10;
  background: rgba(30, 41, 59, 0.6);
  overflow: hidden;
}

.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }

  .projects-section {
    margin-top: 36px;
    padding-top: 28px;
  }
}
</style>
