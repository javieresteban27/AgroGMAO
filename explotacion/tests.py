from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import Parametro, ClaseActividad

class ParametroTests(TestCase):
    def test_se_guarda_y_se_recupera_por_clave(self):
        Parametro.objects.create(clave="nombre_explotacion", valor="Finca Revilla")
        parametro = Parametro.objects.get(pk="nombre_explotacion")
        self.assertEqual(parametro.valor, "Finca Revilla")

    def test_texto_muestra_clave_y_valor(self):
        parametro = Parametro(clave="moneda", valor="EUR")
        self.assertEqual(str(parametro), "moneda = EUR")

class ClaseActividadTests(TestCase):
    def test_nace_activa(self):
        clase = ClaseActividad.objects.create(nombre="Taller", tarifa=Decimal("22.00"))
        self.assertTrue(clase.activa)

    def test_nombre_unico(self):
        ClaseActividad.objects.create(nombre="Taller", tarifa=Decimal("22.00"))
        with self.assertRaises(IntegrityError):
            ClaseActividad.objects.create(nombre="Taller", tarifa=Decimal("25.00"))

    def test_tarifa_no_puede_ser_negativa(self):
        clase = ClaseActividad(nombre="Taller", tarifa=Decimal("-1.00"))
        with self.assertRaises(ValidationError):
            clase.full_clean()

    def test_texto_muestra_nombre_y_tarifa(self):
        clase = ClaseActividad(nombre="Nocturnas", tarifa=Decimal("25.00"))
        self.assertEqual(str(clase), "Nocturnas (25.00 €/h)")