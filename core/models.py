from django.db import models
from django.conf import settings

class Trazable(models.Model):
    """Base abstracta: quién creó el registro y cuándo se creó y modificó (RN-09)."""

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        editable=False,
        on_delete=models.PROTECT,
        related_name="+",
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
