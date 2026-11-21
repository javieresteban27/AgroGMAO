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

class Equipo(models.Model):
    """Máquina o apero de la explotación (EQ-01, EQ-03, EQ-04, EQ-07)."""

    class Estado(models.TextChoices):
        ACTIVO = "activo", "Activo"
        EN_TALLER = "en_taller", "En taller"
        BAJA = "baja", "De baja"

    denominacion = models.CharField(max_length=100)
    familia = models.ForeignKey(
        TipoEquipo, on_delete=models.PROTECT, related_name="equipos"
    )
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    numero_serie = models.CharField(
        max_length=50, unique=True, null=True, blank=True
    )
    fecha_adquisicion=models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=10, choices=Estado.choices, default=Estado.ACTIVO
    )
    fecha_baja = models.DateField(null=True, blank=True)
    observacoines = models.TextField(blank=True)

    class Meta:
        ordering = ["denominacion"]

    def __str__(self):
        return self.denominacion