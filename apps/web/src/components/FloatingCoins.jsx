import { useEffect, useState } from 'react'
import { assetUrl } from '../utils/assets.js'

function randomPosition() {
  return {
    top: `${10 + Math.random() * 75}%`,
    left: `${3 + Math.random() * 90}%`,
  }
}

export default function FloatingCoins() {
  const [coins, setCoins] = useState(() => [randomPosition(), randomPosition()])

  useEffect(() => {
    const interval = setInterval(() => {
      setCoins([randomPosition(), randomPosition()])
    }, 4500)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="pointer-events-none fixed inset-0 z-30 overflow-hidden" aria-hidden="true">
      {coins.map((coin, index) => (
        <img
          key={index}
          src={assetUrl('/assets/img/coin.gif')}
          alt=""
          className="coin-drift absolute h-9 w-9 opacity-60 sm:h-11 sm:w-11"
          style={{
            top: coin.top,
            left: coin.left,
          }}
        />
      ))}
    </div>
  )
}
