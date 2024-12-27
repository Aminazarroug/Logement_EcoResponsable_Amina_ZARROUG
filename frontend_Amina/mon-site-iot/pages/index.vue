<template>
  <div>
    <!-- Header avec menu amélioré -->
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
            <i class="fas fa-newspaper mr-2"></i> Guide Éco-Responsable
          </NuxtLink>
          <NuxtLink to="/Espace_Client" class="hover:text-green-200 flex items-center">
            <i class="fas fa-user-circle mr-2"></i> Espace Client
          </NuxtLink>
        </nav>
      </div>
    </header>

    <!-- Section Hero avec grande image -->
    <section class="relative">
      <!-- Image en arrière-plan -->
      <img src="/public/hero-image.jpg" alt="Hero" class="w-full h-[600px] object-cover" />
      <!-- Texte superposé -->
      <div class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div class="text-center text-white">
          <h1 class="text-4xl font-bold mb-4">Adoptez un mode de vie éco-responsable</h1>
          <p class="text-xl mb-6">
            Découvrez comment réduire votre impact environnemental grâce à des solutions connectées.
          </p>
          <NuxtLink
            to="/Guide"
            class="bg-green-600 text-white px-8 py-4 rounded-lg shadow hover:bg-green-500 text-xl font-bold"
          >
            Découvrir notre guide
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Section des fonctionnalités -->
    <section class="py-20">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-center text-green-700 mb-10">
          Pourquoi choisir EcoHome ?
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Fonctionnalité 1 -->
          <div class="bg-white p-8 rounded-lg shadow-lg hover:shadow-2xl transform hover:-translate-y-2 transition">
            <div class="flex justify-center mb-4">
              <img src="/public/icons/energy.jpg" alt="Energy Optimization" class="h-48 w-72" />
            </div>
            <h3 class="text-2xl font-bold text-green-800 mb-4">Consommation optimisée</h3>
            <p class="text-lg text-gray-600">
              Visualisez et gérez vos consommations d'énergie, d'eau, et de gaz en temps réel.
            </p>
          </div>
          <!-- Fonctionnalité 2 -->
          <div class="bg-white p-8 rounded-lg shadow-lg hover:shadow-2xl transform hover:-translate-y-2 transition">
            <div class="flex justify-center mb-4">
              <img src="/public/icons/environment.jpg" alt="Environmental Impact" class="h-48 w-72" />
            </div>
            <h3 class="text-2xl font-bold text-green-800 mb-4">Impact environnemental</h3>
            <p class="text-lg text-gray-600">
              Réduisez votre empreinte écologique et suivez vos économies réalisées.
            </p>
          </div>
          <!-- Fonctionnalité 3 -->
          <div class="bg-white p-8 rounded-lg shadow-lg hover:shadow-2xl transform hover:-translate-y-2 transition">
            <div class="flex justify-center mb-4">
              <img src="/public/icons/control.png" alt="Control" class="h-48 w-48" />
            </div>
            <h3 class="text-2xl font-bold text-green-800 mb-4">Contrôle intelligent</h3>
            <p class="text-lg text-gray-600">
              Supervisez et contrôlez vos équipements connectés directement depuis votre espace client.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section des témoignages -->
    <section class="bg-gray-100 py-20">
      <div class="container mx-auto text-center">
        <h2 class="text-4xl font-bold text-green-700 mb-10">Ce que nos utilisateurs disent</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Témoignage 1 -->
          <div class="bg-white p-8 rounded-lg shadow">
            <p class="text-xl text-gray-600 italic">"EcoHome a transformé notre façon de consommer. Nous avons réduit nos factures de 30% !"</p>
            <h4 class="mt-4 text-2xl text-green-800 font-bold">- Alice D.</h4>
          </div>
          <!-- Témoignage 2 -->
          <div class="bg-white p-8 rounded-lg shadow">
            <p class="text-xl text-gray-600 italic">"Grâce à EcoHome, nous suivons notre consommation d'énergie en temps réel. Incroyable !"</p>
            <h4 class="mt-4 text-2xl text-green-800 font-bold">- Karim B.</h4>
          </div>
          <!-- Témoignage 3 -->
          <div class="bg-white p-8 rounded-lg shadow">
            <p class="text-xl text-gray-600 italic">"Les graphiques sont superbes et l'expérience utilisateur est impeccable."</p>
            <h4 class="mt-4 text-2xl text-green-800 font-bold">- Sophie L.</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- Section Contact -->
    <section class="py-20 bg-gradient-to-r from-green-50 to-green-100">
      <div class="container mx-auto">
        <h2 class="text-4xl font-bold text-center text-green-700 mb-10">Contactez-nous</h2>
        <div class="max-w-xl mx-auto bg-white p-10 rounded-lg shadow-lg">
          <form>
            <div class="mb-8">
              <label class="block text-gray-700 font-bold mb-2 text-l" for="name">Votre Nom</label>
              <input
                type="text"
                id="name"
                class="w-full px-6 py-4 border rounded-lg text-l focus:ring-2 focus:ring-green-300 focus:outline-none"
                placeholder="Exemple : Jean Dupont"
              />
            </div>
            <div class="mb-8">
              <label class="block text-gray-700 font-bold mb-2 text-l" for="email">Votre Email</label>
              <input
                type="email"
                id="email"
                class="w-full px-6 py-4 border rounded-lg text-l focus:ring-2 focus:ring-green-300 focus:outline-none"
                placeholder="Exemple : jean.dupont@email.com"
              />
            </div>
            <div class="mb-8">
              <label class="block text-gray-700 font-bold mb-2 text-l" for="message">Votre Message</label>
              <textarea
                id="message"
                class="w-full px-6 py-4 border rounded-lg text-l focus:ring-2 focus:ring-green-300 focus:outline-none"
                rows="6"
                placeholder="Dites-nous comment nous pouvons vous aider..."
              ></textarea>
            </div>
            <button
              type="submit"
              class="w-full bg-green-600 text-white px-6 py-4 rounded-lg text-l font-bold shadow-md hover:bg-green-500 transition duration-300"
            >
              Envoyer votre message
            </button>
          </form>
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
