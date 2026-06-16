import { motion } from 'framer-motion'
import ProductCard from './ProductCard'
import SectionTitle from './SectionTitle'

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 279900, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8 },
  { id: 8, title: 'Xbox Wireless Controller', price: 239900, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Xbox Series X', rating: 4.7 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 279900, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Nintendo Switch', rating: 4.6 },
  { id: 10, title: 'Auriculares Gaming', price: 359900, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'Universal', rating: 4.5 },
]

export default function AccessoryGrid() {
  return (
    <section className="py-12 md:py-16">
      <div className="container mx-auto px-4">
        <SectionTitle title="Accesorios" subtitle="Todo lo que necesitas para tu setup" />
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
          {accessories.map((accessory, index) => (
            <motion.div
              key={accessory.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <ProductCard {...accessory} category="accesorio" />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
