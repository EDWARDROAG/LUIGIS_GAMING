import express from 'express'
const router = express.Router()

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 69.99, platform: 'PlayStation 5', rating: 4.8, stock: 15 },
  { id: 8, title: 'Xbox Wireless Controller', price: 59.99, platform: 'Xbox Series X', rating: 4.7, stock: 12 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 69.99, platform: 'Nintendo Switch', rating: 4.9, stock: 10 },
  { id: 10, title: 'Auriculares Gaming RGB', price: 89.99, platform: 'Multiplataforma', rating: 4.6, stock: 20 }
]

router.get('/', (req, res) => {
  res.json({ success: true, data: accessories })
})

router.get('/:id', (req, res) => {
  const accessory = accessories.find((item) => item.id === parseInt(req.params.id))
  if (!accessory) {
    return res.status(404).json({ success: false, message: 'Accesorio no encontrado' })
  }
  res.json({ success: true, data: accessory })
})

export default router
