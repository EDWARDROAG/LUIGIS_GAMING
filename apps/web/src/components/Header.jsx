import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Menu, X } from 'lucide-react'
import { assetUrl } from '../utils/assets.js'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Inicio' },
    { path: '/juegos', label: 'Juegos' },
    { path: '/consolas', label: 'Consolas' },
    { path: '/accesorios', label: 'Explorar' },
  ]

  const linkClass = (path) =>
    `link block px-5 py-4 font-bold transition-colors hover:text-gaming-accent ${
      location.pathname === path ? 'text-gaming-accent' : 'text-white'
    }`

  return (
    <nav className="flex items-center justify-between bg-gray-800 lg:justify-start">
      <div className="logo w-1/6 flex-initial p-2">
        <Link to="/">
          <img src={assetUrl('/assets/img/logo.png')} width="100" alt="Gaming Store" className="h-auto" />
        </Link>
      </div>

      <div className="links hidden w-4/6 md:w-4/6 lg:block">
        <ul className="menu flex items-center justify-center gap-2 md:gap-5">
          {navItems.map((item) => (
            <li key={item.path}>
              <Link to={item.path} className={linkClass(item.path)}>
                {item.label}
              </Link>
            </li>
          ))}
          <li>
            <Link
              to="/reparacion"
              className="inline-block rounded-full border-4 border-gaming-accent p-2 align-middle font-bold text-white transition duration-500 hover:bg-white hover:text-black"
            >
              Reparación
            </Link>
          </li>
          <li>
            <Link
              to="/juegos"
              className="rounded-full bg-red-500 px-4 py-3 font-bold text-white transition duration-500 hover:bg-white hover:text-black"
            >
              Comprar
            </Link>
          </li>
        </ul>
      </div>

      <div className="block w-1/6 lg:hidden">
        <button
          type="button"
          onClick={() => setIsOpen(!isOpen)}
          className="link px-5 py-4 font-bold text-white"
        >
          {isOpen ? <X className="mx-auto h-6 w-6" /> : <Menu className="mx-auto h-6 w-6" />}
        </button>

        <ul
          className={`mobile-links absolute left-0 z-50 w-full bg-gray-800 text-center ${
            isOpen ? 'block' : 'hidden'
          }`}
        >
          {navItems.map((item) => (
            <li key={item.path}>
              <Link to={item.path} onClick={() => setIsOpen(false)} className={linkClass(item.path)}>
                {item.label}
              </Link>
            </li>
          ))}
          <li>
            <Link
              to="/reparacion"
              onClick={() => setIsOpen(false)}
              className="my-4 inline-block rounded-full border-4 border-gaming-accent p-2 font-bold text-white transition duration-500 hover:bg-white hover:text-black"
            >
              Reparación
            </Link>
          </li>
          <li>
            <Link
              to="/juegos"
              onClick={() => setIsOpen(false)}
              className="my-4 inline-block rounded-full bg-red-500 px-4 py-3 font-bold text-white transition duration-500 hover:bg-white hover:text-black"
            >
              Comprar
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  )
}
