import mongoose from "mongoose";

const PetSchema = new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, required: true },
  size: { type: String, required: true },
  age: { type: Number, required: true },
  castrated: { type: Boolean, required: true },
  description: { type: String, required: false },
  available: { type: Boolean, default: true },
  coverImage: { type: String },
});

const Pet = mongoose.model("Pet", PetSchema);

export default Pet;
