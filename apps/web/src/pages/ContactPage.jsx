import { motion } from 'framer-motion'
import { MapPin, Phone, Mail, Clock } from 'lucide-react'
import PageShell from '../components/PageShell'
import ContactForm from '../components/ContactForm'
import PillButton from '../components/PillButton'
import { WHATSAPP_URL } from '../utils/constants'

export default function ContactPage() {
  return (
    <PageShell title="Contáctanos" subtitle="Estamos aquí para ayudarte">
      <div className="mb-8 text-center">
        <PillButton href={WHATSAPP_URL} showArrow>
          Escríbenos por WhatsApp
        </PillButton>
      </div>
      <div className="grid grid-cols-1 gap-10 lg:grid-cols-2">
        <div>
          <ContactForm />
        </div>
        <div className="space-y-6">
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="rounded-2xl border-4 border-gray-100 bg-gray-50 p-6"
          >
            <h3 className="mb-4 text-xl font-black text-gray-900">Información de Contacto</h3>
            <div className="space-y-4">
              <div className="flex items-start gap-3">
                <MapPin className="mt-1 h-5 w-5 text-red-500" />
                <div>
                  <p className="font-bold text-gray-900">Dirección</p>
                  <p className="text-gray-600">Calle Gamer 123, 28001 Madrid</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Phone className="mt-1 h-5 w-5 text-red-500" />
                <div>
                  <p className="font-bold text-gray-900">Teléfono / WhatsApp</p>
                  <p className="text-gray-600">+34 900 123 456</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Mail className="mt-1 h-5 w-5 text-red-500" />
                <div>
                  <p className="font-bold text-gray-900">Email</p>
                  <p className="text-gray-600">info@gamingstore.com</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Clock className="mt-1 h-5 w-5 text-red-500" />
                <div>
                  <p className="font-bold text-gray-900">Horario</p>
                  <p className="text-gray-600">Lunes a Sábado: 10:00 - 21:00</p>
                  <p className="text-gray-600">Domingo: 11:00 - 15:00</p>
                </div>
              </div>
            </div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="rounded-2xl border-4 border-gray-100 bg-gray-50 p-6"
          >
            <h3 className="mb-4 text-xl font-black text-gray-900">¿Por qué elegirnos?</h3>
            <ul className="space-y-2 font-semibold text-gray-600">
              <li>Equipo de expertos en gaming</li>
              <li>Atención personalizada</li>
              <li>Garantía en todos los servicios</li>
              <li>Precios competitivos</li>
              <li>Respuesta rápida por WhatsApp</li>
            </ul>
          </motion.div>
        </div>
      </div>
    </PageShell>
  )
}
