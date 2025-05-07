import express from "express";
import cors from "cors";
import { connectMongo } from "./lib/db.js";
import petsRoutes from "./routes/pets.js";

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use("api/pets", petRoutes);

app.use("/api/pets", petsRoutes);

connectMongo().then(() => {
  app
    .listen(PORT, () => {
      console.log(`🚀 Servidor rodando em http://localhost:${PORT}`);
    })
    .catch((err) => console.log(err));
});
