<script>
import Logo from "../assets/logo.png";
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { authService } from '../services/auth'; 

export default {
  name: "RegisterPage",
  setup() {
    const router = useRouter();
    
    const form = ref({
      name: '',
      email: '',
      password: '',
      confirmPassword: ''
    });
    
    const isLoading = ref(false);
    const errorMessage = ref('');
    
    const handleRegister = async () => {
      if (form.value.password !== form.value.confirmPassword) {
        errorMessage.value = 'As senhas não coincidem';
        return;
      }
      
      if (!form.value.name || !form.value.email || !form.value.password) {
        errorMessage.value = 'Preencha todos os campos!';
        return;
      }
      
      isLoading.value = true;
      errorMessage.value = "";
      
      try {
        // usa o authService para registrar
        await authService.register({
          name: form.value.name,
          email: form.value.email,
          password: form.value.password,
        });
        router.push('/login?newUser=true');
      } catch (error) {
        console.error('Registration error:', error);
        // tenta pegar mensagem do erro do axios, fallback para mensagem genérica
        errorMessage.value = error.response?.data?.message || error.message || 'Erro ao cadastrar. Tente novamente.';
      } finally {
        isLoading.value = false;
      }
    };
    
    return {
      Logo,
      form,
      isLoading,
      errorMessage,
      handleRegister
    };
  }
};
</script>

<template>
  <div class="auth-container">
    <div class="auth-card">
      <router-link to="/">
        <img :src="Logo" alt="Logo Adote Petz" class="logo-image" />
      </router-link>
      <h2 class="auth-title">Cadastro</h2>

      <!-- Mensagem de erro -->
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleRegister" class="auth-form">
        <div class="form-group">
          <label for="name">Nome Completo</label>
          <input
            type="text"
            id="name"
            v-model="form.name"
            placeholder="Digite seu nome completo"
            required
          />
        </div>
        <div class="form-group">
          <label for="email">E-mail</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            placeholder="Digite seu e-mail"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            placeholder="Digite sua senha"
            required
          />
        </div>
        <div class="form-group">
          <label for="confirmPassword">Confirme sua Senha</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="form.confirmPassword"
            placeholder="Confirme sua senha"
            required
          />
        </div>
        <button type="submit" class="auth-button" :disabled="isLoading">
          <span v-if="!isLoading">Cadastrar</span>
          <span v-else>Cadastrando...</span>
        </button>
      </form>
      <p class="auth-link">
        Já tem uma conta? <router-link to="/login">Faça login</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.logo-image {
  display: block;
  margin: 0 auto 20px;
  max-height: 200px;
  width: auto;
  cursor: pointer;
  transition: opacity 0.3s;
}

.logo-image:hover {
  opacity: 0.8;
}

.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #ffffff;
  padding: 20px;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
}

.auth-title {
  color: #2d74be;
  text-align: center;
  margin-bottom: 25px;
  margin-top: 15px;
  font-size: 24px;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  color: #333333;
  font-weight: 500;
}

.form-group input {
  padding: 12px 15px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #2d74be;
}

.auth-button {
  background-color: #fb6d67;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.auth-button:hover {
  background-color: #e05d57;
}

.auth-link {
  text-align: center;
  margin-top: 20px;
  color: #333333;
}

.auth-link a {
  color: #2d74be;
  text-decoration: none;
  font-weight: 500;
}

.auth-link a:hover {
  text-decoration: underline;
}

.error-message {
  color: #fb6d67;
  background-color: #ffeeed;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 15px;
  text-align: center;
  font-size: 14px;
}
</style>
