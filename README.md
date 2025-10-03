# 🚀 Coder avec IA - Stack Docker

Ce projet propose une stack de développement moderne avec Docker Compose :
- **PostgreSQL** (service `db`)
- **FastAPI** (service `fastapi`)
- **React + Vite** (service `vite-react`)

---

## 📦 Structure du projet

```
coder-avec-ia/
├── docker-compose.yml
├── README.md
├── back-fastapi/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── main.py
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       └── models/
│           └── count_table.py
└── coder-ia-gen/
    ├── Dockerfile
    ├── package.json
    ├── src/
    └── public/
```

---

## ⚙️ Démarrage rapide

```bash
# 1. Construire et lancer tous les services
docker compose up --build -d

# 2. Surveiller les logs
docker compose logs -f

# 3. Arrêter tous les services
docker compose down
```

---

## 🐳 Commandes Docker utiles

### Lancer/arrêter des services
```bash
docker compose up -d           # Lancer tous les services
docker compose up fastapi -d   # Lancer uniquement FastAPI
docker compose stop            # Arrêter tous les services
docker compose restart db      # Redémarrer la base de données
```

### Logs et accès shell
```bash
docker compose logs fastapi    # Logs FastAPI
docker compose exec db sh      # Shell PostgreSQL
docker compose exec fastapi bash # Shell FastAPI
```

### Maintenance
```bash
docker compose down -v         # Supprimer conteneurs + volumes (⚠️ données perdues)
docker system prune            # Nettoyer images non utilisées
```

---

## 🔗 Accès aux services

- **API FastAPI** : [http://localhost:8000](http://localhost:8000)
- **Frontend React** : [http://localhost:5173](http://localhost:5173)
- **PostgreSQL** : `localhost:5432` (depuis l'extérieur) ou `db:5432` (depuis Docker)

---

## 🔑 Informations de connexion PostgreSQL

- **Host** : `localhost` (extérieur) ou `db` (depuis Docker)
- **Port** : `5432`
- **Database** : `coder_ia_db`
- **Username** : `postgres`
- **Password** : `postgres123`

---

## ⚠️ Dépannage courant

- **Vérifier les logs** : `docker compose logs [service]`
- **Reconstruire** : `docker compose up --build`
- **Tester la base** : `docker compose exec db pg_isready -U postgres`
- **Problème de CORS** : assurez-vous que FastAPI autorise les requêtes du frontend (voir middleware CORS dans `main.py`).

---

## 📝 Checklist de vérification

- [ ] PostgreSQL accessible sur port 5432
- [ ] FastAPI accessible sur http://localhost:8000
- [ ] React/Vite accessible sur http://localhost:5173
- [ ] Les logs ne montrent pas d'erreurs
- [ ] La base de données contient les tables attendues

---

## 💡 Conseils

- Modifiez les variables d'environnement dans `docker-compose.yml` selon vos besoins.
- Pour la production, restreignez les origines CORS dans FastAPI.
- Pour réinitialiser la base : `docker compose down -v && docker compose up --build -d`

