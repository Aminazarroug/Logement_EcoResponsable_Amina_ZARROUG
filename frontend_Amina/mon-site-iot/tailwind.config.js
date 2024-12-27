/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{vue,js,ts}",
    "./layouts/**/*.{vue,js,ts}",
    "./pages/**/*.{vue,js,ts}",
    "./app.vue",
    "./nuxt.config.ts",
  ],
  theme: {
    extend: {},
  },
  plugins: [],

  resolve: {
    alias: {
      'chart.js': 'chart.js/dist/chart.esm.js',
    },
  },
};

