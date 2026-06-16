# Estructura del proyecto

## Monorepo

```
apps/
├── web/          # Frontend React + Vite + Tailwind
└── api/          # Backend Node.js + Express
docs/             # Documentación
referencias_cliente/  # Referencia visual y assets del cliente
```

## Frontend

```
apps/web/
├── public/       # Assets estáticos (img, videos, favicon)
│   └── assets/
├── src/
│   ├── components/   # Componentes reutilizables
│   ├── pages/        # Páginas de la aplicación
│   ├── hooks/        # Custom hooks
│   └── utils/        # Utilidades (assets.js, constants.js, api.js)
├── index.html    # Entrada HTML (favicon, fuentes)
└── vite.config.js
```

### Utilidades clave (`src/utils/`)

| Archivo | Función |
|---------|---------|
| `assets.js` | `assetUrl()` — rutas correctas para GitHub Pages |
| `constants.js` | `formatPrice()` — precios en COP, WhatsApp, endpoints |
| `api.js` | Cliente HTTP hacia la API |

## Backend

```
src/
├── controllers/  # Controladores
├── routes/       # Rutas de la API
├── models/       # Modelos de datos
└── middleware/   # Middlewares
```

## Documentación

| Archivo | Contenido |
|---------|-----------|
| `ESTRUCTURA.md` | Organización del monorepo |
| `RUTAS.md` | Rutas frontend y API |
| `COMPONENTES.md` | Componentes React |
| `COLORES.md` | Paleta y tokens de diseño |
| `DESPLIEGUE.md` | GitHub Pages y CI/CD |
| `ASSETS.md` | Imágenes, favicon y rutas estáticas |
| `PRECIOS.md` | Precios en pesos colombianos |
