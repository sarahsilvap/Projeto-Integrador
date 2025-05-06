import express from 'express';
import Pet from '../models/Pet.js';

const router = express.Router();

router.get('/', async (req, res) => {
  const pets = await Pet.find();
  res.json(pets);
});

router.post('/', async (req, res) => {
  const newPet = new Pet(req.body);
  await newPet.save();
  res.status(201).json(newPet);
});

export default router;
