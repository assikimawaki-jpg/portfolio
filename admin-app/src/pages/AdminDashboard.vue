<template>
  <div class="admin-layout container">
    <aside class="sidebar admin-sidebar">
      <div>
        <h3>Smart Admin</h3>
        <p class="subtitle">Gestion du portfolio</p>
      </div>
      <nav>
        <button
          :class="{ active: activeSection === 'overview' }"
          @click="activeSection = 'overview'"
        >
          Dashboard
        </button>
        <button
          :class="{ active: activeSection === 'competences' }"
          @click="activeSection = 'competences'"
        >
          Compétences
        </button>
        <button
          :class="{ active: activeSection === 'projets' }"
          @click="activeSection = 'projets'"
        >
          Projets
        </button>
        <button
          :class="{ active: activeSection === 'parcours' }"
          @click="activeSection = 'parcours'"
        >
          Parcours
        </button>
        <button
          :class="{ active: activeSection === 'profil' }"
          @click="activeSection = 'profil'"
        >
          Profil
        </button>
        <button
          :class="{ active: activeSection === 'messages' }"
          @click="activeSection = 'messages'"
        >
          Messages
        </button>
      </nav>
      <button class="button secondary" @click="logout">Déconnexion</button>
    </aside>

    <section class="content">
      <header class="topbar">
        <div>
          <h1>Dashboard</h1>
          <p class="subtitle">Bienvenue, gérez votre portfolio en un coup d'œil.</p>
        </div>
        <div class="topbar-actions">
          <div class="search" :class="{ open: showSearch }">
            <input v-model="searchQuery" type="text" placeholder="Rechercher..." />
          </div>
          <button class="icon-button" aria-label="Recherche" @click="toggleSearch">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M21 21l-4.3-4.3m1.3-5.7a7 7 0 11-14 0 7 7 0 0114 0z"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </button>
          <button class="icon-button notification" aria-label="Notifications">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M15 17h5l-1.4-1.4A2 2 0 0118 14.2V11a6 6 0 10-12 0v3.2a2 2 0 01-.6 1.4L4 17h5"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M9.5 19a2.5 2.5 0 005 0"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
                stroke-linecap="round"
              />
            </svg>
            <span v-if="unreadCount" class="badge-dot">{{ unreadCount }}</span>
          </button>
          <div class="profile">
            <div class="avatar">
              <img :src="profileImage" alt="Photo de profil" />
            </div>
            <div>
              <strong class="profile-name">Salem Swift</strong>
              <p class="role">Manager</p>
            </div>
          </div>
        </div>
      </header>

      <div v-if="activeSection === 'overview'" class="overview">
        <div class="stats-grid">
          <div
            class="card stat-card glass float clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'messages'"
          >
            <div>
              <p class="muted">Messages</p>
              <p class="stat">{{ messages.length }}</p>
              <small>{{ unreadCount }} non lus</small>
            </div>
            <div class="stat-ring">
              <svg viewBox="0 0 36 36">
                <path
                  class="ring-bg"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  class="ring"
                  stroke-dasharray="92, 100"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <text x="18" y="20.35" class="ring-text">92%</text>
              </svg>
            </div>
          </div>
          <div
            class="card stat-card glass float clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'competences'"
          >
            <div>
              <p class="muted">Compétences</p>
              <p class="stat">{{ competences.length }}</p>
              <small>Catégories actives</small>
            </div>
            <div class="stat-ring">
              <svg viewBox="0 0 36 36">
                <path
                  class="ring-bg"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  class="ring"
                  stroke-dasharray="78, 100"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <text x="18" y="20.35" class="ring-text">78%</text>
              </svg>
            </div>
          </div>
          <div
            class="card stat-card glass float clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'projets'"
          >
            <div>
              <p class="muted">Projets</p>
              <p class="stat">{{ projets.length }}</p>
              <small>En ligne</small>
            </div>
            <div class="stat-ring">
              <svg viewBox="0 0 36 36">
                <path
                  class="ring-bg"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  class="ring"
                  stroke-dasharray="64, 100"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <text x="18" y="20.35" class="ring-text">64%</text>
              </svg>
            </div>
          </div>
        </div>

        <div class="overview-grid">
          <div
            class="card highlight-card glow clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'projets'"
          >
            <div>
              <p class="badge">Focus</p>
              <h3>Optimisez votre présence</h3>
              <p class="muted">
                Ajoutez régulièrement des projets et mettez à jour vos compétences
                pour améliorer votre visibilité.
              </p>
            </div>
            <button class="button">Ajouter un projet</button>
          </div>

          <div
            class="card glass clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'messages'"
          >
            <div class="section-header">
              <h3>Derniers messages</h3>
              <small class="muted">5 derniers</small>
            </div>
            <ul class="list">
              <li v-for="message in latestMessages" :key="message.id">
                <div>
                  <strong>{{ message.nom }}</strong>
                  <p class="muted">{{ message.sujet }}</p>
                </div>
                <span class="badge">{{ message.lu ? "Lu" : "Non lu" }}</span>
              </li>
              <li v-if="!latestMessages.length" class="muted">Aucun message.</li>
            </ul>
          </div>

          <div
            class="card glass clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'projets'"
          >
            <div class="section-header">
              <h3>Projets récents</h3>
              <small class="muted">5 derniers</small>
            </div>
            <ul class="list">
              <li v-for="project in latestProjects" :key="project.id">
                <div>
                  <strong>{{ project.titre }}</strong>
                  <p class="muted">{{ project.date_creation }}</p>
                </div>
                <span class="badge">{{ project.lien_demo ? "Demo" : "Draft" }}</span>
              </li>
              <li v-if="!latestProjects.length" class="muted">Aucun projet.</li>
            </ul>
          </div>

          <div
            class="card glass clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'competences'"
          >
            <div class="section-header">
              <h3>Performance</h3>
              <small class="muted">Ce mois</small>
            </div>
            <div class="bars">
              <div v-for="bar in performanceBars" :key="bar.label" class="bar">
                <div class="bar-label">
                  <span>{{ bar.label }}</span>
                  <small>{{ bar.value }}%</small>
                </div>
                <div class="bar-track">
                  <div class="bar-fill" :style="{ width: `${bar.value}%` }"></div>
                </div>
              </div>
            </div>
          </div>

          <div
            class="card glass clickable"
            role="button"
            tabindex="0"
            @click="activeSection = 'messages'"
          >
            <div class="section-header">
              <h3>Agenda</h3>
              <small class="muted">Aujourd'hui</small>
            </div>
            <ul class="timeline">
              <li>
                <span class="dot"></span>
                <div>
                  <strong>Mise à jour des compétences</strong>
                  <p class="muted">09:00 - 10:00</p>
                </div>
              </li>
              <li>
                <span class="dot"></span>
                <div>
                  <strong>Publication d'un projet</strong>
                  <p class="muted">14:00 - 15:00</p>
                </div>
              </li>
              <li>
                <span class="dot"></span>
                <div>
                  <strong>Réponse aux messages</strong>
                  <p class="muted">16:30 - 17:30</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div v-if="activeSection === 'competences'" class="card panel">
        <div class="section-header">
          <h3>Compétences</h3>
          <button class="button" @click="openSkillModal()">Ajouter</button>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th>Nom</th>
              <th>Catégorie</th>
              <th>Niveau</th>
              <th>%</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="skill in filteredCompetences" :key="skill.id">
              <td>
                <div class="skill-cell">
                  <img v-if="skill.icon" :src="skill.icon" :alt="skill.nom" class="skill-icon" />
                  <span>{{ skill.nom }}</span>
                </div>
              </td>
              <td>{{ skill.categorie }}</td>
              <td>{{ skill.niveau }}</td>
              <td>{{ skill.pourcentage }}%</td>
              <td>
                <button class="button secondary" @click="openSkillModal(skill)">
                  Éditer
                </button>
                <button class="button secondary danger" @click="deleteSkill(skill.id)">
                  Supprimer
                </button>
              </td>
            </tr>
            <tr v-if="!filteredCompetences.length">
              <td colspan="5" class="empty-state">
                Aucune compétence. Cliquez sur « Ajouter » pour en créer une.
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="activeSection === 'parcours'" class="card panel">
        <div class="section-header">
          <h3>Parcours professionnel</h3>
          <button class="button" @click="openParcoursModal()">Ajouter</button>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Titre</th>
              <th>Lieu</th>
              <th>Localisation</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in parcours" :key="p.id">
              <td>{{ p.date }}</td>
              <td>{{ p.titre }}</td>
              <td>{{ p.lieu }}</td>
              <td>{{ p.localisation }}</td>
              <td>
                <button class="button secondary" @click="openParcoursModal(p)">Éditer</button>
                <button class="button secondary danger" @click="deleteParcours(p.id)">Supprimer</button>
              </td>
            </tr>
            <tr v-if="!parcours.length">
              <td colspan="5" class="empty-state">Aucune étape. Cliquez sur « Ajouter » pour en créer une.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="activeSection === 'projets'" class="card panel">
        <div class="section-header">
          <h3>Projets</h3>
          <button class="button" @click="openProjectModal()">Ajouter</button>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th>Titre</th>
              <th>Date</th>
              <th>Demo</th>
              <th>GitHub</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="project in filteredProjets" :key="project.id">
              <td>{{ project.titre }}</td>
              <td>{{ project.date_creation }}</td>
              <td>{{ project.lien_demo || "-" }}</td>
              <td>{{ project.lien_github || "-" }}</td>
              <td>
                <button class="button secondary" @click="openProjectModal(project)">
                  Éditer
                </button>
                <button class="button secondary" @click="deleteProject(project.id)">
                  Supprimer
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="activeSection === 'profil'" class="card panel">
        <h3>Profil</h3>
        <form class="form" @submit.prevent="saveProfil">
          <label>
            Nom
            <input v-model="profilForm.nom" type="text" required />
          </label>
          <label>
            Titre
            <input v-model="profilForm.titre_professionnel" type="text" required />
          </label>
          <label>
            Bio
            <textarea v-model="profilForm.bio" rows="5" required></textarea>
          </label>
          <label>
            Email
            <input v-model="profilForm.email" type="email" required />
          </label>
          <label>
            Téléphone
            <input v-model="profilForm.telephone" type="text" />
          </label>
          <label>
            LinkedIn
            <input v-model="profilForm.linkedin" type="url" />
          </label>
          <label>
            GitHub
            <input v-model="profilForm.github" type="url" />
          </label>
          <label>
            Photo
            <input type="file" @change="onProfilPhotoChange" />
          </label>
          <label>
            CV (PDF)
            <input type="file" @change="onProfilCvChange" />
          </label>
          <button class="button" type="submit" :disabled="saving">
          {{ saving ? "Enregistrement…" : "Enregistrer" }}
        </button>
        </form>
      </div>

      <div v-if="activeSection === 'messages'" class="card panel">
        <h3>Messages reçus</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Nom</th>
              <th>Email</th>
              <th>Sujet</th>
              <th>Date</th>
              <th>Lu</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="message in filteredMessages" :key="message.id">
              <td>{{ message.nom }}</td>
              <td>{{ message.email }}</td>
              <td>{{ message.sujet }}</td>
              <td>{{ formatDate(message.date_envoi) }}</td>
              <td>
                <span class="badge">{{ message.lu ? "Lu" : "Non lu" }}</span>
              </td>
              <td>
                <button
                  class="button secondary"
                  @click="markMessageAsRead(message)"
                  :disabled="message.lu"
                >
                  Marquer lu
                </button>
                <button class="button secondary" @click="openReplyMail(message)">
                  Répondre
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>

  <div v-if="showSkillModal" class="modal-backdrop">
    <div class="modal">
      <h3>{{ skillForm.id ? "Modifier" : "Ajouter" }} une compétence</h3>
      <form class="form" @submit.prevent="saveSkill">
        <label>
          Nom
          <input v-model="skillForm.nom" type="text" placeholder="ex: Figma, React..." required />
        </label>
        <label>
          Catégorie
          <select v-model="skillForm.categorie" required>
            <option value="">Sélectionner...</option>
            <option value="Design">Design</option>
            <option value="Développement">Développement</option>
            <option value="Motion & 3D">Motion & 3D</option>
          </select>
        </label>
        <label>
          Niveau
          <select v-model="skillForm.niveau" required>
            <option value="debutant">Débutant</option>
            <option value="intermediaire">Intermédiaire</option>
            <option value="avance">Avancé</option>
            <option value="expert">Expert</option>
          </select>
        </label>
        <label>
          Pourcentage (0-100)
          <input v-model.number="skillForm.pourcentage" type="number" min="0" max="100" required />
        </label>
        <label>
          URL de l'icône
          <input v-model="skillForm.icon" type="url" placeholder="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/..." />
        </label>
        <div class="modal-actions">
          <button class="button" type="submit" :disabled="saving">
            {{ saving ? "Enregistrement…" : "Enregistrer" }}
          </button>
          <button class="button secondary" type="button" :disabled="saving" @click="closeSkillModal">
            Annuler
          </button>
        </div>
      </form>
    </div>
  </div>

  <div v-if="showProjectModal" class="modal-backdrop">
    <div class="modal">
      <h3>{{ projectForm.id ? "Modifier" : "Ajouter" }} un projet</h3>
      <form class="form" @submit.prevent="saveProject">
        <label>
          Titre
          <input v-model="projectForm.titre" type="text" required />
        </label>
        <label>
          Description
          <textarea v-model="projectForm.description" rows="4" required></textarea>
        </label>
        <label>
          Date de création
          <input v-model="projectForm.date_creation" type="date" required />
        </label>
        <label>
          Lien démo
          <input v-model="projectForm.lien_demo" type="url" />
        </label>
        <label>
          Lien GitHub
          <input v-model="projectForm.lien_github" type="url" />
        </label>
        <label>
          Image
          <input type="file" @change="onProjectImageChange" />
        </label>
        <div class="modal-actions">
          <button class="button" type="submit" :disabled="saving">
            {{ saving ? "Enregistrement…" : "Enregistrer" }}
          </button>
          <button class="button secondary" type="button" :disabled="saving" @click="closeProjectModal">
            Annuler
          </button>
        </div>
      </form>
    </div>
  </div>

  <div v-if="showParcoursModal" class="modal-backdrop">
    <div class="modal">
      <h3>{{ parcoursForm.id ? "Modifier" : "Ajouter" }} une étape</h3>
      <form class="form" @submit.prevent="saveParcours">
        <label>
          Date (ex: 2022 - Présent, 2019 - 2022)
          <input v-model="parcoursForm.date" type="text" placeholder="2022 - Présent" required />
        </label>
        <label>
          Titre
          <input v-model="parcoursForm.titre" type="text" placeholder="Directeur Créatif" required />
        </label>
        <label>
          Lieu / Entreprise
          <input v-model="parcoursForm.lieu" type="text" placeholder="Studio Design" required />
        </label>
        <label>
          Localisation
          <input v-model="parcoursForm.localisation" type="text" placeholder="Lomé, Togo" required />
        </label>
        <label>
          Description
          <textarea v-model="parcoursForm.description" rows="4" required></textarea>
        </label>
        <label>
          Ordre d'affichage (0 = premier)
          <input v-model.number="parcoursForm.ordre" type="number" min="0" />
        </label>
        <div class="modal-actions">
          <button class="button" type="submit" :disabled="saving">
            {{ saving ? "Enregistrement…" : "Enregistrer" }}
          </button>
          <button class="button secondary" type="button" :disabled="saving" @click="closeParcoursModal">
            Annuler
          </button>
        </div>
      </form>
    </div>
  </div>

</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";
import { useAuthStore } from "../stores/auth";
import profileImage from "../assets/profile.png";

const router = useRouter();
const authStore = useAuthStore();

const activeSection = ref("overview");
const showSearch = ref(false);
const searchQuery = ref("");
const competences = ref([]);
const projets = ref([]);
const parcours = ref([]);
const messages = ref([]);
const profil = ref(null);

const matchesQuery = (values) => {
  if (!searchQuery.value) return true;
  const query = searchQuery.value.toLowerCase();
  return values.some((value) =>
    String(value || "").toLowerCase().includes(query)
  );
};

const filteredCompetences = computed(() =>
  competences.value.filter((skill) =>
    matchesQuery([skill.nom, skill.categorie, skill.niveau])
  )
);

const filteredProjets = computed(() =>
  projets.value.filter((project) =>
    matchesQuery([project.titre, project.description, project.lien_demo])
  )
);

const filteredMessages = computed(() =>
  messages.value.filter((message) =>
    matchesQuery([message.nom, message.email, message.sujet, message.message])
  )
);

const latestMessages = computed(() => filteredMessages.value.slice(0, 5));
const latestProjects = computed(() => filteredProjets.value.slice(0, 5));
const unreadCount = computed(
  () => messages.value.filter((message) => !message.lu).length
);

const performanceBars = [
  { label: "Visites", value: 74 },
  { label: "Messages", value: 58 },
  { label: "Projets", value: 82 },
  { label: "Profil", value: 66 },
];

const toggleSearch = () => {
  showSearch.value = !showSearch.value;
  if (!showSearch.value) {
    searchQuery.value = "";
  }
};

const showSkillModal = ref(false);
const showProjectModal = ref(false);
const showParcoursModal = ref(false);
const saving = ref(false);

const skillForm = reactive({
  id: null,
  nom: "",
  niveau: "debutant",
  pourcentage: 0,
  categorie: "",
  icon: "",
});

const projectForm = reactive({
  id: null,
  titre: "",
  description: "",
  image: null,
  lien_demo: "",
  lien_github: "",
  date_creation: "",
});

const parcoursForm = reactive({
  id: null,
  date: "",
  titre: "",
  lieu: "",
  localisation: "",
  description: "",
  ordre: 0,
});

const profilForm = reactive({
  id: null,
  nom: "",
  titre_professionnel: "",
  bio: "",
  email: "",
  telephone: "",
  linkedin: "",
  github: "",
  photo: null,
  cv: null,
});

const fetchData = async () => {
  const [skillsRes, projectsRes, parcoursRes, messagesRes, profilRes] = await Promise.all([
    api.get("competences/"),
    api.get("projets/"),
    api.get("parcours/"),
    api.get("messages/"),
    api.get("profil/"),
  ]);

  competences.value = skillsRes.data?.results || skillsRes.data || [];
  projets.value = projectsRes.data?.results || projectsRes.data || [];
  parcours.value = parcoursRes.data?.results || parcoursRes.data || [];
  messages.value = messagesRes.data?.results || messagesRes.data || [];
  profil.value = profilRes.data?.results?.[0] || profilRes.data?.[0] || null;

  if (profil.value) {
    Object.assign(profilForm, {
      id: profil.value.id,
      nom: profil.value.nom,
      titre_professionnel: profil.value.titre_professionnel,
      bio: profil.value.bio,
      email: profil.value.email,
      telephone: profil.value.telephone,
      linkedin: profil.value.linkedin,
      github: profil.value.github,
      photo: null,
      cv: null,
    });
  }
};

const logout = () => {
  authStore.logout();
  router.push({ name: "admin-login" });
};

const openSkillModal = (skill = null) => {
  if (skill) {
    Object.assign(skillForm, skill);
  } else {
    Object.assign(skillForm, {
      id: null,
      nom: "",
      niveau: "debutant",
      pourcentage: 0,
      categorie: "",
      icon: "",
    });
  }
  showSkillModal.value = true;
};

const closeSkillModal = () => {
  showSkillModal.value = false;
};

const getApiErrorMessage = (err) => {
  const data = err.response?.data;
  if (!data) return err.message || "Erreur réseau";
  if (typeof data.detail === "string") return data.detail;
  if (typeof data === "object") {
    const parts = [];
    for (const [key, val] of Object.entries(data)) {
      const msg = Array.isArray(val) ? val.join(", ") : String(val);
      parts.push(`${key}: ${msg}`);
    }
    return parts.join("\n");
  }
  return "Erreur lors de l'enregistrement";
};

const saveSkill = async () => {
  saving.value = true;
  try {
    const payload = {
      nom: skillForm.nom,
      niveau: skillForm.niveau,
      pourcentage: skillForm.pourcentage,
      categorie: skillForm.categorie,
      icon: skillForm.icon || "",
    };
    if (skillForm.id) {
      await api.put(`competences/${skillForm.id}/`, payload);
    } else {
      await api.post("competences/", payload);
    }
    showSkillModal.value = false;
    await fetchData();
  } catch (err) {
    alert(getApiErrorMessage(err));
  } finally {
    saving.value = false;
  }
};

const deleteSkill = async (id) => {
  if (!confirm("Supprimer cette compétence ?")) return;
  try {
    await api.delete(`competences/${id}/`);
    await fetchData();
  } catch (err) {
    alert(err.response?.data?.detail || "Erreur lors de la suppression.");
  }
};

const openParcoursModal = (p = null) => {
  if (p) {
    Object.assign(parcoursForm, p);
  } else {
    Object.assign(parcoursForm, {
      id: null,
      date: "",
      titre: "",
      lieu: "",
      localisation: "",
      description: "",
      ordre: parcours.value.length,
    });
  }
  showParcoursModal.value = true;
};

const closeParcoursModal = () => {
  showParcoursModal.value = false;
};

const saveParcours = async () => {
  saving.value = true;
  try {
    const payload = {
      date: parcoursForm.date,
      titre: parcoursForm.titre,
      lieu: parcoursForm.lieu,
      localisation: parcoursForm.localisation,
      description: parcoursForm.description,
      ordre: parcoursForm.ordre ?? 0,
    };
    if (parcoursForm.id) {
      await api.put(`parcours/${parcoursForm.id}/`, payload);
    } else {
      await api.post("parcours/", payload);
    }
    showParcoursModal.value = false;
    await fetchData();
  } catch (err) {
    alert(getApiErrorMessage(err));
  } finally {
    saving.value = false;
  }
};

const deleteParcours = async (id) => {
  if (!confirm("Supprimer cette étape ?")) return;
  try {
    await api.delete(`parcours/${id}/`);
    await fetchData();
  } catch (err) {
    alert(getApiErrorMessage(err));
  }
};

const openProjectModal = (project = null) => {
  if (project) {
    Object.assign(projectForm, { ...project, image: null });
  } else {
    Object.assign(projectForm, {
      id: null,
      titre: "",
      description: "",
      image: null,
      lien_demo: "",
      lien_github: "",
      date_creation: "",
    });
  }
  showProjectModal.value = true;
};

const closeProjectModal = () => {
  showProjectModal.value = false;
};

const openReplyMail = (message) => {
  const subject = `Re: ${message.sujet || "Votre message"}`;
  const body = `Bonjour ${message.nom || ""},%0D%0A%0D%0A%0D%0A---%0D%0AMessage reçu:%0D%0A${encodeURIComponent(
    message.message || ""
  )}`;
  const mailto = `mailto:${encodeURIComponent(
    message.email
  )}?subject=${encodeURIComponent(subject)}&body=${body}`;
  window.open(mailto, "_blank");
};

const onProjectImageChange = (event) => {
  projectForm.image = event.target.files[0];
};

const saveProject = async () => {
  saving.value = true;
  try {
    const formData = new FormData();
    formData.append("titre", projectForm.titre);
    formData.append("description", projectForm.description);
    formData.append("date_creation", projectForm.date_creation);
    if (projectForm.lien_demo) formData.append("lien_demo", projectForm.lien_demo);
    if (projectForm.lien_github) formData.append("lien_github", projectForm.lien_github);
    if (projectForm.image) formData.append("image", projectForm.image);

    if (projectForm.id) {
      await api.put(`projets/${projectForm.id}/`, formData);
    } else {
      await api.post("projets/", formData);
    }
    showProjectModal.value = false;
    await fetchData();
  } catch (err) {
    alert(getApiErrorMessage(err));
  } finally {
    saving.value = false;
  }
};

const deleteProject = async (id) => {
  await api.delete(`projets/${id}/`);
  await fetchData();
};

const onProfilPhotoChange = (event) => {
  profilForm.photo = event.target.files[0];
};

const onProfilCvChange = (event) => {
  profilForm.cv = event.target.files[0];
};

const saveProfil = async () => {
  saving.value = true;
  try {
    const formData = new FormData();
    formData.append("nom", profilForm.nom);
    formData.append("titre_professionnel", profilForm.titre_professionnel);
    formData.append("bio", profilForm.bio);
    formData.append("email", profilForm.email);
    formData.append("telephone", profilForm.telephone || "");
    formData.append("linkedin", profilForm.linkedin || "");
    formData.append("github", profilForm.github || "");
    if (profilForm.photo) formData.append("photo", profilForm.photo);
    if (profilForm.cv) formData.append("cv", profilForm.cv);

    if (profilForm.id) {
      await api.put(`profil/${profilForm.id}/`, formData);
    } else {
      const response = await api.post("profil/", formData);
      profilForm.id = response.data.id;
    }
    await fetchData();
  } catch (err) {
    alert(getApiErrorMessage(err));
  } finally {
    saving.value = false;
  }
};

const markMessageAsRead = async (message) => {
  await api.patch(`messages/${message.id}/`, { lu: true });
  await fetchData();
};


const formatDate = (value) => {
  if (!value) return "-";
  return new Date(value).toLocaleDateString("fr-FR");
};

onMounted(fetchData);
</script>

<style scoped>
.admin-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 24px;
  align-items: start;
}

.sidebar {
  background: rgba(15, 23, 42, 0.85);
  padding: 24px;
  border-radius: 20px;
  height: fit-content;
  display: grid;
  gap: 18px;
  border: 1px solid rgba(148, 163, 184, 0.15);
  backdrop-filter: blur(16px);
  animation: sidebar-slide-in 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}

@keyframes sidebar-slide-in {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.sidebar nav {
  display: grid;
  gap: 8px;
}

.sidebar button {
  border: none;
  background: transparent;
  text-align: left;
  cursor: pointer;
  padding: 10px 14px;
  border-radius: 12px;
  color: inherit;
  transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
  position: relative;
}

.sidebar button::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 0;
  border-radius: 0 4px 4px 0;
  background: linear-gradient(180deg, #60a5fa, #3b82f6);
  transition: height 0.25s ease;
}

.sidebar button:hover {
  background: rgba(59, 130, 246, 0.1);
  color: #bfdbfe;
}

.sidebar button:hover::before {
  height: 60%;
}

.sidebar button.active {
  background: rgba(59, 130, 246, 0.2);
  color: #bfdbfe;
}

.sidebar button.active::before {
  height: 70%;
}

.content {
  display: grid;
  gap: 24px;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 18px 22px;
  border-radius: 20px;
  animation: topbar-fade-in 0.5s cubic-bezier(0.22, 1, 0.36, 1);
  background: rgba(17, 19, 23, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(12px);
}

@keyframes topbar-fade-in {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.search {
  width: 0;
  overflow: hidden;
  transition: width 0.25s ease;
}

.search input {
  width: 220px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(30, 32, 38, 0.8);
  padding: 8px 14px;
  color: inherit;
}

.search.open {
  width: 220px;
}

.icon-button {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(30, 32, 38, 0.8);
  color: rgba(226, 232, 240, 0.85);
  cursor: pointer;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.icon-button:hover {
  transform: translateY(-1px);
  border-color: rgba(59, 130, 246, 0.4);
}

.icon-button svg {
  width: 18px;
  height: 18px;
}

.notification {
  position: relative;
}

.badge-dot {
  position: absolute;
  top: -6px;
  right: -6px;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  border-radius: 999px;
  background: #ef4444;
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  display: grid;
  place-items: center;
  border: 2px solid rgba(17, 19, 23, 0.92);
}

.profile {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(30, 32, 38, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #60a5fa, #38bdf8);
  color: #0f172a;
  font-weight: 700;
  overflow: hidden;
}

.profile-name {
  font-size: 13px;
  font-weight: 600;
}

.role {
  margin: 0;
  font-size: 11px;
  color: rgba(226, 232, 240, 0.6);
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.overview {
  display: grid;
  gap: 24px;
  animation: overview-fade-in 0.6s cubic-bezier(0.22, 1, 0.36, 1);
}

@keyframes overview-fade-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.stats-grid {
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.stat-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 140px;
  animation: stat-card-in 0.5s cubic-bezier(0.22, 1, 0.36, 1) backwards;
}

.stats-grid .stat-card:nth-child(1) { animation-delay: 0.05s; }
.stats-grid .stat-card:nth-child(2) { animation-delay: 0.1s; }
.stats-grid .stat-card:nth-child(3) { animation-delay: 0.15s; }
.stats-grid .stat-card:nth-child(4) { animation-delay: 0.2s; }

@keyframes stat-card-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.stat-ring {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 700;
}

.stat-ring svg {
  width: 100%;
  height: 100%;
}

.ring-bg {
  fill: none;
  stroke: rgba(148, 163, 184, 0.2);
  stroke-width: 3.2;
}

.ring {
  fill: none;
  stroke: #60a5fa;
  stroke-width: 3.2;
  stroke-linecap: round;
  animation: ring-fill 1.2s ease forwards;
}

.ring-text {
  fill: #e2e8f0;
  font-size: 8px;
  text-anchor: middle;
}

.overview-grid {
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

.clickable {
  cursor: pointer;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.clickable:hover {
  transform: translateY(-4px);
  border-color: rgba(59, 130, 246, 0.35);
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.35), 0 0 24px rgba(59, 130, 246, 0.08);
}

.clickable:focus {
  outline: 2px solid rgba(59, 130, 246, 0.6);
  outline-offset: 2px;
}

.highlight-card {
  display: grid;
  gap: 16px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.35), rgba(15, 23, 42, 0.6));
}

.list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 12px;
}

.list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.15);
}

.list li:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.muted {
  color: rgba(226, 232, 240, 0.7);
}

.bars {
  display: grid;
  gap: 14px;
}

.bar-label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 6px;
}

.bar-track {
  background: rgba(148, 163, 184, 0.15);
  border-radius: 999px;
  height: 8px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #38bdf8, #3b82f6);
  border-radius: 999px;
  animation: bar-fill 1.2s ease;
}

.timeline {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 14px;
}

.timeline li {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.timeline .dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #60a5fa;
  margin-top: 6px;
  box-shadow: 0 0 10px rgba(96, 165, 250, 0.8);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.stat {
  font-size: 32px;
  font-weight: 700;
}

.form {
  display: grid;
  gap: 12px;
}

input,
textarea,
select {
  width: 100%;
  padding: 10px 12px;
  border-radius: 8px;
  border: 1px solid rgba(148, 163, 184, 0.2);
  background: rgba(15, 23, 42, 0.7);
  color: inherit;
  margin-top: 4px;
}

.skill-cell {
  display: flex;
  align-items: center;
  gap: 10px;
}

.skill-icon {
  width: 28px;
  height: 28px;
  object-fit: contain;
  border-radius: 6px;
}

.empty-state {
  text-align: center;
  padding: 24px;
  color: rgba(226, 232, 240, 0.6);
}

.button.danger {
  color: #f87171;
  border-color: rgba(248, 113, 113, 0.4);
}

.button.danger:hover {
  background: rgba(248, 113, 113, 0.15);
}

.modal-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 12px;
}

.panel {
  animation: panel-reveal 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}

@keyframes panel-reveal {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.float {
  animation: float 6s ease-in-out infinite;
}

@keyframes bar-fill {
  from {
    width: 0;
  }
}

@keyframes ring-fill {
  from {
    stroke-dasharray: 0, 100;
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-6px);
  }
}

@media (max-width: 900px) {
  .admin-layout {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
