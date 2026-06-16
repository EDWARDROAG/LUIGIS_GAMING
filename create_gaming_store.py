import os
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

REQUIRED_SECTIONS = ("root", "frontend", "backend", "docs")


def classify_file(filepath):
    """Clasifica un archivo por sección del monorepo."""
    if filepath.startswith("apps/web/"):
        return "frontend"
    if filepath.startswith("apps/api/"):
        return "backend"
    if filepath.startswith("docs/"):
        return "docs"
    return "root"


def derive_directories(filepaths):
    """Obtiene todas las carpetas necesarias a partir de las rutas de archivos."""
    directories = set()
    for filepath in filepaths:
        normalized = filepath.replace("\\", "/")
        folder = os.path.dirname(normalized)
        if not folder:
            continue
        parts = folder.split("/")
        for index in range(1, len(parts) + 1):
            directories.add("/".join(parts[:index]))
    return sorted(directories)


def validate_structure(structure):
    """Verifica que el diccionario incluya las cuatro secciones del monorepo."""
    sections = {classify_file(path) for path in structure}
    missing = [section for section in REQUIRED_SECTIONS if section not in sections]
    if missing:
        raise ValueError(f"Estructura incompleta. Faltan secciones: {', '.join(missing)}")


def create_gaming_store(output_dir=None):
    """Genera la estructura completa del proyecto Gaming Store (raíz, frontend, backend y docs)."""
    if output_dir is None:
        output_dir = SCRIPT_DIR
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    structure = get_project_structure()
    validate_structure(structure)
    directories = derive_directories(structure.keys())

    section_labels = {
        "root": "Raiz",
        "frontend": "Frontend (apps/web)",
        "backend": "Backend (apps/api)",
        "docs": "Documentacion (docs)",
    }
    section_counts = {key: 0 for key in section_labels}
    created_files = []
    errors = []

    print(f"\nGenerando proyecto en: {output_dir}")
    print(f"Archivos a crear: {len(structure)}")
    print(f"Carpetas a crear: {len(directories)}\n")

    for folder in directories:
        folder_path = os.path.join(output_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"[OK] Carpeta: {folder}")

    for filepath, content in structure.items():
        full_path = os.path.join(output_dir, filepath)
        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(content)
            section = classify_file(filepath)
            section_counts[section] += 1
            created_files.append(filepath)
            print(f"[OK] [{section_labels[section]}] {filepath}")
        except OSError as error:
            errors.append((filepath, str(error)))
            print(f"[ERROR] {filepath}: {error}")

    if errors:
        print(f"\n[AVISO] {len(errors)} archivo(s) no se pudieron crear.")
        for filepath, message in errors:
            print(f"   - {filepath}: {message}")

    if len(created_files) != len(structure):
        raise RuntimeError(
            f"Solo se crearon {len(created_files)} de {len(structure)} archivos esperados."
        )

    print("\n[OK] Estructura completa generada con exito.")
    print("\nResumen:")
    for section, label in section_labels.items():
        print(f"   - {label}: {section_counts[section]} archivos")
    print(f"   - Total: {sum(section_counts.values())} archivos")

    print("\nPara iniciar el proyecto:")
    print(f"   cd \"{output_dir}\"")
    print("   npm install")
    print("   npm run dev          # Frontend + Backend en paralelo")
    print("   npm run dev:web      # Solo frontend en http://localhost:5172")
    print("   npm run dev:api      # Solo backend en http://localhost:3000")
    print("\nConfiguracion:")
    print("   cp apps/api/.env.example apps/api/.env")
    print("   # Edita apps/api/.env con tus credenciales")


def get_project_structure():
    """Devuelve el mapa completo de archivos del monorepo."""
    return {
        # ========== ARCHIVOS RAIZ ==========
        "README.md": """# 🎮 Gaming Store

## Tienda de Videojuegos, Consolas y Reparación

### 🚀 Tecnologías
- **Frontend:** React + Vite + TailwindCSS
- **Backend:** Node.js + Express
- **Monorepo:** npm workspaces

### 🛠️ Instalación
```bash
npm install
cd apps/web && npm run dev
cd apps/api && npm run dev
```
""",
        ".env": """TIPO_NEGOCIO=gaming
""",
        ".env.example": """TIPO_NEGOCIO=gaming
""",
        ".gitignore": """node_modules/
dist/
.env
.env.local
.DS_Store
*.log
coverage/
.vscode/
.idea/
""",
        "package.json": """{
"name": "gaming-store-monorepo",
"private": true,
"version": "1.0.0",
"workspaces": ["apps/*"],
"scripts": {
"dev": "npm run dev --workspaces --parallel",
"dev:web": "npm run dev --workspace=gaming-store-web",
"dev:api": "npm run dev --workspace=gaming-store-api",
"build": "npm run build --workspaces",
"build:web": "npm run build --workspace=gaming-store-web",
"preview": "npm run preview --workspace=gaming-store-web"
}
}
""",
        # ========== FRONTEND - APPS/WEB ==========
        "apps/web/package.json": """{
"name": "gaming-store-web",
"private": true,
"version": "1.0.0",
"type": "module",
"scripts": {
"dev": "vite",
"build": "vite build",
"preview": "vite preview"
},
"dependencies": {
"react": "^18.2.0",
"react-dom": "^18.2.0",
"react-router-dom": "^6.16.0",
"framer-motion": "^10.16.4",
"react-hook-form": "^7.47.0",
"zod": "^3.22.4",
"sonner": "^1.0.0",
"axios": "^1.6.0",
"react-icons": "^4.11.0",
"lucide-react": "^0.294.0",
"@hookform/resolvers": "^3.3.2",
"@tanstack/react-query": "^5.8.4"
},
"devDependencies": {
"@types/react": "^18.2.37",
"@types/react-dom": "^18.2.15",
"@vitejs/plugin-react": "^4.2.0",
"autoprefixer": "^10.4.16",
"postcss": "^8.4.31",
"tailwindcss": "^3.3.2",
"vite": "^5.0.0"
}
}
""",
        "apps/web/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
plugins: [react()],
server: {
port: 5172,
proxy: {
'/api': {
target: 'http://localhost:3000',
changeOrigin: true
}
}
}
})
""",
        "apps/web/tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
theme: {
extend: {
colors: {
gaming: {
primary: '#7C3AED',
secondary: '#1E1B4B',
accent: '#F59E0B',
dark: '#0F0A1A',
card: '#1A1430',
text: '#E2E8F0',
'text-light': '#94A3B8',
}
},
fontFamily: {
'gaming': ['"Orbitron"', 'sans-serif'],
},
animation: {
'glow': 'glow 2s ease-in-out infinite alternate',
'float': 'float 3s ease-in-out infinite',
},
keyframes: {
glow: {
'0%': { textShadow: '0 0 10px #7C3AED, 0 0 20px #7C3AED' },
'100%': { textShadow: '0 0 20px #A78BFA, 0 0 40px #7C3AED, 0 0 60px #7C3AED' },
},
float: {
'0%, 100%': { transform: 'translateY(0px)' },
'50%': { transform: 'translateY(-10px)' },
},
},
},
},
plugins: [],
}
""",
        "apps/web/postcss.config.js": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
        "apps/web/.gitignore": """node_modules
dist
.env.local
.DS_Store
*.log
""",
        "apps/web/index.html": """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Gaming Store</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",
        # ========== SRC FRONTEND ==========
        "apps/web/src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from './App.jsx'
import './index.css'

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')).render(
<React.StrictMode>
<QueryClientProvider client={queryClient}>
<App />
</QueryClientProvider>
</React.StrictMode>
)
""",
        "apps/web/src/App.jsx": """import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Toaster } from 'sonner'
import Layout from './components/Layout'
import HomePage from './pages/HomePage'
import GamesPage from './pages/GamesPage'
import ConsolesPage from './pages/ConsolesPage'
import RepairsPage from './pages/RepairsPage'
import AccessoriesPage from './pages/AccessoriesPage'
import ContactPage from './pages/ContactPage'
import ProductDetailPage from './pages/ProductDetailPage'

function App() {
return (
<Router>
<Toaster position="top-right" richColors />
<Routes>
<Route path="/" element={<Layout />}>
<Route index element={<HomePage />} />
<Route path="/juegos" element={<GamesPage />} />
<Route path="/consolas" element={<ConsolesPage />} />
<Route path="/reparacion" element={<RepairsPage />} />
<Route path="/accesorios" element={<AccessoriesPage />} />
<Route path="/contacto" element={<ContactPage />} />
<Route path="/producto/:id" element={<ProductDetailPage />} />
</Route>
</Routes>
</Router>
)
}

export default App
""",
        "apps/web/src/index.css": """:root {
--color-gaming-primary: #7C3AED;
--color-gaming-secondary: #1E1B4B;
--color-gaming-accent: #F59E0B;
--color-gaming-dark: #0F0A1A;
--color-gaming-card: #1A1430;
--color-gaming-text: #E2E8F0;
--color-gaming-text-light: #94A3B8;
}

@tailwind base;
@tailwind components;
@tailwind utilities;

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
font-family: 'Inter', system-ui, -apple-system, sans-serif;
background-color: var(--color-gaming-dark);
color: var(--color-gaming-text);
}

::-webkit-scrollbar {
width: 8px;
}

::-webkit-scrollbar-track {
background: var(--color-gaming-dark);
}

::-webkit-scrollbar-thumb {
background: var(--color-gaming-primary);
border-radius: 4px;
}

@layer utilities {
.text-glow {
text-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
}
.bg-gaming-gradient {
background: linear-gradient(135deg, #1E1B4B 0%, #0F0A1A 100%);
}
.bg-card-gradient {
background: linear-gradient(145deg, #1A1430, #2A1F45);
}
}
""",
        # ========== COMPONENTES ==========
        "apps/web/src/components/Layout.jsx": """import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'

export default function Layout() {
  return (
    <div className="min-h-screen bg-gaming-gradient">
      <Header />
      <main className="pt-16">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}
""",
        "apps/web/src/components/Header.jsx": """import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Menu, X, ShoppingCart, Search, Gamepad2 } from 'lucide-react'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Inicio' },
    { path: '/juegos', label: 'Juegos' },
    { path: '/consolas', label: 'Consolas' },
    { path: '/reparacion', label: 'Reparación' },
    { path: '/accesorios', label: 'Accesorios' },
    { path: '/contacto', label: 'Contacto' },
  ]

  return (
    <header className="fixed top-0 w-full bg-gaming-secondary/90 backdrop-blur-lg border-b border-purple-500/20 z-50">
      <nav className="container mx-auto px-4 py-3">
        <div className="flex justify-between items-center">
          <Link to="/" className="flex items-center gap-2">
            <Gamepad2 className="w-8 h-8 text-purple-400" />
            <span className="text-2xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
              GAMING
            </span>
          </Link>
          <div className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                className={`text-sm font-medium transition-colors hover:text-purple-400 ${
                  location.pathname === item.path ? 'text-purple-400' : 'text-gray-300'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>
          <div className="hidden md:flex items-center gap-4">
            <button className="p-2 hover:bg-purple-500/20 rounded-lg transition-colors">
              <Search className="w-5 h-5 text-gray-300" />
            </button>
            <button className="p-2 hover:bg-purple-500/20 rounded-lg transition-colors relative">
              <ShoppingCart className="w-5 h-5 text-gray-300" />
              <span className="absolute -top-1 -right-1 bg-purple-500 text-white text-xs w-5 h-5 rounded-full flex items-center justify-center">
                0
              </span>
            </button>
          </div>
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 hover:bg-purple-500/20 rounded-lg transition-colors"
          >
            {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
        <motion.div
          initial={{ height: 0, opacity: 0 }}
          animate={{ height: isOpen ? 'auto' : 0, opacity: isOpen ? 1 : 0 }}
          className="md:hidden overflow-hidden"
        >
          <div className="py-4 space-y-2">
            {navItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                onClick={() => setIsOpen(false)}
                className={`block px-4 py-2 rounded-lg transition-colors ${
                  location.pathname === item.path
                    ? 'bg-purple-500/20 text-purple-400'
                    : 'hover:bg-purple-500/10 text-gray-300'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>
        </motion.div>
      </nav>
    </header>
  )
}
""",
        "apps/web/src/components/Footer.jsx": """import { Link } from 'react-router-dom'
import { Gamepad2, Instagram, Twitter, Youtube, Facebook } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="bg-gaming-secondary border-t border-purple-500/20">
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <Link to="/" className="flex items-center gap-2 mb-4">
              <Gamepad2 className="w-8 h-8 text-purple-400" />
              <span className="text-xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
                GAMING
              </span>
            </Link>
            <p className="text-gray-400 text-sm">
              Tu tienda de confianza para videojuegos, consolas y reparación especializada.
            </p>
          </div>
          <div>
            <h3 className="font-bold mb-4 text-purple-400">Enlaces</h3>
            <ul className="space-y-2 text-sm text-gray-400">
              <li><Link to="/juegos" className="hover:text-purple-400 transition-colors">Videojuegos</Link></li>
              <li><Link to="/consolas" className="hover:text-purple-400 transition-colors">Consolas</Link></li>
              <li><Link to="/reparacion" className="hover:text-purple-400 transition-colors">Reparación</Link></li>
              <li><Link to="/accesorios" className="hover:text-purple-400 transition-colors">Accesorios</Link></li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold mb-4 text-purple-400">Contacto</h3>
            <ul className="space-y-2 text-sm text-gray-400">
              <li>+34 900 123 456</li>
              <li>info@gamingstore.com</li>
              <li>Calle Gamer 123, Madrid</li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold mb-4 text-purple-400">Redes Sociales</h3>
            <div className="flex gap-4">
              <a href="#" className="p-2 bg-purple-500/10 rounded-lg hover:bg-purple-500/20 transition-colors">
                <Instagram className="w-5 h-5" />
              </a>
              <a href="#" className="p-2 bg-purple-500/10 rounded-lg hover:bg-purple-500/20 transition-colors">
                <Twitter className="w-5 h-5" />
              </a>
              <a href="#" className="p-2 bg-purple-500/10 rounded-lg hover:bg-purple-500/20 transition-colors">
                <Youtube className="w-5 h-5" />
              </a>
              <a href="#" className="p-2 bg-purple-500/10 rounded-lg hover:bg-purple-500/20 transition-colors">
                <Facebook className="w-5 h-5" />
              </a>
            </div>
          </div>
        </div>
        <div className="border-t border-purple-500/20 mt-8 pt-8 text-center text-sm text-gray-500">
          <p>&copy; 2024 Gaming Store. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  )
}
""",
        "apps/web/src/components/Hero.jsx": """import { motion } from 'framer-motion'
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
""",
        "apps/web/src/components/FeaturedGames.jsx": """import { motion } from 'framer-motion'
import ProductCard from './ProductCard'

const games = [
  { id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 2, title: 'EA Sports FC 24', price: 69.99, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.7 },
  { id: 3, title: 'Call of Duty: Modern Warfare', price: 49.99, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.8 },
]

export default function FeaturedGames() {
  return (
    <section className="py-16">
      <div className="container mx-auto px-4">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
            Videojuegos Destacados
          </h2>
          <p className="text-gray-400 mt-2">Los títulos más populares del momento</p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {games.map((game, index) => (
            <motion.div key={game.id} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
              <ProductCard {...game} category="juego" />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
""",
        "apps/web/src/components/FeaturedConsoles.jsx": """import { motion } from 'framer-motion'
import ProductCard from './ProductCard'

const consoles = [
  { id: 4, title: 'PlayStation 5', price: 499.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.9 },
  { id: 5, title: 'Xbox Series X', price: 499.99, image: 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400', platform: 'Microsoft', rating: 4.8 },
  { id: 6, title: 'Nintendo Switch OLED', price: 349.99, image: 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400', platform: 'Nintendo', rating: 4.7 },
]

export default function FeaturedConsoles() {
  return (
    <section className="py-16 bg-gaming-secondary/50">
      <div className="container mx-auto px-4">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
            Consolas Destacadas
          </h2>
          <p className="text-gray-400 mt-2">La mejor experiencia gaming</p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {consoles.map((item, index) => (
            <motion.div key={item.id} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
              <ProductCard {...item} category="consola" />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
""",
        "apps/web/src/components/RepairServices.jsx": """import { motion } from 'framer-motion'
import { Wrench, Gamepad, Cpu, Clock, Shield, Award } from 'lucide-react'

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
    <section className="py-16">
      <div className="container mx-auto px-4">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
            Servicios de Reparación
          </h2>
          <p className="text-gray-400 mt-2">Expertos en reparación de consolas y controles</p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {services.map((service, index) => (
            <motion.div key={index} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }} className="bg-card-gradient rounded-xl p-6 hover:shadow-xl hover:shadow-purple-500/10 transition-all">
              <div className="w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center mb-4">
                <service.icon className="w-6 h-6 text-purple-400" />
              </div>
              <h3 className="text-lg font-bold text-white mb-2">{service.title}</h3>
              <p className="text-gray-400 text-sm mb-3">{service.description}</p>
              <span className="text-purple-400 font-semibold">{service.price}</span>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
""",
        "apps/web/src/components/AccessoryGrid.jsx": """import { motion } from 'framer-motion'
import ProductCard from './ProductCard'

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8 },
  { id: 8, title: 'Xbox Wireless Controller', price: 59.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Xbox Series X', rating: 4.7 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Nintendo Switch', rating: 4.6 },
  { id: 10, title: 'Auriculares Gaming', price: 89.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'Universal', rating: 4.5 },
]

export default function AccessoryGrid() {
  return (
    <section className="py-16 bg-gaming-secondary/50">
      <div className="container mx-auto px-4">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
            Accesorios
          </h2>
          <p className="text-gray-400 mt-2">Todo lo que necesitas para tu setup</p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {accessories.map((accessory, index) => (
            <motion.div key={accessory.id} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
              <ProductCard {...accessory} category="accesorio" />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
""",
        "apps/web/src/components/ProductCard.jsx": """import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ShoppingCart, Star } from 'lucide-react'
import { toast } from 'sonner'

export default function ProductCard({ id, title, price, image, platform, rating, category }) {
  const addToCart = (e) => {
    e.preventDefault()
    toast.success(`¡${title} añadido al carrito!`)
  }

  return (
    <Link to={`/producto/${id}`}>
      <motion.div whileHover={{ y: -5 }} className="bg-card-gradient rounded-xl overflow-hidden hover:shadow-xl hover:shadow-purple-500/10 transition-all">
        <div className="relative overflow-hidden aspect-square">
          <img src={image} alt={title} className="w-full h-full object-cover hover:scale-105 transition-transform duration-300" />
          <span className="absolute top-2 right-2 px-3 py-1 bg-purple-600 text-white text-xs font-semibold rounded-full">
            {category}
          </span>
        </div>
        <div className="p-4">
          <div className="flex justify-between items-start mb-2">
            <h3 className="font-bold text-white line-clamp-1">{title}</h3>
            <span className="text-purple-400 font-bold">${price}</span>
          </div>
          <div className="flex items-center gap-2 mb-3">
            <div className="flex items-center gap-1">
              <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
              <span className="text-sm text-gray-300">{rating}</span>
            </div>
            <span className="text-xs text-gray-500">{platform}</span>
          </div>
          <button
            onClick={addToCart}
            className="w-full py-2 bg-purple-600 hover:bg-purple-700 rounded-lg text-sm font-semibold transition-colors flex items-center justify-center gap-2"
          >
            <ShoppingCart className="w-4 h-4" /> Añadir al Carrito
          </button>
        </div>
      </motion.div>
    </Link>
  )
}
""",
        "apps/web/src/components/CategoryCard.jsx": """import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

export default function CategoryCard({ title, icon: Icon, description, link, color }) {
  return (
    <Link to={link}>
      <motion.div whileHover={{ scale: 1.05 }} className="bg-card-gradient rounded-xl p-6 text-center hover:shadow-xl hover:shadow-purple-500/10 transition-all">
        <div className={`w-16 h-16 mx-auto rounded-full bg-${color}-500/20 flex items-center justify-center mb-4`}>
          <Icon className={`w-8 h-8 text-${color}-400`} />
        </div>
        <h3 className="text-lg font-bold text-white mb-2">{title}</h3>
        <p className="text-sm text-gray-400">{description}</p>
      </motion.div>
    </Link>
  )
}
""",
        "apps/web/src/components/TestimonialCard.jsx": """import { motion } from 'framer-motion'
import { Star } from 'lucide-react'

export default function TestimonialCard({ name, role, content, rating, image }) {
  return (
    <motion.div whileHover={{ y: -5 }} className="bg-card-gradient rounded-xl p-6 hover:shadow-xl hover:shadow-purple-500/10 transition-all">
      <div className="flex items-center gap-4 mb-4">
        <img src={image || 'https://ui-avatars.com/api/?name=' + name} alt={name} className="w-12 h-12 rounded-full" />
        <div>
          <h4 className="font-bold text-white">{name}</h4>
          <p className="text-sm text-gray-400">{role}</p>
        </div>
      </div>
      <div className="flex gap-1 mb-3">
        {[...Array(5)].map((_, i) => (
          <Star key={i} className={`w-4 h-4 ${i < rating ? 'fill-yellow-400 text-yellow-400' : 'text-gray-600'}`} />
        ))}
      </div>
      <p className="text-gray-300 text-sm">{content}</p>
    </motion.div>
  )
}
""",
        "apps/web/src/components/ContactForm.jsx": """import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { toast } from 'sonner'
import axios from 'axios'

const contactSchema = z.object({
  name: z.string().min(2, 'Nombre muy corto'),
  email: z.string().email('Email inválido'),
  phone: z.string().optional(),
  subject: z.string().min(3, 'Asunto muy corto'),
  message: z.string().min(10, 'Mensaje muy corto'),
})

export default function ContactForm() {
  const { register, handleSubmit, formState: { errors, isSubmitting }, reset } = useForm({
    resolver: zodResolver(contactSchema),
  })

  const onSubmit = async (data) => {
    try {
      await axios.post('/api/contact', data)
      toast.success('Mensaje enviado correctamente')
      reset()
    } catch (error) {
      toast.error('Error al enviar el mensaje')
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-2xl mx-auto">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <input {...register('name')} placeholder="Nombre completo" className="w-full p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white" />
          {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name.message}</p>}
        </div>
        <div>
          <input {...register('email')} placeholder="Email" className="w-full p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white" />
          {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>}
        </div>
      </div>
      <div>
        <input {...register('phone')} placeholder="Teléfono (opcional)" className="w-full p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white" />
      </div>
      <div>
        <input {...register('subject')} placeholder="Asunto" className="w-full p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white" />
        {errors.subject && <p className="text-red-500 text-sm mt-1">{errors.subject.message}</p>}
      </div>
      <div>
        <textarea {...register('message')} placeholder="Mensaje" rows="5" className="w-full p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white resize-none" />
        {errors.message && <p className="text-red-500 text-sm mt-1">{errors.message.message}</p>}
      </div>
      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full py-3 bg-purple-600 hover:bg-purple-700 rounded-lg font-semibold transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isSubmitting ? 'Enviando...' : 'Enviar Mensaje'}
      </button>
    </form>
  )
}
""",
        # ========== PÁGINAS ==========
        "apps/web/src/pages/HomePage.jsx": """import Hero from '../components/Hero'
import FeaturedGames from '../components/FeaturedGames'
import FeaturedConsoles from '../components/FeaturedConsoles'
import RepairServices from '../components/RepairServices'
import AccessoryGrid from '../components/AccessoryGrid'
import TestimonialCard from '../components/TestimonialCard'
import { motion } from 'framer-motion'

const testimonials = [
  { name: 'Carlos Gómez', role: 'Gamer Profesional', content: 'Excelente servicio, repararon mi PS5 en tiempo récord. Totalmente recomendados.', rating: 5 },
  { name: 'María Rodríguez', role: 'Cliente Frecuente', content: 'Los mejores precios en videojuegos y consolas. Siempre encuentran lo que busco.', rating: 5 },
  { name: 'Javier Martínez', role: 'Coleccionista', content: 'Su servicio técnico es impecable. Confío plenamente en ellos para mis consolas.', rating: 4 },
]

export default function HomePage() {
  return (
    <>
      <Hero />
      <FeaturedGames />
      <FeaturedConsoles />
      <RepairServices />
      <AccessoryGrid />
      <section className="py-16">
        <div className="container mx-auto px-4">
          <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">
              Testimonios
            </h2>
            <p className="text-gray-400 mt-2">Lo que nuestros clientes dicen</p>
          </motion.div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {testimonials.map((testimonial, index) => (
              <motion.div key={index} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
                <TestimonialCard {...testimonial} />
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
""",
        "apps/web/src/pages/GamesPage.jsx": """import { useState } from 'react'
import { motion } from 'framer-motion'
import ProductCard from '../components/ProductCard'

const games = [
  { id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 2, title: 'EA Sports FC 24', price: 69.99, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.7 },
  { id: 3, title: 'Call of Duty: Modern Warfare', price: 49.99, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.8 },
  { id: 11, title: 'The Legend of Zelda: Tears', price: 69.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9 },
  { id: 12, title: 'FIFA 24', price: 59.99, image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400', platform: 'PlayStation 5', rating: 4.6 },
  { id: 13, title: 'Halo Infinite', price: 39.99, image: 'https://images.unsplash.com/photo-1542751110-97427bbecf20?w=400', platform: 'Xbox Series X', rating: 4.5 },
]

export default function GamesPage() {
  const [search, setSearch] = useState('')
  const filteredGames = games.filter((game) => game.title.toLowerCase().includes(search.toLowerCase()))

  return (
    <div className="container mx-auto px-4 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">Videojuegos</h1>
        <p className="text-gray-400 mt-2">Todos los títulos disponibles</p>
      </motion.div>
      <div className="mb-8">
        <input
          type="text"
          placeholder="Buscar juegos..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full max-w-md p-3 bg-gaming-secondary/50 border border-purple-500/20 rounded-lg focus:border-purple-500 focus:outline-none transition-colors text-white"
        />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {filteredGames.map((game, index) => (
          <motion.div key={game.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.05 }}>
            <ProductCard {...game} category="juego" />
          </motion.div>
        ))}
      </div>
      {filteredGames.length === 0 && (
        <p className="text-center text-gray-400 py-12">No se encontraron juegos</p>
      )}
    </div>
  )
}
""",
        "apps/web/src/pages/ConsolesPage.jsx": """import { motion } from 'framer-motion'
import ProductCard from '../components/ProductCard'

const consoles = [
  { id: 4, title: 'PlayStation 5', price: 499.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.9 },
  { id: 5, title: 'Xbox Series X', price: 499.99, image: 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400', platform: 'Microsoft', rating: 4.8 },
  { id: 6, title: 'Nintendo Switch OLED', price: 349.99, image: 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400', platform: 'Nintendo', rating: 4.7 },
  { id: 14, title: 'PlayStation 5 Digital', price: 399.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.6 },
  { id: 15, title: 'Xbox Series S', price: 299.99, image: 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400', platform: 'Microsoft', rating: 4.5 },
]

export default function ConsolesPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">Consolas</h1>
        <p className="text-gray-400 mt-2">Las mejores consolas del mercado</p>
      </motion.div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {consoles.map((item, index) => (
          <motion.div key={item.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
            <ProductCard {...item} category="consola" />
          </motion.div>
        ))}
      </div>
    </div>
  )
}
""",
        "apps/web/src/pages/RepairsPage.jsx": """import { motion } from 'framer-motion'
import { Wrench, Gamepad, Cpu, Clock, Shield, Award, CheckCircle } from 'lucide-react'

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
    <div className="container mx-auto px-4 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="text-center mb-12">
        <h1 className="text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">Servicios de Reparación</h1>
        <p className="text-gray-400 mt-2">Expertos en reparación de consolas y controles</p>
      </motion.div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {services.map((service, index) => (
          <motion.div key={index} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }} className="bg-card-gradient rounded-xl p-6 hover:shadow-xl hover:shadow-purple-500/10 transition-all">
            <div className="w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center mb-4">
              <service.icon className="w-6 h-6 text-purple-400" />
            </div>
            <h3 className="text-xl font-bold text-white mb-2">{service.title}</h3>
            <p className="text-gray-400 text-sm mb-4">{service.description}</p>
            <ul className="space-y-2">
              {service.features.map((feature, i) => (
                <li key={i} className="flex items-center gap-2 text-sm text-gray-300">
                  <CheckCircle className="w-4 h-4 text-purple-400" />
                  {feature}
                </li>
              ))}
            </ul>
          </motion.div>
        ))}
      </div>
    </div>
  )
}
""",
        "apps/web/src/pages/AccessoriesPage.jsx": """import { motion } from 'framer-motion'
import ProductCard from '../components/ProductCard'

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8 },
  { id: 8, title: 'Xbox Wireless Controller', price: 59.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Xbox Series X', rating: 4.7 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'Nintendo Switch', rating: 4.6 },
  { id: 10, title: 'Auriculares Gaming', price: 89.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'Universal', rating: 4.5 },
  { id: 16, title: 'Teclado Mecánico RGB', price: 129.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'PC', rating: 4.7 },
  { id: 17, title: 'Mouse Gaming Logitech', price: 79.99, image: 'https://images.unsplash.com/photo-1599669454699-248893623440?w=400', platform: 'PC', rating: 4.6 },
]

export default function AccessoriesPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
        <h1 className="text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">Accesorios</h1>
        <p className="text-gray-400 mt-2">Todo lo que necesitas para tu setup</p>
      </motion.div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {accessories.map((accessory, index) => (
          <motion.div key={accessory.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: index * 0.1 }}>
            <ProductCard {...accessory} category="accesorio" />
          </motion.div>
        ))}
      </div>
    </div>
  )
}
""",
        "apps/web/src/pages/ContactPage.jsx": """import { motion } from 'framer-motion'
import { MapPin, Phone, Mail, Clock } from 'lucide-react'
import ContactForm from '../components/ContactForm'

export default function ContactPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="text-center mb-12">
        <h1 className="text-4xl font-gaming font-bold bg-gradient-to-r from-purple-400 to-purple-600 bg-clip-text text-transparent">Contáctanos</h1>
        <p className="text-gray-400 mt-2">Estamos aquí para ayudarte</p>
      </motion.div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <div>
          <ContactForm />
        </div>
        <div className="space-y-6">
          <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6, delay: 0.2 }} className="bg-card-gradient rounded-xl p-6">
            <h3 className="text-xl font-bold text-white mb-4">Información de Contacto</h3>
            <div className="space-y-4">
              <div className="flex items-start gap-3">
                <MapPin className="w-5 h-5 text-purple-400 mt-1" />
                <div>
                  <p className="font-semibold text-white">Dirección</p>
                  <p className="text-gray-400">Calle Gamer 123, 28001 Madrid</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Phone className="w-5 h-5 text-purple-400 mt-1" />
                <div>
                  <p className="font-semibold text-white">Teléfono</p>
                  <p className="text-gray-400">+34 900 123 456</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Mail className="w-5 h-5 text-purple-400 mt-1" />
                <div>
                  <p className="font-semibold text-white">Email</p>
                  <p className="text-gray-400">info@gamingstore.com</p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <Clock className="w-5 h-5 text-purple-400 mt-1" />
                <div>
                  <p className="font-semibold text-white">Horario</p>
                  <p className="text-gray-400">Lunes a Sábado: 10:00 - 21:00</p>
                  <p className="text-gray-400">Domingo: 11:00 - 15:00</p>
                </div>
              </div>
            </div>
          </motion.div>
          <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6, delay: 0.4 }} className="bg-card-gradient rounded-xl p-6">
            <h3 className="text-xl font-bold text-white mb-4">¿Por qué elegirnos?</h3>
            <ul className="space-y-2 text-gray-400">
              <li>Equipo de expertos en gaming</li>
              <li>Atención personalizada</li>
              <li>Garantía en todos los servicios</li>
              <li>Precios competitivos</li>
              <li>Respuesta rápida a tus consultas</li>
            </ul>
          </motion.div>
        </div>
      </div>
    </div>
  )
}
""",
        "apps/web/src/pages/ProductDetailPage.jsx": """import { useParams, Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ArrowLeft, ShoppingCart, Star, CheckCircle } from 'lucide-react'
import { toast } from 'sonner'

const products = {
  1: { id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, image: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400', platform: 'Nintendo Switch', rating: 4.9, category: 'juego', description: 'El juego de carreras definitivo para Nintendo Switch.', stock: 10 },
  4: { id: 4, title: 'PlayStation 5', price: 499.99, image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400', platform: 'Sony', rating: 4.9, category: 'consola', description: 'La última generación de PlayStation con gráficos 4K.', stock: 5 },
  7: { id: 7, title: 'DualSense Wireless Controller', price: 69.99, image: 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400', platform: 'PlayStation 5', rating: 4.8, category: 'accesorio', description: 'Controlador inalámbrico DualSense con tecnología háptica.', stock: 15 },
}

export default function ProductDetailPage() {
  const { id } = useParams()
  const product = products[id]

  if (!product) {
    return (
      <div className="container mx-auto px-4 py-8 text-center">
        <h2 className="text-2xl font-bold text-white">Producto no encontrado</h2>
        <Link to="/" className="text-purple-400 hover:text-purple-300 mt-4 inline-block">Volver al inicio</Link>
      </div>
    )
  }

  const addToCart = () => {
    toast.success(`¡${product.title} añadido al carrito!`)
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <Link to="/" className="inline-flex items-center gap-2 text-gray-400 hover:text-white mb-6 transition-colors">
        <ArrowLeft className="w-4 h-4" /> Volver
      </Link>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <motion.div initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} className="bg-card-gradient rounded-xl overflow-hidden">
          <img src={product.image} alt={product.title} className="w-full h-auto object-cover" />
        </motion.div>
        <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} className="space-y-6">
          <div>
            <span className="inline-block px-3 py-1 bg-purple-500/20 text-purple-400 text-sm font-semibold rounded-full mb-3">{product.category}</span>
            <h1 className="text-3xl font-gaming font-bold text-white">{product.title}</h1>
            <div className="flex items-center gap-2 mt-2">
              <div className="flex gap-1">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className={`w-5 h-5 ${i < Math.floor(product.rating) ? 'fill-yellow-400 text-yellow-400' : 'text-gray-600'}`} />
                ))}
              </div>
              <span className="text-gray-400">({product.rating})</span>
            </div>
          </div>
          <div className="text-3xl font-bold text-purple-400">${product.price}</div>
          <p className="text-gray-300">{product.description}</p>
          <div className="flex items-center gap-2 text-sm text-gray-400">
            <CheckCircle className="w-4 h-4 text-green-400" />
            <span>En stock ({product.stock} unidades)</span>
          </div>
          <div className="flex items-center gap-2 text-sm text-gray-400">
            <span className="font-semibold text-white">Plataforma:</span>
            <span>{product.platform}</span>
          </div>
          <button
            onClick={addToCart}
            className="w-full py-3 bg-purple-600 hover:bg-purple-700 rounded-lg font-semibold transition-colors flex items-center justify-center gap-2"
          >
            <ShoppingCart className="w-5 h-5" /> Añadir al Carrito
          </button>
        </motion.div>
      </div>
    </div>
  )
}
""",
        # ========== HOOKS ==========
        "apps/web/src/hooks/useScrollAnimation.js": """import { useEffect, useRef } from 'react'
import { useInView } from 'framer-motion'

export function useScrollAnimation() {
const ref = useRef(null)
const isInView = useInView(ref, { once: true, amount: 0.2 })

useEffect(() => {
if (isInView && ref.current) {
ref.current.classList.add('visible')
}
}, [isInView])

return { ref, isInView }
}
""",
        # ========== UTILS FRONTEND ==========
        "apps/web/src/utils/api.js": """import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message = error.response?.data?.message || 'Error de conexion con la API'
    return Promise.reject(new Error(message))
  }
)

export default api
""",
        "apps/web/src/utils/constants.js": """export const CATEGORIES = {
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
""",
        # ========== API ==========
        "apps/api/package.json": """{
"name": "gaming-store-api",
"version": "1.0.0",
"type": "module",
"scripts": {
"dev": "node --watch src/server.js",
"start": "node src/server.js"
},
"dependencies": {
"express": "^4.18.2",
"cors": "^2.8.5",
"dotenv": "^16.3.1",
"bcryptjs": "^2.4.3",
"jsonwebtoken": "^9.0.2",
"mongoose": "^7.5.0"
}
}
""",
        "apps/api/.env.example": """PORT=3000
MONGODB_URI=mongodb://localhost:27017/gaming-store
JWT_SECRET=tu_secreto
EMAIL_USER=correo@gmail.com
EMAIL_PASS=contraseña
""",
        "apps/api/.gitignore": """node_modules/
.env
.DS_Store
*.log
""",
        "apps/api/src/app.js": """import express from 'express'
import cors from 'cors'
import gamesRoutes from './routes/games.js'
import consolesRoutes from './routes/consoles.js'
import accessoriesRoutes from './routes/accessories.js'
import repairsRoutes from './routes/repairs.js'
import contactRoutes from './routes/contact.js'
import { notFound } from './middleware/notFound.js'
import { errorHandler } from './middleware/errorHandler.js'

const app = express()
app.use(cors())
app.use(express.json())

app.get('/api/health', (req, res) => {
  res.json({ success: true, message: 'Gaming Store API operativa' })
})

app.use('/api/games', gamesRoutes)
app.use('/api/consoles', consolesRoutes)
app.use('/api/accessories', accessoriesRoutes)
app.use('/api/repairs', repairsRoutes)
app.use('/api/contact', contactRoutes)

app.use(notFound)
app.use(errorHandler)

export default app
""",
        "apps/api/src/server.js": """import app from './app.js'
import dotenv from 'dotenv'
import { connectDatabase } from './config/database.js'

dotenv.config()

const PORT = process.env.PORT || 3000

async function startServer() {
  await connectDatabase()

  app.listen(PORT, () => {
    console.log(`Gaming Store API en puerto ${PORT}`)
  })
}

startServer().catch((error) => {
  console.error('Error al iniciar el servidor:', error)
  process.exit(1)
})
""",
        "apps/api/src/config/database.js": """import mongoose from 'mongoose'

export async function connectDatabase() {
  const uri = process.env.MONGODB_URI

  if (!uri) {
    console.warn('MONGODB_URI no definida. La API funcionara con datos de ejemplo.')
    return
  }

  try {
    await mongoose.connect(uri)
    console.log('Conexion a MongoDB establecida')
  } catch (error) {
    console.error('Error al conectar con MongoDB:', error.message)
    console.warn('La API seguira funcionando con datos de ejemplo.')
  }
}
""",
        "apps/api/src/middleware/notFound.js": """export function notFound(req, res) {
  res.status(404).json({
    success: false,
    message: `Ruta no encontrada: ${req.method} ${req.originalUrl}`,
  })
}
""",
        "apps/api/src/middleware/errorHandler.js": """export function errorHandler(error, req, res, next) {
  console.error(error)
  res.status(error.status || 500).json({
    success: false,
    message: error.message || 'Error interno del servidor',
  })
}
""",
        "apps/api/src/models/Product.js": """import mongoose from 'mongoose'

const productSchema = new mongoose.Schema(
  {
    title: { type: String, required: true },
    price: { type: Number, required: true },
    category: { type: String, enum: ['juego', 'consola', 'accesorio'], required: true },
    platform: String,
    rating: { type: Number, default: 0 },
    stock: { type: Number, default: 0 },
    image: String,
    description: String,
  },
  { timestamps: true }
)

export default mongoose.models.Product || mongoose.model('Product', productSchema)
""",
        "apps/api/src/routes/games.js": """import express from 'express'
const router = express.Router()

// Datos de ejemplo
const games = [
{ id: 1, title: 'Mario Kart 8 Deluxe', price: 59.99, platform: 'Nintendo Switch', rating: 4.9, stock: 10 },
{ id: 2, title: 'EA Sports FC 24', price: 69.99, platform: 'PlayStation 5', rating: 4.7, stock: 8 },
{ id: 3, title: 'Call of Duty: Modern Warfare', price: 49.99, platform: 'Xbox Series X', rating: 4.8, stock: 12 }
]

router.get('/', (req, res) => {
res.json({ success: true, data: games })
})

router.get('/:id', (req, res) => {
const game = games.find(g => g.id === parseInt(req.params.id))
if (!game) {
return res.status(404).json({ success: false, message: 'Juego no encontrado' })
}
res.json({ success: true, data: game })
})

export default router
""",
        "apps/api/src/routes/consoles.js": """import express from 'express'
const router = express.Router()

const consoles = [
{ id: 4, title: 'PlayStation 5', price: 499.99, platform: 'Sony', rating: 4.9, stock: 5 },
{ id: 5, title: 'Xbox Series X', price: 499.99, platform: 'Microsoft', rating: 4.8, stock: 3 },
{ id: 6, title: 'Nintendo Switch OLED', price: 349.99, platform: 'Nintendo', rating: 4.7, stock: 7 }
]

router.get('/', (req, res) => {
res.json({ success: true, data: consoles })
})

router.get('/:id', (req, res) => {
const console = consoles.find(c => c.id === parseInt(req.params.id))
if (!console) {
return res.status(404).json({ success: false, message: 'Consola no encontrada' })
}
res.json({ success: true, data: console })
})

export default router
""",
        "apps/api/src/routes/repairs.js": """import express from 'express'
const router = express.Router()

const repairServices = [
{ id: 1, name: 'Reparación de Consolas', price: 49, description: 'Diagnóstico y reparación de PlayStation, Xbox, Nintendo y más.' },
{ id: 2, name: 'Reparación de Controles', price: 29, description: 'Joystick drift, botones atascados, conexión y más.' },
{ id: 3, name: 'Mantenimiento Preventivo', price: 39, description: 'Limpieza profunda, cambio de pasta térmica y optimización.' }
]

router.get('/', (req, res) => {
res.json({ success: true, data: repairServices })
})

router.post('/request', (req, res) => {
const { serviceId, description, consoleType } = req.body
res.json({
success: true,
message: 'Solicitud de reparación recibida',
data: { serviceId, description, consoleType, status: 'pending' }
})
})

export default router
""",
        "apps/api/src/routes/contact.js": """import express from 'express'
const router = express.Router()

router.post('/', (req, res) => {
const { name, email, phone, subject, message } = req.body

if (!name || !email || !subject || !message) {
return res.status(400).json({
success: false,
message: 'Faltan campos requeridos'
})
}

// Aquí iría la lógica para enviar email
res.json({
success: true,
message: 'Mensaje recibido correctamente',
data: { name, email, subject }
})
})

export default router
""",
        "apps/api/src/routes/accessories.js": """import express from 'express'
const router = express.Router()

const accessories = [
  { id: 7, title: 'DualSense Wireless Controller', price: 69.99, platform: 'PlayStation 5', rating: 4.8, stock: 15 },
  { id: 8, title: 'Xbox Wireless Controller', price: 59.99, platform: 'Xbox Series X', rating: 4.7, stock: 12 },
  { id: 9, title: 'Nintendo Switch Pro Controller', price: 69.99, platform: 'Nintendo Switch', rating: 4.9, stock: 10 },
  { id: 10, title: 'Auriculares Gaming RGB', price: 89.99, platform: 'Multiplataforma', rating: 4.6, stock: 20 }
]

router.get('/', (req, res) => {
  res.json({ success: true, data: accessories })
})

router.get('/:id', (req, res) => {
  const accessory = accessories.find((item) => item.id === parseInt(req.params.id))
  if (!accessory) {
    return res.status(404).json({ success: false, message: 'Accesorio no encontrado' })
  }
  res.json({ success: true, data: accessory })
})

export default router
""",
        "apps/api/src/controllers/.gitkeep": "",
        # ========== DOCS ==========
        "docs/ESTRUCTURA.md": """# Estructura del proyecto

## Monorepo

```
apps/
├── web/          # Frontend React + Vite + Tailwind
└── api/          # Backend Node.js + Express
docs/             # Documentación
```

## Frontend

```
src/
├── components/   # Componentes reutilizables
├── pages/        # Páginas de la aplicación
├── hooks/        # Custom hooks
└── utils/        # Utilidades
```

## Backend

```
src/
├── controllers/  # Controladores
├── routes/       # Rutas de la API
├── models/       # Modelos de datos
└── middleware/   # Middlewares
```
""",
        "docs/COLORES.md": """# Colores Gaming Store

## Paleta principal
- **Primary:** #7C3AED (Purple)
- **Secondary:** #1E1B4B (Dark Blue)
- **Accent:** #F59E0B (Yellow)
- **Dark:** #0F0A1A (Almost Black)
- **Card:** #1A1430 (Dark Purple)
- **Text:** #E2E8F0 (Light Gray)
- **Text Light:** #94A3B8 (Gray)

## Uso
- **Primary:** Botones principales, enlaces, elementos destacados
- **Secondary:** Fondos, header, footer
- **Accent:** Llama la atención, promociones
- **Dark:** Fondo general
- **Card:** Tarjetas de productos y servicios""",
        "docs/COMPONENTES.md": """# Componentes

## Layout
- **Layout:** Contenedor principal con Header y Footer
- **Header:** Navegación con menú responsive
- **Footer:** Información de contacto y enlaces

## Home
- **Hero:** Banner principal con CTA
- **FeaturedGames:** Videojuegos destacados
- **FeaturedConsoles:** Consolas destacadas
- **RepairServices:** Servicios de reparación
- **AccessoryGrid:** Accesorios disponibles
- **TestimonialCard:** Testimonios de clientes

## Productos
- **ProductCard:** Tarjeta de producto individual
- **CategoryCard:** Tarjeta de categoría
- **ProductDetailPage:** Página de detalle de producto

## Formularios
- **ContactForm:** Formulario de contacto con validación

## Utilidades
- **useScrollAnimation:** Hook para animaciones al hacer scroll""",
        "docs/RUTAS.md": """# Rutas

## Frontend
- `/` - Página de inicio
- `/juegos` - Catálogo de videojuegos
- `/consolas` - Catálogo de consolas
- `/reparacion` - Servicios de reparación
- `/accesorios` - Catálogo de accesorios
- `/contacto` - Página de contacto
- `/producto/:id` - Detalle de producto

## API
- `GET /api/games` - Listar juegos
- `GET /api/games/:id` - Detalle de juego
- `GET /api/consoles` - Listar consolas
- `GET /api/consoles/:id` - Detalle de consola
- `GET /api/accessories` - Listar accesorios
- `GET /api/accessories/:id` - Detalle de accesorio
- `GET /api/repairs` - Listar servicios
- `POST /api/repairs/request` - Solicitar reparación
- `POST /api/contact` - Enviar mensaje de contacto
- `GET /api/health` - Estado de la API"""
    }


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera el monorepo completo de Gaming Store (raiz, frontend, backend y docs)."
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help=f"Directorio donde crear el proyecto (por defecto: carpeta del script)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_gaming_store(output_dir=args.output)