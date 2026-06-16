import PillButton from './PillButton'
import WaveDivider from './WaveDivider'
import { assetUrl } from '../utils/assets.js'

export default function PromoSection() {
  return (
    <section className="bg-yellow-dots">
      <WaveDivider variant="pink" className="relative -top-4" />
      <div className="container mx-auto flex flex-col items-center justify-center px-4 py-8 text-center md:flex-row md:py-10">
        <div className="left w-full p-5 md:w-1/2 lg:w-1/3">
          <h3 className="text-3xl font-black text-yellow-900 sm:text-4xl">
            Centro de
            <br />
            Reparación
            <br />
            Gaming
          </h3>
          <p className="py-4 text-lg text-yellow-950 md:text-xl">
            Diagnóstico, mantenimiento y piezas de calidad para que vuelvas a jugar cuanto antes.
          </p>
          <PillButton to="/reparacion" showArrow>
            Solicitar servicio
          </PillButton>
        </div>

        <div className="right w-full md:w-1/2 lg:w-1/3">
          <img
            src={assetUrl('/assets/img/activity_img3.png')}
            alt="Actividades y servicios gaming"
            className="mx-auto w-full max-w-md md:max-w-full"
          />
        </div>
      </div>
    </section>
  )
}
