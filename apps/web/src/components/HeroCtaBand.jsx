import { Link } from 'react-router-dom'
import WaveDivider from './WaveDivider'

export default function HeroCtaBand() {
  return (
    <section>
      <WaveDivider className="relative -top-2" />
      <div className="flex flex-col items-center justify-center gap-3 bg-wave-dots p-4 text-center md:flex-row">
        <Link
          to="/juegos"
          className="inline-block rounded-3xl border-8 border-transparent bg-black px-12 py-3 text-xl font-bold text-white transition duration-200 hover:border-gray-200 hover:bg-white hover:text-black md:px-16 md:text-2xl"
        >
          Ver Catálogo
        </Link>
        <Link
          to="/reparacion"
          className="inline-block rounded-3xl border-8 border-transparent bg-red-500 px-12 py-3 text-xl font-bold text-white transition duration-200 hover:border-gray-200 hover:bg-white hover:text-black md:px-16 md:text-2xl"
        >
          Aprende a Reparar
        </Link>
      </div>
      <WaveDivider className="relative top-2" />
    </section>
  )
}
