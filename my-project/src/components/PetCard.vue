<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import type { Pet } from "../models/pet.js";
import { ref } from "vue";
import { useFavoriteStore } from "../stores/FavoritesStore.js";
import { computed, nextTick } from "vue";

const props = defineProps<{
  pet: Pet;
}>();

const favoritesStore = useFavoriteStore();
const isFavorite = computed(() => favoritesStore.isFavorite(props.pet._id));

const toggleFavorite = async () => {
  try {
    if (isFavorite.value) {
      await favoritesStore.removeFavorite(props.pet._id);
    } else {
      console.log("Antes de adicionar:", isFavorite.value);
      await favoritesStore.addFavorite(props.pet);
      console.log("Depois de adicionar:", isFavorite.value);
      await nextTick();
    }
  } catch (error) {
    console.error("Erro ao atualizar favorito:", error);
  }
};

const emit = defineEmits(["toggle-favorite"]);

const getPetTypeDisplay = (type: string) => {
  const normalizedType = type
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
  return normalizedType.includes("dog") ? "Cachorro" : "Gato";
};

const getPetSizeDisplay = (size: string) => {
  switch (size.toLowerCase()) {
    case "small":
      return "Pequeno";
    case "medium":
      return "Médio";
    case "large":
      return "Grande";
    default:
      return "Tamanho desconhecido";
  }
};

const isExpanded = ref(false);
</script>

<template>
  <div
    class="pet-card bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 relative flex flex-col"
  >
    <div class="relative">
      <img
        class="w-full h-62 object-cover"
        :src="
          pet.coverImage
            ? `http://localhost:3000${pet.coverImage}`
            : 'https://arktus.com.br/images/image-404.png'
        "
        :alt="pet.name"
      />
      <button
        @click.stop="toggleFavorite"
        class="absolute top-2 right-2 p-2 bg-white/80 rounded-full hover:bg-white transition"
        aria-label="Favoritar"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          :class="
            isFavorite
              ? 'text-red-500 fill-current'
              : 'text-gray-400 fill-none stroke-current'
          "
          viewBox="0 0 24 24"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
          />
        </svg>
      </button>
    </div>

    <div class="p-4 flex flex-col flex-grow">
      <div>
        <div class="flex justify-between items-start mb-2">
          <h3 class="text-xl font-bold text-gray-800">
            {{ pet.name || "Nome não disponível" }}
          </h3>
          <span
            class="px-2 py-1 text-xs font-semibold rounded-full"
            :class="
              getPetTypeDisplay(pet.type) === 'Cachorro'
                ? 'bg-blue-100 text-blue-800'
                : 'bg-purple-100 text-purple-800'
            "
          >
            {{ getPetTypeDisplay(pet.type) }}
          </span>
        </div>

        <div class="flex flex-wrap gap-2 mb-3">
          <span class="text-xs bg-gray-100 px-2 py-1 rounded">
            {{ getPetSizeDisplay(pet.size) }}
          </span>
          <span class="text-xs bg-gray-100 px-2 py-1 rounded">
            {{ pet.castrated ? "Castrado" : "Não castrado" }}
          </span>
          <span class="text-xs bg-gray-100 px-2 py-1 rounded">
            {{ pet.age }} {{ pet.age === 1 ? "ano" : "anos" }}
          </span>
          <span class="text-xs bg-gray-100 px-2 py-1 rounded">
            {{ pet.available ? "Disponível" : "Indisponível" }}
          </span>
        </div>

        <div class="relative">
          <p
            class="text-gray-600 mb-4"
            :class="{ 'line-clamp-2': !isExpanded }"
          >
            {{
              pet.description
                ? pet.description
                : "Este pet está procurando um lar amoroso!"
            }}
          </p>
          <button
            v-if="pet.description && pet.description.length > 100"
            @click="isExpanded = !isExpanded"
            class="text-[#2d74be] text-sm font-medium hover:underline focus:outline-none"
          >
            {{ isExpanded ? "Ver menos" : "Ver mais" }}
          </button>
        </div>
      </div>

      <button
        class="mt-auto w-full flex items-center justify-center gap-2 px-4 py-2 bg-[#2d74be] hover:bg-[#79bbec] text-white rounded-lg transition"
        :disabled="!pet.available"
        :class="{ 'opacity-50 cursor-not-allowed': !pet.available }"
      >
        {{ pet.available ? "Quero adotar" : "Indisponível" }}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M14 5l7 7m0 0l-7 7m7-7H3"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.pet-card {
  transition: transform 0.2s ease;
  min-height: 500px; /* ou qualquer altura que faça sentido para seu layout */
}

.pet-card:hover {
  transform: translateY(-4px);
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
