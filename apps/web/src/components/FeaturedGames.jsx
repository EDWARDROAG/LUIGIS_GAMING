import { motion } from 'framer-motion'
import ProductCard from './ProductCard'
import SectionTitle from './SectionTitle'

const games = [
  { id: 1, title: 'Mario Kart 8 Deluxe', price: 249900, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 2, title: 'EA Sports FC 24', price: 289900, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.7 },
  { id: 3, title: 'Call of Duty: Modern Warfare', price: 199900, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.8 },
]

export default function FeaturedGames() {
  return (
    <section className="py-12 md:py-16">
      <div className="container mx-auto px-4">
        <SectionTitle title="Videojuegos Destacados" subtitle="Los títulos más populares del momento" />
        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {games.map((game, index) => (
            <motion.div
              key={game.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <ProductCard {...game} category="juego" />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
