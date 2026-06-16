import express from 'express'
const router = express.Router()

// Datos de ejemplo
const games = [
{ id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, platform: 'Nintendo Switch', rating: 4.9, stock: 10 },
{ id: 2, title: 'EA Sports FC 24', price: 69.99, platform: 'PlayStation 5', rating: 4.7, stock: 8 },
{ id: 3, title: 'Call of Duty: Modern Warfare', price: 49.99, platform: 'Xbox Series X', rating: 4.8, stock: 12 }
]

router.get('/', (req, res) => {
res.json({ success: true, data: games })
})

router.get('/:id', (req, res) => {
const game = games.find(g => g.id === parseInt(req.params.id))
if (!game) {
return res.status(404).json({ success: false, message: 'Juego no encontrado' })
}
res.json({ success: true, data: game })
})

export default router
