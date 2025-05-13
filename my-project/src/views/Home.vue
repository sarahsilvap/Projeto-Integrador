<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useFavoriteStore } from "../stores/FavoritesStore";
import type { Pet } from "../models/pet.js";
import Menu from "../components/Menu.vue";
import Cards from "../components/Cards.vue";

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

const isPetFavorite = (name: string) => {
  return favoritesStore.isFavorite(name);
};
</script>

<template>
  <Menu />
  <div
    class="col-span-4 text-primary text-5xl text-center bg-[#efefef] p-6"
  >
    <h1>🐶 Animais para adoção 😺</h1>
  </div>
  <main
    class="w-full min-h-screen bg-[#efefef] grid grid-cols-4 gap-6 p-5 sm:gap-4 md:gap-3"
  >
    <div
      class="col-span-5 grid grid-cols-1 sm:grid-cols- lg:grid-cols-5 gap-6"
    >
      <Cards v-for="pet in pets" :key="pet._id" :pet="pet" />
    </div>
  </main>
</template>

<style scoped>
.add-button:hover {
  transform: scale(1.15);
}
</style>
