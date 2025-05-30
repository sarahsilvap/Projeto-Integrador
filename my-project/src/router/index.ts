import { createRouter, createWebHistory } from "vue-router";
import NotFound from "../views/NotFound.vue";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Cadastro from "../views/Cadastro.vue";
import AdminPetsView from "../views/AdminPetsView.vue";
import Doacao from "../views/Doacao.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      component: Home,
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
      component: AdminPetsView,
      path: "/adm",
    },
    {
      component: Doacao,
      path: "/doacao",
    },
    {
      component: NotFound,
      path: "/:pathMatch(.*)*",
    },
  ],
});

export default router;
