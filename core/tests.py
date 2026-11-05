from django.test import TestCase
from django.urls import reverse


class InicioTests(TestCase):
    def test_inicio_responde_y_conecta_con_la_base_de_datos(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "AgroGMAOxx")
        self.assertContains(respuesta, "PostgreSQL")