// stores/Filter.ts
import { defineStore } from "pinia";
import { ref } from "vue";

export const useFilterStore = defineStore("filter", () => {
  const type = ref<string[]>([]);
  const size = ref<string[]>([]);
  const castrated = ref<boolean | null>(null);
  const age = ref<string[]>([]);

  // Objeto para facilitar o acesso dinâmico
  const filterState = {
    type,
    size,
    castrated,
    age,
  };

  function updateFilter<T extends keyof typeof filterState>(
    filterType: T,
    value: (typeof filterState)[T]["value"]
  ) {
    filterState[filterType].value = value;
  }

  function resetFilters() {
    type.value = [];
    size.value = [];
    castrated.value = null;
    age.value = [];
  }

  return { type, size, castrated, age, updateFilter, resetFilters };
});
