<template>
  <div class="grid grid-cols-5 gap-5 px-8 w-full">
    <div
      class="flip-container"
      v-for="character in characters"
      :key="character.name"
    >
      <div
        :style="
          character.imageUrl
            ? { backgroundImage: `url(${character.imageUrl})` }
            : {}
        "
        class="character-card bg-gray-50 p-4 rounded-lg flipper"
      >
        <div class="front">
          <h2 class="text-xl font-semibold text-gray-900">
            {{ character.name }}
          </h2>
        </div>
        <div
          class="back w-full h-full flex flex-col items-center justify-start px-4 text-center rounded-lg"
        >
          <h3 class="silver-text mt-3">Informações</h3>
          <div class="flex-1 flex flex-col justify-center items-center w-full">
            <h4 class="silver-text">
              Aparece nos filmes:
              <ul class="mb-5">
                <li
                  class="flex items-center"
                  v-for="(film, index) in character.filmTitles"
                  :key="index"
                >
                  <span class="material-symbols-outlined"> chevron_right </span
                  >{{ film }}
                </li>
              </ul>
              Gênero: {{ character.gender }} <br />
              Altura: {{ character.height }} cm <br />
              Ano de nascimento: {{ character.birth_year }} <br />
            </h4>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-1 mt-2">
        <span class="material-symbols-outlined text-gray-500 text-xl">
          link
        </span>
        <input
          v-model="character.imageUrl"
          type="text"
          placeholder="Cole a URL da imagem aqui"
          class="flex-1 px-2 py-1 rounded border border-gray-500"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import type { CharacterFilms } from "../models/characther.ts";

const character = defineProps<{
  characters: CharacterFilms[];
}>();
</script>

<style scoped>
.character-card {
  background-size: cover;
  background-position: center;
  height: 500px;
  display: flex;
  align-items: center;
  flex-direction: column;
  white-space: nowrap;
}

.character-card h2 {
  background-color: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 10px;
  border-radius: 4px;
}

.flip-container {
  perspective: 1000px;
  width: 100%;
  height: 100%;
}

.flipper {
  transition: 0.6s;
  transform-style: preserve-3d;
}

.front,
.back {
  backface-visibility: hidden;
  position: absolute;
  top: 0;
}

.back {
  transform: rotateY(180deg);
  background: linear-gradient(
    to right,
    #bf953f,
    #fcf6ba,
    #b38728,
    #fbf5b7,
    #aa771c
  );
  font-size: 1.2rem;
  background-size: 210% 190%;
}

.flip-container:hover .flipper {
  transform: rotateY(180deg);
}

.silver-text {
  background: linear-gradient(
    90deg,
    #707070 0%,
    #e6e5e5 50%,
    #707070 100%
  );
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}
</style>
