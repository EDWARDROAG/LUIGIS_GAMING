# Assets estáticos (imágenes, favicon, videos)

## Ubicación de archivos

Los recursos públicos viven en:

```
apps/web/public/assets/
├── img/       # Logo, favicon, fondos, personajes, etc.
└── videos/    # Videos de la sección showcase
```

Referencia de diseño del cliente: `referencias_cliente/assets/`

## Problema en GitHub Pages

GitHub Pages sirve el sitio bajo un subpath (`/nombre-repo/`), no en la raíz `/`.

Las rutas absolutas como `/assets/img/logo.png` apuntan a la raíz del dominio y **no cargan** en producción.

| Entorno | Ruta incorrecta | Ruta correcta |
|---------|-----------------|---------------|
| GitHub Pages | `/assets/img/logo.png` | `/LUIGIS_GAMING/assets/img/logo.png` |
| Local (`npm run dev`) | `/assets/img/logo.png` | `/assets/img/logo.png` ✓ |

## Solución: `assetUrl()`

Archivo: `apps/web/src/utils/assets.js`

```js
import { assetUrl } from '../utils/assets.js'

<img src={assetUrl('/assets/img/logo.png')} alt="Logo" />
<video src={assetUrl('/assets/videos/video01.mp4')} />
```

`assetUrl()` antepone `import.meta.env.BASE_URL` automáticamente según el entorno.

### Usar en componentes JSX

Siempre que se referencie un archivo de `public/`:

```jsx
src={assetUrl('/assets/img/hero.jpg')}
```

**No usar** rutas absolutas con `/` en JSX.

## Fondos en CSS

Vite no reescribe `url('/assets/...')` dentro de CSS. Los fondos decorativos usan variables CSS inyectadas al iniciar la app:

- `applyPublicAssetCssVars()` se llama en `main.jsx`
- Clases como `.bg-wave-white` usan `var(--asset-wave-white)`

Para añadir un fondo nuevo:

1. Agregar el archivo en `public/assets/img/`
2. Registrar la variable en `PUBLIC_BG_ASSETS` dentro de `assets.js`
3. Usar la variable en `index.css`

## Favicon (pestaña del navegador)

Archivo: `apps/web/public/assets/img/logo_favicon.png`

Referencia original del cliente: colocar `logo_favicon.png` en `referencias_cliente/assets/img/` y copiarlo a `public/assets/img/`.

Configuración en `apps/web/index.html`:

```html
<link rel="icon" type="image/png" href="/assets/img/logo_favicon.png" />
```

Vite reescribe esta ruta en el build con el `base path` de GitHub Pages.

## Logo del header

El logo visible en la navegación usa `logo.png` (no el favicon):

```jsx
<img src={assetUrl('/assets/img/logo.png')} alt="Gaming Store" />
```

| Archivo | Uso |
|---------|-----|
| `logo_favicon.png` | Icono de la pestaña del navegador |
| `logo.png` | Logo en el header y navegación |

## Checklist al agregar assets nuevos

- [ ] Archivo en `apps/web/public/assets/`
- [ ] Referencia con `assetUrl()` en JSX
- [ ] Si es fondo CSS, registrar en `assets.js` + `index.css`
- [ ] Probar build con `VITE_BASE_PATH` antes de hacer push
