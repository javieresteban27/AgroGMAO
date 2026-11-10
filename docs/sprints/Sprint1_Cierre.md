# Cierre del Sprint 1 'Esqueleto técnico'

Fecha de cierre: 9 de noviembre de 2026 (previsto: 6-19 de noviembre).

## Resultado

| Tarjeta | Puntos | Estado
| --- | --- | --- |
| Esqueleto Django + PostgreSQL con docker compose (DE-01) | 5 | Hecha |
| Configuración por variables de entorno (DE-04) | 2 | Hecha |
| Integración continua con GitHub Actions: pruebas y cobertura (DE-05) | 3 | Hecha |
| Plantilla base mobile-first con Bootstrap 5 y textos traducibles (UX-01, UX-04, UX-08) | 3 | Hecha |

**Velocidad del sprint: 13 puntos completados de 13 planificados.** El tiempo real ha sido acorde a los puntos estimados.

## Qué queda construido

- Aplicación Django 5.2 LTS con PostgreSQL 16, arrancable con un solo comando (`docker compose up`).
- Configuración íntegra por variables de entorno; `.env.example` documentado y sin credenciales en el repositorio.
- Integración continua con GitHub Actions: pruebas contra un PostgreSQL real e informe de cobertura con umbral mínimo del 80%. Cobertura de partida del Hito 1: 98%.
- Plantilla base con Bootstrap 5.3.8 servido en local, menú colapsable, mensajes unificados, áreas táctiles de 48px, contraste alto y textos con el sistema de traducción de Django.
- Pruebas automáticas que protegen la plantilla base y el uso de Bootstrap en local.
- El check 'pruebas' es obligatorio en el ruleset de `main` para fusionar.

## Pendiente que pasa al siguiente sprint

- Probar el esqueleto en el ordenador de sobremesa (criterio de aceptación sin marcar a propósito, sin issue propio).

## Retrospectiva

**Ha ido bien**
- La integración continua y la cobertura de medidas desde el primer día.
- Docker: el mismo entorno en cualquier equipo.
- Construir cada pieza a mano, paso a paso, para poder defenderla en la memoria.

**Ha costado**
- Mezclar cambios ajenos en un mismo commit (`.env.example` en el commit del CI).
- La red de la universidad bloqueó el DNS y con él las descargas de Docker.

**Cambios para el Sprint 2**
- Un pull request por tarjeta, sin mezclar cambios: añadir con `git add` solo los archivos de la tarjeta.

## Ideas opcionales a valorar
- Fijar `runs-on: ubuntu-24.04` en el workflow para que el CI no dependa de lo que GitHub llame 'latest'.
- Planificar el Sprint 2 (16 puntos propuestos) frente a la velocidad real de 13.