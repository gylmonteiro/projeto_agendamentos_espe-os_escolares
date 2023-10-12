from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.turmas, name="cadastrar_turmas"),
    path("lista_turmas/", views.turmas_detalhes, name="listagem_turmas")
   
]