// src/services/api.ts
import axios, { AxiosInstance, AxiosResponse } from "axios";
import { Pet } from "../models/pet";

// Cria instância do Axios com URL base da API
const apiClient: AxiosInstance = axios.create({
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
  getPets(): Promise<AxiosResponse<Pet[]>> {
    return apiClient.get("/pets");
  },

  addPet(pet: FormData | Omit<Pet, "_id">): Promise<AxiosResponse<Pet>> {
    return apiClient.post("/pets", pet, {
      headers: { "Content-Type": "multipart/form-data" },
    });
  },

  updatePet(
    id: string,
    pet: FormData | Partial<Pet>
  ): Promise<AxiosResponse<Pet>> {
    const isFormData = pet instanceof FormData;
    return apiClient.put(`/pets/${id}`, pet, {
      headers: isFormData
        ? { "Content-Type": "multipart/form-data" }
        : undefined,
    });
  },

  deletePet(id: string): Promise<AxiosResponse<void>> {
    return apiClient.delete(`/pets/${id}`);
  },
};
