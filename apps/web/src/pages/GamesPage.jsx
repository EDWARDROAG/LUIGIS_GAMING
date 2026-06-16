import { useState } from 'react'
import { motion } from 'framer-motion'
import PageShell from '../components/PageShell'
import ProductCard from '../components/ProductCard'

const games = [
  { id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 2, title: 'EA Sports FC 24', price: 69.99, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.7 },
  { id: 3, title: 'Call of Duty: Modern Warfare', price: 49.99, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.8 },
  { id: 11, title: 'The Legend of Zelda: Tears', price: 69.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 12, title: 'FIFA 24', price: 59.99, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.6 },
  { id: 13, title: 'Halo Infinite', price: 39.99, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.5 },
]

export default function GamesPage() {
  const [search, setSearch] = useState('')
  const filteredGames = games.filter((game) => game.title.toLowerCase().includes(search.toLowerCase()))

  return (
    <PageShell title="Videojuegos" subtitle="Todos los títulos disponibles">
      <div className="mb-8">
        <input
          type="text"
          placeholder="Buscar juegos..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="input-gaming max-w-md"
        />
      </div>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {filteredGames.map((game, index) => (
          <motion.div
            key={game.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.05 }}
          >
            <ProductCard {...game} category="juego" />
          </motion.div>
        ))}
      </div>
      {filteredGames.length === 0 && (
        <p className="py-12 text-center font-bold text-gray-500">No se encontraron juegos</p>
      )}
    </PageShell>
  )
}
