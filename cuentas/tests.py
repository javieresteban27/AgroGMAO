from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

from django.core.exceptions import PermissionDenied
from django.test import RequestFactory
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

from .permisos import (
    GERENTE,
    MECANICO,
    OPERARIO,
    PerfilRequeridoMixin,
    perfil_requerido,
    tiene_perfil,
)

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

class SeguridadTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="luis", password="clave-123"
        )

    def test_la_contrasena_se_guarda_con_hash(self):
        self.assertNotIn("clave-123", self.usuario.password)
        self.assertTrue(self.usuario.check_password("clave-123"))

    def test_el_formulario_exige_token_csrf(self):
        cliente = Client(enforce_csrf_checks=True)
        respuesta = cliente.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        self.assertEqual(respuesta.status_code, 403)

    def test_la_cookie_de_sesion_no_es_accesible_desde_javascript(self):
        self.client.post(
            reverse("login"), {"username": "luis", "password": "clave-123"}
        )
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        self.assertTrue(cookie["httponly"])
        self.assertEqual(cookie["samesite"], "Lax")

    def test_el_formulario_esta_pensado_para_el_movil(self):
        respuesta = self.client.get(reverse("login"))
        self.assertContains(respuesta, 'autocomplete="username"')
        self.assertContains(respuesta, 'autocomplete="current-password"')
        self.assertContains(respuesta, "form-control-lg")

class GruposDePerfilTests(TestCase):
    def test_los_tres_grupos_existen_tras_migrar(self):
        nombres = set(Group.objects.values_list("name", flat=True))
        self.assertLessEqual({"Operario", "Mecánico", "Gerente"}, nombres)

class PermisosTests(TestCase):
    def crear_usuario(self, nombre, *grupos, **extra):
        usuario = Usuario.objects.create_user(
            username=nombre, password="clave-123", **extra
        )
        for grupo in grupos:
            usuario.groups.add(Group.objects.get(name=grupo))
        return usuario

    def test_un_perfil_solo_pasa_con_su_grupo(self):
        operario = self.crear_usuario("operario", OPERARIO)
        self.assertTrue(tiene_perfil(operario, OPERARIO))
        self.assertFalse(tiene_perfil(operario, GERENTE))

    def test_cada_perfil_se_distingue_de_los_demas(self):
        for perfil in (OPERARIO, MECANICO, GERENTE):
            usuario = self.crear_usuario(f"u-{perfil}", perfil)
            otros = {OPERARIO, MECANICO, GERENTE} - {perfil}
            self.assertTrue(tiene_perfil(usuario, perfil))
            for otro in otros:
                self.assertFalse(tiene_perfil(usuario, otro))

    def test_un_usuario_con_varios_grupos_suma_sus_permisos(self):
        todoterreno = self.crear_usuario("todo", OPERARIO, MECANICO, GERENTE)
        self.assertTrue(tiene_perfil(todoterreno, GERENTE))
        self.assertTrue(tiene_perfil(todoterreno, MECANICO))
        mecanico_y_operario = self.crear_usuario("dos", OPERARIO, MECANICO)
        self.assertTrue(tiene_perfil(mecanico_y_operario, MECANICO, GERENTE))
        self.assertFalse(tiene_perfil(mecanico_y_operario, GERENTE))

    def test_sin_grupos_no_hay_perfil(self):
        sin_perfil = self.crear_usuario("nadie")
        self.assertFalse(tiene_perfil(sin_perfil, OPERARIO, MECANICO, GERENTE))

    def test_un_anonimo_no_tiene_perfil(self):
        self.assertFalse(tiene_perfil(AnonymousUser(), OPERARIO))

    def test_el_superusuario_pasa_siempre(self):
        admin = Usuario.objects.create_superuser("admin", password="clave-123")
        self.assertTrue(tiene_perfil(admin, GERENTE))

    def test_el_decorador_deja_pasar_o_deniega(self):
        @perfil_requerido(GERENTE)
        def vista(request):
            return HttpResponse("ok")

        fabrica = RequestFactory()
        peticion = fabrica.get("/")
        peticion.user = self.crear_usuario("gerente", GERENTE)
        self.assertEqual(vista(peticion).status_code, 200)

        peticion.user = self.crear_usuario("operario", OPERARIO)
        with self.assertRaises(PermissionDenied):
            vista(peticion)

    def test_el_mixin_deja_pasar_o_deniega(self):
        class VistaDeGerente(PerfilRequeridoMixin, View):
            perfiles = (GERENTE,)

            def get(self, request):
                return HttpResponse("ok")

        fabrica = RequestFactory()
        peticion = fabrica.get("/")
        peticion.user = self.crear_usuario("gerente", GERENTE)
        self.assertEqual(VistaDeGerente.as_view()(peticion).status_code, 200)

        peticion.user = self.crear_usuario("mecanico", MECANICO)
        with self.assertRaises(PermissionDenied):
            VistaDeGerente.as_view()(peticion)