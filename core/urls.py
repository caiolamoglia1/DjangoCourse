from django.urls import path

from .views import artigos, cadastro, contato, home_page, login_page, logout_page, recursos, sobre

urlpatterns = [
    path("", home_page, name="home"),
    path("artigos/", artigos, name="artigos"),
    path("sobre/", sobre, name="sobre"),
    path("contato/", contato, name="contato"),
    path("recursos/", recursos, name="recursos"),
    path("cadastro/", cadastro, name="cadastro"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
]
