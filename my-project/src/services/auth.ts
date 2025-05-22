// src/services/auth.ts
import axios, { AxiosResponse } from "axios";

const API_URL = "http://localhost:3000/api/auth";

interface RegisterData {
  name: string;
  email: string;
  password: string;
}

interface LoginData {
  email: string;
  password: string;
}

interface LoginResponse {
  token: string;
  // qualquer outro dado que seu backend retornar no login
}

export const authService = {
  register(data: RegisterData): Promise<AxiosResponse> {
    return axios.post(`${API_URL}/register`, data);
  },

  login(data: LoginData): Promise<AxiosResponse<LoginResponse>> {
    return axios.post(`${API_URL}/login`, data);
  },

  logout() {
    localStorage.removeItem("token");
  },

  getProfile() {
    const token = localStorage.getItem("token");
    if (!token) {
      return Promise.reject(new Error("Token não encontrado"));
    }
    return axios.get(`${API_URL}/profile`, {
      headers: { Authorization: `Bearer ${token}` },
    });
  },
};
