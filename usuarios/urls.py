from django.urls import path
from . import views
urlpatterns = [
    path("acessar/", views.acessar,name="acessar"),
    path("cadastrar_usuario", views.cadastrar_usuario, name="cadastrar_usuario"),
]