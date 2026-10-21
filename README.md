# AgroGMAO

Sistema de gestión del mantenimiento asistido por ordenador (GMAO) para maquinaria y equipos agrícolas.

> Proyecto en desarrollo. El nombre es provisional.

## Descripción

Las averías de la maquinaria agrícola pueden provocar retrasos y costes importantes durante las campañas. AgroGMAO es una aplicación web que permite gestionar el mantenimiento de una explotación agrícola, con especial atención a la gestión de activos, el mantenimiento preventivo y correctivo, la trazabilidad y el análisis de costes.

Este proyecto es un Trabajo de Fin de Grado (TFG) del Grado en Ingeniería Informática de la Universidad de Burgos.

- **Título del TFG:** GII 26.16 Desarrollo de un sistema de gestión del mantenimiento de maquinaria y equipos agrícolas
- **Autor:** Javier Esteban González
- **Tutor:** David González Asenjo

## Funcionalidades previstas

- Inventario de equipos (cosechadoras, aperos y otra maquinaria).
- Registro de incidencias.
- Órdenes de trabajo de mantenimiento correctivo y preventivo, con tiempo y materiales empleados.
- Planificación de revisiones mediante hojas de ruta asociadas a cada equipo, con descripción y periodicidad.
- Avisos de revisiones pendientes.
- Históricos, listados de costes e incidencias por equipo.
- Perfiles de usuario con distintos permisos.
- Informes.
- Uso cómodo desde el móvil y ordenador, pensado también para personas con poca experiencia digital.

## Tecnologías previstas

Pila provisional, pendiente de confirmar:

- Python
- PostgreSQL
- Docker y Docker Compose
- Aplicación web adaptable a móvil y ordenador

## Estado del proyecto

En fase inicial: configruación del repositorio y de la gestión del poroyecto.

## Gestión del proyecto

- **Código:** este repositorio de GitHub.
- **Tareas y planificación:** Zube.io (enlace pendiente de añadir).

## Cómo contribuir

El flujo de trabajo es el siguiente:

1. Cada cambio parte de un issue.
2. Se crea una rama corta desde `main` con el formato `tipo/número-descripcion` (por ejemplo, `feature/12-hoja-de-ruta`).
3. Se abre un pull request hacia `main` que cierre el issue (`Closes #12`).
4. Tras fusionarlo, se borra la rama.

## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
