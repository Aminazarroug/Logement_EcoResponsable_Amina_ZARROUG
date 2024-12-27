<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

// Références pour les champs du formulaire
const email = ref("");
const password = ref("");
const errorMessage = ref("");
const router = useRouter();

// Fonction de connexion
const login = async () => {
  try {
    // Appel API pour la connexion
    const response = await axios.post("http://127.0.0.1:8000/login", {
      email: email.value,
      password: password.value,
    });

    // Si succès, enregistrer l'email et le mot de passe dans localStorage
    localStorage.setItem("email", email.value);
    localStorage.setItem("password", password.value);

    // Si succès, redirection vers Mon espace avec les données du logement
    router.push({
      path: "/MonEspace",
      query: {
        email: email.value, // Passer l'email dans les query params
        logement: JSON.stringify(response.data.logement), // Passer les données du logement
      },
    });
  } catch (error) {
    // Gestion des erreurs
    console.error("Erreur API : ", error);
    if (error.response && error.response.status === 401) {
      errorMessage.value = "Email ou mot de passe invalide.";
    } else {
      errorMessage.value = "Une erreur est survenue. Veuillez réessayer.";
    }
  }
};

// Fonction pour rediriger vers la page de création de compte
const goToSubscription = () => {
  router.push("/Subscription");
};
</script>

<template>
  <div class="bg-gray-100 min-h-screen">
    <header class="bg-green-600 text-white py-4">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold">Espace Client</h1>
      </div>
    </header>

    <section class="container mx-auto py-20 grid grid-cols-1 md:grid-cols-2 gap-10">
      <!-- Section de gauche -->
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-4xl font-bold text-green-800 mb-4">Bienvenue dans l'espace client</h2>
        <p class="text-lg text-gray-700 mb-6">
          Connectez-vous avec votre email et mot de passe pour accéder à vos informations de logement.
        </p>
      </div>

      <!-- Section de droite -->
      <div class="bg-green-50 p-6 rounded-lg shadow">
        <h2 class="text-3xl font-bold text-center text-green-800 mb-6">Connexion</h2>
        <form @submit.prevent="login">
          <div class="mb-6">
            <label for="email" class="block text-green-700 font-bold mb-2">Adresse Email :</label>
            <input
              type="email"
              id="email"
              name="email"
              v-model="email"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none text-lg"
              placeholder="Votre adresse email"
              required
            />
          </div>
          <div class="mb-6">
            <label for="password" class="block text-green-700 font-bold mb-2">Mot de passe :</label>
            <input
              type="password"
              id="password"
              name="password"
              v-model="password"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none text-lg"
              placeholder="Votre mot de passe"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full bg-green-600 text-white py-3 px-4 rounded-lg hover:bg-green-500 transition text-lg font-bold"
          >
            Se connecter
          </button>
        </form>
        <div v-if="errorMessage" class="text-red-500 mt-4 text-center font-bold">
          {{ errorMessage }}
        </div>
        <div class="mt-6 text-center">
          <button
            @click="goToSubscription"
            class="text-green-600 underline text-lg font-bold"
          >
            Créer un compte
          </button>
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
