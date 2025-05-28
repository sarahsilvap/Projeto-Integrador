<script setup lang="ts">
import { useRouter, RouterView } from 'vue-router';
import { ref, computed } from 'vue';

const router = useRouter();

const buttonRouteLabel = computed(() => {
  return router.currentRoute.value.path === "/" ?
    "Doações" : "Home"
})

const changePage = () => {
  if (router.currentRoute.value.path === "/") {
    router.push("/doacao");
  } else {
    router.push("/");
  }
} 

</script>

<template>
    <button class="text-gray-800 font-medium hover:text-[#fb6d67] hover:cursor-pointer" @click="changePage">{{ buttonRouteLabel }}</button>
</template>

<style scoped>

</style>
