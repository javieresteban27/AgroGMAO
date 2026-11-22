from django.contrib.auth import views as vistas_auth
from django.urls import path

urlpatterns = [
    path(
        "entrar/",
        vistas_auth.LoginView.as_view(
            template_name="cuentas/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("salir/", vistas_auth.LogoutView.as_view(), name="logout"),
]