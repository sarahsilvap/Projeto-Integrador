<template>
  <main
    class="w-full min-h-screen bg-gradient-to-r from-gray-950 via-blue-950 to-fuchsia-800 text-white grid grid-cols-4 p-10">
    <div class="col-span-4 text-primary text-5xl text-center flex flex-col items-center justify-center">
      <h1>
        🚀 Personagens de Star Wars 🛸
      </h1>
      <div class="m-8 flex items-center text-lg">
        <p>Seguir para:</p>
        <ButtonRouteLabel />
      </div>
    </div>
    <div class="col-start-2 col-span-2">
      <table class="w-full border-collapse border table-auto text-center rounded-lg shadow-lg">
        <thead>
          <tr class="bg-indigo-600/50">
            <th class="border p-4 relative text-center">Personagem</th>
            <th class="border p-4">Favoritar </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="character in characters" :key="character.name"
            class="hover:bg-indigo-600/50 transition-all bg-indigo-600/25">
            <td class="border p-3">{{ character.name }}</td>
            <td class="border p-3">
              <span class="heart-favorite material-symbols-outlined cursor-pointer hover:text-red-500"
                :class="{ 'text-red-500': isCharacterFavorite(character.name) }"
                @click="toggleFavorite(character)">
                favorite
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import type { CharacterFilms } from "../models/characther.ts";
import ButtonRouteLabel from "../components/ButtonRouteLabel.vue";
import { useFavoriteStore } from '../stores/FavoritesStore';
import type { Character } from "../models/characther.ts";

onMounted(async () => {
  try {
    const response = await axios.get("https://swapi.py4e.com/api/people/");
    const charactersData = response.data.results;

    for (let character of charactersData) {
      const filmTitles = await getFilmTitles(character.films);
      character.filmTitles = filmTitles;
      console.log(`Filmes de ${character.name}:`, filmTitles); // ✅ Aqui!
    }

    characters.value = charactersData;
  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  }
});

const getFilmTitles = async (filmUrls: string[]) => {
  const filmRequests = filmUrls.map((url) => axios.get(url));
  const filmResponses = await axios.all(filmRequests);
  return filmResponses.map((response) => response.data.title);
};

const characters = ref<CharacterFilms[]>([]);

const favoritesStore = useFavoriteStore();

const loadingFavorits = ref(false);

const toggleFavorite = async (character: Character) => {
  if (favoritesStore.isFavorite(character.name)) {
    favoritesStore.removeFavorite(character.name);
  } else {
    const filmTitles = await getFilmTitles(character.films);
    const characterWithFilms = { ...character, filmTitles };
    favoritesStore.addFavorite(characterWithFilms);
  }
};

const isCharacterFavorite = (name: string) => {
  return favoritesStore.isFavorite(name);
};

</script>

<style scoped>
.add-button:hover {
  transform: scale(1.15);
}
</style>
