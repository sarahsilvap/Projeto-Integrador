import { defineStore } from "pinia";
export const useFavoriteStore = defineStore("favorites", {
    state: () => ({
        favorites: [],
    }),
    actions: {
        addFavorite(newFavorite) {
            const deepCopy = JSON.parse(JSON.stringify(newFavorite));
            this.favorites.push(deepCopy);
        },
        removeFavorite(id) {
            const index = this.favorites.findIndex((a) => a._id === id);
            if (index >= 0) {
                this.favorites.splice(index, 1);
            }
        },
        isFavorite(id) {
            return this.favorites.some((a) => a._id === id);
        },
    },
    getters: {},
});
