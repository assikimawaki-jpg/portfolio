# Déploiement du backend sur Railway

## Étapes

### 1. Créer un compte Railway
- Allez sur [railway.app](https://railway.app) et connectez-vous avec GitHub.

### 2. Nouveau projet
- Cliquez sur **New Project**
- Choisissez **Deploy from GitHub repo**
- Sélectionnez votre dépôt `assikimawaki-jpg/portfolio`

### 3. Configurer le service (OBLIGATOIRE)
- Railway détecte le dépôt racine (Node.js) par défaut. **Vous DEVEZ définir le Root Directory** :
  1. Cliquez sur le service **portfolio**
  2. Onglet **Settings**
  3. Section **Build** → **Root Directory** → saisissez : `portfolio_backend`
  4. Sauvegardez
- Sans cette étape, le build échouera avec "No start command was found"

### 4. Ajouter PostgreSQL
- Dans votre projet, cliquez sur **+ New** → **Database** → **PostgreSQL**
- Railway créera une base et injectera automatiquement `DATABASE_URL`

### 5. Variables d'environnement
Dans **Variables**, ajoutez :

| Variable | Valeur |
|----------|--------|
| `DJANGO_SECRET_KEY` | Une clé secrète (générez-en une avec `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `DJANGO_DEBUG` | `false` |
| `DJANGO_ALLOWED_HOSTS` | `*` ou `votre-app.railway.app` |
| `CORS_ALLOWED_ORIGINS` | `https://votre-site.vercel.app` (l'URL exacte de votre frontend Vercel) |
| `CSRF_TRUSTED_ORIGINS` | `https://votre-site.vercel.app` |

### 6. Déployer
- Railway déploie automatiquement à chaque push sur GitHub.
- Une fois déployé, récupérez l'URL publique : **Settings** → **Networking** → **Generate Domain**

### 7. Créer un superutilisateur
- Ouvrez le **Terminal** dans Railway (onglet du service)
- Exécutez : `python manage.py createsuperuser`
- Entrez : Mawaki, email, Antoine@05#

### 8. Configurer Vercel (frontend)
- Dans Vercel → **Settings** → **Environment Variables**
- Ajoutez : `VITE_API_URL` = `https://votre-app.railway.app/api/`
- Redéployez le frontend

---

## URL finale
- **API** : `https://votre-app.railway.app/api/`
- **Token** : `https://votre-app.railway.app/api/token/`
