from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.turmas, name="cadastrar_turmas"),
    path("lista_turmas/", views.turmas_detalhes, name="listagem_turmas"),
    path("deleta_turmas/<int:id>", views.deletar_turmas, name = "deleta_turmas" ),
    path("atualiza_turma/<int:id>", views.atualizar_turmas, name="atualiza_turmas")
]