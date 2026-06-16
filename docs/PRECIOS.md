# Precios en pesos colombianos (COP)

Todos los precios del proyecto están en **pesos colombianos**, no en dólares ni euros.

## Formato

Función centralizada en `apps/web/src/utils/constants.js`:

```js
import { formatPrice } from '../utils/constants'

formatPrice(249900)  // → "$249.900"
```

Usa `Intl.NumberFormat` con locale `es-CO` y moneda `COP`, sin decimales.

## Almacenamiento

Los precios se guardan como **números enteros** (valor en pesos):

```js
{ id: 1, title: 'Mario Kart 8 Deluxe', price: 249900, ... }
```

**No** usar decimales ni strings con símbolo de moneda en los datos.

## Dónde se muestran

| Componente / archivo | Uso |
|----------------------|-----|
| `ProductCard.jsx` | Tarjetas de catálogo |
| `ProductDetailPage.jsx` | Página de detalle |
| `RepairServices.jsx` | Precios de reparación (texto fijo, ej. `Desde $220.000`) |

## Datos duplicados (frontend y API)

Los precios están definidos en:

**Frontend**
- `FeaturedGames.jsx`, `FeaturedConsoles.jsx`, `AccessoryGrid.jsx`
- `GamesPage.jsx`, `ConsolesPage.jsx`, `AccessoriesPage.jsx`
- `ProductDetailPage.jsx`
- `RepairServices.jsx`

**API**
- `apps/api/src/routes/games.js`
- `apps/api/src/routes/consoles.js`
- `apps/api/src/routes/accessories.js`
- `apps/api/src/routes/repairs.js`

Al cambiar un precio, actualizar ambos lados si se usa la API en producción.

## Referencia de precios actuales

### Juegos
| Producto | Precio (COP) |
|----------|--------------|
| Mario Kart 8 Deluxe | $249.900 |
| EA Sports FC 24 | $289.900 |
| Call of Duty: Modern Warfare | $199.900 |
| The Legend of Zelda: Tears | $289.900 |
| FIFA 24 | $249.900 |
| Halo Infinite | $159.900 |

### Consolas
| Producto | Precio (COP) |
|----------|--------------|
| PlayStation 5 | $2.299.900 |
| Xbox Series X | $2.199.900 |
| Nintendo Switch OLED | $1.499.900 |
| PlayStation 5 Digital | $1.899.900 |
| Xbox Series S | $1.299.900 |

### Accesorios
| Producto | Precio (COP) |
|----------|--------------|
| DualSense Wireless Controller | $279.900 |
| Xbox Wireless Controller | $239.900 |
| Nintendo Switch Pro Controller | $279.900 |
| Auriculares Gaming | $359.900 |
| Teclado Mecánico RGB | $519.900 |
| Mouse Gaming Logitech | $319.900 |

### Reparaciones
| Servicio | Precio (COP) |
|----------|--------------|
| Reparación de Consolas | Desde $220.000 |
| Reparación de Controles | Desde $130.000 |
| Mantenimiento Preventivo | Desde $175.000 |
| Servicio Express | Desde $265.000 |

Los valores son referenciales para el mercado colombiano y pueden ajustarse según la tienda.
