import { useParams, Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ArrowLeft, ShoppingCart, Star, CheckCircle } from 'lucide-react'
import { toast } from 'sonner'
import PageShell from '../components/PageShell'
import PillButton from '../components/PillButton'
import { getWhatsAppUrl, formatPrice } from '../utils/constants'

const products = {
  1: { id: 1, title: 'Mario Kart 8 Deluxe', price: 249900, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9, category: 'juego', description: 'El juego de carreras definitivo para Nintendo Switch.', stock: 10 },
  4: { id: 4, title: 'PlayStation 5', price: 2299900, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.9, category: 'consola', description: 'La última generación de PlayStation con gráficos 4K.', stock: 5 },
  7: { id: 7, title: 'DualSense Wireless Controller', price: 279900, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8, category: 'accesorio', description: 'Controlador inalámbrico DualSense con tecnología háptica.', stock: 15 },
}

export default function ProductDetailPage() {
  const { id } = useParams()
  const product = products[id]

  if (!product) {
    return (
      <PageShell title="Producto no encontrado" subtitle="">
        <div className="text-center">
          <Link to="/" className="mt-4 inline-block font-bold text-red-500 hover:underline">
            Volver al inicio
          </Link>
        </div>
      </PageShell>
    )
  }

  const addToCart = () => {
    toast.success(`¡${product.title} añadido al carrito!`)
  }

  const whatsappProduct = getWhatsAppUrl(`Hola, me interesa: ${product.title}`)

  return (
    <PageShell title={product.title} subtitle={product.platform}>
      <Link
        to="/"
        className="mb-6 inline-flex items-center gap-2 font-bold text-gray-500 transition hover:text-gray-900"
      >
        <ArrowLeft className="h-4 w-4" /> Volver
      </Link>
      <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="overflow-hidden rounded-2xl border-4 border-gray-100"
        >
          <img src={product.image} alt={product.title} className="h-auto w-full object-cover" />
        </motion.div>
        <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} className="space-y-6">
          <div>
            <span className="mb-3 inline-block rounded-full bg-red-500 px-3 py-1 text-sm font-bold text-white">
              {product.category}
            </span>
            <div className="mt-2 flex items-center gap-2">
              <div className="flex gap-1">
                {[...Array(5)].map((_, i) => (
                  <Star
                    key={i}
                    className={`h-5 w-5 ${i < Math.floor(product.rating) ? 'fill-yellow-400 text-yellow-400' : 'text-gray-300'}`}
                  />
                ))}
              </div>
              <span className="font-semibold text-gray-500">({product.rating})</span>
            </div>
          </div>
          <div className="text-3xl font-black text-red-500">{formatPrice(product.price)}</div>
          <p className="text-gray-700">{product.description}</p>
          <div className="flex items-center gap-2 text-sm font-semibold text-gray-600">
            <CheckCircle className="h-4 w-4 text-green-500" />
            <span>En stock ({product.stock} unidades)</span>
          </div>
          <div className="flex flex-wrap gap-4">
            <button
              onClick={addToCart}
              className="flex items-center justify-center gap-2 rounded-3xl border-8 border-transparent bg-red-500 px-8 py-3 font-black text-white transition hover:border-gray-200 hover:bg-white hover:text-black"
            >
              <ShoppingCart className="h-5 w-5" /> Añadir al Carrito
            </button>
            <PillButton href={whatsappProduct} showArrow>
              Consultar
            </PillButton>
          </div>
        </motion.div>
      </div>
    </PageShell>
  )
}
