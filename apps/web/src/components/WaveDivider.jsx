export default function WaveDivider({ variant = 'white', className = '' }) {
  const variants = {
    white: 'bg-wave-white',
    pink: 'bg-wave-pink',
    dots: 'bg-wave-dots',
  }

  return (
    <div
      className={`h-6 w-full bg-repeat-x ${variants[variant] || variants.white} ${className}`}
      aria-hidden="true"
    />
  )
}
