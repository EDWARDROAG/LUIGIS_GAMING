import { motion } from 'framer-motion'
import { ArrowRight, Gamepad2 } from 'lucide-react'
import { Link } from 'react-router-dom'

export default function Hero() {
  return (
    <section className="relative min-h-[90vh] flex items-center overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-r from-gaming-dark via-gaming-secondary to-gaming-dark" />
      <div className="absolute inset-0 overflow-hidden">
        <motion.div
          animate={{ y: [0, -20, 0] }}
          transition={{ duration: 4, repeat: Infinity }}
          className="absolute top-20 right-20 text-purple-500/10"
        >
          <Gamepad2 className="w-64 h-64" />
        </motion.div>
        <motion.div
          animate={{ y: [0, 20, 0] }}
          transition={{ duration: 5, repeat: Infinity }}
          className="absolute bottom-20 left-20 text-purple-500/10"
        >
          <Gamepad2 className="w-96 h-96" />
        </motion.div>
      </div>
      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-3xl">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
            <span className="inline-block px-4 py-2 bg-purple-500/20 rounded-full text-purple-400 text-sm font-semibold mb-6">
              Bienvenido a Gaming Store
            </span>
          </motion.div>
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="text-5xl md:text-7xl font-gaming font-bold leading-tight"
          >
            <span className="bg-gradient-to-r from-purple-400 via-purple-500 to-purple-600 bg-clip-text text-transparent">
              Level Up
            </span>
            <br />
            <span className="text-white">Tu Experiencia</span>
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl text-gray-300 mt-6"
          >
            Encuentra los mejores videojuegos, consolas y accesorios.
            Servicio técnico especializado y atención personalizada.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.3 }}
            className="flex flex-wrap gap-4 mt-8"
          >
            <Link
              to="/juegos"
              className="group px-8 py-4 bg-purple-600 hover:bg-purple-700 rounded-lg font-semibold transition-all flex items-center gap-2"
            >
              Ver Catálogo
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </Link>
            <Link
              to="/reparacion"
              className="px-8 py-4 border border-purple-500/50 hover:bg-purple-500/10 rounded-lg font-semibold transition-all"
            >
              Reparación
            </Link>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="grid grid-cols-3 gap-8 mt-12 max-w-xl"
          >
            {[
              { label: 'Juegos', value: '500+' },
              { label: 'Consolas', value: '50+' },
              { label: 'Clientes', value: '1000+' },
            ].map((stat) => (
              <div key={stat.label}>
                <div className="text-2xl font-gaming text-purple-400">{stat.value}</div>
                <div className="text-sm text-gray-400">{stat.label}</div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  )
}
