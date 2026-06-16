import { motion } from 'framer-motion'
import { Wrench, Gamepad, Cpu, Clock, Shield, Award } from 'lucide-react'
import { Link } from 'react-router-dom'
import SectionTitle from './SectionTitle'

const services = [
  { icon: Wrench, title: 'Reparación de Consolas', description: 'Diagnóstico y reparación de PlayStation, Xbox, Nintendo y más.', price: 'Desde 49€' },
  { icon: Gamepad, title: 'Reparación de Controles', description: 'Joystick drift, botones atascados, conexión y más.', price: 'Desde 29€' },
  { icon: Cpu, title: 'Mantenimiento Preventivo', description: 'Limpieza profunda, cambio de pasta térmica y optimización.', price: 'Desde 39€' },
  { icon: Clock, title: 'Servicio Express', description: 'Reparaciones urgentes en 24-48 horas.', price: 'Desde 59€' },
  { icon: Shield, title: 'Garantía', description: 'Todos nuestros trabajos tienen 3 meses de garantía.', price: 'Incluido' },
  { icon: Award, title: 'Certificados', description: 'Técnicos certificados y piezas originales.', price: 'Calidad' },
]

export default function RepairServices() {
  return (
    <section className="py-12 md:py-16">
      <div className="container mx-auto px-4">
        <SectionTitle title="Servicios de Reparación" subtitle="Expertos en reparación de consolas y controles" />
        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {services.map((service, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
              className="rounded-2xl bg-white p-6 shadow-lg transition hover:shadow-xl"
            >
              <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-red-500/15">
                <service.icon className="h-6 w-6 text-red-500" />
              </div>
              <h3 className="mb-2 text-lg font-black text-gray-900">{service.title}</h3>
              <p className="mb-3 text-sm text-gray-600">{service.description}</p>
              <span className="font-black text-red-500">{service.price}</span>
            </motion.div>
          ))}
        </div>
        <div className="mt-8 text-center">
          <Link
            to="/reparacion"
            className="inline-block rounded-3xl border-8 border-transparent bg-red-500 px-10 py-2 font-black text-white transition hover:border-gray-200 hover:bg-white hover:text-black"
          >
            Ver todos los servicios
          </Link>
        </div>
      </div>
    </section>
  )
}
