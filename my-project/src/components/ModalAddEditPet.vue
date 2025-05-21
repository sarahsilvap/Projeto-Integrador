<script setup lang="ts">
import { ref, watch } from "vue";
import type { Pet } from "../models/pet.js";

interface Props {
  mode: "add" | "edit";
  petData?: Pet | null;
}

const props = defineProps<Props>();
const fileInput = ref<HTMLInputElement | null>(null);

const emit = defineEmits<{
  (e: "close"): void;
  (e: "confirm", formData: FormData): void;
}>();

// Form state
const form = ref<Partial<Pet>>({
  name: "",
  type: undefined,
  size: undefined,
  age: 1,
  castrated: false,
  available: true,
  description: "",
  coverImage: "",
});

// UI state
const errorMessage = ref<string>("");
const fileInputRef = ref<HTMLInputElement | null>(null);
const fileInputKey = ref(0)
const imageFile = ref<File | null>(null);
const isLoadingImage = ref<boolean>(false);

// Convert image URL to Base64 for preview
const convertImageUrlToBase64 = async (url: string): Promise<string> => {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to fetch image");
    const blob = await response.blob();
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result as string);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
  } catch (error) {
    console.error("Error converting image:", error);
    return "";
  }
};

// Watch for petData changes (when editing)
watch(
  () => props.petData,
  async (newPet) => {
    if (props.mode === "edit" && newPet) {
      form.value = {
        ...newPet,
        name: newPet.name || "",
        description: newPet.description || "",
      };

      // Handle existing image preview
      if (newPet.coverImage) {
        isLoadingImage.value = true;
        try {
          if (newPet.coverImage.startsWith("http")) {
            form.value.coverImage = await convertImageUrlToBase64(
              newPet.coverImage
            );
          } else if (newPet.coverImage.startsWith("data:image")) {
            form.value.coverImage = newPet.coverImage;
          } else {
            form.value.coverImage = `http://localhost:3000${newPet.coverImage}`;
          }
        } catch (error) {
          console.error("Error loading image:", error);
          form.value.coverImage = "";
        } finally {
          isLoadingImage.value = false;
        }
      } else {
        form.value.coverImage = "";
      }

      imageFile.value = null;
    } else if (props.mode === "add") {
      resetForm();
    }
  },
  { immediate: true }
);

// Reset form to initial state
const resetForm = () => {
  form.value = {
    name: "",
    type: undefined,
    size: undefined,
    age: 1,
    castrated: false,
    available: true,
    description: "",
    coverImage: "",
  };
  imageFile.value = null;
  fileInputKey.value++;
  errorMessage.value = "";
};

// Handle form submission
const handleSubmit = async () => {
  errorMessage.value = "";

  // Validation
  if (!form.value.name?.trim()) {
    errorMessage.value = "O nome do pet é obrigatório.";
    return;
  }
  if (!form.value.type) {
    errorMessage.value = "O tipo do pet é obrigatório.";
    return;
  }
  if (!form.value.size) {
    errorMessage.value = "O tamanho do pet é obrigatório.";
    return;
  }
  if (props.mode === "add" && !imageFile.value) {
    errorMessage.value = "Por favor, selecione uma imagem para o pet.";
    return;
  }

  try {
    const formData = new FormData();

    // Add ID if editing
    if (props.mode === "edit" && props.petData?._id) {
      formData.append("_id", props.petData._id);
    }

    // Add image file if exists
    if (imageFile.value) {
      formData.append("coverImage", imageFile.value);
    }

    // Add other fields
    formData.append("name", form.value.name ?? "");
    formData.append("type", form.value.type ?? "");
    formData.append("size", form.value.size ?? "");
    formData.append("age", String(form.value.age ?? 1));
    formData.append("castrated", String(form.value.castrated ?? false));
    formData.append("available", String(form.value.available ?? true));
    formData.append("description", form.value.description ?? "");

    emit("confirm", formData);
  } catch (error) {
    errorMessage.value = "Erro ao preparar dados para envio.";
    console.error(error);
  }
};

// Handle file upload
const handleFileChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  const file = input.files?.[0];
  errorMessage.value = "";

  if (!file) return;

  // Validate file
  if (file.size > 5 * 1024 * 1024) {
    errorMessage.value = "A imagem é muito grande (máximo 5MB)";
    return;
  }

  if (!["image/jpeg", "image/png"].includes(file.type)) {
    errorMessage.value = "Formato inválido (use JPEG ou PNG)";
    return;
  }

  // Set file and create preview
  imageFile.value = file;
  form.value.coverImage = URL.createObjectURL(file);
};

// Reset file input
const resetFileInput = () => {
  form.value.coverImage = "";
  imageFile.value = null;
  fileInputKey.value++;
};
</script>

<template>
  <div
    class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50 p-4"
  >
    <div
      class="bg-white rounded-xl w-full max-w-md max-h-[90vh] overflow-y-auto shadow-xl"
    >
      <div class="p-6">
        <!-- Header -->
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-800">
            {{ mode === "add" ? "Adicionar Novo Pet" : "Editar Pet" }}
          </h2>
          <button
            @click="
              $emit('close');
              resetForm();
            "
            class="text-gray-500 hover:text-gray-700 transition-colors"
            aria-label="Fechar modal"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <!-- Error message -->
        <div
          v-if="errorMessage"
          class="mb-4 p-3 bg-red-50 text-red-600 rounded-lg text-sm flex items-start"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 mr-2 mt-0.5 flex-shrink-0"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
              clip-rule="evenodd"
            />
          </svg>
          <span>{{ errorMessage }}</span>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-5">
          <!-- Name -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5"
              >Nome *</label
            >
            <input
              v-model.trim="form.name"
              required
              placeholder="Digite o nome do pet"
              class="w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-blue-200 focus:border-blue-500 transition-all"
            />
          </div>

          <!-- Type and Size -->
          <div class="grid grid-cols-2 gap-4">
            <!-- Type -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1.5"
                >Tipo *</label
              >
              <select
                v-model="form.type"
                required
                class="w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-blue-200 focus:border-blue-500 transition-all appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9Ii82Yjc1OGQyIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBvbHlsaW5lIHBvaW50cz0iNiA5IDEyIDE1IDE4IDkiPjwvcG9seWxpbmU+PC9zdmc+')] bg-no-repeat bg-[center_right_1rem]"
              >
                <option :value="undefined" disabled selected>
                  Selecione...
                </option>
                <option value="dog">Cachorro</option>
                <option value="cat">Gato</option>
              </select>
            </div>

            <!-- Size -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1.5"
                >Tamanho *</label
              >
              <select
                v-model="form.size"
                required
                class="w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-blue-200 focus:border-blue-500 transition-all appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9Ii82Yjc1OGQyIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBvbHlsaW5lIHBvaW50cz0iNiA5IDEyIDE1IDE4IDkiPjwvcG9seWxpbmU+PC9zdmc+')] bg-no-repeat bg-[center_right_1rem]"
              >
                <option :value="undefined" disabled selected>
                  Selecione...
                </option>
                <option value="small">Pequeno</option>
                <option value="medium">Médio</option>
                <option value="large">Grande</option>
              </select>
            </div>
          </div>

          <!-- Age -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5"
              >Idade *</label
            >
            <input
              v-model.number="form.age"
              type="number"
              min="0"
              max="30"
              required
              placeholder="Idade em anos"
              class="w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-blue-200 focus:border-blue-500 transition-all"
            />
          </div>

          <!-- Checkboxes -->
          <div class="grid grid-cols-2 gap-4">
            <!-- Castrated -->
            <div class="flex items-center">
              <input
                v-model="form.castrated"
                type="checkbox"
                id="castrated"
                class="h-4 w-4 text-blue-500 border-gray-300 rounded focus:ring-blue-200"
              />
              <label for="castrated" class="ml-2 block text-sm text-gray-700"
                >Castrado</label
              >
            </div>

            <!-- Available -->
            <div class="flex items-center">
              <input
                v-model="form.available"
                type="checkbox"
                id="available"
                class="h-4 w-4 text-blue-500 border-gray-300 rounded focus:ring-blue-200"
              />
              <label for="available" class="ml-2 block text-sm text-gray-700"
                >Disponível</label
              >
            </div>
          </div>

          <!-- Description -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5"
              >Descrição</label
            >
            <textarea
              v-model="form.description"
              rows="3"
              placeholder="Descreva o pet (personalidade, hábitos, etc)"
              class="w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-blue-200 focus:border-blue-500 transition-all"
            ></textarea>
          </div>

          <!-- Photo Upload -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">
              Foto {{ mode === "add" ? "*" : "" }}
              <span class="text-xs text-gray-500 ml-1"
                >(JPEG/PNG, máximo 5MB)</span
              >
            </label>

            <div
              @click="fileInputRef!.click()"
              class="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center cursor-pointer hover:border-blue-300 transition-colors"
              :class="{ 'border-blue-400': form.coverImage }"
            >
              <input
                :key="fileInputKey"
                ref="fileInputRef"
                type="file"
                @change="handleFileChange"
                accept="image/jpeg, image/png"
                class="hidden"
              />

              <template v-if="isLoadingImage">
                <div class="py-8 flex flex-col items-center justify-center">
                  <svg
                    class="animate-spin h-8 w-8 text-blue-500"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    ></circle>
                    <path
                      class="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                  <p class="mt-2 text-sm text-gray-500">Carregando imagem...</p>
                </div>
              </template>

              <template v-else>
                <div v-if="!form.coverImage" class="py-8">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-10 w-10 mx-auto text-gray-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="1.5"
                      d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  <p class="mt-1 text-sm text-gray-600">
                    Clique para adicionar uma foto
                  </p>
                </div>

                <div v-else class="relative">
                  <img
                    :src="form.coverImage"
                    class="h-40 w-full object-contain rounded-lg mx-auto border"
                    alt="Pré-visualização da foto"
                    @error="form.coverImage = ''"
                  />
                  <button
                    type="button"
                    @click.stop="resetFileInput"
                    class="absolute top-0 right-0 -mt-2 -mr-2 bg-red-500 text-white rounded-full p-1 hover:bg-red-600 transition-colors"
                    aria-label="Remover foto"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M6 18L18 6M6 6l12 12"
                      />
                    </svg>
                  </button>
                </div>
              </template>
            </div>
          </div>

          <!-- Form Footer -->
          <div class="flex justify-end space-x-3 pt-2">
            <button
              type="button"
              @click="
                $emit('close');
                resetForm();
              "
              class="px-5 py-2.5 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="px-5 py-2.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors focus:ring-2 focus:ring-blue-200 focus:outline-none"
            >
              {{ mode === "add" ? "Adicionar Pet" : "Salvar Alterações" }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
