# Corriger l'erreur "connection to localhost failed" sur Railway

Django essaie de se connecter à `localhost` car la variable `DATABASE_URL` n'est pas définie. Voici comment la configurer.

---

## Solution : ajouter la variable DATABASE_URL

### Étape 1 : Identifier le nom du service PostgreSQL

1. Railway → votre projet
2. Regardez la **liste des services** à gauche
3. Notez le **nom exact** du service PostgreSQL (ex. `Postgres`, `PostgreSQL`, `postgres`)

### Étape 2 : Ajouter la variable au service backend

1. Cliquez sur le service **backend** (votre app Django), **PAS** sur Postgres
2. Onglet **Variables**
3. Cliquez **+ New Variable** ou **Add Variable**
4. Dans le champ **Name** : `DATABASE_URL`
5. Dans le champ **Value** : tapez `${{` puis utilisez l'**autocomplete** :
   - Railway affiche une liste de services
   - Sélectionnez votre service Postgres (ex. `Postgres`)
   - Puis `.DATABASE_URL`
   - Résultat : `${{Postgres.DATABASE_URL}}`
6. **Save** ou **Add**
7. Railway redéploie automatiquement

### Étape 3 : Vérifier

- Onglet **Deployments** → attendez la fin du déploiement
- Si l'erreur persiste : vérifiez que le **nom du service** est exact (casse, espaces)

---

## Alternative : variables individuelles

Si la référence ne fonctionne pas, ajoutez ces 5 variables (remplacez `Postgres` par le nom de votre service) :

| Name | Value |
|------|-------|
| `PGHOST` | `${{Postgres.PGHOST}}` |
| `PGPORT` | `${{Postgres.PGPORT}}` |
| `PGDATABASE` | `${{Postgres.PGDATABASE}}` |
| `PGUSER` | `${{Postgres.PGUSER}}` |
| `PGPASSWORD` | `${{Postgres.PGPASSWORD}}` |

---

## Schéma

```
[Service Backend]  --(Variables)-->  DATABASE_URL = ${{Postgres.DATABASE_URL}}
                                              |
                                              v
[Service Postgres]  <--(expose)-->   DATABASE_URL, PGHOST, PGPORT, etc.
```
