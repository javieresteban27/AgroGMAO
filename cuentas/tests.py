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

    def test_el_error_es_el_mismo_si_falla_el_usuario_o_la_contrasena(self):
        usuario_inexistente = self.client.post(
            reverse("login"), {"username": "nadie", "password": "clave-123"}
        )
        contrasena_incorrecta = self.client.post(
            reverse("login"), {"username": "luis", "password": "otra-clave"}
        )
        errores_1 = usuario_inexistente.context["form"].non_field_errors()
        errores_2 = contrasena_incorrecta.context["form"].non_field_errors()
        self.assertTrue(errores_1)
        self.assertEqual(errores_1, errores_2)

class BloqueoTests(TestCase):
    def setUp(self):
        Usuario.objects.create_user(username="luis", password="clave-123")

    def fallar(self, veces):
        for _ in range(veces):
            self.client.post(
                reverse("login"), {"username": "luis", "password": "incorrecta"}
            )

    def test_se_bloquea_tras_demasiados_intentos_fallidos(self):
        self.fallar(3)
        respuesta = self.client.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        self.assertContains(respuesta, "bloqueado", status_code=429)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_un_acceso_correcto_reinicia_el_contador(self):
        self.fallar(2)
        entrada = self.client.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        self.assertEqual(entrada.status_code, 302)
        self.client.post(reverse("logout"))
        self.fallar(2)
        entrada = self.client.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        self.assertEqual(entrada.status_code, 302)

    def test_el_bloqueo_no_depende_de_que_el_usuario_exista(self):
        for _ in range(3):
            self.client.post(
                reverse("login"), {"username": "inexistente", "password": "incorrecta"}
            )
        respuesta = self.client.post(
            reverse("login"), {"username": "inexistente", "password": "incorrecta"}
        )
        self.assertContains(respuesta, "bloqueado", status_code=429)