<template>
  <header class="bg-white shadow-md z-10 relative">
    <div class="flex items-center justify-between px-6 py-4">
      <router-link to="/">
        <img :src="logo2" alt="Logo Adote Petz" class="logo-image h-12 mr-4"/>
      </router-link>

      <nav class="flex gap-6 items-center">
        <Menu as="div" class="relative">
          <MenuButton
            class="text-gray-800 hover:cursor-pointer font-medium hover:text-[#fd6b67] flex items-center gap-1">
            Institucional
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </MenuButton>
          <Transition enter="transition duration-100 ease-out" enter-from="transform scale-95 opacity-0"
            enter-to="transform scale-100 opacity-100" leave="transition duration-75 ease-in"
            leave-from="transform scale-100 opacity-100" leave-to="transform scale-95 opacity-0">
            <MenuItems class="absolute mt-2 w-56 rounded-md bg-white shadow-lg ring-opacity-5 focus:outline-none z-50">
              <div class="p-1 text-sm text-gray-800">
                <MenuItem v-slot="{ active }">
                <a :class="itemClass(active)" href="#">Sobre o Adote Petz</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                <a :class="itemClass(active)" href="#">Os pets nas lojas</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                <a :class="itemClass(active)" href="#">Transparência com você</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                <a :class="itemClass(active)" href="#">Como posso ajudar?</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                <a :class="itemClass(active)" href="#">Projetos sociais</a>
                </MenuItem>
              </div>
            </MenuItems>
          </Transition>
        </Menu>

        <ButtonRouteLabel />
        
      </nav>

      <div class="flex items-center gap-4">
        <button v-if="isLoggedIn" @click="handleLogout"
          class="text-gray-800 border px-3 py-1 rounded hover:bg-gray-100 hover:cursor-pointer">
          Sair
        </button>

        <!-- Se NÃO estiver logada -->
        <router-link v-else to="/login"
          class="text-white bg-[#fd6b67] border px-3 py-1 rounded hover:bg-[#fe827e] hover:cursor-pointer">
          Quero adotar
        </router-link>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Menu, MenuButton, MenuItems, MenuItem } from "@headlessui/vue";
import logo2 from "../assets/logo2.png";
import ButtonRouteLabel from "./ButtonRouteLabel.vue";

const isLoggedIn = ref(false);
const router = useRouter();

onMounted(() => {
  isLoggedIn.value = !!localStorage.getItem('token');
});

const handleLogout = () => {
  localStorage.removeItem('token');
  isLoggedIn.value = false;
  router.push('/login');
};

const itemClass = (active) =>
  `block px-4 py-2 ${active ? "bg-gray-100 text-[#fb6d67]" : "text-gray-800"}`;
</script>

<style scoped>
.logo-image {
  display: block;
  cursor: pointer;
  transition: opacity 0.3s;
}</style>