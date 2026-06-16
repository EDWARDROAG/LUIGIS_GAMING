import express from 'express'
import cors from 'cors'
import gamesRoutes from './routes/games.js'
import consolesRoutes from './routes/consoles.js'
import accessoriesRoutes from './routes/accessories.js'
import repairsRoutes from './routes/repairs.js'
import contactRoutes from './routes/contact.js'
import { notFound } from './middleware/notFound.js'
import { errorHandler } from './middleware/errorHandler.js'
import { corsOptions } from './config/cors.js'

const app = express()
app.use(cors(corsOptions))
app.use(express.json())

app.get('/api/health', (req, res) => {
  res.json({ success: true, message: 'Gaming Store API operativa' })
})

app.use('/api/games', gamesRoutes)
app.use('/api/consoles', consolesRoutes)
app.use('/api/accessories', accessoriesRoutes)
app.use('/api/repairs', repairsRoutes)
app.use('/api/contact', contactRoutes)

app.use(notFound)
app.use(errorHandler)

export default app
