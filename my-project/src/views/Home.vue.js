import axios from "axios";
import { ref, onMounted } from "vue";
import { useFavoriteStore } from "../stores/FavoritesStore";
import Menu from "../components/Menu.vue";
import Cards from "../components/Cards.vue";
onMounted(async () => {
    try {
        const response = await axios.get("http://localhost:3000/api/pets");
        pets.value = response.data;
    }
    catch (error) {
        console.error("Erro ao buscar dados:", error);
    }
});
const pets = ref([]);
const favoritesStore = useFavoriteStore();
const toggleFavorite = async (pet) => {
    if (favoritesStore.isFavorite(pet.name)) {
        favoritesStore.removeFavorite(pet.name);
    }
};
const isPetFavorite = (name) => {
    return favoritesStore.isFavorite(name);
};
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
    ...{ class: "w-full min-h-screen bg-[#fb7991] text-primary grid grid-cols-4 p-10" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "col-span-4 text-primary text-5xl text-center flex flex-col items-center justify-center" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.h1, __VLS_intrinsicElements.h1)({});
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "col-span-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-10" },
});
for (const [pet] of __VLS_getVForSourceType((__VLS_ctx.pets))) {
    /** @type {[typeof Cards, ]} */ ;
    // @ts-ignore
    const __VLS_3 = __VLS_asFunctionalComponent(Cards, new Cards({
        key: (pet._id),
        pet: (pet),
    }));
    const __VLS_4 = __VLS_3({
        key: (pet._id),
        pet: (pet),
    }, ...__VLS_functionalComponentArgsRest(__VLS_3));
}
/** @type {__VLS_StyleScopedClasses['w-full']} */ ;
/** @type {__VLS_StyleScopedClasses['min-h-screen']} */ ;
/** @type {__VLS_StyleScopedClasses['bg-[#fb7991]']} */ ;
/** @type {__VLS_StyleScopedClasses['text-primary']} */ ;
/** @type {__VLS_StyleScopedClasses['grid']} */ ;
/** @type {__VLS_StyleScopedClasses['grid-cols-4']} */ ;
/** @type {__VLS_StyleScopedClasses['p-10']} */ ;
/** @type {__VLS_StyleScopedClasses['col-span-4']} */ ;
/** @type {__VLS_StyleScopedClasses['text-primary']} */ ;
/** @type {__VLS_StyleScopedClasses['text-5xl']} */ ;
/** @type {__VLS_StyleScopedClasses['text-center']} */ ;
/** @type {__VLS_StyleScopedClasses['flex']} */ ;
/** @type {__VLS_StyleScopedClasses['flex-col']} */ ;
/** @type {__VLS_StyleScopedClasses['items-center']} */ ;
/** @type {__VLS_StyleScopedClasses['justify-center']} */ ;
/** @type {__VLS_StyleScopedClasses['col-span-4']} */ ;
/** @type {__VLS_StyleScopedClasses['grid']} */ ;
/** @type {__VLS_StyleScopedClasses['grid-cols-1']} */ ;
/** @type {__VLS_StyleScopedClasses['sm:grid-cols-2']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:grid-cols-3']} */ ;
/** @type {__VLS_StyleScopedClasses['gap-8']} */ ;
/** @type {__VLS_StyleScopedClasses['mt-10']} */ ;
var __VLS_dollars;
const __VLS_self = (await import('vue')).defineComponent({
    setup() {
        return {
            Menu: Menu,
            Cards: Cards,
            pets: pets,
        };
    },
});
export default (await import('vue')).defineComponent({
    setup() {
        return {};
    },
});
; /* PartiallyEnd: #4569/main.vue */
