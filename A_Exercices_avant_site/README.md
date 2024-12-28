# A_Exos_avant_site - Logement Éco-Responsable

Ce dossier contient toutes les étapes préliminaires du TP "Logement Éco-Responsable", où les exercices avant la conception complète du site web sont réalisés. Vous trouverez ici les solutions organisées selon les parties et les exercices demandés.

---

## 📋 Contenu

1. **Fichiers présents dans ce dossier** :
   - **`Logement.sql`** : Contient les commandes SQL pour créer la base de données, ses tables et insérer des données initiales.
   - **`remplissage.py`** : Script Python utilisé pour ajouter des données fictives (mesures, factures, etc.) dans la base de données.
   - **`FastAPI.py`** : Serveur RESTful développé avec FastAPI, permettant de remplir, consulter et manipuler les données via des requêtes API.
   - **`Commandes Curl.txt`** : Script Bash contenant des exemples de requêtes `curl` pour tester les endpoints RESTful.

---

## 🛠️ Détails par exercice

### **1. Base de données (`Logement.sql`)**
- Réponses aux questions de la partie 1 :
  - **Question 1 :** Modèle relationnel validé avec les tables nécessaires (Logement, Pièce, Capteur/Actionneur, Mesure, Facture).
  - **Question 2 :** Commandes SQL pour détruire toutes les tables existantes.
  - **Question 3 :** Commandes SQL pour créer toutes les tables.
  - **Question 4 :** Ajout d’un logement avec 4 pièces.
  - **Question 5 :** Ajout d’au moins 4 types de capteurs/actionneurs.
  - **Question 6 :** Ajout d’au moins 2 capteurs/actionneurs.
  - **Question 7 :** Ajout d’au moins 2 mesures par capteur/actionneur.
  - **Question 8 :** Ajout d’au moins 4 factures.

Vous pouvez exécuter le fichier `Logement.sql` avec la commande suivante :
```bash
sqlite3 Amina.db
.read Logement.sql
```

### **2. Remplissage de la base de données et Serveur RESTful**

#### **2. Remplissage de la base de données (`remplissage.py`)**
Ce fichier complète les données de la base en ajoutant des informations fictives pour les tests. Les fonctionnalités principales incluent :
- Génération de mesures réalistes associées aux capteurs/actionneurs (température, humidité, consommation d'énergie, etc.).
- Ajout de factures fictives avec des montants, dates, et détails cohérents pour simuler un scénario réel.

**Pour exécuter le script de remplissage :**
1. Assurez-vous que la base de données `Amina.db` a été initialisée avec `Logement.sql`.
2. Lancez la commande suivante :
   ```bash
   python remplissage.py
    ```

### **3. Serveur RESTful (`FastAPI.py`)**

Le fichier `FastAPI.py` implémente un serveur backend RESTful avec plusieurs endpoints permettant d'interagir avec la base de données. Il facilite la gestion des logements, des pièces, des capteurs/actionneurs, des mesures et des factures.

#### **Fonctionnalités principales**
- **Gestion des logements** :
  - Récupérer la liste des logements existants.
  - Ajouter de nouveaux logements.
- **Gestion des pièces** :
  - Récupérer les pièces associées à un logement spécifique.
  - Ajouter une pièce à un logement existant.
- **Gestion des capteurs/actionneurs** :
  - Récupérer les capteurs/actionneurs associés à une pièce.
  - Ajouter ou supprimer un capteur/actionneur.
- **Gestion des mesures** :
  - Récupérer les mesures collectées par un capteur spécifique.
  - Ajouter des mesures pour un capteur donné.
- **Gestion des factures** :
  - Récupérer toutes les factures associées à un logement.
  - Générer un graphique camembert des factures avec l'endpoint `/factures/chart` (via Google Charts).

#### **Comment démarrer le serveur ?**
1. Lancez le serveur en exécutant la commande suivante :
   ```bash
   uvicorn FastAPI:app --reload --host 127.0.0.1 --port 8000
