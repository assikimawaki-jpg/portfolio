# Lier PostgreSQL au backend sur Railway

Si vous avez l'erreur `connection to server at "localhost" failed`, c'est que `DATABASE_URL` n'est pas configurée.

## Étapes

1. **Railway** → votre projet
2. Cliquez sur le service **backend** (poetic-youth ou portfolio), **pas** sur Postgres
3. Onglet **Variables**
4. Cliquez **+ New Variable** ou **Add Variable**
5. **Name** : `DATABASE_URL`
6. **Value** : `${{Postgres.DATABASE_URL}}`

   **Important** : Remplacez `Postgres` par le **nom exact** de votre service PostgreSQL (visible dans le projet à gauche). Par exemple :
   - `${{Postgres.DATABASE_URL}}`
   - `${{PostgreSQL.DATABASE_URL}}`
   - `${{postgres.DATABASE_URL}}`
7. Utilisez l'**autocomplete** : en tapant `${{`, Railway propose les services et variables disponibles
8. **Deploy** (ou laissez Railway redéployer automatiquement)

## Vérifier le nom du service

Le nom du service PostgreSQL est affiché sur la carte du service dans le projet (ex. "Postgres", "PostgreSQL", "postgres", etc.). Il doit être exact, y compris la casse.
