import { motion } from 'framer-motion'

export default function SectionTitle({ title, subtitle }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      viewport={{ once: true }}
      className="mb-10 text-center"
    >
      <h2 className="text-3xl font-black text-white md:text-4xl">{title}</h2>
      {subtitle && <p className="mt-2 text-lg font-bold text-white/85">{subtitle}</p>}
    </motion.div>
  )
}
