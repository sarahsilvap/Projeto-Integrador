import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { storeToRefs } from 'pinia';
import { useFilterStore } from "../stores/Filter";
import Menu from "../components/Menu.vue";
import PetCard from "../components/PetCard.vue";
import SideBar from "../components/SideBar.vue";
// Stores
const filtersStore = useFilterStore();
const { type, size, castrated, age } = storeToRefs(filtersStore);
const { resetFilters } = filtersStore;
const pets = ref([]);
const loading = ref(false);
// Função auxiliar para grupo etário
function getAgeGroup(age) {
    if (age < 2)
        return 'filhote';
    if (age < 5)
        return 'jovem';
    if (age < 10)
        return 'adulto';
    return 'senior';
}
// Computed para pets filtrados
const filteredPets = computed(() => {
    return pets.value.filter(pet => {
        const normalizedPetType = pet.type.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
        const normalizedPetSize = pet.size.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
        // Filtro por tipo
        if (type.value.length > 0) {
            const shouldInclude = type.value.some(filterType => filterType === normalizedPetType);
            if (!shouldInclude)
                return false;
        }
        // Filtro por tamanho
        if (size.value.length > 0) {
            const shouldInclude = size.value.some(filterSize => filterSize === normalizedPetSize);
            if (!shouldInclude)
                return false;
        }
        // Filtro por castração
        if (castrated.value !== null && pet.castrated !== castrated.value) {
            return false;
        }
        // Filtro por idade
        if (age.value.length > 0) {
            const petAgeGroup = getAgeGroup(pet.age);
            if (!age.value.includes(petAgeGroup)) {
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
    }
    catch (error) {
        console.error("Erro ao buscar dados:", error);
    }
    finally {
        loading.value = false;
    }
});
debugger; /* PartiallyEnd: #3632/scriptSetup.vue */
const __VLS_ctx = {};
let __VLS_components;
let __VLS_directives;
// CSS variable injection 
// CSS variable injection end 
/** @type {[typeof Menu, ]} */ ;
// @ts-ignore
const __VLS_0 = __VLS_asFunctionalComponent(Menu, new Menu({}));
const __VLS_1 = __VLS_0({}, ...__VLS_functionalComponentArgsRest(__VLS_0));
__VLS_asFunctionalElement(__VLS_intrinsicElements.main, __VLS_intrinsicElements.main)({
    ...{ class: "w-full min-h-screen bg-[#efefef] grid grid-cols-1 lg:grid-cols-5 gap-6 p-5" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "lg:col-span-1" },
});
/** @type {[typeof SideBar, ]} */ ;
// @ts-ignore
const __VLS_3 = __VLS_asFunctionalComponent(SideBar, new SideBar({}));
const __VLS_4 = __VLS_3({}, ...__VLS_functionalComponentArgsRest(__VLS_3));
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "lg:col-span-4" },
});
if (__VLS_ctx.loading) {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
        ...{ class: "text-center py-12" },
    });
    __VLS_asFunctionalElement(__VLS_intrinsicElements.span, __VLS_intrinsicElements.span)({
        ...{ class: "animate-pulse text-lg" },
    });
}
else {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
    if (__VLS_ctx.filteredPets.length === 0) {
        __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
            ...{ class: "text-center py-12" },
        });
        __VLS_asFunctionalElement(__VLS_intrinsicElements.p, __VLS_intrinsicElements.p)({
            ...{ class: "text-xl mb-4" },
        });
        __VLS_asFunctionalElement(__VLS_intrinsicElements.button, __VLS_intrinsicElements.button)({
            ...{ onClick: (__VLS_ctx.resetFilters) },
            ...{ class: "px-4 py-2 bg-[#fd6b67] hover:bg-[#fe827e] text-white rounded-lg hover:bg-[#fcca4f] transition" },
        });
    }
    else {
        __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
            ...{ class: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6" },
        });
        for (const [pet] of __VLS_getVForSourceType((__VLS_ctx.filteredPets))) {
            /** @type {[typeof PetCard, ]} */ ;
            // @ts-ignore
            const __VLS_6 = __VLS_asFunctionalComponent(PetCard, new PetCard({
                key: (pet._id),
                pet: (pet),
            }));
            const __VLS_7 = __VLS_6({
                key: (pet._id),
                pet: (pet),
            }, ...__VLS_functionalComponentArgsRest(__VLS_6));
        }
    }
}
/** @type {__VLS_StyleScopedClasses['w-full']} */ ;
/** @type {__VLS_StyleScopedClasses['min-h-screen']} */ ;
/** @type {__VLS_StyleScopedClasses['bg-[#efefef]']} */ ;
/** @type {__VLS_StyleScopedClasses['grid']} */ ;
/** @type {__VLS_StyleScopedClasses['grid-cols-1']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:grid-cols-5']} */ ;
/** @type {__VLS_StyleScopedClasses['gap-6']} */ ;
/** @type {__VLS_StyleScopedClasses['p-5']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:col-span-1']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:col-span-4']} */ ;
/** @type {__VLS_StyleScopedClasses['text-center']} */ ;
/** @type {__VLS_StyleScopedClasses['py-12']} */ ;
/** @type {__VLS_StyleScopedClasses['animate-pulse']} */ ;
/** @type {__VLS_StyleScopedClasses['text-lg']} */ ;
/** @type {__VLS_StyleScopedClasses['text-center']} */ ;
/** @type {__VLS_StyleScopedClasses['py-12']} */ ;
/** @type {__VLS_StyleScopedClasses['text-xl']} */ ;
/** @type {__VLS_StyleScopedClasses['mb-4']} */ ;
/** @type {__VLS_StyleScopedClasses['px-4']} */ ;
/** @type {__VLS_StyleScopedClasses['py-2']} */ ;
/** @type {__VLS_StyleScopedClasses['bg-[#fd6b67]']} */ ;
/** @type {__VLS_StyleScopedClasses['hover:bg-[#fe827e]']} */ ;
/** @type {__VLS_StyleScopedClasses['text-white']} */ ;
/** @type {__VLS_StyleScopedClasses['rounded-lg']} */ ;
/** @type {__VLS_StyleScopedClasses['hover:bg-[#fcca4f]']} */ ;
/** @type {__VLS_StyleScopedClasses['transition']} */ ;
/** @type {__VLS_StyleScopedClasses['grid']} */ ;
/** @type {__VLS_StyleScopedClasses['grid-cols-1']} */ ;
/** @type {__VLS_StyleScopedClasses['sm:grid-cols-2']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:grid-cols-3']} */ ;
/** @type {__VLS_StyleScopedClasses['xl:grid-cols-4']} */ ;
/** @type {__VLS_StyleScopedClasses['gap-6']} */ ;
var __VLS_dollars;
const __VLS_self = (await import('vue')).defineComponent({
    setup() {
        return {
            Menu: Menu,
            PetCard: PetCard,
            SideBar: SideBar,
            resetFilters: resetFilters,
            loading: loading,
            filteredPets: filteredPets,
        };
    },
});
export default (await import('vue')).defineComponent({
    setup() {
        return {};
    },
});
; /* PartiallyEnd: #4569/main.vue */
