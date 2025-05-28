import { ref, onMounted } from "vue";
import CardPetAdm from "../components/CardPetAdm.vue";
import ModalAddEditPet from "../components/ModalAddEditPet.vue";
import { computed } from "vue";
import logo2 from "../assets/logo2.png";
const filteredPets = computed(() => pets.value.filter((pet) => pet.name.toLowerCase().includes(query.value.toLowerCase())));
const pets = ref([]);
const showModal = ref(false);
const modalMode = ref("add");
const currentPet = ref(null);
const fetchPets = async () => {
    try {
        const res = await fetch("/api/pets");
        pets.value = await res.json();
    }
    catch (error) {
        console.error("Erro ao buscar pets:", error);
    }
};
const openAddModal = () => {
    modalMode.value = "add";
    currentPet.value = null;
    showModal.value = true;
};
const openEditModal = (pet) => {
    modalMode.value = "edit";
    currentPet.value = { ...pet };
    showModal.value = true;
};
const closeModal = () => {
    showModal.value = false;
};
const handleModalConfirm = async (formData) => {
    try {
        // Verifica se é edição ou adição pela presença do _id no formData
        const petId = formData.get("_id");
        const url = petId ? `/api/pets/${petId}` : "/api/pets";
        const method = petId ? "PUT" : "POST";
        const res = await fetch(url, {
            method,
            body: formData, // Aqui passa o FormData diretamente, sem definir headers
        });
        if (!res.ok) {
            throw new Error("Erro ao salvar pet");
        }
        closeModal();
        fetchPets();
    }
    catch (error) {
        console.error("Erro ao salvar pet:", error);
    }
};
const deletePet = async (id) => {
    try {
        await fetch(`/api/pets/${id}`, { method: "DELETE" });
        fetchPets();
    }
    catch (error) {
        console.error("Erro ao deletar pet:", error);
    }
};
const query = ref("");
const handleSearch = (event) => {
    const target = event.target;
    query.value = target.value; // Atualiza o estado query com o valor digitado no campo de pesquisa.
};
onMounted(fetchPets);
debugger; /* PartiallyEnd: #3632/scriptSetup.vue */
const __VLS_ctx = {};
let __VLS_components;
let __VLS_directives;
// CSS variable injection 
// CSS variable injection end 
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "admin-container p-4" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "flex items-center justify-between mb-4" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.h1, __VLS_intrinsicElements.h1)({
    ...{ class: "text-2xl font-bold" },
});
const __VLS_0 = {}.RouterLink;
/** @type {[typeof __VLS_components.RouterLink, typeof __VLS_components.routerLink, typeof __VLS_components.RouterLink, typeof __VLS_components.routerLink, ]} */ ;
// @ts-ignore
const __VLS_1 = __VLS_asFunctionalComponent(__VLS_0, new __VLS_0({
    to: "/",
}));
const __VLS_2 = __VLS_1({
    to: "/",
}, ...__VLS_functionalComponentArgsRest(__VLS_1));
__VLS_3.slots.default;
__VLS_asFunctionalElement(__VLS_intrinsicElements.img)({
    src: (__VLS_ctx.logo2),
    alt: "Logo Adote Petz",
    ...{ class: "h-12 mr-4" },
});
var __VLS_3;
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
    ...{ class: "flex justify-between items-center mb-5" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.button, __VLS_intrinsicElements.button)({
    ...{ onClick: (__VLS_ctx.openAddModal) },
    ...{ class: "bg-green-500 text-white px-4 py-2 rounded" },
});
__VLS_asFunctionalElement(__VLS_intrinsicElements.input)({
    ...{ onInput: (__VLS_ctx.handleSearch) },
    type: "text",
    placeholder: "Pesquisar Pet",
    ...{ class: "p-2 w-94 h-1/2 rounded-md border border-gray-300" },
    value: (__VLS_ctx.query),
});
if (__VLS_ctx.pets.length) {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
        ...{ class: "grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4" },
    });
    for (const [pet] of __VLS_getVForSourceType((__VLS_ctx.filteredPets))) {
        /** @type {[typeof CardPetAdm, ]} */ ;
        // @ts-ignore
        const __VLS_4 = __VLS_asFunctionalComponent(CardPetAdm, new CardPetAdm({
            ...{ 'onEdit': {} },
            ...{ 'onDelete': {} },
            key: (pet._id),
            pet: (pet),
        }));
        const __VLS_5 = __VLS_4({
            ...{ 'onEdit': {} },
            ...{ 'onDelete': {} },
            key: (pet._id),
            pet: (pet),
        }, ...__VLS_functionalComponentArgsRest(__VLS_4));
        let __VLS_7;
        let __VLS_8;
        let __VLS_9;
        const __VLS_10 = {
            onEdit: (__VLS_ctx.openEditModal)
        };
        const __VLS_11 = {
            onDelete: (__VLS_ctx.deletePet)
        };
        var __VLS_6;
    }
}
else {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
        ...{ class: "text-gray-500" },
    });
}
if (__VLS_ctx.showModal) {
    /** @type {[typeof ModalAddEditPet, ]} */ ;
    // @ts-ignore
    const __VLS_12 = __VLS_asFunctionalComponent(ModalAddEditPet, new ModalAddEditPet({
        ...{ 'onClose': {} },
        ...{ 'onConfirm': {} },
        mode: (__VLS_ctx.modalMode),
        petData: (__VLS_ctx.currentPet),
    }));
    const __VLS_13 = __VLS_12({
        ...{ 'onClose': {} },
        ...{ 'onConfirm': {} },
        mode: (__VLS_ctx.modalMode),
        petData: (__VLS_ctx.currentPet),
    }, ...__VLS_functionalComponentArgsRest(__VLS_12));
    let __VLS_15;
    let __VLS_16;
    let __VLS_17;
    const __VLS_18 = {
        onClose: (__VLS_ctx.closeModal)
    };
    const __VLS_19 = {
        onConfirm: (__VLS_ctx.handleModalConfirm)
    };
    var __VLS_14;
}
/** @type {__VLS_StyleScopedClasses['admin-container']} */ ;
/** @type {__VLS_StyleScopedClasses['p-4']} */ ;
/** @type {__VLS_StyleScopedClasses['flex']} */ ;
/** @type {__VLS_StyleScopedClasses['items-center']} */ ;
/** @type {__VLS_StyleScopedClasses['justify-between']} */ ;
/** @type {__VLS_StyleScopedClasses['mb-4']} */ ;
/** @type {__VLS_StyleScopedClasses['text-2xl']} */ ;
/** @type {__VLS_StyleScopedClasses['font-bold']} */ ;
/** @type {__VLS_StyleScopedClasses['h-12']} */ ;
/** @type {__VLS_StyleScopedClasses['mr-4']} */ ;
/** @type {__VLS_StyleScopedClasses['flex']} */ ;
/** @type {__VLS_StyleScopedClasses['justify-between']} */ ;
/** @type {__VLS_StyleScopedClasses['items-center']} */ ;
/** @type {__VLS_StyleScopedClasses['mb-5']} */ ;
/** @type {__VLS_StyleScopedClasses['bg-green-500']} */ ;
/** @type {__VLS_StyleScopedClasses['text-white']} */ ;
/** @type {__VLS_StyleScopedClasses['px-4']} */ ;
/** @type {__VLS_StyleScopedClasses['py-2']} */ ;
/** @type {__VLS_StyleScopedClasses['rounded']} */ ;
/** @type {__VLS_StyleScopedClasses['p-2']} */ ;
/** @type {__VLS_StyleScopedClasses['w-94']} */ ;
/** @type {__VLS_StyleScopedClasses['h-1/2']} */ ;
/** @type {__VLS_StyleScopedClasses['rounded-md']} */ ;
/** @type {__VLS_StyleScopedClasses['border']} */ ;
/** @type {__VLS_StyleScopedClasses['border-gray-300']} */ ;
/** @type {__VLS_StyleScopedClasses['grid']} */ ;
/** @type {__VLS_StyleScopedClasses['grid-cols-1']} */ ;
/** @type {__VLS_StyleScopedClasses['md:grid-cols-3']} */ ;
/** @type {__VLS_StyleScopedClasses['lg:grid-cols-4']} */ ;
/** @type {__VLS_StyleScopedClasses['gap-4']} */ ;
/** @type {__VLS_StyleScopedClasses['text-gray-500']} */ ;
var __VLS_dollars;
const __VLS_self = (await import('vue')).defineComponent({
    setup() {
        return {
            CardPetAdm: CardPetAdm,
            ModalAddEditPet: ModalAddEditPet,
            logo2: logo2,
            filteredPets: filteredPets,
            pets: pets,
            showModal: showModal,
            modalMode: modalMode,
            currentPet: currentPet,
            openAddModal: openAddModal,
            openEditModal: openEditModal,
            closeModal: closeModal,
            handleModalConfirm: handleModalConfirm,
            deletePet: deletePet,
            query: query,
            handleSearch: handleSearch,
        };
    },
});
export default (await import('vue')).defineComponent({
    setup() {
        return {};
    },
});
; /* PartiallyEnd: #4569/main.vue */
