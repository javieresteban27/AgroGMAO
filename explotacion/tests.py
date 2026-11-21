from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.db.models import ProtectedError

from cuentas.models import Usuario

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

class TrazabilidadTests(TestCase):
    def test_registra_fecha_de_creacion_y_de_modificacion(self):
        clase = ClaseActividad.objects.create(nombre="Taller", tarifa=Decimal("22.00"))
        creado = clase.creado_en
        self.assertIsNotNone(creado)
        clase.tarifa = Decimal("25.00")
        clase.save()
        clase.refresh_from_db()
        self.assertEqual(clase.creado_en, creado)
        self.assertGreaterEqual(clase.modificado_en, creado)

    def test_creado_por_es_opcional(self):
        clase = ClaseActividad.objects.create(nombre="Taller", tarifa=Decimal("22.00"))
        self.assertIsNone(clase.creado_por)

    def test_no_se_puede_borrar_un_usuario_con_registros(self):
        usuario = Usuario.objects.create_user(
            username="ana", password="clave-123"
        )
        ClaseActividad.objects.create(
            nombre="Taller", tarifa=Decimal("22.00"), creado_por=usuario
        )
        with self.assertRaises(ProtectedError):
            usuario.delete()
