<template>
  <main
    class="w-full min-h-screen bg-gradient-to-r from-gray-950 via-blue-950 to-fuchsia-800 text-white">
    <div class="col-span-4 text-primary text-5xl text-center flex flex-col items-center justify-center">
      <h1 class="mt-8">
        🚀 Meus Favoritos de Star Wars 🛸
      </h1>
      <div class="m-8 flex items-center text-lg">
        <p>Seguir para:</p>
        <ButtonRouteLabel />
      </div>
    </div>
    <Cards :characters="characters" />
  </main>
</template>

<script setup lang="ts">
import Cards from "../components/Cards.vue"
import ButtonRouteLabel from "../components/ButtonRouteLabel.vue";
import { useFavoriteStore } from '../stores/FavoritesStore';
import { computed } from "vue";
// import Menu from "../components/Menu.vue";

const favoritesStore = useFavoriteStore();

const characters = computed(() => favoritesStore.favorites);

</script>

<style scoped></style>