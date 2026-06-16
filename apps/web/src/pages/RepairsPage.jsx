import { motion } from 'framer-motion'
import { Wrench, Gamepad, Cpu, Clock, Shield, Award, CheckCircle } from 'lucide-react'
import PageShell from '../components/PageShell'
import PillButton from '../components/PillButton'
import { WHATSAPP_URL } from '../utils/constants'

const services = [
  { icon: Wrench, title: 'Reparación de Consolas', description: 'Diagnóstico completo y reparación de PlayStation, Xbox, Nintendo Switch y más.', features: ['Diagnóstico gratuito', 'Piezas originales', 'Garantía de 3 meses'] },
  { icon: Gamepad, title: 'Reparación de Controles', description: 'Arreglo de joystick drift, botones atascados, problemas de conexión y más.', features: ['Reparación rápida', 'Piezas de calidad', 'Garantía de 2 meses'] },
  { icon: Cpu, title: 'Mantenimiento Preventivo', description: 'Limpieza profunda, cambio de pasta térmica y optimización de rendimiento.', features: ['Limpieza profesional', 'Optimización', 'Prevención de fallos'] },
  { icon: Clock, title: 'Servicio Express', description: 'Reparaciones urgentes con prioridad máxima, listas en 24-48 horas.', features: ['Prioridad máxima', 'Entrega rápida', 'Seguimiento en tiempo real'] },
  { icon: Shield, title: 'Garantía Extendida', description: 'Todos nuestros trabajos incluyen garantía y soporte post-reparación.', features: ['3 meses de garantía', 'Soporte técnico', 'Revisiones gratuitas'] },
  { icon: Award, title: 'Técnicos Certificados', description: 'Equipo profesional con años de experiencia en reparación gaming.', features: ['Certificados oficiales', 'Experiencia comprobada', 'Calidad garantizada'] },
]

export default function RepairsPage() {
  return (
    <PageShell title="Servicios de Reparación" subtitle="Expertos en reparación de consolas y controles">
      <div className="mb-8 text-center">
        <PillButton href={WHATSAPP_URL} showArrow>
          Cotizar por WhatsApp
        </PillButton>
      </div>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        {services.map((service, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
            className="rounded-2xl border-4 border-gray-100 bg-gray-50 p-6 shadow-md transition hover:shadow-lg"
          >
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-red-500/15">
              <service.icon className="h-6 w-6 text-red-500" />
            </div>
            <h3 className="mb-2 text-xl font-black text-gray-900">{service.title}</h3>
            <p className="mb-4 text-sm text-gray-600">{service.description}</p>
            <ul className="space-y-2">
              {service.features.map((feature, i) => (
                <li key={i} className="flex items-center gap-2 text-sm font-semibold text-gray-700">
                  <CheckCircle className="h-4 w-4 text-red-500" />
                  {feature}
                </li>
              ))}
            </ul>
          </motion.div>
        ))}
      </div>
    </PageShell>
  )
}
