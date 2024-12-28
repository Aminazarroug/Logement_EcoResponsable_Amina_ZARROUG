<script setup>
import { ref } from 'vue';

// Gestion de l'état pour le déroulement
const showArticle1 = ref(false);
const showArticle2 = ref(false);
const showArticle3 = ref(false);
</script>

<template>
  <div>
    <!-- Header avec menu  -->
    <header class="bg-green-600 text-white py-4">
      <div class="container mx-auto flex justify-between items-center">
        <!-- Logo avec icône -->
        <h1 class="text-3xl font-bold flex items-center">
          <i class="fas fa-leaf mr-2"></i> EcoHome
        </h1>
        <!-- Menu de navigation -->
        <nav class="flex space-x-8 text-xl items-center">
          <NuxtLink to="/" class="hover:text-green-200 flex items-center">
            <i class="fas fa-home mr-2"></i> Accueil
          </NuxtLink>
          <NuxtLink to="/Guide" class="hover:text-green-200 flex items-center">
            <i class="fas fa-newspaper mr-2"></i> Articles
          </NuxtLink>
          <NuxtLink to="/Espace_Client" class="hover:text-green-200 flex items-center">
            <i class="fas fa-user-circle mr-2"></i> Espace Client
          </NuxtLink>
        </nav>
      </div>
    </header>

    <!-- Section Articles -->
    <section class="py-20 bg-gray-100">
      <div class="container mx-auto">
        <h2 class="text-4xl font-bold text-center text-green-700 mb-10">
          Notre guide Éco-Responsable
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Article 1 -->
          <div class="bg-white rounded-lg shadow-lg overflow-hidden">
            <img src="/public/icons/energy.jpg" alt="Consommation optimisée" class="w-full h-48 object-cover">
            <div class="p-6">
              <h3 class="text-2xl font-bold text-green-700 mb-2">
                Consommation optimisée
              </h3>
              <p class="text-gray-600 mb-4">
                Visualisez et gérez vos consommations d'énergie, d'eau, et de gaz en temps réel pour réduire vos factures.
              </p>
              <button
                @click="showArticle1 = !showArticle1"
                class="text-green-600 font-bold hover:underline"
              >
                {{ showArticle1 ? 'Masquer l\'article' : 'Lire l\'article →' }}
              </button>
              <div v-if="showArticle1" class="mt-4 text-gray-700 text-lg">
                <p>
                  Une gestion efficace de la consommation énergétique commence par une analyse de vos habitudes quotidiennes. 
                  Identifiez les appareils qui consomment le plus et apprenez à les utiliser de manière plus responsable.
                  Par exemple, éteignez les appareils électroniques lorsqu'ils ne sont pas utilisés et adoptez des systèmes intelligents
                  pour optimiser vos consommations.
                </p>
                <p class="mt-2">
                  Investir dans des équipements connectés tels que des thermostats intelligents ou des systèmes d'éclairage automatisés 
                  peut également grandement réduire votre consommation globale, tout en améliorant votre confort.
                </p>
              </div>
            </div>
          </div>

          <!-- Article 2 -->
          <div class="bg-white rounded-lg shadow-lg overflow-hidden">
            <img src="/public/icons/environment.jpg" alt="Impact environnemental" class="w-full h-48 object-cover">
            <div class="p-6">
              <h3 class="text-2xl font-bold text-green-700 mb-2">
                Impact environnemental
              </h3>
              <p class="text-gray-600 mb-4">
                Réduisez votre empreinte écologique et découvrez les économies réalisées grâce à nos solutions.
              </p>
              <button
                @click="showArticle2 = !showArticle2"
                class="text-green-600 font-bold hover:underline"
              >
                {{ showArticle2 ? 'Masquer l\'article' : 'Lire l\'article →' }}
              </button>
              <div v-if="showArticle2" class="mt-4 text-gray-700 text-lg">
                <p>
                  L'empreinte écologique est un indicateur clé de l'impact de vos activités sur l'environnement. 
                  Pour la réduire, privilégiez des sources d'énergie renouvelable et des équipements à faible consommation. 
                  Par exemple, installez des panneaux solaires ou des chauffe-eaux solaires pour réduire votre dépendance aux énergies fossiles.
                </p>
                <p class="mt-2">
                  De plus, trier vos déchets, composter et utiliser des produits recyclables sont des étapes simples mais efficaces 
                  pour réduire votre impact au quotidien. Ces petits gestes peuvent se traduire par de grandes économies.
                </p>
              </div>
            </div>
          </div>

          <!-- Article 3 -->
          <div class="bg-white rounded-lg shadow-lg overflow-hidden">
            <img src="/public/icons/control.png" alt="Contrôle intelligent" class="w-full h-48 object-cover">
            <div class="p-6">
              <h3 class="text-2xl font-bold text-green-700 mb-2">
                Contrôle intelligent
              </h3>
              <p class="text-gray-600 mb-4">
                Supervisez et contrôlez vos équipements connectés directement depuis votre espace client.
              </p>
              <button
                @click="showArticle3 = !showArticle3"
                class="text-green-600 font-bold hover:underline"
              >
                {{ showArticle3 ? 'Masquer l\'article' : 'Lire l\'article →' }}
              </button>
              <div v-if="showArticle3" class="mt-4 text-gray-700 text-lg">
                <p>
                  Le contrôle intelligent permet d'optimiser l'utilisation de vos appareils connectés. Grâce à des plateformes centralisées, 
                  vous pouvez ajuster la température de votre maison, programmer vos éclairages ou surveiller vos consommations d'énergie en temps réel.
                </p>
                <p class="mt-2">
                  Ces outils offrent une gestion simplifiée et efficace, tout en réduisant les coûts inutiles. 
                  Ils sont également idéaux pour anticiper les besoins en énergie et maintenir un confort optimal dans votre habitat.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-green-600 text-white py-6">
      <div class="container mx-auto text-center">
        <p class="text-l">© 2024 EcoHome. Tous droits réservés.</p>
      </div>
    </footer>
  </div>
</template>
