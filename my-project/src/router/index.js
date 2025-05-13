import { createRouter, createWebHistory } from "vue-router";
import FavoritesPets from "../views/FavoritesPets.vue";
import NotFound from "../views/NotFound.vue";
import Home from "../views/Home.vue";
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            component: FavoritesPets,
            path: "/favorites",
        },
        {
            component: Home,
            path: "/",
        },
        {
            component: NotFound,
            path: "/:pathMatch(.*)*",
        },
    ],
});
export default router;
