import express from 'express'
const router = express.Router()

router.post('/', (req, res) => {
const { name, email, phone, subject, message } = req.body

if (!name || !email || !subject || !message) {
return res.status(400).json({
success: false,
message: 'Faltan campos requeridos'
})
}

// Aquí iría la lógica para enviar email
res.json({
success: true,
message: 'Mensaje recibido correctamente',
data: { name, email, subject }
})
})

export default router
