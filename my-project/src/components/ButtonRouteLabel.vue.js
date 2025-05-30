import { useRouter } from 'vue-router';
import { computed } from 'vue';
const router = useRouter();
const buttonRouteLabel = computed(() => {
    return router.currentRoute.value.path === "/" ?
        "Doações" : "Home";
});
const changePage = () => {
    if (router.currentRoute.value.path === "/") {
        router.push("/donation");
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
    ...{ class: "text-gray-800 font-medium hover:text-[#fb6d67] hover:cursor-pointer" },
});
(__VLS_ctx.buttonRouteLabel);
/** @type {__VLS_StyleScopedClasses['text-gray-800']} */ ;
/** @type {__VLS_StyleScopedClasses['font-medium']} */ ;
/** @type {__VLS_StyleScopedClasses['hover:text-[#fb6d67]']} */ ;
/** @type {__VLS_StyleScopedClasses['hover:cursor-pointer']} */ ;
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
