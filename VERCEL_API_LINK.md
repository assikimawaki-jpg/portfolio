# Corriger "Impossible de joindre l'API"

Si le frontend affiche cette erreur, vérifiez d'abord que **l'API Railway répond** :
ouvrez `https://poetic-youth-production-f0d6.up.railway.app/api/` dans le navigateur.
Si vous voyez "Application failed to respond" → le backend est down, consultez les **logs Railway** (Deployments → View Logs).

Sinon, suivez ces 3 étapes :

---

## 1. Vercel : VITE_API_URL

1. [vercel.com](https://vercel.com) → votre projet **frontend**
2. **Settings** → **Environment Variables**
3. **Add** :
   - **Name** : `VITE_API_URL`
   - **Value** : `https://poetic-youth-production-f0d6.up.railway.app/api/`
   - **Environments** : Production, Preview
4. **Save**
5. **Deployments** → **Redeploy** (obligatoire !)

---

## 2. Railway : CORS

1. [railway.app](https://railway.app) → votre projet
2. Service **poetic-youth** (backend) → **Variables**
3. **Add** :
   - **Name** : `CORS_ALLOW_ALL`
   - **Value** : `true`
4. Railway redéploie automatiquement

---

## 3. Vérifier

- Attendez 1 à 2 minutes après les redéploiements
- Rafraîchissez la page de connexion
- Réessayez
