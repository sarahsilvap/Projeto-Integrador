<script setup lang="ts">
import PetCard from "../components/PetCard.vue";
import Menu from "../components/Menu.vue";
import { ref, onMounted } from "vue";
import { Pet } from "../models/pet";
import axios from "axios";

const favorites = ref<Pet[]>([])

const loadFavorites = async () => {
  try {
    const response = await axios.get<Pet[]>("http://localhost:3000/api/favorites", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token") || ""}`,
      },
    });
    favorites.value = response.data;
  } catch (error) {
    console.error("Erro ao carregar favoritos:", error);
  }
};

onMounted(() => {
  loadFavorites();
});
</script>

<template>
  <Menu />

  <div class="container mx-auto px-4 py-8">
    <div class="flex items-center justify-between mb-4">
      <h1 class="text-2xl font-bold">Painel de Administração</h1>
    </div>

    <div
      v-if="favorites.length > 0"
      class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 gap-6"
    >
      <PetCard
        v-for="pet in favorites"
        :key="pet._id"
        :pet="pet"
        :is-favorite="true"
      />
    </div>

    <div v-else class="text-center py-12">
      <p class="text-gray-500 text-lg">Nenhum pet favoritado ainda</p>
      <router-link
        to="/"
        class="mt-4 inline-block px-6 py-2 bg-[#2d74be] text-white rounded-lg hover:bg-[#1a5a9c] transition"
      >
        Explorar Pets
      </router-link>
    </div>
  </div>
</template>
