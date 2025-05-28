// src/services/api.ts
import axios from "axios";
// Cria instância do Axios com URL base da API
const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:3000/api",
});
// Interceptor para token (se usar autenticação)
apiClient.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");
    if (token && config.headers) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});
// Exporta funções CRUD usando Axios com tipagem adequada
export const api = {
    getPets() {
        return apiClient.get("/pets");
    },
    addPet(pet) {
        return apiClient.post("/pets", pet, {
            headers: { "Content-Type": "multipart/form-data" },
        });
    },
    updatePet(id, pet) {
        const isFormData = pet instanceof FormData;
        return apiClient.put(`/pets/${id}`, pet, {
            headers: isFormData
                ? { "Content-Type": "multipart/form-data" }
                : undefined,
        });
    },
    deletePet(id) {
        return apiClient.delete(`/pets/${id}`);
    },
};
