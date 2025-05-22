import { defineStore } from "pinia";
import { api } from "../services/api"; // seu arquivo api.ts com axios
import { Pet } from "../models/pet";

export const useFavoriteStore = defineStore("favorites", {
  state: () => ({
    favorites: [] as Pet[],
  }),
  actions: {
    async loadFavorites() {
      try {
        console.log("Carregando favoritos do backend...");
        const response = await api.getFavorites();
        if (response.success) {
          this.favorites = response.data;
          console.log("Favoritos carregados:", this.favorites);
        } else {
          throw new Error(response.message || "Falha ao carregar favoritos");
        }
      } catch (error) {
        console.error("Erro ao carregar favoritos:", error);
      }
    },
    async addFavorite(pet: Pet) {
      try {
        console.log("Chamando API para adicionar favorito:", pet._id);
        await api.addFavorite(pet._id);
        this.favorites = [...this.favorites, pet];
      } catch (error) {
        console.error("Erro ao adicionar favorito (store):", error);
      }
    },
    async removeFavorite(petId: string) {
      try {
        console.log(
          "Enviando para backend o pet para remover dos favoritos:",
          petId
        );
        await api.removeFavorite(petId);
        this.favorites = this.favorites.filter((p) => p._id !== petId);
        console.log("Pet removido dos favoritos locais:", petId);
      } catch (error) {
        console.error("Erro ao remover favorito:", error);
      }
    },
    isFavorite(id: string) {
      return this.favorites.some((p) => p._id === id);
    },
  },
});
