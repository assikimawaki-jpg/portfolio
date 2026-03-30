# Portfolio statique

Version **100 % statique** du portfolio, sans backend ni API.

## Contenu

- **Accueil** : profil, services
- **À propos** : parcours professionnel, témoignages
- **Compétences** : outils par catégorie (Design, Développement, Motion & 3D)
- **Contact** : formulaire → ouverture du client mail (mailto)
- **Connexion** : message indiquant que l'admin n'est pas disponible

## Développement

```bash
npm install
npm run dev
```

Ouvre http://localhost:5173

## Build (fichiers statiques)

```bash
npm run build
```

Les fichiers sont générés dans `dist/`. Vous pouvez :
- Servir le dossier `dist/` avec n'importe quel serveur web
- Déployer sur GitHub Pages, Netlify, Vercel (sans backend)
- Ouvrir `dist/index.html` localement (avec `base: "./"`)

## Données

Toutes les données sont dans `src/data/static.js`. Modifiez ce fichier pour changer le contenu (profil, parcours, compétences, projets).
