import mongoose from "mongoose";
import dotenv from "dotenv"; 

dotenv.config();

export async function connectMongo() {
  const mongoUri = process.env.MONGO_URI;

  if (!mongoUri) {
    throw new Error("❌ Variável de ambiente MONGO_URI não definida no arquivo .env");
  }

  try {
    await mongoose.connect(mongoUri);
    console.log("✅ Conectado ao MongoDB");
  } catch (err) {
    console.error("❌ Erro ao conectar ao MongoDB:", err);
    process.exit(1);
  }
}
