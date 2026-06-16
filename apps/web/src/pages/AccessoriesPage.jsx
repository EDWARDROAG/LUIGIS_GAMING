import { motion } from 'framer-motion'
import PageShell from '../components/PageShell'
import ProductCard from '../components/ProductCard'

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8 },
  { id: 8, title: 'Xbox Wireless Controller', price: 59.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Xbox Series X', rating: 4.7 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Nintendo Switch', rating: 4.6 },
  { id: 10, title: 'Auriculares Gaming', price: 89.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'Universal', rating: 4.5 },
  { id: 16, title: 'Teclado Mecánico RGB', price: 129.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'PC', rating: 4.7 },
  { id: 17, title: 'Mouse Gaming Logitech', price: 79.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'PC', rating: 4.6 },
]

export default function AccessoriesPage() {
  return (
    <PageShell title="Accesorios" subtitle="Todo lo que necesitas para tu setup">
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        {accessories.map((accessory, index) => (
          <motion.div
            key={accessory.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <ProductCard {...accessory} category="accesorio" />
          </motion.div>
        ))}
      </div>
    </PageShell>
  )
}
