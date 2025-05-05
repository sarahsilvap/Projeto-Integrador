import { createRouter, createWebHistory } from "vue-router";
import FavoritesCharacters from "../views/FavoritesCharacters.vue";
import ListCharacters from "../views/ListCharacters.vue";
import NotFound from "../views/NotFound.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      component: FavoritesCharacters,
      path: "/favorites",
    },
    {
      component: ListCharacters,
      path: "/",
    },
    {
      component: NotFound,
      path: "/:pathMatch(.*)*",
    },
  ],
});

export default router;
