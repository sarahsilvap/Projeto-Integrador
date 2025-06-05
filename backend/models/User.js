import mongoose from 'mongoose'
import bcrypt from 'bcryptjs'

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true,
  },
  password: {
    type: String,
    required: true,
    minlength: 6,
  },
  favorites: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Pet'
  }]
}, {
  timestamps: true
})

// Criptografa a senha antes de salvar
userSchema.pre('save', async function (next) {
  console.log('Hook pre-save ativado, senha atual:', this.password);
  
  if (!this.isModified('password')) {
    console.log('Senha NÃO modificada, pulando hash');
    return next();
  }

  console.log('Senha modificada, vamos fazer hash:', this.password);

  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
  console.log('Senha criptografada:', this.password);
  next();
});

// Método de instância para comparar senhas
userSchema.methods.comparePassword = function (candidatePassword) {
  return bcrypt.compare(candidatePassword, this.password);
};

// Verifica as credenciais
userSchema.statics.findByCredentials = async function (email, password) {
  const user = await this.findOne({ email })
  if (!user) throw new Error('Credenciais inválidas')
  const isMatch = await bcrypt.compare(password, user.password)
  if (!isMatch) throw new Error('Credenciais inválidas')
  return user
}

const User = mongoose.model('User', userSchema)

export default User