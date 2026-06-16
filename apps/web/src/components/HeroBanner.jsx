import { assetUrl } from '../utils/assets.js'

export default function HeroBanner() {
  return (
    <section className="header w-full overflow-hidden">
      <img
        src={assetUrl('/assets/img/hero.jpg')}
        alt="Gaming Store - videojuegos, consolas y reparación"
        className="h-auto w-full object-cover"
      />
    </section>
  )
}
