import express from 'express'
import auth from '../middleware/auth.js'
import Favorite from '../models/Favorite.js'
import Pet from '../models/Pet.js' // Importe o modelo Pet

const router = express.Router()

// Obter todos os favoritos do usuário
router.get('/', auth, async (req, res) => {
  try {
    const favorites = await Favorite.find({ user: req.user._id })
      .populate({
        path: 'pet',
        select: 'name type size age coverImage' // Apenas campos necessários
      })
      
    res.status(200).json({
      success: true,
      data: favorites.map(f => f.pet)
    })
  } catch (error) {
    console.error('Erro ao buscar favoritos:', error)
    res.status(500).json({
      success: false,
      message: 'Erro interno ao buscar favoritos'
    })
  }
})

// Adicionar favorito
router.post('/:petId', auth, async (req, res) => {
  try {
    // 1. Verifica se o pet existe
    const pet = await Pet.findById(req.params.petId)
    if (!pet) {
      return res.status(404).json({
        success: false,
        message: 'Pet não encontrado'
      })
    }

    // 2. Verifica se já é favorito
    const existingFavorite = await Favorite.findOne({
      pet: req.params.petId,
      user: req.user._id
    })

    if (existingFavorite) {
      return res.status(400).json({
        success: false,
        message: 'Pet já está nos favoritos'
      })
    }

    // 3. Cria o favorito
    const favorite = new Favorite({
      pet: req.params.petId,
      user: req.user._id
    })

    await favorite.save()
    
    res.status(201).json({
      success: true,
      data: pet // Retorna os dados do pet favoritado
    })
  } catch (error) {
    console.error('Erro ao adicionar favorito:', error)
    res.status(400).json({
      success: false,
      message: 'Erro ao adicionar favorito',
      error: error.message
    })
  }
})

// Remover favorito
router.delete('/:petId', auth, async (req, res) => {
  try {
    const deleted = await Favorite.findOneAndDelete({
      pet: req.params.petId,
      user: req.user._id
    })

    if (!deleted) {
      return res.status(404).json({
        success: false,
        message: 'Favorito não encontrado'
      })
    }

    res.status(200).json({
      success: true,
      message: 'Favorito removido com sucesso'
    })
  } catch (error) {
    console.error('Erro ao remover favorito:', error)
    res.status(500).json({
      success: false,
      message: 'Erro interno ao remover favorito'
    })
  }
})

export default router