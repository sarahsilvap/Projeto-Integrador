import { defineStore } from "pinia";
import { Animal } from "../models/pet";

export type FavoriteStore = {
  favorites: Array<Animal>;
};

export const useFavoriteStore = defineStore("favorites", {
  state: () => ({
    favorites: [] as Animal[],
  }),
  actions: {
    addFavorite(newFavorite: Animal) {
      const deepCopy = JSON.parse(JSON.stringify(newFavorite));
      this.favorites.push(deepCopy);
    },
    removeFavorite(id: string) {
      const index = this.favorites.findIndex((a) => a.id === id);
      if (index >= 0) {
        this.favorites.splice(index, 1);
      }
    },
    isFavorite(id: string) {
      return this.favorites.some((a) => a.id === id);
    },
  },

  getters: {},
});
