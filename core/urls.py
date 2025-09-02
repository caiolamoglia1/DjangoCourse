from django.urls import path

from .views import (
    artigos,
    avatar_test,
    cadastro,
    cadastro_simples,
    contato,
    home_page,
    login_page,
    logout_page,
    perfil,
    recursos,
    sobre,
)

urlpatterns = [
    path("", home_page, name="home"),
    path("artigos/", artigos, name="artigos"),
    path("sobre/", sobre, name="sobre"),
    path("contato/", contato, name="contato"),
    path("recursos/", recursos, name="recursos"),
    path("cadastro/", cadastro, name="cadastro"),
    path("cadastro-simples/", cadastro_simples, name="cadastro_simples"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("perfil/", perfil, name="perfil"),
    path("avatar-test/", avatar_test, name="avatar_test"),
]
