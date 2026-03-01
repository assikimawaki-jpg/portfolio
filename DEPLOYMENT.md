# Procédure de déploiement complète

Ce guide décrit comment déployer le portfolio (frontend, admin, backend + base de données).

---

## Vue d'ensemble

| Composant | Plateforme | URL exemple |
|-----------|------------|-------------|
| Frontend (site public) | Vercel | `https://portfolio.vercel.app` |
| Admin (tableau de bord) | Vercel | `https://portfolio-admin.vercel.app` |
| Backend API + PostgreSQL | Railway | `https://portfolio-api.railway.app` |

---

## Partie 1 : Backend sur Railway

### Étape 1.1 – Créer un compte
1. Allez sur [railway.app](https://railway.app)
2. Cliquez sur **Login** → **Login with GitHub**
3. Autorisez Railway à accéder à votre GitHub

### Étape 1.2 – Nouveau projet
1. Cliquez sur **New Project**
2. Choisissez **Deploy from GitHub repo**
3. Sélectionnez le dépôt `assikimawaki-jpg/portfolio` (ou votre fork)
4. Railway crée un service

### Étape 1.3 – Root Directory (obligatoire)
1. Cliquez sur le service **portfolio**
2. Onglet **Settings**
3. Section **Build** → **Root Directory**
4. Saisissez : `portfolio_backend`
5. Cliquez **Save** ou laissez Railway sauvegarder

### Étape 1.4 – Base de données PostgreSQL
1. Dans le projet, cliquez sur **+ New**
2. Choisissez **Database** → **PostgreSQL**
3. Railway crée la base et injecte `DATABASE_URL` dans le service

### Étape 1.5 – Variables d'environnement
1. Cliquez sur le service **portfolio** (pas la base)
2. Onglet **Variables**
3. Ajoutez les variables suivantes :

| Variable | Valeur |
|----------|--------|
| `DJANGO_SECRET_KEY` | Générez avec : `python -c "import secrets; print(secrets.token_hex(32))"` |
| `DJANGO_DEBUG` | `false` |
| `DJANGO_ALLOWED_HOSTS` | `*` |
| `CORS_ALLOWED_ORIGINS` | `https://VOTRE-FRONTEND.vercel.app,https://VOTRE-ADMIN.vercel.app` |
| `CSRF_TRUSTED_ORIGINS` | `https://VOTRE-FRONTEND.vercel.app,https://VOTRE-ADMIN.vercel.app` |

Remplacez `VOTRE-FRONTEND.vercel.app` et `VOTRE-ADMIN.vercel.app` par vos URLs réelles (vous pourrez les mettre à jour après le déploiement sur Vercel).

### Étape 1.6 – Domaine public
1. Toujours dans le service **portfolio**
2. Onglet **Settings** → **Networking**
3. Cliquez **Generate Domain**
4. Notez l’URL (ex. `portfolio-production-xxxx.up.railway.app`)

### Étape 1.7 – Superutilisateur

Le superutilisateur est **créé automatiquement** au premier démarrage (Mawaki / Antoine@05#).

Pour personnaliser, ajoutez ces variables sur Railway :
| Variable | Valeur |
|----------|--------|
| `DJANGO_SUPERUSER_USERNAME` | Mawaki |
| `DJANGO_SUPERUSER_EMAIL` | votre@email.com |
| `DJANGO_SUPERUSER_PASSWORD` | votre mot de passe |

---

## Partie 2 : Frontend sur Vercel

### Étape 2.1 – Connexion GitHub
1. Allez sur [vercel.com](https://vercel.com)
2. **Sign Up** ou **Login** avec GitHub
3. Autorisez Vercel

### Étape 2.2 – Importer le projet
1. **Add New** → **Project**
2. Importez le dépôt `assikimawaki-jpg/portfolio`
3. **Root Directory** : `frontend` (ou laissez vide si vous utilisez le `vercel.json` à la racine)
4. Si Root Directory = vide : le `vercel.json` à la racine gère le build du frontend

### Étape 2.3 – Variables d'environnement
1. **Settings** → **Environment Variables**
2. Ajoutez :

| Name | Value | Environment |
|------|-------|-------------|
| `VITE_API_URL` | `https://VOTRE-API.railway.app/api/` | Production, Preview |

Remplacez par l’URL Railway de l’étape 1.6.

### Étape 2.4 – Déployer
1. Cliquez **Deploy**
2. Notez l’URL du frontend (ex. `portfolio-xxx.vercel.app`)

---

## Partie 3 : Admin sur Vercel

### Étape 3.1 – Nouveau projet
1. **Add New** → **Project**
2. Importez le même dépôt `assikimawaki-jpg/portfolio`
3. **Root Directory** : `admin-app`

### Étape 3.2 – Variables d'environnement
1. **Settings** → **Environment Variables**
2. Ajoutez :

| Name | Value | Environment |
|------|-------|-------------|
| `VITE_API_URL` | `https://VOTRE-API.railway.app/api/` | Production, Preview |

### Étape 3.3 – Déployer
1. Le fichier `admin-app/vercel.json` est déjà configuré pour le routage SPA
2. Cliquez **Deploy**
3. Notez l’URL de l’admin (ex. `portfolio-admin.vercel.app`)

---

## Partie 4 : Mise à jour CORS (Railway)

Une fois les URLs Vercel connues :

1. Railway → service **portfolio** → **Variables**
2. Modifiez `CORS_ALLOWED_ORIGINS` :
   ```
   https://portfolio-xxx.vercel.app,https://portfolio-admin-xxx.vercel.app
   ```
3. Modifiez `CSRF_TRUSTED_ORIGINS**` avec les mêmes URLs
4. Railway redéploiera automatiquement

---

## Partie 5 : Lien Admin (Frontend)

1. Vercel → projet **frontend** → **Settings** → **Environment Variables**
2. Ajoutez (optionnel) :

| Name | Value |
|------|-------|
| `VITE_ADMIN_URL` | `https://portfolio-admin-xxx.vercel.app` |

Cela permet au bouton « Portfolio » / page de connexion de rediriger vers l’admin après login.

---

## Récapitulatif des URLs

Après déploiement, vous aurez :

- **Site public** : `https://votre-frontend.vercel.app`
- **Connexion admin** : `https://votre-frontend.vercel.app/connexion` ou directement `https://votre-admin.vercel.app/admin-login`
- **Tableau de bord** : `https://votre-admin.vercel.app/admin-dashboard`
- **API** : `https://votre-api.railway.app/api/`

---

## Dépannage

| Problème | Solution |
|----------|----------|
| "Application failed to respond" (Railway) | **Logs** : Railway → poetic-youth → Deployments → ⋮ → View Logs. Vérifiez : Root Directory = `portfolio_backend`, `DATABASE_URL` injecté (Postgres connecté), `DJANGO_ALLOWED_HOSTS` = `*` |
| "No start command" sur Railway | Vérifiez que **Root Directory** = `portfolio_backend` |
| "Impossible de joindre l'API" | 1) Vérifiez que l'API répond : ouvrez `https://VOTRE-API.railway.app/api/` dans le navigateur. Si erreur → backend down, consultez les logs Railway. 2) `VITE_API_URL` sur Vercel + redéploy. 3) `CORS_ALLOW_ALL` = `true` sur Railway |
| "Identifiants invalides" | Le superutilisateur est créé au démarrage. Redéployez Railway pour lancer `ensure_superuser`. |
| Erreur CORS | Utilisez `CORS_ALLOW_ALL` = `true` sur Railway, ou ajoutez vos URLs Vercel dans `CORS_ALLOWED_ORIGINS` |
| 404 sur les routes admin | Vérifiez `vercel.json` avec la règle `rewrites` pour SPA |
