# Portfolio professionnel (Django + Vue 3)

Architecture séparée avec backend Django REST API et deux frontends Vue 3 (client + admin). Authentification JWT, PostgreSQL, prêt pour la production.

## Structure du projet

```
Portfolio/
├── portfolio_backend/
│   ├── api/
│   ├── portfolio_backend/
│   ├── manage.py
│   └── requirements.txt
├── frontend/ (client)
│   ├── src/
│   ├── index.html
│   └── package.json
└── admin-app/ (admin)
    ├── src/
    ├── index.html
    └── package.json
```

## Backend (Django)

### Installation

```bash
cd portfolio_backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Configuration

Copiez `portfolio_backend/.env.example` en `portfolio_backend/.env` et adaptez vos paramètres PostgreSQL.

### Base de données

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Lancer l'API

```bash
python manage.py runserver
```

## Frontend client (Vue 3)

### Installation

```bash
cd frontend
npm install
```

### Configuration

Copiez `frontend/.env.example` en `frontend/.env` et adaptez l'URL de l'API si nécessaire.

### Lancer le frontend client

```bash
npm run dev
```

## Frontend admin (Vue 3)

### Installation

```bash
cd admin-app
npm install
```

### Configuration

Copiez `admin-app/.env.example` en `admin-app/.env` si nécessaire.

### Lancer le frontend admin

```bash
npm run dev
```

Admin disponible sur `http://localhost:5174/admin-login`.

## Endpoints principaux

Base URL : `http://localhost:8000/api/`

| Ressource | URL | Accès |
| --- | --- | --- |
| Profil | `/profil/` | Lecture publique, admin pour écrire |
| Compétences | `/competences/` | Lecture publique, admin pour écrire |
| Projets | `/projets/` | Lecture publique, admin pour écrire |
| Messages | `/messages/` | Création publique, lecture admin |
| JWT | `/token/`, `/token/refresh/` | Auth |

## Exemples de requêtes API

### Récupérer le profil

```bash
curl http://localhost:8000/api/profil/
```

### Se connecter (JWT)

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"admin\",\"password\":\"votre_mot_de_passe\"}"
```

### Créer une compétence (admin)

```bash
curl -X POST http://localhost:8000/api/competences/ \
  -H "Authorization: Bearer VOTRE_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"nom\":\"Vue.js\",\"niveau\":\"avance\",\"pourcentage\":85,\"categorie\":\"Frontend\"}"
```

### Envoyer un message

```bash
curl -X POST http://localhost:8000/api/messages/ \
  -H "Content-Type: application/json" \
  -d "{\"nom\":\"Jean\",\"email\":\"jean@email.com\",\"sujet\":\"Contact\",\"message\":\"Bonjour\"}"
```

## Sécurité

- Routes admin protégées par JWT.
- Permissions en lecture publique, écriture admin.
- CORS configuré pour le frontend.
- Uploads gérés via `MEDIA_URL` et `MEDIA_ROOT`.

## Notes de production

- Définissez `DJANGO_DEBUG=false`.
- Fournissez `DJANGO_SECRET_KEY` et `DJANGO_ALLOWED_HOSTS`.
- Servez les fichiers statiques et médias via un serveur dédié (Nginx/S3).
