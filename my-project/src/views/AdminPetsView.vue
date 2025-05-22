<template>
  <div class="admin-container p-4">
    <div class="flex items-center justify-between mb-4">
      <h1 class="text-2xl font-bold">Painel de Administração</h1>
      <router-link to="/">
        <img :src="logo2" alt="Logo Adote Petz" class="h-12 mr-4" />
      </router-link>
    </div>

    <div class="flex justify-between items-center mb-5">
      <button
        @click="openAddModal"
        class="bg-green-500 text-white px-4 py-2 rounded"
      >
        Adicionar Novo Pet
      </button>

      <input
        type="text"
        placeholder="Pesquisar Pet"
        class="p-2 w-94 h-1/2 rounded-md border border-gray-300"
        @input="handleSearch"
        :value="query"
      />
    </div>

    <div
      v-if="pets.length"
      class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4"
    >
      <CardPetAdm
        v-for="pet in filteredPets"
        :key="pet._id"
        :pet="pet"
        @edit="openEditModal"
        @delete="deletePet"
      />
    </div>

    <div v-else class="text-gray-500">Nenhum pet cadastrado ainda.</div>

    <!-- Modal para adicionar/editar -->
    <ModalAddEditPet
      v-if="showModal"
      :mode="modalMode"
      :petData="currentPet"
      @close="closeModal"
      @confirm="handleModalConfirm"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import CardPetAdm from "../components/CardPetAdm.vue";
import ModalAddEditPet from "../components/ModalAddEditPet.vue";
import type { Pet } from "../models/pet";
import { computed } from "vue";
import logo2 from "../assets/logo2.png";

const filteredPets = computed(() =>
  pets.value.filter((pet) =>
    pet.name.toLowerCase().includes(query.value.toLowerCase())
  )
);

const pets = ref<Pet[]>([]);
const showModal = ref(false);
const modalMode = ref<"add" | "edit">("add");
const currentPet = ref<Pet | null>(null);

const fetchPets = async () => {
  try {
    const res = await fetch("/api/pets");
    pets.value = await res.json();
  } catch (error) {
    console.error("Erro ao buscar pets:", error);
  }
};

const openAddModal = () => {
  modalMode.value = "add";
  currentPet.value = null;
  showModal.value = true;
};

const openEditModal = (pet: Pet) => {
  modalMode.value = "edit";
  currentPet.value = { ...pet };
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const handleModalConfirm = async (formData: FormData) => {
  try {
    // Verifica se é edição ou adição pela presença do _id no formData
    const petId = formData.get("_id") as string | null;

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
  } catch (error) {
    console.error("Erro ao salvar pet:", error);
  }
};

const deletePet = async (id: string) => {
  try {
    await fetch(`/api/pets/${id}`, { method: "DELETE" });
    fetchPets();
  } catch (error) {
    console.error("Erro ao deletar pet:", error);
  }
};

const query = ref("");

const handleSearch = (event: Event) => {
  const target = event.target as HTMLInputElement;
  query.value = target.value; // Atualiza o estado query com o valor digitado no campo de pesquisa.
};

onMounted(fetchPets);
</script>

<style scoped>
.admin-container {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
