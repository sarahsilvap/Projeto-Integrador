const axios = require("axios");

//Cria instância di Axios com URL base da API
const apiClient = axios.create({
  baseURL: "http://localhost:3000/api/pets",
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

//Exporta funções CRUD usando Axios

export const api = {
  getPets() {
    return apiClient.get("/");
  },
  addPet(pet) {
    return apiClient.post("/", pet);
  },
  updatePet(id, pet) {
    return apiClient.put(`/${id}`, pet);
  },
  deletePet(id) {
    return apiClient.delete(`/${id}`);
  },
};
