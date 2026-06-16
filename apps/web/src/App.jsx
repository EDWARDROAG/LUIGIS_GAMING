import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Toaster } from 'sonner'
import Layout from './components/Layout'
import HomePage from './pages/HomePage'
import GamesPage from './pages/GamesPage'
import ConsolesPage from './pages/ConsolesPage'
import RepairsPage from './pages/RepairsPage'
import AccessoriesPage from './pages/AccessoriesPage'
import ContactPage from './pages/ContactPage'
import ProductDetailPage from './pages/ProductDetailPage'

const routerBasename =
  import.meta.env.BASE_URL === '/' ? undefined : import.meta.env.BASE_URL.replace(/\/$/, '')

function App() {
  return (
    <Router basename={routerBasename}>
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

