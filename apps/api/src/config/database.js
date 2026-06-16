import mongoose from 'mongoose'

export async function connectDatabase() {
  const uri = process.env.MONGODB_URI

  if (!uri) {
    console.warn('MONGODB_URI no definida. La API funcionara con datos de ejemplo.')
    return
  }

  try {
    await mongoose.connect(uri)
    console.log('Conexion a MongoDB establecida')
  } catch (error) {
    console.error('Error al conectar con MongoDB:', error.message)
    console.warn('La API seguira funcionando con datos de ejemplo.')
  }
}
