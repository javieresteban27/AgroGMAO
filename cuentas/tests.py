from django.test import TestCase
from .models import Usuario

class UsuarioTests(TestCase):
    def test_perfil_por_defecto_es_operario(self):
        usuario = Usuario.objects.create_user(
            username="luis", password="clave-123"
        )
        self.assertEqual(usuario.perfil, Usuario.Perfil.OPERARIO)

    def test_texto_usa_nombre_completo_o_usuario(self):
        sin_nombre = Usuario(username="luis")
        con_nombre = Usuario(username="luis", first_name="Luis", last_name="González")
        self.assertEqual(str(sin_nombre), "luis")
        self.assertEqual(str(con_nombre), "Luis González")