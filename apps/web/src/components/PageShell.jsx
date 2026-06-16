import WaveDivider from './WaveDivider'

export default function PageShell({ title, subtitle, children, contentClassName = '' }) {
  return (
    <>
      <WaveDivider />
      <section className="bg-pattern-gaming py-10 md:py-14">
        <div className="container mx-auto px-4">
          <div className="mb-8 text-center md:mb-10">
            <h1 className="text-4xl font-black text-white md:text-5xl">{title}</h1>
            {subtitle && (
              <p className="mx-auto mt-3 max-w-2xl text-lg font-bold text-white/90 md:text-xl">
                {subtitle}
              </p>
            )}
          </div>
          <div
            className={`mx-auto max-w-6xl rounded-2xl bg-white p-5 shadow-xl md:p-8 ${contentClassName}`}
          >
            {children}
          </div>
        </div>
      </section>
      <WaveDivider className="relative top-2" />
    </>
  )
}
