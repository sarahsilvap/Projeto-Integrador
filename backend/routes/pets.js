import express from "express";
import multer from "multer";
import path from "path";
import Pet from "../models/Pet.js";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const router = express.Router();

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, "/uploads"),
  filename: (req, file, cb) => cb(null, `${Date.now()}-${file.originalname}`),
});

const upload = multer({ storage });

router.post("/", upload.single("image"), async (req, res) => {
  const { name, age, castrated, available } = req.body;
  const { type, size } = req.body;
  // Validação
  if (!["cachorro", "gato", "Cachorro", "Gato"].includes(type)) {
    return res.status(400).json({ error: "Tipo inválido" });
  }

  if (!["pequeno", "medio", "grande", "Pequeno", "Medio", "Grande"].includes(size)) {
    return res.status(400).json({ error: "Tamanho inválido" });
  }

  const coverImage = req.file ? `/uploads/${req.file.filename}` : null;

  try {
    const newPet = new Pet({
      name,
      type,
      size,
      age,
      castrated,
      available,
      coverImage,
    });
    await newPet.save();
    res.status(201).json(newPet);
  } catch (err) {
    res.status(500).json({ message: "Erro ao salvar PET", err });
  }
});

router.get("/", async (req, res) => {
  const pets = await Pet.find();
  res.json(pets);
});

router.delete("/:id", async (req, res) => {
  try {
    await Pet.findByIdAndDelete(req.params.id); // ou Book.findByIdAndDelete
    res.status(200).json({ message: "Pet deletado com sucesso" });
  } catch (error) {
    res.status(500).json({ message: "Erro ao deletar pet", error });
  }
});

export default router;
