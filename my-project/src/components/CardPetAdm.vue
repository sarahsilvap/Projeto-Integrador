<script setup lang="ts">
import type { Pet } from "../models/pet.js";
import { ref } from 'vue';

const props = defineProps<{
  pet: Pet;
}>();

const emit = defineEmits(["edit", "delete"]);

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

const confirmDelete = () => {
  if (confirm(`Tem certeza que deseja excluir ${props.pet.name}?`)) {
    emit('delete', props.pet._id);
  }
};

const isExpanded = ref(false);
</script>

<template>
  <div
    class="pet-card-admin bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 relative flex flex-col"
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
      <!-- Botões de administração -->
      <div class="absolute top-2 right-2 flex gap-2">
        <button
          @click.stop="emit('edit', pet)"
          class="p-2 bg-white/80 rounded-full hover:bg-white transition"
          aria-label="Editar"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
        </button>
        <button
          @click.stop="confirmDelete"
          class="p-2 bg-white/80 rounded-full hover:bg-white transition"
          aria-label="Excluir"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </div>
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
          <p class="text-gray-600 mb-4" :class="{ 'line-clamp-2': !isExpanded }">
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
            {{ isExpanded ? 'Ver menos' : 'Ver mais' }}
          </button>
        </div>
      </div>

      <!-- Status de disponibilidade mais destacado -->
      <div class="mt-auto">
        <div class="text-center py-2 rounded-lg" 
             :class="pet.available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
          {{ pet.available ? "Disponível para adoção" : "Indisponível" }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pet-card-admin {
  transition: transform 0.2s ease;
  min-height: 450px;
}

.pet-card-admin:hover {
  transform: translateY(-4px);
}
</style>