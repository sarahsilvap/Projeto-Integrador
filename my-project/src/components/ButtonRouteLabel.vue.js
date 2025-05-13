import { useRouter } from 'vue-router';
import { computed } from 'vue';
const router = useRouter();
const buttonRouteLabel = computed(() => {
    return router.currentRoute.value.path === "/" ?
        "Favoritos" : "Lista de Personagens";
});
const changePage = () => {
    if (router.currentRoute.value.path === "/") {
        router.push("/favorites");
    }
    else {
        router.push("/");
    }
};
debugger; /* PartiallyEnd: #3632/scriptSetup.vue */
const __VLS_ctx = {};
let __VLS_components;
let __VLS_directives;
// CSS variable injection 
// CSS variable injection end 
__VLS_asFunctionalElement(__VLS_intrinsicElements.button, __VLS_intrinsicElements.button)({
    ...{ onClick: (__VLS_ctx.changePage) },
    ...{ class: "ml-2 text-purple-600 hover:text-purple-400 cursor-pointer" },
});
(__VLS_ctx.buttonRouteLabel);
/** @type {__VLS_StyleScopedClasses['ml-2']} */ ;
/** @type {__VLS_StyleScopedClasses['text-purple-600']} */ ;
/** @type {__VLS_StyleScopedClasses['hover:text-purple-400']} */ ;
/** @type {__VLS_StyleScopedClasses['cursor-pointer']} */ ;
var __VLS_dollars;
const __VLS_self = (await import('vue')).defineComponent({
    setup() {
        return {
            buttonRouteLabel: buttonRouteLabel,
            changePage: changePage,
        };
    },
});
export default (await import('vue')).defineComponent({
    setup() {
        return {};
    },
});
; /* PartiallyEnd: #4569/main.vue */
