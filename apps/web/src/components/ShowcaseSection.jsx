import VideoCard from './VideoCard'
import { assetUrl } from '../utils/assets.js'

export default function ShowcaseSection() {
  return (
    <section className="bg-pattern-gaming py-12 md:py-20">
      <div className="container mx-auto px-4">
        <div className="mb-8 text-center md:mb-10">
          <h2 className="text-4xl font-black text-white md:text-6xl">Todo para tu setup</h2>
          <p className="mx-auto mt-4 max-w-3xl text-xl font-bold text-white md:text-2xl">
            Juegos, consolas, accesorios y servicio técnico en un solo lugar.
          </p>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-white/90">
            Tutoriales, ofertas y contenido exclusivo para la comunidad gamer.
          </p>
        </div>

        <div className="mb-10 flex justify-center">
          <img
            src={assetUrl('/assets/img/character-l.png')}
            alt="Gaming Store"
            className="h-40 w-auto object-contain md:h-56 lg:h-64"
          />
        </div>

        <div className="mx-auto grid max-w-5xl grid-cols-1 items-start gap-8 md:grid-cols-2 md:gap-10">
          <VideoCard
            video={assetUrl('/assets/videos/video01.mp4')}
            title="Aprende a reparar tú mismo"
            description="Tutoriales paso a paso para diagnosticar y arreglar tu consola o mando sin salir de casa."
            cta="Ver tutoriales"
            ctaTo="/reparacion"
          />
          <VideoCard
            video={assetUrl('/assets/videos/video02.mp4')}
            title="Sigue nuestra página"
            description="Contenido nuevo cada semana: reseñas, unboxings y consejos de mantenimiento."
            cta="Ir a redes"
            ctaTo="/contacto"
          />
        </div>
      </div>
    </section>
  )
}
