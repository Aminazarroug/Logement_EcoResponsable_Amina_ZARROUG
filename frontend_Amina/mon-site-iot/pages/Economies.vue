<template>
    <div>
      <NavigationBar />
  
      <main class="container mx-auto py-10">
        <h1 class="text-green-700 text-4xl text-center mb-6">Économies Réalisées</h1>
  
        <!-- Texte explicatif -->
        <p class="text-lg text-gray-600 text-center mb-8">
          Cette section affiche vos économies réalisées uniquement pour 
          <strong>l'électricité</strong>, <strong>l'eau</strong>, et <strong>le gaz</strong>.
        </p>
  
        <!-- Sélecteur de date -->
        <div class="flex justify-center mb-6">
          <input
            type="month"
            v-model="selectedDate"
            @change="fetchEconomies"
            class="px-4 py-2 rounded-md bg-white border"
          />
        </div>
  
        <!-- Résumé des moyennes -->
        <div v-if="economies" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="(data, type) in economies"
            :key="type"
            class="p-6 bg-white rounded-lg shadow-lg border"
          >
            <h2 class="text-xl font-bold text-green-700 mb-4">{{ type }}</h2>
            <p class="text-gray-600">
              <strong>Moyenne actuelle :</strong> 
              {{ data.moyenne_actuelle.toFixed(2) }} 
              {{ type === "Eau" ? "litres" : type === "Électricité" ? "kWh" : type === "Gaz" ? "m³" : "unités" }}
            </p>
            <p class="text-gray-600">
              <strong>Moyenne période précédente :</strong> 
              {{ data.moyenne_periode_precedente.toFixed(2) }} 
              {{ type === "Eau" ? "litres" : type === "Électricité" ? "kWh" : type === "Gaz" ? "m³" : "unités" }}
            </p>
            <p class="text-gray-600">
              <strong>Économies en consommation :</strong> 
              {{ data.economie_consommation.toFixed(2) }} 
              {{ type === "Eau" ? "litres" : type === "Électricité" ? "kWh" : type === "Gaz" ? "m³" : "unités" }}
            </p>
            <p class="text-gray-600">
              <strong>Économies financières :</strong> {{ data.economie_financiere.toFixed(2) }} €
            </p>
            <!-- Commentaire -->
            <p 
              class="text-gray-700 font-semibold mt-4"
              :class="data.economie_consommation > 0 ? 'text-green-600' : 'text-red-600'"
            >
              {{ data.economie_consommation > 0 
                ? 'Bravo ! Vous avez réalisé des économies cette période.' 
                : 'Attention ! Votre consommation a augmenté par rapport à la période précédente.' 
              }}
            </p>
          </div>
        </div>
  
        <!-- Graphique -->
        <div class="flex justify-center mt-8">
          <canvas id="economiesChart" width="800" height="400"></canvas>
        </div>
      </main>
  
      <footer class="bg-green-700 text-white py-4 mt-10">
        <div class="container mx-auto text-center">
          <p>© 2024 EcoHome. Tous droits réservés.</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { Chart, registerables } from "chart.js";
  import NavigationBar from "~/components/NavigationBar.vue";
  
  Chart.register(...registerables);
  
  const selectedDate = ref(new Date().toISOString().slice(0, 7)); // Mois actuel
  const economies = ref(null); // Données des économies
  const chartInstance = ref(null); // Instance du graphique
  
  // Fonction pour récupérer les données d'économies via l'API
  const fetchEconomies = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/economies/consommation?date=${selectedDate.value}&periode=mensuelle`
      );
      const data = await response.json();
      economies.value = data.economies;
      afficherGraphique();
    } catch (error) {
      console.error("Erreur lors de la récupération des données :", error);
    }
  };
  
// Fonction pour afficher le graphique avec normalisation
const afficherGraphique = () => {
  if (chartInstance.value) {
    chartInstance.value.destroy();
  }

  const ctx = document.getElementById("economiesChart").getContext("2d");

  // Définir les plages pour la normalisation des capteurs
  const ranges = {
    Électricité: { min: 1, max: 10 }, 
    Eau: { min: 0, max: 500 },         
    Gaz: { min: 200, max: 1000 },       
  };

  const labels = Object.keys(economies.value); // Types de capteurs (Électricité, Eau, Gaz)

  // Normaliser les données des capteurs
  const normalize = (value, type) => {
    const range = ranges[type];
    return (value - range.min) / (range.max - range.min);
  };

  const moyennesActuelles = labels.map((type) =>
    normalize(economies.value[type].moyenne_actuelle, type)
  );
  const moyennesPeriodesPrecedentes = labels.map((type) =>
    normalize(economies.value[type].moyenne_periode_precedente, type)
  );
  const economiesFinancieres = labels.map((type) =>
    normalize(economies.value[type].economie_financiere, type)
  );

  chartInstance.value = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "Moyenne Actuelle (Normalisée)",
          data: moyennesActuelles,
          backgroundColor: "rgba(75, 192, 192, 0.5)",
        },
        {
          label: "Moyenne Période Précédente (Normalisée)",
          data: moyennesPeriodesPrecedentes,
          backgroundColor: "rgba(192, 75, 75, 0.5)",
        },
        {
          label: "Économies Financières (Normalisées)",
          data: economiesFinancieres,
          backgroundColor: "rgba(75, 192, 75, 0.5)",
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
            label: (tooltipItem) => {
              const typeCapteur = tooltipItem.label;
              const value = tooltipItem.raw;

              // Ajouter des unités spécifiques pour chaque type
              let unit = "unités";
              if (typeCapteur === "Électricité") unit = "kWh";
              else if (typeCapteur === "Eau") unit = "litres";
              else if (typeCapteur === "Gaz") unit = "m³";

              return `Valeur normalisée : ${value.toFixed(2)} (${unit})`;
            },
          },
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "Valeurs Normalisées (0 à 1)",
          },
        },
        x: {
          title: {
            display: true,
            text: "Type de Capteur",
          },
        },
      },
    },
  });
};


  
  // Charger les données au montage
  onMounted(() => {
    fetchEconomies();
  });
  </script>
  
  <style>
  button, select, input {
    cursor: pointer;
  }
  
  button.bg-green-700 {
    color: white;
  }
  
  button.bg-gray-300 {
    color: black;
  }
  </style>
  