<script setup lang="ts">
import { defineProps } from "vue";
import { Pet } from "../models/pet.js";

const props = defineProps<{
  pet: Pet;
}>();
</script>

<template>
  <div class="">
    <div
      :style="pet.imageUrl ? { backgroundImage: `url(${pet.imageUrl})` } : {}"
      class="max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm box-border dark:bg-gray-800 dark:border-gray-700"
    >
      <div
        class="max-w-sm bg-white rounded-lg"
      >
        <a href="#">
          <img
            class="rounded-t-lg"
            src="https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2024/03/14/264292112-golden-retriever-1.jpg"
            alt=""
          />
        </a>
        <div class="p-5">
          <a href="#">
            <h5
              class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
            >
              {{ pet.name }}
            </h5>
          </a>
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            Here are the biggest enterprise technology acquisitions of 2021 so
            far, in reverse chronological order.
          </p>
          <a
            href="#"
            class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-[#faa72d] rounded-lg hover:bg-[#fcca4f] focus:ring-4 focus:outline-none focus:ring-[#fedb61]"
          >
            Quero adotar
            <svg
              class="rtl:rotate-180 w-3.5 h-3.5 ms-2"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M1 5h12m0 0L9 1m4 4L9 9"
              />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
