import mongoose from "mongoose";

const PetSchema = new mongoose.Schema({
  name: { type: String, required: true },
  species: { type: String, required: true },
  size: { type: String, required: true },
  age: { type: Number, required: true },
  available: { type: Boolean, default: true },
});

const Pet = mongoose.model("Pet", PetSchema);

export default Pet;
