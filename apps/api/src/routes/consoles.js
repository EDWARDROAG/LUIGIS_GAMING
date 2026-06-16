import express from 'express'
const router = express.Router()

const consoles = [
{ id: 4, title: 'PlayStation 5', price: 499.99, platform: 'Sony', rating: 4.9, stock: 5 },
{ id: 5, title: 'Xbox Series X', price: 499.99, platform: 'Microsoft', rating: 4.8, stock: 3 },
{ id: 6, title: 'Nintendo Switch OLED', price: 349.99, platform: 'Nintendo', rating: 4.7, stock: 7 }
]

router.get('/', (req, res) => {
res.json({ success: true, data: consoles })
})

router.get('/:id', (req, res) => {
const console = consoles.find(c => c.id === parseInt(req.params.id))
if (!console) {
return res.status(404).json({ success: false, message: 'Consola no encontrada' })
}
res.json({ success: true, data: console })
})

export default router
