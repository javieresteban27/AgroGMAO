from django.db import models
from django.core.validators import MinValueValidator

from decimal import Decimal


class Parametro(models.Model):
    """Dato de configuración de la explotación en formato clave-valor (CF-01)."""

    clave = models.CharField(max_length=50, primary_key=True)
    valor = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "parámetro"
        verbose_name_plural = "parámetros"

    def __str__(self):
        return f"{self.clave} = {self.valor}"


class ClaseActividad(models.Model):
    """Clase de actividad con su tarifa por hora: taller, extras, nocturnas (CF-02)."""

    nombre = models.CharField(max_length=50, unique=True)
    tarifa = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0"))],
    )
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "clase de actividad"
        verbose_name_plural = "clases de actividad"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.tarifa} €/h)"