# Rutas

## Frontend
- `/` - Página de inicio
- `/juegos` - Catálogo de videojuegos
- `/consolas` - Catálogo de consolas
- `/reparacion` - Servicios de reparación
- `/accesorios` - Catálogo de accesorios
- `/contacto` - Página de contacto
- `/producto/:id` - Detalle de producto

## API
- `GET /api/games` - Listar juegos
- `GET /api/games/:id` - Detalle de juego
- `GET /api/consoles` - Listar consolas
- `GET /api/consoles/:id` - Detalle de consola
- `GET /api/accessories` - Listar accesorios
- `GET /api/accessories/:id` - Detalle de accesorio
- `GET /api/repairs` - Listar servicios
- `POST /api/repairs/request` - Solicitar reparación
- `POST /api/contact` - Enviar mensaje de contacto
- `GET /api/health` - Estado de la API