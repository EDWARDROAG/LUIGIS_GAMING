# Despliegue en GitHub Pages

## URL del sitio

Tras publicar, el frontend queda disponible en:

```
https://<usuario>.github.io/<nombre-repo>/
```

Ejemplo: `https://edwardroag.github.io/LUIGIS_GAMING/`

## Requisito previo (obligatorio)

Antes del primer despliegue, activar GitHub Pages en el repositorio:

1. Ir a **Settings → Pages**
2. En **Build and deployment → Source**, elegir **GitHub Actions**
3. Guardar cambios

Si Pages no está habilitado, el job `deploy` falla con error **404 Not Found** al crear el despliegue.

## Workflow

Archivo: `.github/workflows/deploy.yml`

| Job | Descripción |
|-----|-------------|
| `build` | Instala dependencias, compila el frontend y sube el artefacto |
| `deploy` | Publica el artefacto en GitHub Pages |

Se ejecuta automáticamente en push a `main` o `master`, o manualmente desde **Actions → Deploy to GitHub Pages → Run workflow**.

## Variables de entorno en el build

| Variable | Uso |
|----------|-----|
| `VITE_BASE_PATH` | Subpath del repo, ej. `/LUIGIS_GAMING/` |
| `VITE_API_URL` | URL de la API en producción (variable de repositorio) |

`VITE_BASE_PATH` se define en el workflow y alimenta `vite.config.js` y `import.meta.env.BASE_URL`.

## Routing SPA

Tras el build se copia `index.html` como `404.html` para que las rutas del cliente (`/juegos`, `/consolas`, etc.) funcionen al recargar la página en GitHub Pages.

## Probar el build localmente

Simular el entorno de GitHub Pages:

```powershell
$env:VITE_BASE_PATH="/LUIGIS_GAMING/"
npm run build:web
npm run preview
```

Reemplazar `LUIGIS_GAMING` por el nombre real del repositorio.

## API en producción

El despliegue de Pages solo publica el frontend. La API se despliega por separado con `.github/workflows/deploy-api.yml` (Render o Railway).
