<template>
  <!-- Section principale du composant -->
  <div>
    <!-- Menu de navigation inclus depuis le composant NavigationBar -->
    <NavigationBar />

    <!-- Contenu principal -->
    <main class="container mx-auto py-10">
      <!-- Titre principal -->
      <h1 class="text-green-700 text-4xl text-center mb-6">Mon espace</h1>

      <!-- Message d'erreur en cas de problème -->
      <div v-if="errorMessage" class="text-center text-red-500 text-lg font-bold">
        {{ errorMessage }}
      </div>

      <!-- Informations du logement si disponibles -->
      <section
        v-if="!errorMessage && logement && Object.keys(logement).length > 0"
        class="grid grid-cols-1 md:grid-cols-2 gap-10"
      >
        <!-- Carte des informations -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h2 class="text-2xl font-bold text-green-700 mb-4">Informations du logement</h2>
          <ul class="space-y-4 text-gray-700 text-lg">
            <li><strong>Adresse :</strong> {{ logement?.Adresse || "Non disponible" }}</li>
            <li><strong>Téléphone :</strong> {{ logement?.Téléphone || "Non disponible" }}</li>
            <li><strong>Adresse IP :</strong> {{ logement?.Adresse_IP || "Non disponible" }}</li>
            <li><strong>Date d'inscription :</strong> {{ logement?.Date_Insertion || "Non disponible" }}</li>
          </ul>
        </div>

        <!-- Image du logement -->
        <div class="bg-gray-100 p-4 rounded-lg shadow-lg">
          <img
            :src="`/logement${logement?.ID_Logement}.png`"
            alt="Image du logement"
            class="w-full h-auto object-cover rounded-lg"
          />
        </div>
      </section>
    </main>

    <!-- Pied de page -->
    <footer class="bg-green-700 text-white py-4 mt-10">
      <div class="container mx-auto text-center">
        <p>© 2024 EcoHome. Tous droits réservés.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
/**********************************************
 * IMPORTATIONS
 **********************************************/
import { onMounted, ref } from "vue";
import axios from "axios";
import NavigationBar from "@/components/NavigationBar.vue"; // Assurez-vous que le chemin est correct

/**********************************************
 * VARIABLES REACTIVES
 **********************************************/
// Stockage des informations du logement
const logement = ref({});
// Message d'erreur pour signaler un problème
const errorMessage = ref("");
// Stockage des identifiants utilisateur
const email = ref("");
const password = ref("");

/**********************************************
 * FONCTIONS PRINCIPALES
 **********************************************/
// Fonction pour récupérer les informations du logement depuis l'API
const fetchLogement = async () => {
  try {
    // Validation des identifiants
    if (!email.value || !password.value) {
      errorMessage.value = "Email ou mot de passe non disponible. Veuillez vous connecter.";
      return;
    }

    // Appel API
    const response = await axios.post("http://127.0.0.1:8000/login", {
      email: email.value,
      password: password.value,
    });

    // Traitement de la réponse
    if (response.data && response.data.logement) {
      logement.value = response.data.logement;
    } else {
      errorMessage.value = "Impossible de récupérer les informations du logement.";
    }
  } catch (error) {
    console.error("Erreur lors de la récupération des données du logement :", error);
    errorMessage.value = "Une erreur est survenue lors de la récupération des données.";
  }
};

/**********************************************
 * LIFECYCLE HOOKS
 **********************************************/
// Exécuter lors du montage du composant
onMounted(() => {
  // Récupérer l'email et le mot de passe depuis localStorage
  email.value = localStorage.getItem("email") || "";
  password.value = localStorage.getItem("password") || "";

  // Si les identifiants sont disponibles, charger les informations
  if (email.value && password.value) {
    fetchLogement();
  } else {
    errorMessage.value = "Veuillez vous connecter pour accéder aux informations du logement.";
  }
});
</script>

<style>
/**********************************************
 * STYLE DU COMPOSANT
 **********************************************/
body {
  font-family: "Poppins", sans-serif;
  background-color: #f9f9f9;
  margin: 0;
}

img {
  max-height: 300px;
  object-fit: cover;
}
</style>
