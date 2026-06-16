export const CATEGORIES = {
  games: 'juego',
  consoles: 'consola',
  accessories: 'accesorio',
}

export const API_ENDPOINTS = {
  games: '/games',
  consoles: '/consoles',
  accessories: '/accessories',
  repairs: '/repairs',
  contact: '/contact',
  health: '/health',
}

export const WHATSAPP_PHONE = '34900123456'
export const WHATSAPP_MESSAGE = 'Hola, me interesa información sobre Gaming Store.'
export const WHATSAPP_URL = `https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(WHATSAPP_MESSAGE)}`

export function formatPrice(amount) {
  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount)
}

export function getWhatsAppUrl(message = WHATSAPP_MESSAGE) {
  return `https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(message)}`
}
