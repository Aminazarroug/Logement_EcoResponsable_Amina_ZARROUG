<template>
  <div>
    <!-- Navigation Bar -->
    <NavigationBar />

    <!-- Titre principal -->
    <main class="container mx-auto py-10">
      <h1 class="text-green-700 text-4xl text-center mb-6">Mesures & suivi des moyennes de consommation</h1>

      <!-- Message pour les nouveaux logements -->
      <p v-if="messageTechnicien" class="text-center text-red-600 font-bold mb-6">
        {{ messageTechnicien }}
      </p>

      <!-- Sélecteur de type de mesure -->
      <div class="flex justify-center mb-6">
        <select
          v-model="typeMesure"
          @change="changerParametres"
          class="px-4 py-2 rounded-md bg-white border"
        >
          <option v-for="type in typesMesure" :key="type">{{ type }}</option>
        </select>
      </div>

      <!-- Sélecteur de période -->
      <div class="flex justify-center mb-6">
        <button
          v-for="p in ['annuelle', 'mensuelle', 'hebdomadaire']"
          :key="p"
          @click="changerParametres(p)"
          class="px-4 py-2 mx-2 rounded-md text-white"
          :class="{
            'bg-green-700': periodeActuelle === p,
            'bg-gray-300': periodeActuelle !== p,
          }"
        >
          {{ p.charAt(0).toUpperCase() + p.slice(1) }}
        </button>
      </div>

      <!-- Graphique -->
      <div class="flex justify-center">
        <canvas id="consommationChart" width="800" height="400"></canvas>
      </div>
    </main>

    <!-- Footer -->
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
import { ref, onMounted } from "vue";
import { Chart, registerables } from "chart.js";
import NavigationBar from "~/components/NavigationBar.vue"; // Import de la barre de navigation

Chart.register(...registerables);

/**********************************************
 * VARIABLES RÉACTIVES
 **********************************************/
// Variables pour les données de consommation
const consommation = ref([]);
const typeMesure = ref(""); // Type de mesure sélectionné
const periodeActuelle = ref("annuelle"); // Période par défaut
const chartInstance = ref(null);
const typesMesure = ref([]); // Liste des types de mesure disponibles
const logementId = ref(null); // ID du logement
const messageTechnicien = ref(""); // Message pour les nouveaux logements

// Map des unités en fonction du type de capteur
const unitMap = {
  Électricité: "kWh",
  Eau: "litres",
  Gaz: "m³",
  Température: "°C",
  Humidité: "%",
  Lumière: "lumens",
};

/**********************************************
 * FONCTIONS PRINCIPALES
 **********************************************/
// Fonction pour récupérer l'ID du logement
const fetchLogementId = async () => {
  try {
    const response = await fetch(`http://localhost:8000/logement/id?email=${localStorage.getItem("email")}`);
    const data = await response.json();
    logementId.value = data.id;

    // Si l'ID est supérieur à 100, afficher le message
    if (logementId.value > 100) {
      messageTechnicien.value =
        "Des techniciens viendront vous placer des capteurs dans 48h. Ils vous appelleront avant, et c'est ainsi que nous pourrons commencer à suivre vos différentes consommations.";
    }
  } catch (error) {
    console.error("Erreur lors de la récupération de l'ID du logement :", error);
  }
};

// Fonction pour récupérer les types de capteurs depuis l'API
const fetchTypesMesure = async () => {
  try {
    const response = await fetch("http://localhost:8000/capteurs/types");
    const data = await response.json();
    typesMesure.value = data.types || [];
    if (typesMesure.value.length > 0) {
      typeMesure.value = typesMesure.value[0]; // Définit le premier type par défaut
    }
  } catch (error) {
    console.error("Erreur lors de la récupération des types de mesure :", error);
  }
};

// Fonction pour récupérer les données de consommation depuis l'API
const fetchConsommation = async () => {
  try {
    if (!typeMesure.value) return; // Ne rien faire si aucun type n'est sélectionné

    const response = await fetch(
      `http://localhost:8000/consommation?type_capteur=${typeMesure.value}&periode=${periodeActuelle.value}`
    );
    const data = await response.json();
    consommation.value = data.donnees || [];
    afficherGraphique();
  } catch (error) {
    console.error("Erreur lors de la récupération des données :", error);
  }
};

// Fonction pour afficher le graphique
const afficherGraphique = () => {
  if (chartInstance.value) {
    chartInstance.value.destroy();
  }

  // Trier les données par période (échelle croissante temporelle)
  const sortedData = consommation.value.sort((a, b) =>
    a.periode.localeCompare(b.periode)
  );

  const labels = sortedData.map((data) => data.periode);
  const values = sortedData.map((data) => data.consommation);

  const ctx = document.getElementById("consommationChart").getContext("2d");
  chartInstance.value = new Chart(ctx, {
    type: periodeActuelle === "annuelle" ? "line" : "bar",
    data: {
      labels,
      datasets: [
        {
          label: `Consommation (${typeMesure.value} - ${periodeActuelle.value})`,
          data: values,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 2,
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        tooltip: {
          callbacks: {
            label: (context) => {
              const unit = unitMap[typeMesure.value] || "unités";
              return `${context.raw} ${unit}`;
            },
          },
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: `Consommation (${unitMap[typeMesure.value] || "unités"})`,
          },
          ticks: {
            callback: (value) => {
              const unit = unitMap[typeMesure.value] || "unités";
              return `${value} ${unit}`;
            },
          },
        },
        x: {
          title: {
            display: true,
            text: "Période",
          },
        },
      },
    },
  });
};

// Fonction pour gérer le changement de période ou de type
const changerParametres = (nouvellePeriode) => {
  if (["annuelle", "mensuelle", "hebdomadaire"].includes(nouvellePeriode)) {
    periodeActuelle.value = nouvellePeriode;
    fetchConsommation();
  } else {
    console.error(`Période non valide : ${nouvellePeriode}`);
  }
};

// Charger les données au montage
onMounted(() => {
  fetchLogementId(); // Récupérer l'ID du logement
  fetchTypesMesure().then(() => fetchConsommation());
});
</script>

<style>
body {
  font-family: "Poppins", sans-serif;
  background-color: #f9f9f9;
  margin: 0;
}

header nav a {
  font-size: 1rem;
  font-weight: bold;
  text-decoration: none;
}

button, select {
  cursor: pointer;
}

button.bg-green-700 {
  color: white;
}

button.bg-gray-300 {
  color: black;
}
</style>
