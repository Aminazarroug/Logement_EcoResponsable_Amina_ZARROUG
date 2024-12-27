export default defineNuxtConfig({
  // Lien vers ton fichier principal de styles
  css: ['@/assets/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },




  compatibilityDate: '2024-12-13',
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000', // URL de base pour votre API
    },
  },

  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/icon?family=Material+Icons",
        },
      ],
    },
  },
  


});
