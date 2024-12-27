# Logement Éco-Responsable - Projet IoT

Ce projet vise à développer une solution complète pour gérer un logement connecté et éco-responsable. Il intègre :
- Un backend RESTful avec FastAPI pour gérer les dispositifs, logements et consommations.
- Un frontend interactif avec Nuxt.js pour permettre aux utilisateurs de visualiser et contrôler leurs données.
- Une base de données SQLite pour stocker toutes les informations nécessaires.

Ce projet a été réalisé dans le cadre du TP IoT.

---

## 🌟 Fonctionnalités

- Gestion des dispositifs connectés : ajout, suppression, visualisation.
- Visualisation des consommations énergétiques.
- Suivi des économies réalisées grâce aux dispositifs éco-responsables.
- Configuration et gestion des logements.

---

## 📁 Structure du Projet

- **Backend_et_BDD_Amina/** :
  - `backend.py` : Code du serveur backend.
  - `logement.sql` : Script SQL pour créer la base de données.
  - `remplissage.py` : Script pour insérer des données fictives dans la base de données.
- **Frontend_Amina/** :
  - `mon-site-iot/` :
    - `pages/` : Contient les pages principales du site web.
    - `components/` : Contient les composants réutilisables.
    - `public/` : Contient les images et ressources statiques.
- **README.md** : Ce fichier contient une description générale du projet.

---

## ⚙️ Pré-requis

- Python 3.9 ou supérieur
- Node.js 16 ou supérieur
- SQLite3 installé sur votre machine

---

## 🚀 Installation

### 1. Clonez le repository
```bash
git clone https://github.com/Aminazarroug/Logement_EcoResponsable_Amina_ZARROUG.git
cd Logement_EcoResponsable_Amina_ZARROUG
