from django.db import connection
from django.shortcuts import render


def inicio(request):
    """Pantalla de inicio provisional: confirma que la aplicación y la base de datos funcionan."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT version()")
        version_bd = cursor.fetchone()[0]
    return render(request, "core/inicio.html", {"version_bd": version_bd})