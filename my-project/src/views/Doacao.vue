<template>
  <nav class="menu">
      <router-link to="/" class="home-link">
        <span>← Voltar à Página Inicial</span>
      </router-link>
      <h1 class="site-title">Adote um Amigo</h1>
    </nav>
  <div class="adoption-container">
    <div class="adoption-card">
      <h1>Adote um Amigo Peludo!</h1>
      <p class="description">
        Sua doação ajuda a cuidar de cães que precisam de um lar. Qualquer valor
        é bem-vindo e faz toda a diferença!
      </p>

      <div class="qr-code-section">
        <h2>Faça sua doação via PIX</h2>
        <div class="qr-code-container">
          <!-- Substitua pelo seu QR code real -->
          <img
            src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=PIX_CODIGO_AQUI"
            alt="QR Code para PIX"
            class="qr-code"
          />
        </div>
        <p class="pix-key">Chave PIX: seu-email@adocao.com</p>
        <p class="note">Escaneie o QR code ou use a chave PIX acima</p>
      </div>

      <div class="thank-you">
        <p>Obrigado por ajudar nossos amigos caninos!</p>
        <p>🐶 ❤️</p>
      </div>
    </div>
  </div>
</template>

<script>
import Menu from "../components/Menu.vue";
export default {
  name: "AdoptionDonation",
};
</script>

<style scoped>
.menu {
  background-color: #ff6b6b;
  padding: 10px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.adoption-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
}

.adoption-card {
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 30px;
  max-width: 500px;
  text-align: center;
}

h1 {
  color: #ff6b6b;
  margin-bottom: 20px;
}

.description {
  font-size: 1.1rem;
  color: #555;
  margin-bottom: 30px;
  line-height: 1.6;
}

.qr-code-section {
  margin: 25px 0;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
}

.qr-code-container {
  margin: 15px auto;
  padding: 10px;
  background: white;
  display: inline-block;
  border: 1px solid #eee;
}

.qr-code {
  width: 200px;
  height: 200px;
}

.pix-key {
  font-weight: bold;
  color: #2c3e50;
  margin: 15px 0;
  word-break: break-all;
}

.note {
  font-size: 0.9rem;
  color: #777;
}

.thank-you {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #ff6b6b;
}
</style>
