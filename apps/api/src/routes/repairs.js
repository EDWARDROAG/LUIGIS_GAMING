import express from 'express'
const router = express.Router()

const repairServices = [
{ id: 1, name: 'Reparación de Consolas', price: 49, description: 'Diagnóstico y reparación de PlayStation, Xbox, Nintendo y más.' },
{ id: 2, name: 'Reparación de Controles', price: 29, description: 'Joystick drift, botones atascados, conexión y más.' },
{ id: 3, name: 'Mantenimiento Preventivo', price: 39, description: 'Limpieza profunda, cambio de pasta térmica y optimización.' }
]

router.get('/', (req, res) => {
res.json({ success: true, data: repairServices })
})

router.post('/request', (req, res) => {
const { serviceId, description, consoleType } = req.body
res.json({
success: true,
message: 'Solicitud de reparación recibida',
data: { serviceId, description, consoleType, status: 'pending' }
})
})

export default router
