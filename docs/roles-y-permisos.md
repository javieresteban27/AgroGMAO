# Roles y permisos (US-02)

Cada usuario tiene uno o varios perfiles, que limitan lo que ve y lo que hace. El perfil **no es un campo** del model `Usuario`: sale de los grupos de Django.

## Los tres perfiles

Se crean con una migración de datos (`cuentas/migrations/0002_grupos_de_perfil.py`), así que existen en cualquier instalación nueva:

- **Operario**: maquinista o tractorista. Avisa de averías y consulta sus avisos.
- **Mecánico**: responsable del taller. Atiende incidencias, ejecuta órdenes y revisiones, imputa horas y repuestos.
- **Gerente**: titular o encargado. Administra equipos, repuestos, usuarios y tarifas, y consulta costes.

Una misma persona puede tener varios perfiles, porque a menudo es operario, mecánico y gerente a la vez. Sus permisos **se suman**: basta con que uno de sus grupos esté permitido. Los superusuarios pasan siempre.

Mientras no exista la gestión de usuarios (US-03), los grupos se asignan desde el administrador de Django (`/admin/`).

## Cómo proteger una vista

Los permisos se comprueban **en el servidor, en cada vista**, no solo ocultando botones. Las herramientas están en `cuentas/permisos.py`:

```python
from cuentas.permisos import GERENTE, MECANICO, PerfilRequeridoMixin, perfil_requerido

# Vista de función
@perfil_requerido(GERENTE)
def costes(request):
    ...

# Vista de clase
class ListaDeOrdenes(PerfilRequeridoMixin, ListView):
    perfiles = (MECANICO, GERENTE)
```

- Sin sesión, `LoginRequiredMiddleware` redirige al inicio de sesión.
- Con sesión pero sin el perfil, se lanza `PermisionDenied` y se muestra `templates/403.html`: 'No tienes permiso para ver esto'.

## Permisos por perfil

Esta es la tabla del catálogo funcional. Cada vista nueva debe respetarla.

| Acción | Operario | Mecánico | Gerente |
| --- | --- | --- | --- |
| Ver equipos y su estado | Sí | Sí | Sí |
| Alta, edición y baja de equipos | No | No | Sí |
| Reportar incidencia | Sí | Sí | Sí |
| Ver incidencias | Las suyas | Todas | Todas |
| Asignar y cambiar estado de incidencias | No | Sí | Sí |
| Crear y ejecutar órdenes de trabajo | No | Sí | Sí |
| Imputar horas y consumir repuestos | No | Sí | Sí |
| Ver cantidades de repuestos | No | Sí | Sí |
| Alta y precio de repuestos | No | No | Sí |
| Registrar entradas de stock | No | Sí | Sí |
| Ver revisiones próximas | Sí | Sí | Sí |
| Ejecutar revisiones | No | Sí | Sí |
| Crear y editar hojas de ruta | No | No | Sí |
| Ver importes y costes | No | No | Sí |
| Configurar tarifas, clases y parámetros | No | No | Sí |
| Gestionar usuarios | No | No | Sí |
| Reabrir órdenes cerradas | No | No | Sí |
| Ver registro de actividad | No | No | Sí |

## Pruebas

Las pruebas de `cuentas/tests.py` cubren cada perfil, la suma de grupos, los anónimos, el decorador, el mixin y la pantalla de permiso denegado. Usan una vista de ejemplo, porque las vistas de usuarios y equipos aún no existen. Cuando existan (US-03 y EQ-01), se les pone el decorador y se añade su prueba.