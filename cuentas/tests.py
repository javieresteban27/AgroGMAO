from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Usuario

class UsuarioTests(TestCase):
    def test_django_usa_nuestro_modelo_de_usuario(self):
        self.assertIs(get_user_model(), Usuario)

    def test_nace_activo(self):
        usuario = Usuario.objects.create_user(
            username="luis", password="clave-123"
        )
        self.assertTrue(usuario.is_active)