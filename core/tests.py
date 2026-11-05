from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders


class InicioTests(TestCase):
    def test_inicio_responde_y_conecta_con_la_base_de_datos(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "AgroGMAO")
        self.assertContains(respuesta, "PostgreSQL")

    def test_usa_la_plantilla_base_mobile_first(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, '<html lang="es">')
        self.assertContains(respuesta, 'name="viewport"')
        self.assertContains(respuesta, "navbar-toggler")

    def test_bootstrap_se_sirve_en_local(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertNotContains(respuesta, "cdn.")
        self.assertIsNotNone(finders.find("core/vendor/bootstrap/bootstrap.min.css"))
        self.assertIsNotNone(finders.find("core/vendor/bootstrap/bootstrap.bundle.min.js"))