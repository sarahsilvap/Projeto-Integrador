// middleware/auth.js
import jwt from 'jsonwebtoken'
import User from '../models/User.js'

const auth = async (req, res, next) => {
  try {
    const token = req.header('Authorization')?.replace('Bearer ', '')
    if (!token) throw new Error('Token ausente')

    const decoded = jwt.verify(token, 'seu_segredo_jwt')
    const user = await User.findById(decoded._id)

    if (!user) throw new Error('Usuário não encontrado')

    req.user = user
    next()
  } catch (err) {
    res.status(401).send({ error: 'Autenticação necessária.' })
  }
}

export default auth
