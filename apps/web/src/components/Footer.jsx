import { Link } from 'react-router-dom'
import PillButton from './PillButton'
import WaveDivider from './WaveDivider'

export default function Footer() {
  return (
    <footer>
      <section className="bg-black">
        <WaveDivider className="relative -top-4" />

        <div className="container mx-auto w-11/12 max-w-4xl py-10 text-center md:w-2/3">
          <div className="pb-5">
            <PillButton to="/contacto" showArrow>
              Atención al cliente
            </PillButton>
          </div>

          <div className="text-white">
            <p className="py-2 text-sm text-gray-300">
              Gaming Store — venta de videojuegos, consolas, accesorios y servicio técnico especializado.
            </p>
            <p className="py-2 text-sm text-gray-400">
              Los precios y disponibilidad pueden variar. Consulta en tienda o por contacto directo.
            </p>
            <p className="py-2 text-sm text-gray-400">
              Reparaciones con garantía. Piezas originales y compatibles según disponibilidad.
            </p>
            <p className="py-4 text-sm text-gray-500">
              &copy; {new Date().getFullYear()} Gaming Store. Todos los derechos reservados.
            </p>
            <div className="flex flex-wrap justify-center gap-4 text-sm">
              <Link to="/juegos" className="text-gray-400 hover:text-gaming-accent">
                Juegos
              </Link>
              <Link to="/consolas" className="text-gray-400 hover:text-gaming-accent">
                Consolas
              </Link>
              <Link to="/reparacion" className="text-gray-400 hover:text-gaming-accent">
                Reparación
              </Link>
              <Link to="/contacto" className="text-gray-400 hover:text-gaming-accent">
                Contacto
              </Link>
            </div>
          </div>
        </div>
      </section>
    </footer>
  )
}
