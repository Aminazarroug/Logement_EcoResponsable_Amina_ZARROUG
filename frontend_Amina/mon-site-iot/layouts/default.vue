<template>
    <div>
      <header class="bg-green-600 text-white py-4">
        <div class="container mx-auto flex justify-between items-center">
          <h1 class="text-xl font-bold">EcoHome</h1>
          <nav class="space-x-4">
            <NuxtLink to="/" class="hover:text-green-200">Accueil</NuxtLink>
            <NuxtLink to="/articles" class="hover:text-green-200">Articles</NuxtLink>
            <NuxtLink to="/Espace_Client" class="hover:text-green-200">Espace Client</NuxtLink>
          </nav>
        </div>
      </header>
      <NuxtPage />
    </div>
</template>