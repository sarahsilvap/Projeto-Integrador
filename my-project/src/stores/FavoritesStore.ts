import { defineStore } from "pinia";
import { Pet } from "../models/pet";

export type FavoriteStore = {
  favorites: Array<Pet>;
};

export const useFavoriteStore = defineStore("favorites", {
  state: () => ({
    favorites: [] as Pet[],
  }),
  actions: {
    addFavorite(newFavorite: Pet) {
      const exists = this.favorites.some((a: Pet) => a._id === newFavorite._id);
      if (!exists) {
        const deepCopy = JSON.parse(JSON.stringify(newFavorite));
        this.favorites.push(deepCopy);
      }
    },
    removeFavorite(id: string) {
      const index = this.favorites.findIndex((a: Pet) => a._id === id);
      if (index >= 0) {
        this.favorites.splice(index, 1);
      }
    },
    isFavorite(id: string) {
      return this.favorites.some((a: Pet) => a._id === id);
    },
  },

  getters: {},
});
