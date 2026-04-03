# Wiki del proyecto

## Objetivo
`pera` es el backend de Gabinet. Aquí vive la API y la lógica de servidor.

## Ruta oficial de trabajo
`/Volumes/RAID/Repos/apps/pera`

## Rama de trabajo
`dev`

## Estructura útil
- `main.py`: entrada principal
- `config/`: base de configuración
- `middlewares/`: autenticación y manejo de errores
- `models/`: modelos
- `routers/`: endpoints
- `schemas/`: esquemas de datos
- `utils/`: utilidades, JWT y apoyo interno

## Reglas de trabajo
- No subir secretos ni tokens
- Mantener contratos de API estables
- Hacer cambios pequeños y claros
- Documentar endpoints antes de romper compatibilidad

## Qué falta documentar
- Cómo arrancarlo en local
- Variables de entorno necesarias
- Endpoints disponibles
- Flujo de autenticación

## Siguiente mejora recomendada
Añadir una guía de arranque y una referencia corta de la API en `docs/`.
