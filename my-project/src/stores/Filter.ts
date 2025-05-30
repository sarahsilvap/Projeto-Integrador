// stores/Filter.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { PetType, PetSize, AgeGroup } from '../models/pet';

export const useFilterStore = defineStore("filter", () => {
  // Estado dos filtros
  const type = ref<PetType[]>([]);
  const size = ref<PetSize[]>([]);
  const castrated = ref<boolean | null>(null);
  const age = ref<AgeGroup[]>([]);

  function updateFilter(filterType: string, value: any) {
    switch (filterType) {
      case "type":
        type.value = Array.isArray(value)
          ? value.map((v) => v.toLowerCase())
          : [];
        break;
      case "size":
        size.value = Array.isArray(value)
          ? value.map((v) =>
              v
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "")
                .toLowerCase()
            )
          : [];
        break;
      case "castrated":
        castrated.value = value;
        break;
      case "age":
        age.value = Array.isArray(value) ? value : [];
        break;
    }
  }

  function resetFilters() {
    type.value = [];
    size.value = [];
    castrated.value = null;
    age.value = [];
  }

  return {
    type,
    size,
    castrated,
    age,
    updateFilter,
    resetFilters,
  };
});
