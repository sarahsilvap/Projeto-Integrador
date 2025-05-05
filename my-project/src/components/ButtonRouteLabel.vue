<script setup lang="ts">
import { useRouter, RouterView } from 'vue-router';
import { ref, computed } from 'vue';

const router = useRouter();

const buttonRouteLabel = computed(() => {
  return router.currentRoute.value.path === "/" ?
    "Favoritos" : "Lista de Personagens"
})

const changePage = () => {
  if (router.currentRoute.value.path === "/") {
    router.push("/favorites");
  } else {
    router.push("/");
  }
} 

</script>

<template>
    <button class="ml-2 text-purple-600 hover:text-purple-400 cursor-pointer" @click="changePage">{{ buttonRouteLabel }}</button>
</template>

<style scoped>

</style>
