<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import type { Pet } from "../models/pet.js";

const props = defineProps<{
  pet: Pet;
  isFavorite: boolean;
}>();

const emit = defineEmits(['toggle-favorite']);
</script>

<template>
  <div class="pet-card bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
    <div class="relative">
      <img
        class="w-full h-48 object-cover"
        :src="pet.imageUrl || 'https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb'"
        :alt="pet.name"
      />
      <button
        @click.stop="emit('toggle-favorite')"
        class="absolute top-2 right-2 p-2 bg-white/80 rounded-full hover:bg-white transition"
        aria-label="Favoritar"
      >
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          class="h-6 w-6" 
          :class="isFavorite ? 'text-red-500 fill-current' : 'text-gray-400 fill-none stroke-current'"
          viewBox="0 0 24 24"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </button>
    </div>
    
    <div class="p-4">
      <div class="flex justify-between items-start mb-2">
        <h3 class="text-xl font-bold text-gray-800">{{ pet.name }}</h3>
        <span 
          class="px-2 py-1 text-xs font-semibold rounded-full"
          :class="pet.type === 'dog' ? 'bg-blue-100 text-blue-800' : 'bg-purple-100 text-purple-800'"
        >
          {{ pet.type === 'dog' ? 'Cachorro' : 'Gato' }}
        </span>
      </div>
      
      <div class="flex flex-wrap gap-2 mb-3">
        <span class="text-xs bg-gray-100 px-2 py-1 rounded">
          {{ pet.size === 'small' ? 'Pequeno' : pet.size === 'medium' ? 'Médio' : 'Grande' }}
        </span>
        <span class="text-xs bg-gray-100 px-2 py-1 rounded">
          {{ pet.castrated ? 'Castrado' : 'Não castrado' }}
        </span>
        <span class="text-xs bg-gray-100 px-2 py-1 rounded">
          {{ pet.age }} anos
        </span>
      </div>
      
      <p class="text-gray-600 mb-4 line-clamp-2">
        {{ pet.description || 'Este pet está procurando um lar amoroso!' }}
      </p>
      
      <button
        class="w-full flex items-center justify-center gap-2 px-4 py-2 bg-[#faa72d] hover:bg-[#fcca4f] text-white rounded-lg transition"
      >
        Quero adotar
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.pet-card {
  transition: transform 0.2s ease;
}

.pet-card:hover {
  transform: translateY(-4px);
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>