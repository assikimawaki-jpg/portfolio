# Configuration rapide (5 minutes)

Suivez ces étapes dans l'ordre. Une fois fait, chaque `git push` déclenchera un déploiement automatique.

---

## Étape 1 : Railway (Backend) — 2 min

1. **[railway.app](https://railway.app)** → Login with GitHub
2. **New Project** → **Deploy from GitHub repo** → `assikimawaki-jpg/portfolio`
3. **IMPORTANT** : Cliquez sur le service créé → **Settings** → **Root Directory** : `portfolio_backend` → Save  
   (Sans ça : erreur "Error creating build plan with Railpack")
4. **+ New** → **Database** → **PostgreSQL**
5. **IMPORTANT** : Cliquez sur le service **portfolio** (backend, pas Postgres) → **Variables** → Add :
   - `DATABASE_URL` = `${{Postgres.DATABASE_URL}}` (remplacez "Postgres" par le nom exact de votre service PostgreSQL si différent)
   - `DJANGO_SECRET_KEY` : exécutez `python -c "import secrets; print(secrets.token_hex(32))"` et collez le résultat
   - `DJANGO_DEBUG` : `false`
   - `DJANGO_ALLOWED_HOSTS` : `*`
6. **Settings** → **Networking** → **Generate Domain** → copiez l'URL (ex. `https://xxx.up.railway.app`)
7. Une fois déployé : **Terminal** (ou View Logs) → `python manage.py createsuperuser` → Mawaki / Antoine@05#

---

## Étape 2 : Vercel Frontend — 1 min

1. **[vercel.com](https://vercel.com)** → Login with GitHub
2. **Add New** → **Project** → Import `assikimawaki-jpg/portfolio`
3. **Root Directory** : cliquez **Edit** → `frontend`
4. **Environment Variables** → Add :
   - Key : `VITE_API_URL`
   - Value : `https://VOTRE-URL-RAILWAY/api/` (collez l'URL de l'étape 1)
5. **Deploy**
6. Copiez l'URL du frontend (ex. `https://portfolio-xxx.vercel.app`)

---

## Étape 3 : Vercel Admin — 1 min

1. **Add New** → **Project** → Import le même dépôt
2. **Root Directory** : `admin-app`
3. **Environment Variables** → `VITE_API_URL` = `https://VOTRE-URL-RAILWAY/api/`
4. **Deploy**
5. Copiez l'URL de l'admin (ex. `https://portfolio-admin-xxx.vercel.app`)

---

## Étape 4 : CORS (Railway) — 1 min

1. Retour sur **Railway** → service portfolio → **Variables**
2. Add ou modifiez :
   - `CORS_ALLOWED_ORIGINS` : `https://portfolio-xxx.vercel.app,https://portfolio-admin-xxx.vercel.app` (vos URLs)
   - `CSRF_TRUSTED_ORIGINS` : même valeur
3. Railway redéploie automatiquement

---

## C'est tout

- **Site** : votre URL frontend
- **Admin** : votre URL admin → `/admin-login`
- **Connexion** : Mawaki / Antoine@05#
