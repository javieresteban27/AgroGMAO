from django.test import TestCase
from django.db import IntegrityError

from .models import TipoEquipo

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