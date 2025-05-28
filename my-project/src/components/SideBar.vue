<script setup lang="ts">
import { useFilterStore } from '../stores/Filter';
import { storeToRefs } from 'pinia';
import type { PetType, PetSize, AgeGroup } from '../models/pet';


const filtersStore = useFilterStore();
const { type, size, castrated, age } = storeToRefs(filtersStore);
const { updateFilter, resetFilters } = filtersStore;

const ageGroups: { value: AgeGroup; label: string }[] = [
  { value: "filhote", label: "Filhote (0-2 anos)" },
  { value: "jovem", label: "Jovem (2-5 anos)" },
  { value: "adulto", label: "Adulto (5-10 anos)" },
  { value: "idoso", label: "Idoso (10+ anos)" },
];

const typeMap = {
  cachorro: "dog",
  gato: "cat"
};

const sizeMap = {
  pequeno: "small",
  medio: "medium",
  grande: "large"
};

function handleTypeChange(e: Event, petType: PetType) {
  const target = e.target as HTMLInputElement;
  const newTypes = target.checked
    ? [...type.value, petType]
    : type.value.filter(t => t !== petType);
  updateFilter('type', newTypes);
}

function handleSizeChange(e: Event, petSize: PetSize) {
  const target = e.target as HTMLInputElement;
  const newSizes = target.checked
    ? [...size.value, petSize]
    : size.value.filter((s) => s !== petSize);
  updateFilter("size", newSizes);
}

function handleAgeChange(e: Event, ageGroup: AgeGroup) {
  const target = e.target as HTMLInputElement;
  const newAges = target.checked
    ? [...age.value, ageGroup]
    : age.value.filter((a) => a !== ageGroup);
  updateFilter("age", newAges);
}

function handleCastratedChange(value: boolean | null) {
  updateFilter("castrated", value);
}

function handleReset() {
  resetFilters();
}


</script>

<template>
  <div class="bg-white p-5 rounded-lg shadow-sm sticky top-5">
    <h2 class="text-xl font-bold mb-6 text-gray-800">Filtrar por:</h2>

    <!-- Tipo de Animal -->
    <div class="mb-6">
      <h3 class="font-semibold mb-3 text-gray-700">Tipo</h3>
      <div class="space-y-2">
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="type.includes('dog')"
            @change="(e) => handleTypeChange(e, 'dog')"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Cachorro</span>
        </label>
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="type.includes('cat')"
            @change="(e) => handleTypeChange(e, 'cat')"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Gato</span>
        </label>
      </div>
    </div>

    <!-- Tamanho -->
    <div class="mb-6">
      <h3 class="font-semibold mb-3 text-gray-700">Tamanho</h3>
      <div class="space-y-2">
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="size.includes('small')"
            @change="(e) => handleSizeChange(e, 'small')"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Pequeno</span>
        </label>
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="size.includes('medium')"
            @change="(e) => handleSizeChange(e, 'medium')"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Médio</span>
        </label>
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="size.includes('large')"
            @change="(e) => handleSizeChange(e, 'large')"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Grande</span>
        </label>
      </div>
    </div>

    <!-- Castração -->
    <div class="mb-6">
      <h3 class="font-semibold mb-3 text-gray-700">Castrado</h3>
      <div class="space-y-2">
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="radio"
            :checked="castrated === true"
            @change="() => handleCastratedChange(true)"
            class="rounded-full h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Sim</span>
        </label>
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="radio"
            :checked="castrated === false"
            @change="() => handleCastratedChange(false)"
            class="rounded-full h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Não</span>
        </label>
        <label class="flex items-center gap-3 cursor-pointer">
          <input
            type="radio"
            :checked="castrated === null"
            @change="() => updateFilter('castrated', null)"
            class="rounded-full h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">Todos</span>
        </label>
      </div>
    </div>

    <!-- Idade -->
    <div class="mb-6">
      <h3 class="font-semibold mb-3 text-gray-700">Idade</h3>
      <div class="space-y-2">
        <label
          v-for="group in ageGroups"
          :key="group.value"
          class="flex items-center gap-3 cursor-pointer"
        >
          <input
            type="checkbox"
             :checked="age.includes(group.value)"
            @change="(e) => handleAgeChange(e, group.value)"
            class="rounded h-4 w-4 text-[#faa72d] focus:ring-[#fcca4f]"
          />
          <span class="text-gray-600">{{ group.label }}</span>
        </label>
      </div>
    </div>

    <button
      @click="handleReset"
      class="w-full py-2 bg-gray-200 hover:bg-gray-300 rounded-lg transition font-medium text-gray-700"
    >
      Limpar Filtros
    </button>
  </div>
</template>

<style scoped>
.sticky {
  position: sticky;
  top: 1rem;
}
</style>
