# Frontend pour Logement Éco-Responsable

Ce dossier contient l'interface utilisateur développée avec **Nuxt.js** pour le projet **Logement Éco-Responsable**. Le frontend permet aux utilisateurs de gérer leurs dispositifs connectés, de visualiser leur consommation énergétique, et de suivre les économies réalisées.

---

## 📋 Contenu du dossier

1. **`pages/`** :
   - Contient toutes les pages principales de l'application (comme l'accueil, l'espace client, l'ajout de dispositifs, les consommations, etc.).
2. **`components/`** :
   - Composants réutilisables pour l'interface (comme la barre de navigation).
3. **`assets/`** :
   - Contient les fichiers CSS et les ressources liées au style.
4. **`public/`** :
   - Contient les images et autres fichiers statiques utilisés dans l'application.
5. **`nuxt.config.ts`** :
   - Configuration principale de l'application Nuxt.js.
6. **`package.json`** :
   - Fichier contenant les informations du projet et les dépendances nécessaires.
7. **`tailwind.config.js`** :
   - Configuration pour Tailwind CSS, utilisé pour styliser l'application.

---

## ⚙️ Installation et lancement

### Pré-requis
Assurez-vous que les outils suivants sont installés sur votre machine :
- **Node.js** (version 16 ou supérieure)
- **npm** (installé avec Node.js)

### Étapes pour installer et lancer le projet :

1. **Installation des dépendances**
   - Ouvrez un terminal dans le dossier contenant ce projet ( `mon-site-iot`).
   - Installez les dépendances avec la commande suivante :
     ```bash
     npm install
     ```

2. **Lancement du serveur de développement**
   - Lancez l'application en mode développement avec :
     ```bash
     npm run dev
     ```
   - Accédez à l'application dans votre navigateur à l'adresse suivante :
     - [http://localhost:3000](http://localhost:3000) (peut être une autre adresse à vérifier une fois la commande npm run dev exécutée)

--- 

## 🖥️ Structure des fichiers principaux

- **`pages/`** : Contient les pages principales du site web.
  - `index.vue` : Page d'accueil du site.
  - `Guide.vue` : Guide pour l'utilisation du système.
  - `Espace_client.vue` : Page qui permet de se connecter au compte personnel.
  - `SSubscription.vue` : Page pour ajouter un nouveau logement.
  - `MonEspace.vue` : Page d'acceuil dans l'espace client.
  - `Devices.vue` : Page pour visualiser les capteurs/actionneurs et leurs états.
  - `Ajout.vue` : Page pour ajouter ou supprimer des capteurs/actionneurs.
  - `Consommation.vue` : Page pour visualiser les mesures.
  - `Economies.vue` : Page pour suivre les économies réalisées.
- **`components/`** : Contient les composants réutilisables comme :
  - `NavigationBar.vue` : Barre de navigation principale.
- **`nuxt.config.ts`** : Fichier de configuration Nuxt.js.
- **`tailwind.config.js`** : Configuration pour le framework CSS Tailwind.

---

## ⚠️ Remarques importantes

1. **Configuration backend**
   - Le frontend est configuré pour envoyer des requêtes au backend sur l'adresse `http://127.0.0.1:8000`. Assurez-vous que le backend est lancé et accessible avant de tester le frontend.

2. **Dépendances**
   - Toutes les dépendances nécessaires sont spécifiées dans le fichier `package.json`. L'utilisation de `npm install` garantit leur installation.

3. **Port par défaut**
   - L'application frontend est configurée pour s'exécuter sur le port `http://localhost:3000` en mode développement. Assurez-vous que ce port est libre sur votre machine.

---

## 🌟 Points forts

- **Interface intuitive** :
  - Conçue pour une navigation facile et une expérience utilisateur fluide.
- **Architecture modulaire** :
  - Pages et composants bien organisés pour faciliter la maintenance et les ajouts futurs.

---

## 🔗 Références

- **Nuxt.js** : Framework utilisé pour le frontend ([Documentation officielle](https://nuxtjs.org/)).
- **Tailwind CSS** : Framework CSS pour le style ([Documentation officielle](https://tailwindcss.com/)).
- Assistance avec **ChatGPT** dans l'apprentissage d'utilisation de Nuxt.js.

---

## Remarque importante

- Pour le test de l'ajout de dispositifs, il est important de respecter la répartition des pièces par logement : 
- **Logement 1** : ID des pièces uniquement 1, 2 et 5. 
- **Logement 2** : ID des pièces uniquement 3, 4 et 6. 

