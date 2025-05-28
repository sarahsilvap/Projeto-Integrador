// src/composables/useAuth.ts
import { ref, computed } from 'vue';
const token = ref(localStorage.getItem('token'));
export function useAuth() {
    const isAuthenticated = computed(() => !!token.value);
    function setToken(newToken) {
        token.value = newToken;
        localStorage.setItem('token', newToken);
    }
    function logout() {
        token.value = null;
        localStorage.removeItem('token');
    }
    return {
        token,
        isAuthenticated,
        setToken,
        logout,
    };
}
