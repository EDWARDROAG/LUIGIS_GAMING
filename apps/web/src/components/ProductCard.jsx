import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ShoppingCart, Star } from 'lucide-react'
import { toast } from 'sonner'

export default function ProductCard({ id, title, price, image, platform, rating, category }) {
  const addToCart = (e) => {
    e.preventDefault()
    toast.success(`¡${title} añadido al carrito!`)
  }

  return (
    <Link to={`/producto/${id}`}>
      <motion.div
        whileHover={{ y: -5 }}
        className="overflow-hidden rounded-2xl bg-white text-gray-900 shadow-lg transition-all hover:shadow-xl"
      >
        <div className="relative aspect-square overflow-hidden">
          <img
            src={image}
            alt={title}
            className="h-full w-full object-cover transition-transform duration-300 hover:scale-105"
          />
          <span className="absolute right-2 top-2 rounded-full bg-red-500 px-3 py-1 text-xs font-bold text-white">
            {category}
          </span>
        </div>
        <div className="p-4">
          <div className="mb-2 flex items-start justify-between gap-2">
            <h3 className="line-clamp-1 font-black">{title}</h3>
            <span className="shrink-0 font-black text-red-500">${price}</span>
          </div>
          <div className="mb-3 flex items-center gap-2">
            <div className="flex items-center gap-1">
              <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
              <span className="text-sm font-semibold text-gray-600">{rating}</span>
            </div>
            <span className="text-xs text-gray-500">{platform}</span>
          </div>
          <button
            onClick={addToCart}
            className="flex w-full items-center justify-center gap-2 rounded-3xl border-4 border-transparent bg-red-500 py-2 text-sm font-black text-white transition hover:border-gray-200 hover:bg-white hover:text-black"
          >
            <ShoppingCart className="h-4 w-4" /> Añadir al Carrito
          </button>
        </div>
        <div className="flex justify-between px-4 pb-3">
          <div className="h-3 w-3 rounded-full bg-gaming-primary" />
          <div className="h-3 w-3 rounded-full bg-gaming-primary" />
        </div>
      </motion.div>
    </Link>
  )
}
