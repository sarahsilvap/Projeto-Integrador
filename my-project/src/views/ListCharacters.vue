<template>
  <Menu />
  <main
    class="w-full min-h-screen bg-gradient-to-r from-gray-950 via-blue-950 to-fuchsia-800 text-white grid grid-cols-4 p-10"
  >
    <div
      class="col-span-4 text-primary text-5xl text-center flex flex-col items-center justify-center"
    >
      <h1>🐶 Animais para adoção 😺</h1>
    </div>
    <div
      class="col-span-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-10"
    >
      <AnimalCard v-for="pet in pets" :key="pet.id" :pet="pet" />
    </div>
  </main>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useFavoriteStore } from "../stores/FavoritesStore";
import type { Pet } from "../models/pet.js";
import Menu from "../components/Menu.vue";

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:3000/api/pets");
    pets.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  }
});

const pets = ref<Pet[]>([]);

const favoritesStore = useFavoriteStore();

const toggleFavorite = async (pet: Pet) => {
  if (favoritesStore.isFavorite(pet.name)) {
    favoritesStore.removeFavorite(pet.name);
  }
};

const isCharacterFavorite = (name: string) => {
  return favoritesStore.isFavorite(name);
};
</script>

<style scoped>
.add-button:hover {
  transform: scale(1.15);
}
</style>
