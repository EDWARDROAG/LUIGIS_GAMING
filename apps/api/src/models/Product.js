import mongoose from 'mongoose'

const productSchema = new mongoose.Schema(
  {
    title: { type: String, required: true },
    price: { type: Number, required: true },
    category: { type: String, enum: ['juego', 'consola', 'accesorio'], required: true },
    platform: String,
    rating: { type: Number, default: 0 },
    stock: { type: Number, default: 0 },
    image: String,
    description: String,
  },
  { timestamps: true }
)

export default mongoose.models.Product || mongoose.model('Product', productSchema)
