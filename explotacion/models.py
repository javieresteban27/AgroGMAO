from django.db import models

class Parametro(models.Model):
    """Dato de configuración de la explotación en formato clave-valor (CF-01)."""

    clave = models.CharField(max_length=50, primary_key=True)
    valor = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "parámetro"
        verbose_name_plural = "parámetros"

    def __str__(self):
        return f"{self.clave} = {self.valor}"