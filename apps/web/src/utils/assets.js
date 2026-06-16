export function assetUrl(path) {
  const normalized = path.startsWith('/') ? path.slice(1) : path
  return `${import.meta.env.BASE_URL}${normalized}`
}

const PUBLIC_BG_ASSETS = {
  '--asset-wave-white': 'assets/img/wave-white.png',
  '--asset-wave-pink': 'assets/img/wave-pink.png',
  '--asset-pattern-white-dots': 'assets/img/pattern-white-dots.png',
  '--asset-pattern-characters-red': 'assets/img/pattern-characters-red.png',
  '--asset-character-gaming': 'assets/img/wp2983043-super-mario-and-luigi-wallpaper.jpg',
  '--asset-pattern-yellow-dots': 'assets/img/pattern-yellow-dots.png',
}

export function applyPublicAssetCssVars() {
  const root = document.documentElement
  for (const [name, path] of Object.entries(PUBLIC_BG_ASSETS)) {
    root.style.setProperty(name, `url(${assetUrl(path)})`)
  }
}
