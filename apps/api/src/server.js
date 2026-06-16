import app from './app.js'
import dotenv from 'dotenv'
import { connectDatabase } from './config/database.js'

dotenv.config()

const PORT = process.env.PORT || 3000

async function startServer() {
  await connectDatabase()

  app.listen(PORT, () => {
    console.log(`Gaming Store API en puerto ${PORT}`)
  })
}

startServer().catch((error) => {
  console.error('Error al iniciar el servidor:', error)
  process.exit(1)
})
