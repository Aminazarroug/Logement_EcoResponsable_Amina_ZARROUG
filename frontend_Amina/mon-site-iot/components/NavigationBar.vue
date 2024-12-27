<template>
  <!-- Menu de navigation -->
  <header class="bg-green-700 text-white py-6 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <!-- Logo -->
      <h1 class="text-3xl font-bold flex items-center">
        <span class="material-icons mr-2">home</span> Espace Client
      </h1>

      <!-- Menu de navigation -->
      <nav class="flex space-x-8 items-center">
        <a href="/MonEspace" class="hover:text-yellow-300 flex items-center">
          <span class="material-icons mr-1">person</span> Mon espace
        </a>
        <a href="/Devices" class="hover:text-yellow-300 flex items-center">
          <span class="material-icons mr-1">devices</span> Devices
        </a>
        <a href="/Ajout" class="hover:text-yellow-300 flex items-center">
          <span class="material-icons mr-1">add_circle</span> Gestion des devices
        </a>
        <a href="/Consommation" class="hover:text-yellow-300 flex items-center">
          <span class="material-icons mr-1">analytics</span> Mesures
        </a>
        <a href="/Economies" class="hover:text-yellow-300 flex items-center">
          <span class="material-icons mr-1">savings</span> Économies
        </a>

        <!-- Bouton de déconnexion -->
        <button
          class="btn-deconnexion ml-4"
          @click="logout"
        >
          Déconnexion
        </button>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "NavigationBar",
  methods: {
    logout() {
      // Supprimer les informations de connexion stockées
      localStorage.removeItem("email");
      localStorage.removeItem("password");

      // Redirection vers la page d'accueil
      window.location.href = "/";
    },
  },
};
</script>

<style>
header nav a {
  font-size: 1rem;
  font-weight: bold;
  text-decoration: none;
}

a.active {
  color: yellow;
}

/* Style spécifique pour le bouton de déconnexion */
.btn-deconnexion {
  background-color: red;
  color: white;
  border: none;
  padding: 10px 15px;
  font-size: 14px;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-deconnexion:hover {
  background-color: rgb(243, 101, 101);
}
</style>
