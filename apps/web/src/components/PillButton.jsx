import { Link } from 'react-router-dom'

function ArrowIcon() {
  return (
    <span
      className="ml-2 inline-block h-4 w-4 rotate-45 border-r-[5px] border-t-[5px] border-solid border-gaming-accent transition-all group-hover:ml-4 group-hover:border-gaming-primary"
      aria-hidden="true"
    />
  )
}

export default function PillButton({
  children,
  to,
  href,
  variant = 'red',
  className = '',
  showArrow = false,
  onClick,
}) {
  const base =
    'group inline-block rounded-3xl border-8 border-transparent px-10 py-2 font-black transition duration-200 hover:border-gray-200 hover:bg-white hover:text-black xl:text-xl md:px-16'

  const variants = {
    red: 'bg-red-500 text-white',
    black: 'bg-black text-white',
    outline: 'border-4 border-gaming-accent bg-transparent text-white hover:text-black',
  }

  const classes = `${base} ${variants[variant]} ${className}`

  const content = (
    <>
      {children}
      {showArrow && <ArrowIcon />}
    </>
  )

  if (to) {
    return (
      <Link to={to} className={classes}>
        {content}
      </Link>
    )
  }

  if (href) {
    return (
      <a href={href} target="_blank" rel="noreferrer" className={classes}>
        {content}
      </a>
    )
  }

  return (
    <button type="button" onClick={onClick} className={classes}>
      {content}
    </button>
  )
}
