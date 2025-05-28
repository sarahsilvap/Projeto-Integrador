// src/services/auth.ts
import axios from "axios";
const API_URL = import.meta.env.VITE_API_BASE_URL
    ? `${import.meta.env.VITE_API_BASE_URL}/auth`
    : "http://localhost:3000/api/auth";
export const authService = {
    register(data) {
        return axios.post(`${API_URL}/register`, data);
    },
    login(data) {
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
