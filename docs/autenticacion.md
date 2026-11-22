# Autenticación (US-01)

Acceso con usuario y contraseña mediante la autenticación de Django, con sesiones en servidor. Modelo de usuario propio: `cuentas.Usuario`.

## Qué cubre
- **Sin sesión no se accede a nada.** Lo garantiza `LoginRequiredMiddleware` de Django: toda vista exige sesión salvo las marcadas con `login_not_required` (por ahora, solo la pantalla de entrada). Las vistas nuevas nacen protegidas.
- **Error genérico.** El mensaje de un acceso fallido es el mismo si falla el usuario o la contraseña, y también si el usuario no existe.
- **Contraseñas con hash** del propio Django. Nunca se guardan en claro.
- **CSRF** activado en todos los formularios.
- **Cookies.** La de sesión es `HttpOnly` y `SameSite=Lax`. Con `DJANGO_COOKIES_SEGURAS=true` (despliegue con HTTPS) las cookies de sesión y CSRF solo viajan cifradas. Por defecto está en `false`, porque en desarrollo se usa HTTP y el inicio de sesión no funcionaría.

## Bloqueo temporal

Se usa [django-axes](https://github.com/jazzband/django-axes) 9.0.0.

| Parámetro | Valor | Motivo |
| --- | --- | --- |
| `AXES_FAILURE_LIMIT` | 3 intentos fallidos | Valor por defecto de la biblioteca |
| `AXES_COOLOFF_TIME` | 3 minutos | Corto, para que un despiste en el móvil no deje al usuario fuera mucho rato |
| `AXES_LOCKOUT_PARAMETERS` | `["username"]` | Ver más abajo |
| `AXES_RESET_ON_SUCCESS` | `True` | Un acceso correcto reinicia el contador |

El bloqueo responde con **HTTP 429** y la pantalla `cuentas/bloqueado.html`.

### Por qué se bloquea por usuario y no por IP

Detrás de Docker o de un proxy todas las peticiones pueden llegar con la misma IP. Un bloqueo por IP dejaría sin acceso a todos los usuarios a la vez. La contrapartida es que alguien podría bloquear la cuenta de otro adivinando su nombre de usuario, y que no se limita a quien prueba muchos usuarios distintos desde una misma IP. Se acepta para el alcande del proyecto (pocos usuarios, una explotación). Axes avisa de esto con `axes.W006`, que se silencia a propósito en `SILENCED_SYSTEM_CHECKS`. **Revisar al desplegar en un servidor propio.**

### Por qué django-axes y no una implementación propia

- Contar intentos y bloquear parece sencillo, pero es fácil hacerlo mal: carreras entre peticiones simultáneas, limpieza de registros caducados, usuarios inexistentes.
- Es una biblioteca muy extendida y mantenida, compatible con Django 5.2 y Python 3.13.
- **Licencia MIT**, compatible con la del proyecto (RNF-08).
- Coste: una dependencia más y sus propias tablas (migraciones de `axes`).