from django.test import TestCase
from django.db import IntegrityError
from django.db.models import ProtectedError

from .models import TipoEquipo, Equipo

class TipoEquipoTests(TestCase):
    def test_nace_activa(self):
        familia = TipoEquipo.objects.create(nombre="Tractor")
        self.assertTrue(familia.activa)

    def test_nombre_unico(self):
        TipoEquipo.objects.create(nombre="Tractor")
        with self.assertRaises(IntegrityError):
            TipoEquipo.objects.create(nombre="Tractor")

    def test_texto_es_el_nombre(self):
        self.assertEqual(str(TipoEquipo(nombre="Cosechadora")), "Cosechadora")

class EquipoTests(TestCase):
    def setUp(self):
        self.familia = TipoEquipo.objects.create(nombre="Tractor")

    def test_nace_activo(self):
        equipo = Equipo.objects.create(
            denominacion="Tractor grande", familia=self.familia
        )

    def test_serie_unica_si_se_informa(self):
        Equipo.objects.create(
            denominacion="A", familia=self.familia, numero_serie="X123"
        )
        with self.assertRaises(IntegrityError):
            Equipo.objects.create(
                denominacion="B", familia=self.familia, numero_serie="X123"
            )

    def test_varios_equipos_pueden_no_tener_serie(self):
        Equipo.objects.create(denominacion="A", familia=self.familia)
        Equipo.objects.create(denominacion="B", familia=self.familia)
        self.assertEqual(Equipo.objects.count(), 2)

    def test_no_se_puede_borrar_una_familia_con_equipos(self):
        Equipo.objects.create(denominacion="A", familia=self.familia)
        with self.assertRaises(ProtectedError):
            self.familia.delete()

    def test_texto_es_la_denominacion(self):
        equipo = Equipo(denominacion="Tractor viejo", familia=self.familia)
        self.assertEqual(str(equipo), "Tractor viejo")