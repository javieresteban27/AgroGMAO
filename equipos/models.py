from django.db import models

class TipoEquipo(models.Model):
    """Familia de equipo: tractor, cosechadora, sembradora... (CF-03)."""

    nombre = models.CharField(max_length =50, unique=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "familia de equipo"
        verbose_name_plural = "familias de equipo"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    