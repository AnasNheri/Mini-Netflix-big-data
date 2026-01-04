# 🎬 Mini Netflix — Système de Recommandation Big Data

## 📌 Description
Ce projet consiste à construire une plateforme de recommandation de films inspirée de Netflix, basée sur les **ratings des utilisateurs**.  
Il met en œuvre un **pipeline Big Data complet** allant du nettoyage des données jusqu’à la visualisation temps réel avec **Grafana**.

---

## 🎯 Objectifs du projet
- Maîtriser **Apache Spark** et ses composants
- Implémenter un modèle de recommandation **ALS (MLlib)**
- Construire un **graphe de similarité utilisateurs** (Cosine Similarity)
- Nettoyer, filtrer et agréger des données massives
- Simuler un **streaming de nouveaux ratings**
- Visualiser les résultats via **Grafana**

---

## 🏗️ Architecture Globale

Core Data
↓
Spark SQL (Analytics)
↓
MLlib (ALS)
↓
User Similarity Graph
↓
Streaming (New Ratings)
↓
Grafana Dashboard

yaml
Copy code

---

## 🔄 Pipeline de Données

MovieLens Dataset
↓
Data Cleaning
↓
SQL Analytics
↓
ALS Recommendation Model
↓
User Similarity Graph
↓
Streaming Ratings
↓
Grafana Metrics

yaml
Copy code

---

## 📂 Dataset
- **Nom** : MovieLens 100k
- **Description** : 100 000 ratings, 943 utilisateurs, 1682 films
- **Lien officiel** :  
  👉 https://grouplens.org/datasets/movielens/100k/

---

## ⚙️ Technologies Utilisées

### 🧠 Big Data & ML
- **Apache Spark 4.x**
- **PySpark**
- **Spark SQL**
- **MLlib (ALS)**

### 📊 Visualisation
- **Grafana**
- CSV Metrics (File-based datasource)

### 🛠️ Outils
- **Python 3.12 (venv)**
- **VS Code**
- **Docker**
- **Pandas / NumPy / Scikit-learn**

---

## 📁 Structure du Projet

mini-netflix/
│
├── data/ # Dataset brut MovieLens
│
├── scripts/
│ ├── 01_clean_data.py
│ ├── 02_sql_analytics.py
│ ├── 03_als_model.py
│ ├── 04_als_evaluation.py
│ ├── 05_user_similarity.py
│ └── 06_streaming_ratings.py
│
├── stream/
│ └── ratings/ # Simulation streaming (CSV)
│
├── output/
│ ├── clean/
│ ├── analytics/
│ ├── als/
│ ├── similarity/
│ └── streaming/
│ ├── metrics/
│ └── checkpoints/
│
├── docker/
│ └── docker-compose.yml
│
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🚀 Fonctionnalités Implémentées

- ⭐ Top films par note moyenne
- 🎯 Recommandation personnalisée via ALS
- 🧑‍🤝‍🧑 Graphe de similarité utilisateurs (Cosine)
- 🔁 Ingestion de nouveaux ratings en streaming
- 📈 Prédictions ALS mises à jour
- 📊 Tableaux et métriques exploitables par Grafana

---

## 📊 Dashboard Grafana

### Visualisations disponibles :
- Distribution des ratings
- Nombre de nouveaux ratings par minute
- Évolution du **RMSE**
- Liste des recommandations générées
- Top films du moment
- Heatmap des similarités utilisateurs
- Courbe du volume de ratings
- Table temps réel des nouveaux ratings

---

## ▶️ Lancement du Projet

### 1️⃣ Activer l’environnement virtuel
```bash
.venv\Scripts\activate
2️⃣ Lancer les scripts dans l’ordre
bash
Copy code
python scripts/01_clean_data.py
python scripts/02_sql_analytics.py
python scripts/03_als_model.py
python scripts/04_als_evaluation.py
python scripts/05_user_similarity.py
python scripts/06_streaming_ratings.py
3️⃣ Simuler le streaming
bash
Copy code
copy output\clean\ratings.csv stream\ratings\ratings_0001.csv
📌 Résultats Clés
RMSE ≈ 0.98

Recommandations cohérentes et personnalisées

Graphe utilisateur exploitable pour la détection de communautés

Dashboard Grafana temps réel fonctionnel