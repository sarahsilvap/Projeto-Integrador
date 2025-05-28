// stores/Filter.ts
import { defineStore } from "pinia";
import { ref } from "vue";
export const useFilterStore = defineStore("filter", () => {
    // Estado dos filtros
    const type = ref([]);
    const size = ref([]);
    const castrated = ref(null);
    const age = ref([]);
    function updateFilter(filterType, value) {
        switch (filterType) {
            case "type":
                type.value = Array.isArray(value)
                    ? value.map((v) => v.toLowerCase())
                    : [];
                break;
            case "size":
                size.value = Array.isArray(value)
                    ? value.map((v) => v
                        .normalize("NFD")
                        .replace(/[\u0300-\u036f]/g, "")
                        .toLowerCase())
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
