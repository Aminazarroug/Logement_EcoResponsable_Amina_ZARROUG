<template>
  <div>
    <!-- Navigation Bar -->
    <NavigationBar />

    <!-- Contenu Principal -->
    <main class="container mx-auto py-10">
      <h1 class="text-green-700 text-4xl text-center mb-6">Gestion des Dispositifs</h1>
      <p class="text-lg text-gray-600 text-center mb-8">
        Ajoutez ou supprimez des dispositifs facilement depuis cette page.
      </p>

      <!-- Section pour Ajouter un Dispositif -->
      <section class="mb-10">
        <h2 class="text-2xl text-green-700 font-bold mb-4">Ajouter un Dispositif</h2>
        <form @submit.prevent="addDevice" class="bg-white p-6 rounded-lg shadow-lg">
          <label class="block mb-2 font-bold">Type de Dispositif</label>
          <select v-model="newDevice.id_type" class="w-full px-4 py-2 mb-4 border rounded-md">
            <option v-for="type in deviceTypes" :key="type.id_type" :value="type.id_type">
              {{ type.nom_type }}
            </option>
          </select>

          <label class="block mb-2 font-bold">ID de la Pièce</label>
          <input
            v-model="newDevice.id_piece"
            type="number"
            class="w-full px-4 py-2 mb-4 border rounded-md"
            required
          />

          <label class="block mb-2 font-bold">Référence Commerciale</label>
          <input
            v-model="newDevice.reference_commerciale"
            type="text"
            class="w-full px-4 py-2 mb-4 border rounded-md"
            required
          />

          <label class="block mb-2 font-bold">Port de Communication</label>
          <input
            v-model="newDevice.port_communication"
            type="text"
            class="w-full px-4 py-2 mb-4 border rounded-md"
            required
          />

          <button
            type="submit"
            class="px-4 py-2 bg-green-700 text-white rounded-md hover:bg-green-800"
          >
            Ajouter le Dispositif
          </button>
        </form>
      </section>

      <!-- Section pour Supprimer un Dispositif -->
      <section>
        <h2 class="text-2xl text-red-700 font-bold mb-4">Supprimer un Dispositif</h2>
        <form @submit.prevent="deleteDevice" class="bg-white p-6 rounded-lg shadow-lg">
          <label class="block mb-2 font-bold">ID du Dispositif à Supprimer</label>
          <input
            v-model="deleteDeviceId"
            type="number"
            class="w-full px-4 py-2 mb-4 border rounded-md"
            required
          />

          <button
            type="submit"
            class="px-4 py-2 bg-red-700 text-white rounded-md hover:bg-red-800"
          >
            Supprimer le Dispositif
          </button>
        </form>
      </section>

      <!-- Message d'erreur ou de succès -->
      <div v-if="message" class="mt-8 text-center">
        <p
          :class="{
            'text-red-500': isError,
            'text-green-500': !isError
          }"
          class="text-lg font-bold"
        >
          {{ message }}
        </p>
      </div>
    </main>
  </div>
</template>

<script setup>
/**********************************************
 * IMPORTATIONS
 **********************************************/
import { ref, onMounted } from "vue";
import NavigationBar from "@/components/NavigationBar.vue";
import axios from "axios";

/**********************************************
 * VARIABLES REACTIVES
 **********************************************/
const deviceTypes = ref([]); // Liste des types de dispositifs
const newDevice = ref({
  id_type: null,
  id_piece: null,
  reference_commerciale: "",
  port_communication: "",
}); // Nouveau dispositif à ajouter
const deleteDeviceId = ref(null); // ID du dispositif à supprimer
const message = ref(""); // Message de succès ou d'erreur
const isError = ref(false); // Indicateur pour afficher le message en rouge ou vert

/**********************************************
 * FONCTIONS PRINCIPALES
 **********************************************/
// Fonction pour récupérer les types de dispositifs
const fetchDeviceTypes = async () => {
  try {
    const response = await axios.get("http://localhost:8000/devices/types");
    deviceTypes.value = response.data.types || [];
  } catch (error) {
    console.error("Erreur lors de la récupération des types de dispositifs :", error);
    message.value = "Erreur lors de la récupération des types de dispositifs.";
    isError.value = true;
  }
};

// Fonction pour ajouter un dispositif
const addDevice = async () => {
  try {
    // Récupérer l'email et le mot de passe du localStorage
    const email = localStorage.getItem("email");
    const password = localStorage.getItem("password");

    if (!email || !password) {
      message.value = "Utilisateur non authentifié. Veuillez vous connecter.";
      isError.value = true;
      return;
    }

    // Préparer les données pour la requête
    const requestData = {
      email: email,
      password: password,
      id_type: newDevice.value.id_type,
      id_piece: newDevice.value.id_piece,
      reference_commerciale: newDevice.value.reference_commerciale,
      port_communication: newDevice.value.port_communication,
    };

    // Envoyer la requête POST pour ajouter le dispositif
    const response = await axios.post("http://localhost:8000/devices/add", requestData);

    // Message de succès
    message.value = response.data.message || "Dispositif ajouté avec succès.";
    isError.value = false;

    // Réinitialiser le formulaire
    newDevice.value = {
      id_type: null,
      id_piece: null,
      reference_commerciale: "",
      port_communication: "",
    };
  } catch (error) {
    console.error("Erreur lors de l'ajout du dispositif :", error);
    message.value = "Erreur lors de l'ajout du dispositif.";
    isError.value = true;
  }
};

// Fonction pour supprimer un dispositif
const deleteDevice = async () => {
  try {
    const response = await axios.delete("http://localhost:8000/devices/delete", {
      data: { id_device: deleteDeviceId.value },
    });
    message.value = response.data.message || "Dispositif supprimé avec succès.";
    isError.value = false;
    // Réinitialiser le champ ID
    deleteDeviceId.value = null;
  } catch (error) {
    console.error("Erreur lors de la suppression du dispositif :", error);
    message.value = "Erreur lors de la suppression du dispositif.";
    isError.value = true;
  }
};

// Fonction pour enregistrer les données d'utilisateur
const saveUserData = (email, password) => {
  localStorage.setItem("email", email);
  localStorage.setItem("password", password);
  alert("Utilisateur enregistré !");
};

/**********************************************
 * LIFECYCLE HOOKS
 **********************************************/
onMounted(() => {
  fetchDeviceTypes(); // Récupérer les types de dispositifs au montage
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

button {
  cursor: pointer;
}

button:hover {
  opacity: 0.9;
}
</style>
