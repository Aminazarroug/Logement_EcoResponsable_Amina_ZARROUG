<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

// Références pour les champs du formulaire
const adresse = ref("");
const telephone = ref("");
const adresse_ip = ref("");
const adresse_email = ref("");
const mot_de_passe = ref("");
const successMessage = ref("");
const errorMessage = ref("");
const router = useRouter();

// Fonction pour créer un logement
const createLogement = async () => {
  try {
    // Envoi des données à l'API
    await axios.post("http://127.0.0.1:8000/logements", {
      adresse: adresse.value,
      telephone: telephone.value,
      adresse_ip: adresse_ip.value,
      adresse_email: adresse_email.value,
      mot_de_passe: mot_de_passe.value,
    });

    // Afficher un message de succès
    successMessage.value = "Logement créé avec succès ! Redirection vers la page de connexion...";

    // Rediriger vers la page de connexion après 2 secondes
    setTimeout(() => {
      router.push("/bienvenue"); // Redirection 
    }, 2000);
  } catch (error) {
    console.error("Erreur API : ", error);
    errorMessage.value = "Une erreur est survenue lors de l'inscription. Veuillez réessayer.";
  }
};
</script>



<template>
    <div class="bg-gray-100 min-h-screen">
      <header class="bg-green-600 text-white py-4">
        <div class="container mx-auto flex justify-between items-center">
          <h1 class="text-2xl font-bold">Inscription</h1>
        </div>
      </header>
  
      <section class="container mx-auto py-20">
        <div class="bg-white p-6 rounded-lg shadow">
          <h2 class="text-3xl font-bold text-center text-green-800 mb-6">Formulaire d'Inscription</h2>
          <form @submit.prevent="createLogement">
            <div class="mb-6">
              <label class="block text-green-700 font-bold mb-2">Adresse :</label>
              <input
                type="text"
                v-model="adresse"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
                placeholder="Votre adresse"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-green-700 font-bold mb-2">Téléphone :</label>
              <input
                type="text"
                v-model="telephone"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
                placeholder="Votre téléphone"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-green-700 font-bold mb-2">Adresse IP :</label>
              <input
                type="text"
                v-model="adresse_ip"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
                placeholder="Votre adresse IP"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-green-700 font-bold mb-2">Email :</label>
              <input
                type="email"
                v-model="adresse_email"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
                placeholder="Votre email"
                required
              />
            </div>
            <div class="mb-6">
              <label class="block text-green-700 font-bold mb-2">Mot de Passe :</label>
              <input
                type="password"
                v-model="mot_de_passe"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
                placeholder="Votre mot de passe"
                required
              />
            </div>
            <button
              type="submit"
              class="w-full bg-green-600 text-white py-3 px-4 rounded-lg hover:bg-green-500 transition text-lg font-bold"
            >
              Créer un logement
            </button>
          </form>
          <div v-if="successMessage" class="text-green-500 mt-4 text-center font-bold">
            {{ successMessage }}
          </div>
          <div v-if="errorMessage" class="text-red-500 mt-4 text-center font-bold">
            {{ errorMessage }}
          </div>
        </div>
      </section>
  
      <footer class="bg-green-600 text-white py-4">
        <div class="container mx-auto text-center">
          <p>© 2024 EcoHome. Tous droits réservés.</p>
        </div>
      </footer>
    </div>
</template>
  