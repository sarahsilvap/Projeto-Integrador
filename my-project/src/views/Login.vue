<script>
import Logo from "../assets/logo.png";
import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      Logo: Logo,
      errorMessage: null,
      isLoading: false,
    };
  },
  methods: {
    async handleLogin() {
      this.errorMessage = null;
      this.isLoading = true;
      try {
        const response = await axios.post('http://localhost:3000/api/auth/login', {
          email: this.email,
          password: this.password
        });

        // Exemplo: salva token no localStorage (ajuste conforme seu fluxo)
        localStorage.setItem('token', response.data.token);

        // Redireciona para outra página após login, ex:
        this.$router.push('/');
      } catch (error) {
        console.error("Erro no login:", error);
        this.errorMessage = error.response?.data?.error || 'Erro ao tentar logar.';
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<template>
  <div class="auth-container">
    <div class="auth-card">
      <router-link to="/">
        <img :src="Logo" alt="Logo Adote Petz" class="logo-image" />
      </router-link>
      <h2 class="auth-title">Login</h2>
      <p class="p" v-if="errorMessage" style="color: red; margin-bottom: 10px;">{{ errorMessage }}</p>
      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label for="email">E-mail</label>
          <input type="email" id="email" v-model="email" placeholder="Digite seu e-mail" required />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input type="password" id="password" v-model="password" placeholder="Digite sua senha" required />
        </div>
        <button type="submit" class="auth-button" :disabled="isLoading">{{ isLoading ? 'Entrando...' : 'Entrar' }}</button>
      </form>
      <p class="auth-link">
        Não tem uma conta? <router-link to="/cadastro">Cadastre-se</router-link>
      </p>
      <p class="home-link">
        <router-link to="/">
          ← Voltar à página inicial
        </router-link>
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

.p {
  text-align: center;
  margin-bottom: 25px;
  margin-top: 15px;
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

.home-link {
  text-align: center;
  margin-top: 20px;
}

.home-link:hover {
  text-decoration: underline;
}
</style>
