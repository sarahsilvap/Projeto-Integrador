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
  const { name, species, size, age, available } = req.body;
  const coverImage = req.file ? `/uploads/${req.file.filename}` : null;

  try {
    const newPet = new Pet({ name, species, size, age, available, coverImage });
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

export default router;
