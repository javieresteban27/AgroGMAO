from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Usuario

class UsuarioTests(TestCase):
    def test_django_usa_nuestro_modelo_de_usuario(self):
        self.assertIs(get_user_model(), Usuario)

    def test_nace_activo(self):
        usuario = Usuario.objects.create_user(
            username="luis", password="clave-123"
        )
        self.assertTrue(usuario.is_active)

class AutenticacionTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="luis", password="clave-123"
        )

    def test_la_pantalla_de_entrada_se_muestra(self):
        respuesta = self.client.get(reverse("login"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Entrar")

    def test_entra_con_credenciales_correctas_y_va_al_inicio(self):
        respuesta = self.client.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        self.assertRedirects(respuesta, reverse("inicio"))

    def test_credenciales_incorrectas_no_abren_sesion(self):
        respuesta = self.client.post(
            reverse("login"), {"username": "luis", "password": "otra-clave"}
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotIn("auth_user_id", self.client.session)

    def test_salir_cierra_la_sesion(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse("logout"))
        self.assertRedirects(respuesta, reverse("login"))
        self.assertNotIn("_auth_user_id", self.client.session)