import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

export default function CategoryCard({ title, icon: Icon, description, link, color }) {
  return (
    <Link to={link}>
      <motion.div whileHover={{ scale: 1.05 }} className="bg-card-gradient rounded-xl p-6 text-center hover:shadow-xl hover:shadow-purple-500/10 transition-all">
        <div className={`w-16 h-16 mx-auto rounded-full bg-${color}-500/20 flex items-center justify-center mb-4`}>
          <Icon className={`w-8 h-8 text-${color}-400`} />
        </div>
        <h3 className="text-lg font-bold text-white mb-2">{title}</h3>
        <p className="text-sm text-gray-400">{description}</p>
      </motion.div>
    </Link>
  )
}
