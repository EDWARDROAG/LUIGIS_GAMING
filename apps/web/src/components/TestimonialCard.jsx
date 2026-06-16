import { motion } from 'framer-motion'
import { Star } from 'lucide-react'

export default function TestimonialCard({ name, role, content, rating, image }) {
  return (
    <motion.div whileHover={{ y: -5 }} className="bg-card-gradient rounded-xl p-6 hover:shadow-xl hover:shadow-purple-500/10 transition-all">
      <div className="flex items-center gap-4 mb-4">
        <img src={image || 'https://ui-avatars.com/api/?name=' + name} alt={name} className="w-12 h-12 rounded-full" />
        <div>
          <h4 className="font-bold text-white">{name}</h4>
          <p className="text-sm text-gray-400">{role}</p>
        </div>
      </div>
      <div className="flex gap-1 mb-3">
        {[...Array(5)].map((_, i) => (
          <Star key={i} className={`w-4 h-4 ${i < rating ? 'fill-yellow-400 text-yellow-400' : 'text-gray-600'}`} />
        ))}
      </div>
      <p className="text-gray-300 text-sm">{content}</p>
    </motion.div>
  )
}
