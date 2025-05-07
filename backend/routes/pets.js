import express from "express";
const multer = requite("multer");
const path = require("path");
import Pet from "../models/Pet.js";

const router = express.Router();

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, "/uploads"),
  filename: (req, file, cb) => cb(null, `${Date.now()}-${file.originalname}`),
});

const upload = multer({ storage });

router.post("/", upload.single("image"), async (req, res) => {
  const { name, species, size, age, available } = new Pet(req.body);
  const coverImage = req.file ? `/uploads/${req.file.filename}` : null;

  try {
    const newPet = new Pet({ name, species, size, age, available, coverImage });
    await newPet.save();
    res.status(201).json(newPet);
  } catch (err) {
    res.status(500).json({ message: "Erro ao salvar PET", err });
  }

  router.get("/", async (req, res) => {
    const pets = await Pet.find();
    res.json(pets);
  });
});

export default router;
