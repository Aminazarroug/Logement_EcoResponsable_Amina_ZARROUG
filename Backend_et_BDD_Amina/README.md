# Backend et Scripts pour Logement Éco-Responsable

Ce répertoire contient l'implémentation du backend pour le projet **Logement Éco-Responsable**, ainsi que des scripts supplémentaires pour la gestion des données. L'objectif principal est de fournir des services API pour gérer les logements connectés, les capteurs, et les données de consommation.

---

## 📋 Contenu

1. **`backend.py`** : Le backend principal développé avec FastAPI. Il expose plusieurs routes API pour gérer les utilisateurs, les capteurs et les consommations.
2. **`Logement.sql`** : Script SQL pour créer la structure de la base de données (tables, relations, etc.).
3. **`remplissage.py`** : Script Python pour générer des données fictives et les insérer dans la base de données.

---

## 🛠️ Fonctionnalités Principales

### `backend.py`
- **Authentification des utilisateurs** :
  - Route : `/login`
  - Vérifie les identifiants d'un utilisateur (email et mot de passe) et retourne les informations associées à son logement.

- **Gestion des capteurs** :
  - Récupérer les capteurs associés à un logement : `/devices`
  - Ajouter un capteur : `/devices/add`
  - Supprimer un capteur : `/devices/delete`
  - Liste des types de capteurs disponibles : `/devices/types`

- **Données de consommation** :
  - Mesures d'énergie (électricité, gaz, eau, température) pour une période donnée : `/consommation`
  - Calcul des économies réalisées (en termes de consommation et finances) : `/economies/consommation`

- **Types de capteurs** :
  - Liste des types de capteurs compatibles avec le système : `/capteurs/types`

---

### `Logement.sql`
- Crée les tables nécessaires pour stocker les données du système :
  - **Logement** : Stocke les informations sur les logements.
  - **Device** : Stocke les informations sur les capteurs.
  - **Mesure** : Stocke les données mesurées par les capteurs (température, consommation, etc.).
  - **Device_TYPE** : Définit les types de capteurs disponibles (température, humidité, etc.).

---

### `remplissage.py`
- Génère des données fictives pour les capteurs, avec des valeurs réalistes :
  - Température (°C), humidité (%), électricité (kWh), gaz (ppm), lumière (Lux), eau (litres).
- Ajoute ces données dans la table **Mesure** de la base de données pour chaque capteur d'un logement.
- Permet de simuler des scénarios d'utilisation pour tester l'API et visualiser les données.

---

## 🚀 Lancement du Backend et Ajout des Données Fictives

### Pré-requis
1. **SQLite3** installé pour gérer la base de données.
2. **Modules Python nécessaires** (FastAPI, pydantic) :
   - Installez-les via `pip` :
     ```bash
     pip install -r requirements.txt
     ```

### Étapes pour démarrer le backend et ajouter des données :

1. **Initialiser la Base de Données**
   - Ouvrez un terminal dans le répertoire contenant le fichier `Logement.sql`.
   - Exécutez les commandes suivantes pour créer la base de données `Amina.db` :
     ```bash
     sqlite3 Amina.db
     .read Logement.sql
     ```

2. **Lancer le Backend**
   - Placez-vous dans le répertoire contenant le fichier `backend.py`.
   - Démarrez le serveur FastAPI avec la commande suivante :
     ```bash
     uvicorn backend:app --reload --host 127.0.0.1 --port 8000
     ```
   - **Attention** : Le backend doit être lancé sur le port `127.0.0.1:8000` car le frontend est configuré pour envoyer ses requêtes API à cette adresse précise.

   - Une fois démarré, vous pouvez accéder à la documentation interactive des API sur [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

3. **Ajouter des Données Fictives**
   - Ouvrez le fichier `remplissage.py` et vérifiez que le chemin vers la base de données `Amina.db` est correct.
   - Exécutez le script pour ajouter des données de test dans la base de données :
     ```bash
     python remplissage.py
     ```
   - Ce script générera des données fictives (température, consommation, etc.) pour les capteurs des logements.

---

## 🔗 Références et Outils Utilisés

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLite Documentation](https://sqlite.org/docs.html)
- Assistance avec **ChatGPT** pour structurer les fichiers (il y aura une section ChatGPT dans la présentation lors de la soutenance).

---

## 🌟 Points Forts

- **Conception Modulaire** : Chaque fonctionnalité est isolée dans une route ou un script spécifique.
- **Facilité de Test** : Les données fictives permettent de simuler des scénarios réalistes.
