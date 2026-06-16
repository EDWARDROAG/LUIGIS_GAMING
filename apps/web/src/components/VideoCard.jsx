import PillButton from './PillButton'

export default function VideoCard({ video, title, description, cta, ctaTo, ctaHref, className = '' }) {
  return (
    <div className={`card mx-auto w-full max-w-md overflow-hidden rounded-2xl bg-white text-center shadow-lg ${className}`}>
      <div className="cover bg-black">
        <video
          src={video}
          autoPlay
          loop
          muted
          playsInline
          className="aspect-video w-full object-cover"
        />
      </div>
      <div className="content relative -top-3 bg-wave-white bg-repeat-x">
        <h3 className="py-8 text-3xl font-black text-gray-900 md:text-4xl">{title}</h3>
        <p className="px-4 text-lg text-gray-700 md:text-xl">{description}</p>
        <div className="pb-6 pt-2">
          <PillButton to={ctaTo} href={ctaHref} showArrow>
            {cta}
          </PillButton>
        </div>
      </div>
      <div className="dots flex justify-between p-4">
        <div className="h-3 w-3 rounded-full bg-gaming-primary" />
        <div className="h-3 w-3 rounded-full bg-gaming-primary" />
      </div>
    </div>
  )
}
