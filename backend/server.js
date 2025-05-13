import express from "express";
import cors from "cors";
import { fileURLToPath } from "url";
import path from "path";
import { dirname } from "path";
import { connectMongo } from "./lib/db.js";
import petsRoutes from "./routes/pets.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.use("/uploads", express.static(path.join(__dirname, "uploads")));

app.use("/api/pets", petsRoutes);

connectMongo().then(() => {
  app.listen(PORT, (err) => {
    if (err) {
      console.log("❌ Erro ao inicar o servidor", err);
    } else {
      console.log(`🚀 Servidor rodando em http://localhost:${PORT}`);
    }
  });
});
