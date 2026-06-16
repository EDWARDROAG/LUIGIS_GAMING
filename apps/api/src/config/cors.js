import cors from 'cors'

const localhostPattern = /^http:\/\/localhost(:\d+)?$/

function isAllowedOrigin(origin) {
  if (!origin) return true

  if (localhostPattern.test(origin)) return true

  if (process.env.FRONTEND_URL && origin === process.env.FRONTEND_URL) {
    return true
  }

  if (/^https:\/\/[\w-]+\.github\.io$/.test(origin)) {
    return true
  }

  return false
}

export const corsOptions = {
  origin(origin, callback) {
    callback(null, isAllowedOrigin(origin))
  },
}
