import { defineStore } from "pinia";
import type { CharacterFilms } from "../models/characther.js";

export type FavoriteStore = {
  favorites: Array<CharacterFilms>;
};

export const useFavoriteStore = defineStore("favorites", {
  state: () => ({
    favorites: [] as CharacterFilms[],
  }),
  actions: {
    addFavorite(newFavorite: CharacterFilms) {
      const deepCopy = JSON.parse(JSON.stringify(newFavorite));
      this.favorites.push(deepCopy);
    },
    removeFavorite(name: string) {
      const index = this.favorites.findIndex((env) => env.name === name);
      if (index >= 0) {
        this.favorites.splice(index, 1);
      }
    },
    isFavorite(characterName: string) {
      return this.favorites.some((c) => c.name === characterName);
    },
  },

  getters: {},
});
