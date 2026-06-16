import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'
import FloatingCoins from './FloatingCoins'
import WhatsAppButton from './WhatsAppButton'

export default function Layout() {
  return (
    <div className="relative min-h-screen bg-gaming-dark">
      <FloatingCoins />
      <Header />
      <main>
        <Outlet />
      </main>
      <Footer />
      <WhatsAppButton />
    </div>
  )
}
