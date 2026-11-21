from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    Usuario de AgroGMAO.

    El perfil (operario, mecánico, gerente) no es un campo: sale de los 
    grupos de Django (US-02). Se define un modelo propio ahora porque cambiarlo
    más adelante obligaría a rehacer la base de datos.
    """