from django.test import TestCase
from .models import Parametro

class ParametroTests(TestCase):
    def test_se_guarda_y_se_recupera_por_clave(self):
        Parametro.objects.create(clave="nombre_explotacion", valor="Finca Revilla")
        parametro = Parametro.objects.get(pk="nombre_explotacion")
        self.assertEqual(parametro.valor, "Finca Revilla")

    def test_texto_muestra_clave_y_valor(self):
        parametro = Parametro(clave="moneda", valor="EUR")
        self.assertEqual(str(parametro), "moneda = EUR")