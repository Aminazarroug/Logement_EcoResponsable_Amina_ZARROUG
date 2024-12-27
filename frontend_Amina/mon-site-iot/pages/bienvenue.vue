<script setup>
import { ref } from "vue";


</script>

<template>
  <div class="bg-gray-100 min-h-screen">
    <header class="bg-green-600 text-white py-4">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold">Bienvenue !</h1>
      </div>
    </header>

    <section class="container mx-auto py-20">
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-3xl font-bold text-center text-green-800 mb-6">
          Félicitations pour votre nouveau compte ! À vous l'éco-responsabilité !
        </h2>

        <p class="text-lg text-center text-gray-700 mb-6">
          Nos techniciens viendront installer les dispositifs nécessaires dans les prochains jours. Ils vous
          contacteront à l'avance pour convenir d'un rendez-vous. Une fois les dispositifs installés, vous pourrez suivre
          vos consommations et économies directement sur votre tableau de bord. D'ici là, nous vous souhaitons bon courage !
        </p>

        <!-- Animation interactive -->
        <div class="flex justify-center">
          <div class="w-1/2 h-1/2">
            <img
              src="/public/technicians-working.png"
              alt="Techniciens"
              class="rounded-lg shadow-lg"
            />
          </div>
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
