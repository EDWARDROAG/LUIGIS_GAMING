import { motion } from 'framer-motion'
import PageShell from '../components/PageShell'
import ProductCard from '../components/ProductCard'

const consoles = [
  { id: 4, title: 'PlayStation 5', price: 499.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.9 },
  { id: 5, title: 'Xbox Series X', price: 499.99, image: 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400', platform: 'Microsoft', rating: 4.8 },
  { id: 6, title: 'Nintendo Switch OLED', price: 349.99, image: 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400', platform: 'Nintendo', rating: 4.7 },
  { id: 14, title: 'PlayStation 5 Digital', price: 399.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.6 },
  { id: 15, title: 'Xbox Series S', price: 299.99, image: 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400', platform: 'Microsoft', rating: 4.5 },
]

export default function ConsolesPage() {
  return (
    <PageShell title="Consolas" subtitle="Las mejores consolas del mercado">
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        {consoles.map((item, index) => (
          <motion.div
            key={item.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <ProductCard {...item} category="consola" />
          </motion.div>
        ))}
      </div>
    </PageShell>
  )
}
