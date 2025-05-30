<template>
  <div class="not-found">
    <h1>404 - Página Não Encontrada</h1>
    <p>A página que você está procurando não existe ou foi movida.</p>
    <button @click="goHome" class="home-button">Voltar para a página inicial</button>
  </div>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  padding: 20px;
}

h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 20px;
}

p {
  color: #7f8c8d;
  font-size: 1.2rem;
  margin-bottom: 30px;
}

.home-button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.home-button:hover {
  background-color: #3aa876;
}
</style>