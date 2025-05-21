import { createRouter, createWebHistory } from "vue-router";
import FavoritesPets from "../views/FavoritesPets.vue";
import NotFound from "../views/NotFound.vue";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Cadastro from "../views/Cadastro.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      component:  Home,
      path: "/",
    },
    {
      component: Login,
      path: "/login",
    },
    {
      component: Cadastro,
      path: "/cadastro",
    },
    {
      component: FavoritesPets,
      path: "/favorites",
    },
    {
      component: NotFound,
      path: "/:pathMatch(.*)*",
    },
  ],
});

export default router;
