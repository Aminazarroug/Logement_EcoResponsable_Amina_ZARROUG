<template>
  <!-- Section principale du composant -->
  <div>
    <!-- Menu de navigation inclus depuis le composant NavigationBar -->
    <NavigationBar />

    <!-- Contenu principal -->
    <main class="container mx-auto py-10">
      <!-- Section des capteurs -->
      <h1 class="text-green-700 text-4xl text-center mb-6">Capteurs</h1>
      <p class="text-lg text-gray-600 text-center mb-8">
        Voici l'état de vos capteurs connectés et leurs informations détaillées :
      </p>

      <!-- Message d'erreur si disponible -->
      <div v-if="errorMessage" class="text-center text-red-500 font-bold">
        {{ errorMessage }}
      </div>

      <!-- Chargement ou liste des capteurs -->
      <div v-else-if="sensors.length === 0" class="text-center text-gray-600">
        Chargement des capteurs...
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="sensor in sensors"
          :key="sensor.ID_Device"
          class="p-6 bg-white rounded-lg shadow-lg border"
        >
          <h2 class="text-xl font-bold text-green-700 mb-4">{{ sensor.Nom_Type }}</h2>
          <p class="text-gray-600">
            <strong>ID :</strong> {{ sensor.ID_Device }}
          </p>
          <p class="text-gray-600">
            <strong>Référence :</strong> {{ sensor.Référence_commerciale }}
          </p>
          <p class="text-gray-600">
            <strong>Port :</strong> {{ sensor.Port_communication }}
          </p>
          <p class="text-gray-600">
            <strong>État :</strong>
            <span
              :class="{
                'text-green-600': sensor.Etat === 1,
                'text-red-600': sensor.Etat === 0,
              }"
            >
              {{ sensor.Etat === 1 ? 'Allumé' : 'Éteint' }}
            </span>
          </p>
        </div>
      </div>

      <!-- Section des actionneurs -->
      <h1 class="text-green-700 text-4xl text-center mt-12 mb-6">Actionneurs</h1>
      <p class="text-lg text-gray-600 text-center mb-8">
        Voici l'état de vos actionneurs connectés et leurs informations détaillées :
      </p>

      <!-- Chargement ou liste des actionneurs -->
      <div v-if="actuators.length === 0" class="text-center text-gray-600">
        Chargement des actionneurs...
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="actuator in actuators"
          :key="actuator.ID_Device"
          class="p-6 bg-white rounded-lg shadow-lg border"
        >
          <h2 class="text-xl font-bold text-green-700 mb-4">{{ actuator.Nom_Type }}</h2>
          <p class="text-gray-600">
            <strong>ID :</strong> {{ actuator.ID_Device }}
          </p>
          <p class="text-gray-600">
            <strong>Référence :</strong> {{ actuator.Référence_commerciale }}
          </p>
          <p class="text-gray-600">
            <strong>Port :</strong> {{ actuator.Port_communication }}
          </p>
          <p class="text-gray-600">
            <strong>État :</strong>
            <span
              :class="{
                'text-green-600': actuator.Etat === 1,
                'text-red-600': actuator.Etat === 0,
              }"
            >
              {{ actuator.Etat === 1 ? 'Allumé' : 'Éteint' }}
            </span>
          </p>
        </div>
      </div>
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
import NavigationBar from "@/components/NavigationBar.vue"; // Assurez-vous que le chemin est correct

/**********************************************
 * VARIABLES REACTIVES
 **********************************************/
// Stockage des capteurs et actionneurs
const sensors = ref([]);
const actuators = ref([]);
const email = ref("");
const password = ref("");
const errorMessage = ref("");

/**********************************************
 * FONCTIONS PRINCIPALES
 **********************************************/
const fetchDevices = async () => {
  try {
    // Validation des identifiants
    if (!email.value || !password.value) {
      errorMessage.value = "Veuillez vous connecter.";
      return;
    }

    const response = await fetch("http://localhost:8000/devices", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email.value, password: password.value }),
    });

    const data = await response.json();
    if (!data.devices) {
      errorMessage.value = "Impossible de récupérer les dispositifs.";
      return;
    }

    // Séparer capteurs et actionneurs
    sensors.value = data.devices.filter((device) =>
      ["Température", "Humidité", "Électricité", "Gaz", "Lumière", "Eau"].includes(device.Nom_Type)
    );
    actuators.value = data.devices.filter((device) =>
      ["Présence", "Volet"].includes(device.Nom_Type)
    );
  } catch (error) {
    console.error("Erreur lors de la récupération des dispositifs :", error);
    errorMessage.value = "Une erreur est survenue lors de la récupération des dispositifs.";
  }
};

/**********************************************
 * VÉRIFICATION DE L'AUTHENTIFICATION
 **********************************************/
const verifyAuth = () => {
  email.value = localStorage.getItem("email") || "";
  password.value = localStorage.getItem("password") || "";

  if (!email.value || !password.value) {
    errorMessage.value = "Vous devez être connecté pour accéder à cette page.";
    setTimeout(() => (window.location.href = "/login"), 2000); // Rediriger vers la page de connexion
  }
};

/**********************************************
 * LIFECYCLE HOOKS
 **********************************************/
onMounted(() => {
  verifyAuth(); // Vérification des identifiants
  fetchDevices(); // Récupération des dispositifs
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
