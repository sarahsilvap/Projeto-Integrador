<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { storeToRefs } from 'pinia';
import { useFavoriteStore } from "../stores/FavoritesStore";
import { useFilterStore } from "../stores/Filter";
import type { Pet } from "../models/pet.js";
import Menu from "../components/Menu.vue";
import PetCard from "../components/PetCard.vue";
import SideBar from "../components/SideBar.vue";

// Stores
const filtersStore = useFilterStore();
const { type, size, castrated, age } = storeToRefs(filtersStore);
const { resetFilters } = filtersStore;
const pets = ref<Pet[]>([]);
const loading = ref(false);

type AgeGroup = 'filhote' | 'jovem' | 'adulto' | 'senior';
// Função auxiliar para grupo etário
function getAgeGroup(age: number): AgeGroup {
  if (age < 2) return 'filhote';
  if (age < 5) return 'jovem';
  if (age < 10) return 'adulto';
  return 'senior';
}

// Computed para pets filtrados
const filteredPets = computed(() => {
  return pets.value.filter(pet => {
    const normalizedPetType = pet.type.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    const normalizedPetSize = pet.size.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    // Filtro por tipo
    if (type.value.length > 0) {
      const shouldInclude = type.value.some(filterType => 
        filterType === normalizedPetType
      );
      if (!shouldInclude) return false;
    }
    
    // Filtro por tamanho
    if (size.value.length > 0) {
      const shouldInclude = size.value.some(filterSize => 
        filterSize === normalizedPetSize
      );
      if (!shouldInclude) return false;
    }
    
    // Filtro por castração
    if (castrated.value !== null && pet.castrated !== castrated.value) {
      return false;
    }
    
    // Filtro por idade
    if (age.value.length > 0) {
      const petAgeGroup = getAgeGroup(pet.age);
      if (!(age.value as string[]).includes(petAgeGroup)) {
        return false;
      }
    }
    
    return true;
  });
});

// Carregar pets
onMounted(async () => {
  loading.value = true;
  try {
    const response = await axios.get("http://localhost:3000/api/pets");
    pets.value = response.data;
    console.log(response.data);
  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  } finally {
    loading.value = false;
  }
});

// Lógica de favoritos
const favoritesStore = useFavoriteStore();

const toggleFavorite = (pet: Pet) => {
  if (favoritesStore.isFavorite(pet._id)) {
    favoritesStore.removeFavorite(pet._id);
  } else {
    favoritesStore.addFavorite(pet);
  }
};

const isPetFavorite = (id: string) => {
  return favoritesStore.isFavorite(id);
};
</script>

<template>
  <Menu />
  
  <main class="w-full min-h-screen bg-[#efefef] grid grid-cols-1 lg:grid-cols-5 gap-6 p-5">
    <!-- SideBar -->
    <div class="lg:col-span-1">
      <SideBar />
    </div>
    <div class="lg:col-span-4">

      <div v-if="loading" class="text-center py-12">
        <span class="animate-pulse text-lg">Carregando pets...</span>
      </div>

      <div v-else>
        <div v-if="filteredPets.length === 0" class="text-center py-12">
          <p class="text-xl mb-4">Nenhum pet encontrado com os filtros selecionados.</p>
          <button 
            @click="resetFilters"
            class="px-4 py-2 bg-[#fd6b67] hover:bg-[#fe827e] text-white rounded-lg hover:bg-[#fcca4f] transition"
          >
            Limpar filtros
          </button>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <PetCard 
            v-for="pet in filteredPets" 
            :key="pet._id" 
            :pet="pet"
            :is-favorite="isPetFavorite(pet._id)"
            @toggle-favorite="toggleFavorite(pet)"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.add-button:hover {
  transform: scale(1.15);
  transition: transform 0.2s ease;
}
</style>