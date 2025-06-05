// routes/auth.js
import express from 'express'
import jwt from 'jsonwebtoken'
import User from '../models/User.js'

const router = express.Router()

router.post('/register', async (req, res) => {
  try {
    console.log('BODY recebido no register:', req.body);
    
    const { email, password, name } = req.body

    console.log('Recebido no register:', { email, password, name })

    const existingUser = await User.findOne({ email })
    if (existingUser) {
      return res.status(400).send({ error: 'Usuário já cadastrado' })
    }

    const user = new User({ email, password, name })
    console.log('User antes do save:', user);

    console.log('Salvando usuário:', user)
    await user.save()
    console.log('Usuário salvo!')

    res.status(201).send({ message: 'Usuário criado com sucesso' })
  } catch (err) {
    console.error('Erro no register:', err)
    res.status(500).send({ error: 'Erro no servidor' })
  }
})


router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body

    if (!email || !password) {
      return res.status(400).send({ error: 'Email e senha são obrigatórios' })
    }

    const user = await User.findOne({ email })
    if (!user) {
      return res.status(400).send({ error: 'Usuário não encontrado' })
    }

    const isMatch = await user.comparePassword(password)
    if (!isMatch) {
      return res.status(400).send({ error: 'Senha incorreta' })
    }

    // Gera token JWT - troque 'seu_segredo_jwt' por uma variável de ambiente segura
    const token = jwt.sign({ _id: user._id }, 'seu_segredo_jwt', { expiresIn: '1h' })

    res.send({ token, user: { _id: user._id, email: user.email, name: user.name } })
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: 'Erro no servidor' })
  }
})

export default router
