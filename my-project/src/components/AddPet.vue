<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "AddPetPage",
  setup() {
    const router = useRouter();
    const fileInput = ref(null);
    const previewImage = ref(null);
    const isSubmitting = ref(false);
    const errorMessage = ref("");
    const successMessage = ref("");

    const pet = ref({
      name: "",
      type: "",
      size: "",
      age: "",
      castrated: "",
      description: "",
      available: "",
      image: null,
    });

    const handleImageUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        // Verifica se o arquivo é uma imagem
        if (!file.type.match("image.*")) {
          errorMessage.value =
            "Por favor, selecione um arquivo de imagem válido";
          return;
        }

        // Limita o tamanho do arquivo (ex: 2MB)
        if (file.size > 2 * 1024 * 1024) {
          errorMessage.value = "A imagem deve ter menos de 2MB";
          return;
        }

        pet.value.image = file;

        // Cria preview da imagem
        const reader = new FileReader();
        reader.onload = (e) => {
          previewImage.value = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    };

    const handleSubmit = async () => {
      errorMessage.value = "";
      successMessage.value = "";
      isSubmitting.value = true;

      try {
        // Validação básica
        if (!pet.value.image) {
          throw new Error("Por favor, adicione uma imagem do pet");
        }

        // FormData para enviar arquivos
        const formData = new FormData();
        formData.append("image", pet.value.image);
        formData.append("name", pet.value.name);
        formData.append("type", pet.value.type);
        formData.append("size", pet.value.size);
        formData.append("age", pet.value.age);
        formData.append("castrated", pet.value.castrated);
        formData.append("description", pet.value.description);
        formData.append("available", pet.value.available);

        // Adicione logs para debug
        console.log("Enviando dados:", {
          name: pet.value.name,
          type: pet.value.type,
          size: pet.value.size,
          age: pet.value.age,
          castrated: pet.value.castrated,
          description: pet.value.description,
          available: pet.value.available,
        });

        const response = await fetch("http://localhost:3000/api/pets", {
          method: "POST",
          body: formData,
        });

        const responseText = await response.text();
        console.log("Resposta completa:", responseText);

        if (!response.ok) {
          let errorData;
          try {
            errorData = JSON.parse(responseText);
          } catch {
            throw new Error(errorData.error || "Erro ao cadastrar pet");
          }
          throw new Error(responseText || "Erro no servidor");
        }

        const responseData = JSON.parse(responseText);
        successMessage.value = "Pet cadastrado com sucesso!";

        // Limpa o formulário após 2 segundos
        setTimeout(() => {
          resetForm();
          router.push("/admin/pets"); // Redireciona para lista de pets
        }, 2000);
      } catch (error) {
        console.error("Erro ao cadastrar pet:", error);
        errorMessage.value =
          error.message || "Ocorreu um erro ao cadastrar o pet";

        // Se for erro de sintaxe JSON, mostre mensagem mais clara
        if (error instanceof SyntaxError) {
          errorMessage.value =
            "O servidor retornou uma resposta inválida. Verifique o console para detalhes.";
        }
      } finally {
        isSubmitting.value = false;
      }
    };

    const resetForm = () => {
      pet.value = {
        name: "",
        type: "",
        size: "",
        age: "",
        castrated: "",
        description: "",
        available: "",
        image: null,
      };
      previewImage.value = null;
      if (fileInput.value) {
        fileInput.value.value = "";
      }
    };

    return {
      pet,
      previewImage,
      fileInput,
      isSubmitting,
      errorMessage,
      successMessage,
      handleImageUpload,
      handleSubmit,
    };
  },
};
</script>

<template>
  <div class="admin-container">
    <h1>Adicionar Novo Pet</h1>

    <form @submit.prevent="handleSubmit" class="pet-form">
      <!-- Upload de Imagem -->
      <div class="form-group image-upload">
        <label>Foto do Pet</label>
        <div class="image-preview" v-if="previewImage">
          <img :src="previewImage" alt="Preview da imagem do pet" />
        </div>
        <input
          type="file"
          accept="image/*"
          @change="handleImageUpload"
          ref="fileInput"
          required
        />
      </div>

      <!-- Campos do Formulário -->
      <div class="form-group">
        <label for="name">Nome do Pet</label>
        <input v-model="pet.name" id="name" required />
      </div>

      <div class="form-group">
        <label for="type">Tipo</label>
        <select v-model="pet.type" id="type" required>
          <option value="">Selecione</option>
          <option value="dog">Cachorro</option>
          <option value="cat">Gato</option>
        </select>
      </div>

      <div class="form-group">
        <label for="size">Porte</label>
        <select v-model="pet.size" id="size" required>
          <option value="">Selecione</option>
          <option value="small">Pequeno</option>
          <option value="medium">Médio</option>
          <option value="large">Grande</option>
        </select>
      </div>

      <div class="form-group">
        <label for="age">Idade (anos)</label>
        <input v-model="pet.age" type="number" id="age" min="0" required />
      </div>

      <div class="form-group">
        <label for="castrated">Castrado</label>
        <select v-model="pet.castrated" id="castrated" required>
          <option value="">Selecione</option>
          <option value="true">Sim</option>
          <option value="false">Não</option>
        </select>
      </div>

      <div class="form-group">
        <label for="available">Disponível para adoção</label>
        <select v-model="pet.available" id="available" required>
          <option value="">Selecione</option>
          <option value="true">Sim</option>
          <option value="false">Não</option>
        </select>
      </div>

      <div class="form-group">
        <label for="description">Descrição do Pet:</label>
        <textarea
          id="description"
          v-model="pet.description"
          rows="3"
          placeholder="Descreva características, comportamento, história..."
          class="w-full p-2 border rounded"
        ></textarea>
      </div>

      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? "Salvando..." : "Adicionar Pet" }}
      </button>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
    </form>
  </div>
</template>

<style scoped>
/* Estilos mantidos iguais ao exemplo anterior */
</style>
