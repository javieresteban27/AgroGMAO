from functools import wraps

from django.core.exceptions import PermissionDenied

OPERARIO = "Operario"
MECANICO = "Mecánico"
GERENTE = "Gerente"

def tiene_perfil(usuario, *perfiles):
    """
    Dice si el usuario tiene alguno de los perfiles indicados.

    Un usuario puede estar en varios grupos y suma sus permisos: basta con que
    uno de ellos esté entre los admitidos.
    """
    if not usuario.is_authenticated:
        return False
    if usuario.is_superuser:
        return True
    return usuario.groups.filter(name__in=perfiles).exists()

def perfil_requerido(*perfiles):
    """
    Decorador para vistas de función: deniega el acceso sin el perfil.
    """

    def decorador(vista):
        @wraps(vista)
        def envoltura(request, *args, **kwargs):
            if not tiene_perfil(request.user, *perfiles):
                raise PermissionDenied
            return vista(request, *args, **kwargs)

        return envoltura

    return decorador

class PerfilRequeridoMixin:
    """
    Mixin para vistas de clase: se indican los perfiles admitidos en `perfiles`.
    """

    perfiles = ()

    def dispatch(self, request, *args, **kwargs):
        if not tiene_perfil(request.user, *self.perfiles):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)