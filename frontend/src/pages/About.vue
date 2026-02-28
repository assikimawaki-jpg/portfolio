<template>
  <section class="about-page">
    <div class="page-noise" aria-hidden="true"></div>
    <div class="about-hero">
      <div class="about-hero-accent"></div>
      <div class="hero-glow"></div>
      <div class="about-hero-content">
        <div class="about-badge animate-in">
          <span class="badge-line"></span>
          <span>À propos</span>
        </div>
        <h1 class="about-title animate-in" style="--delay: 0.05s">
          Je suis <span class="brand-name">{{ profil?.nom || "Assiki Mawaki" }}</span>, Designer & Développeur Web
        </h1>
        <div class="about-intro-block animate-in" style="--delay: 0.1s">
          <p class="about-intro">
            {{ profil?.bio || "Je suis un designer passionné spécialisé dans la création d'expériences numériques innovantes et attrayantes." }}
          </p>
          <p class="about-intro">
            Mon approche combine créativité, stratégie et technologie pour concevoir des solutions visuelles qui non seulement sont esthétiquement plaisantes, mais aussi fonctionnelles et centrées sur l'utilisateur. Je crois fermement que le bon design doit raconter une histoire tout en résolvant des problèmes.
          </p>
        </div>
      </div>
    </div>

    <section class="parcours-section futuristic-section reveal-section">
      <p class="eyebrow animate-on-scroll">Parcours</p>
      <h2 class="glow-text section-title animate-on-scroll" style="--i: 1">Mon Parcours Professionnel</h2>
      <p class="section-desc animate-on-scroll" style="--i: 2">
        Mon chemin professionnel et académique qui a façonné mon expertise en design et développement.
      </p>
      <div class="timeline-infographic">
        <div class="timeline-path">
          <svg viewBox="0 0 24 800" preserveAspectRatio="none">
            <path
              class="path-line"
              d="M12 0 Q 2 100 12 200 Q 22 300 12 400 Q 2 500 12 600 Q 22 700 12 800"
              fill="none"
              stroke="currentColor"
              stroke-width="3"
              stroke-linecap="round"
            />
          </svg>
        </div>
        <div
          v-for="(item, i) in parcoursDisplay"
          :key="i"
          class="timeline-step animate-step"
          :class="{ left: i % 2 === 0, right: i % 2 === 1 }"
          :style="{ '--accent': stepColors[i % 4], '--i': i }"
        >
          <div class="step-icon-wrap">
            <svg v-if="(i % 4) === 0" class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1 .34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-2A2.5 2.5 0 0 1 9.5 2Z"/>
              <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0-.34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-2A2.5 2.5 0 0 0 14.5 2Z"/>
            </svg>
            <svg v-else-if="(i % 4) === 1" class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M4 4l7 7m0 0l4-4m-4 4v10"/>
              <path d="M20 20l-7-7m0 0l-4 4m4-4V7"/>
            </svg>
            <svg v-else-if="(i % 4) === 2" class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M9 18h6"/><path d="M10 22h4"/>
              <path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>
              <path d="M12 2v2"/><path d="M4 12H2"/><path d="M22 12h-2"/><path d="M19.07 4.93l-1.41 1.41"/><path d="M6.34 6.34L4.93 4.93"/>
            </svg>
            <svg v-else class="step-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M8 21l4-4 4 4"/><path d="M12 17v4"/>
              <path d="M4 14l2-2 2 2 2-2 2 2 2-2"/><path d="M2 10h2l2-2 2 2 2-2 2 2 2-2 2 2h2"/><path d="M4 6l2 2 2-2 2 2 2-2 2 2"/>
            </svg>
          </div>
          <div class="step-text">
            <span class="step-date">{{ item.date }}</span>
            <h3 class="step-title">
              <span class="step-title-label">Étape</span>
              <span class="step-title-accent">{{ String(i + 1).padStart(2, '0') }}</span>
              <span class="step-title-main"> — {{ item.title }}</span>
            </h3>
            <p class="step-place">{{ item.place }}</p>
            <p class="step-description">{{ item.description }}</p>
            <span class="step-location">{{ item.location }}</span>
          </div>
        </div>
      </div>
    </section>

    <section class="testimonials-section futuristic-section reveal-section">
      <p class="eyebrow animate-on-scroll">Témoignages</p>
      <h2 class="glow-text section-title animate-on-scroll" style="--i: 1">Ce que disent mes clients</h2>
      <p class="section-desc animate-on-scroll" style="--i: 2">
        Des retours d'expérience de personnes avec qui j'ai eu le plaisir de collaborer.
      </p>
      <div class="testimonial-wrapper animate-on-scroll" style="--i: 3">
        <div class="testimonial-card-new">
          <div class="testimonial-avatar-wrap">
            <img
              src="https://i.postimg.cc/rmmxsmbQ/Capture-d-ecran-2026-02-28-120529.png"
              alt="Photo du témoin"
              class="testimonial-avatar"
            />
          </div>
          <h3 class="testimonial-name">Noor Hassan</h3>
          <p class="testimonial-title">Founder</p>
          <p class="testimonial-firm">Interior Design Firm</p>
          <blockquote class="testimonial-quote-new">
            <span class="quote-mark quote-open">"</span>
            Un talent rare qui combine expertise technique et vision artistique. Notre site web a non seulement une
            <strong class="highlight">apparence exceptionnelle</strong>, mais il offre également une expérience utilisateur fluide et intuitive.
            <span class="quote-mark quote-close">"</span>
          </blockquote>
          <div class="testimonial-stars">
            <span class="star" v-for="i in 5" :key="i" aria-hidden="true">★</span>
          </div>
        </div>
      </div>
    </section>

    <section class="about-cta reveal-section">
      <RouterLink class="button cta-futuristic animate-on-scroll" to="/contact">
        <span class="cta-text">Discutons de votre projet</span>
        <span class="cta-shine"></span>
      </RouterLink>
    </section>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { RouterLink } from "vue-router";
import api from "../services/api";

const profil = ref(null);
const parcours = ref([]);

const fallbackParcours = [
  { date: "2022 - Présent", titre: "Directeur Créatif", lieu: "Studio Design", localisation: "Lomé, Togo", description: "Direction des projets créatifs, gestion des équipes de design et développement de la stratégie visuelle pour les clients majeurs." },
  { date: "2021", titre: "Formation UX/UI Avancée", lieu: "École du Design", localisation: "En ligne", description: "Formation spécialisée en conception d'expérience utilisateur et interfaces innovantes." },
  { date: "2019 - 2022", titre: "Designer Senior", lieu: "Agence Digitale Creative", localisation: "Lomé, Togo", description: "Conception et réalisation de projets web et mobiles pour des clients internationaux. Responsable de l'identité visuelle et de l'expérience utilisateur." },
  { date: "2018", titre: "Master en Design Graphique", lieu: "Université des Arts", localisation: "Lomé, Togo", description: "Spécialisation en design d'interface et communication visuelle. Projet de fin d'études sur l'accessibilité dans le design web." },
  { date: "2016 - 2019", titre: "Designer Web", lieu: "StartUp Innovante", localisation: "Lomé, Togo", description: "Création de sites web, applications et supports marketing pour une startup en pleine croissance." },
];

const parcoursDisplay = computed(() => {
  const list = parcours.value.length ? parcours.value : fallbackParcours;
  return list.map((p) => ({
    date: p.date,
    title: p.titre,
    place: p.lieu,
    location: p.localisation,
    description: p.description,
  }));
});

const stepColors = ["#ef4444", "#f97316", "#eab308", "#22c55e"];

const loadProfil = async () => {
  try {
    const response = await api.get("profil/");
    profil.value = response.data?.results?.[0] || response.data?.[0] || null;
  } catch {
    profil.value = null;
  }
};

const loadParcours = async () => {
  try {
    const res = await api.get("parcours/");
    parcours.value = res.data?.results || res.data || [];
  } catch {
    parcours.value = [];
  }
};

onMounted(() => {
  loadProfil();
  loadParcours();
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    { threshold: 0.1, rootMargin: "0px 0px -50px 0px" }
  );
  document.querySelectorAll(".animate-on-scroll, .animate-step, .reveal-section").forEach((el) => observer.observe(el));
});
</script>

<style scoped>
.about-page {
  display: grid;
  gap: 48px;
  position: relative;
  isolation: isolate;
}

/* Texture grain overlay - léger filtre sur la page */
.page-noise {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.animate-in {
  animation: fade-slide-in 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  animation-delay: var(--delay, 0s);
  opacity: 0;
}

@keyframes fade-slide-in {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Scroll-triggered animations */
.animate-on-scroll,
.animate-step {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1),
    transform 0.7s cubic-bezier(0.22, 1, 0.36, 1),
    filter 0.4s ease;
  transition-delay: calc(var(--i, 0) * 0.1s);
}

.animate-on-scroll.visible,
.animate-step.visible {
  opacity: 1;
  transform: translateY(0);
}

.animate-step {
  transition-delay: calc(var(--i, 0) * 0.12s);
}

.eyebrow {
  color: #93c5fd;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 3px;
  font-size: 12px;
  margin-bottom: 8px;
}

.futuristic-card {
  position: relative;
  padding: 40px;
  border-radius: 20px;
  background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(59, 130, 246, 0.15), transparent 60%),
    linear-gradient(160deg, rgba(15, 23, 42, 0.9), rgba(2, 6, 23, 0.95));
  border: 1px solid rgba(59, 130, 246, 0.25);
  backdrop-filter: blur(16px);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.about-hero {
  position: relative;
  display: grid;
  grid-template-columns: 1fr;
  border-radius: 24px;
  overflow: hidden;
  background: radial-gradient(ellipse 70% 50% at 0% 50%, rgba(59, 130, 246, 0.12), transparent 50%),
    linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(2, 6, 23, 0.99) 100%);
  border: 1px solid rgba(59, 130, 246, 0.25);
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.04);
  transition: box-shadow 0.5s ease, transform 0.5s ease;
}

.about-hero:hover {
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.4), 0 0 60px rgba(59, 130, 246, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.06);
}

.hero-glow {
  position: absolute;
  top: -50%;
  right: -20%;
  width: 60%;
  height: 150%;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
  pointer-events: none;
  animation: hero-glow-pulse 8s ease-in-out infinite;
}

@keyframes hero-glow-pulse {
  0%, 100% { opacity: 0.6; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.05); }
}

.about-hero-accent {
  position: absolute;
  top: 0;
  left: 0;
  width: 6px;
  height: 100%;
  background: linear-gradient(180deg, #3b82f6, #60a5fa, #93c5fd);
  opacity: 0.9;
  animation: accent-shimmer 3s ease-in-out infinite;
}

@keyframes accent-shimmer {
  0%, 100% { opacity: 0.85; }
  50% { opacity: 1; }
}

.about-hero-content {
  padding: 48px 48px 48px 40px;
  position: relative;
  z-index: 1;
}

.about-badge {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.badge-line {
  width: 32px;
  height: 3px;
  background: linear-gradient(90deg, #3b82f6, transparent);
  border-radius: 2px;
  animation: badge-line-grow 0.8s ease-out 0.3s forwards;
  transform-origin: left;
  transform: scaleX(0);
}

@keyframes badge-line-grow {
  to { transform: scaleX(1); }
}

.about-badge span:last-child {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 4px;
  color: #60a5fa;
  text-transform: uppercase;
}

.about-title {
  font-size: clamp(26px, 4.5vw, 40px);
  font-weight: 700;
  color: #f8fafc;
  line-height: 1.35;
  margin: 0 0 28px;
  max-width: 720px;
}

.brand-name {
  font-family: var(--font-brand);
  background: linear-gradient(135deg, #93c5fd, #60a5fa);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 0 20px rgba(96, 165, 250, 0.3));
  animation: brand-shimmer 6s ease-in-out infinite;
}

@keyframes brand-shimmer {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}

.about-intro-block {
  display: grid;
  gap: 18px;
  max-width: 680px;
}

.about-intro {
  color: rgba(226, 232, 240, 0.9);
  line-height: 1.85;
  margin: 0;
  font-size: 16px;
  transition: color 0.3s ease;
}

.about-intro-block:hover .about-intro {
  color: rgba(226, 232, 240, 0.95);
}

.futuristic-section {
  padding-top: 32px;
  border-top: 1px solid rgba(59, 130, 246, 0.2);
  position: relative;
}

.reveal-section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.35), transparent);
}

.section-title {
  font-size: clamp(22px, 3.5vw, 30px);
  font-weight: 700;
  margin: 0 0 8px;
  text-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
}
.glow-text {
  animation: glow-pulse 4s ease-in-out infinite;
}
@keyframes glow-pulse {
  0%, 100% { text-shadow: 0 0 20px rgba(59, 130, 246, 0.3); }
  50% { text-shadow: 0 0 30px rgba(59, 130, 246, 0.5); }
}

.section-desc {
  color: rgba(226, 232, 240, 0.75);
  font-size: 15px;
  margin: 0 0 36px;
}

/* Timeline infographic - design serpentin */
.timeline-infographic {
  position: relative;
  max-width: 720px;
  margin: 0 auto;
  padding: 0 20px;
}

.timeline-path {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 24px;
  margin-left: -12px;
  color: #14b8a6;
}

.timeline-path svg {
  width: 100%;
  height: 100%;
}

.path-line {
  stroke: currentColor;
  opacity: 0;
  animation: path-fade-in 1.2s ease-out 0.3s forwards;
}

@keyframes path-fade-in {
  to { opacity: 0.85; }
}

.timeline-step {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 40px;
  z-index: 1;
  max-width: calc(50% - 30px);
}

.timeline-step:last-child {
  margin-bottom: 0;
}

.timeline-step.left {
  flex-direction: row;
  margin-right: auto;
}

.timeline-step.right {
  flex-direction: row-reverse;
  margin-left: auto;
}

.step-icon-wrap {
  flex-shrink: 0;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid #14b8a6;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  display: grid;
  place-items: center;
  transition: transform 0.35s ease, box-shadow 0.35s ease, filter 0.35s ease;
}

.timeline-step:hover .step-icon-wrap {
  transform: scale(1.08);
  box-shadow: 0 8px 28px rgba(20, 184, 166, 0.35);
  filter: drop-shadow(0 0 20px rgba(20, 184, 166, 0.4));
}

.step-icon {
  width: 28px;
  height: 28px;
  color: #0f172a;
}

.step-text {
  flex: 1;
  min-width: 0;
  padding: 20px 24px;
  border-radius: 16px;
  background: linear-gradient(160deg, rgba(15, 23, 42, 0.95), rgba(2, 6, 23, 0.98));
  border: 1px solid rgba(20, 184, 166, 0.3);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

.timeline-step:hover .step-text {
  transform: translateX(4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35), 0 0 24px rgba(20, 184, 166, 0.1);
  border-color: rgba(20, 184, 166, 0.5);
}

.timeline-step.right:hover .step-text {
  transform: translateX(-4px);
}

.step-date {
  display: block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--accent, #14b8a6);
  margin-bottom: 6px;
}

.step-title {
  font-size: 18px;
  font-weight: 700;
  color: #e2e8f0;
  margin: 0 0 8px;
  line-height: 1.3;
}

.step-title-label {
  color: rgba(226, 232, 240, 0.8);
  font-weight: 600;
}

.step-title-accent {
  color: var(--accent, #14b8a6);
  font-weight: 700;
}

.step-title-main {
  color: #e2e8f0;
  font-weight: 700;
}

.step-place {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: rgba(226, 232, 240, 0.7);
  margin: 0 0 10px;
}

.step-description {
  font-size: 14px;
  line-height: 1.65;
  color: rgba(226, 232, 240, 0.85);
  margin: 0 0 8px;
}

.step-location {
  font-size: 13px;
  color: #14b8a6;
}

.testimonials-section {
  position: relative;
  background: #141828;
  border-radius: 20px;
  padding: 48px 32px;
  overflow: hidden;
}

.testimonials-section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(ellipse 80% 50% at 20% 50%, rgba(99, 102, 241, 0.12), transparent),
    radial-gradient(ellipse 60% 40% at 80% 20%, rgba(255, 140, 66, 0.08), transparent);
  pointer-events: none;
}

.testimonial-wrapper {
  position: relative;
  max-width: 520px;
  margin: 0 auto;
}

.testimonial-card-new {
  background: #ffffff;
  border-radius: 24px;
  border: 2px solid #ff8c42;
  box-shadow: 0 0 40px rgba(255, 140, 66, 0.2), 0 20px 60px rgba(0, 0, 0, 0.3);
  padding: 48px 36px 32px;
  text-align: center;
  position: relative;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
}

.testimonial-wrapper:hover .testimonial-card-new {
  transform: translateY(-4px);
  box-shadow: 0 0 50px rgba(255, 140, 66, 0.25), 0 24px 70px rgba(0, 0, 0, 0.35);
}

.testimonial-avatar-wrap {
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%);
  width: 88px;
  height: 88px;
  border-radius: 50%;
  padding: 4px;
  background: linear-gradient(135deg, #fff, #e5e7eb);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.testimonial-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #fff;
}

.testimonial-name {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 16px 0 4px;
  font-family: "Inter", "Segoe UI", sans-serif;
}

.testimonial-title {
  font-size: 14px;
  font-weight: 600;
  color: #555;
  margin: 0;
}

.testimonial-firm {
  font-size: 13px;
  color: #555;
  margin: 0 0 20px;
}

.testimonial-quote-new {
  font-size: 16px;
  line-height: 1.7;
  color: #333;
  margin: 0 0 24px;
  text-align: justify;
  position: relative;
  padding: 0 8px;
}

.quote-mark {
  font-size: 48px;
  font-weight: 700;
  color: #ff8c42;
  line-height: 1;
  font-family: Georgia, serif;
}

.quote-open {
  float: left;
  margin: -8px 4px 0 -4px;
}

.quote-close {
  float: right;
  margin: 0 -4px -24px 4px;
}

.testimonial-quote-new .highlight {
  color: #ff8c42;
  font-weight: 700;
}

.testimonial-stars {
  display: inline-flex;
  gap: 4px;
  background: #ff8c42;
  color: #fff;
  padding: 10px 24px;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.testimonial-stars .star {
  font-size: 18px;
  color: #fff;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.2);
}

.about-cta {
  padding: 32px 0;
  text-align: center;
}

.cta-futuristic {
  position: relative;
  overflow: hidden;
  padding: 16px 36px;
  font-size: 16px;
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 24px rgba(59, 130, 246, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.cta-futuristic:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 12px 40px rgba(59, 130, 246, 0.55);
}

.cta-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 50%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
  animation: cta-shine 4s ease-in-out infinite;
}

@keyframes cta-shine {
  0% { left: -100%; }
  50%, 100% { left: 150%; }
}

@media (max-width: 768px) {
  .timeline-path {
    left: 28px;
    margin-left: 0;
  }

  .timeline-step {
    max-width: none;
    padding-left: 72px;
    margin-left: 0 !important;
    margin-right: 0 !important;
    flex-direction: row !important;
  }

  .step-icon-wrap {
    position: absolute;
    left: 0;
    top: 0;
    width: 48px;
    height: 48px;
  }

  .step-icon {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 600px) {
  .futuristic-card {
    padding: 24px;
  }

  .about-hero-content {
    padding: 32px 24px 32px 28px;
  }

  .about-hero-accent {
    width: 4px;
  }

  .about-badge {
    margin-bottom: 16px;
  }

  .about-title {
    margin-bottom: 20px;
  }

  .timeline-infographic {
    padding: 0 12px;
  }

  .step-text {
    padding: 16px 18px;
  }

  .testimonial-card-new {
    padding: 40px 20px 24px;
  }

  .testimonial-quote-new {
    font-size: 15px;
  }

  .quote-mark {
    font-size: 36px;
  }
}
</style>
