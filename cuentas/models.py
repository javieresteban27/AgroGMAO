from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """Usuario de AgroGMAO: el de Django es más un perfil (US-02, US-03)."""

    class Perfil(models.TextChoices):
        OPERARIO = "operario", "Operario"
        MECANICO = "mecanico", "Mecánico"
        GERENTE = "gerente", "Gerente"

    perfil = models.CharField(
        max_length= 10,
        choices=Perfil.choices,
        default=Perfil.OPERARIO,
    )

    def __str__(self):
        return self.get_full_name() or self.username