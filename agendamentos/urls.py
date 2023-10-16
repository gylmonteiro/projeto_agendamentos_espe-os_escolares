from django.urls import path
from . import views

urlpatterns = [
    path("lista_agendamentos/", views.listar_agendamentos, name="lista_agendamentos"),
    path("agendar_espaco/", views.criar_agendamento, name="agenda_sala"),
    path("", views.pesquisar_espaco, name="pesquisa_espaco"),
    path("filtragem_agendamentos_por_sala/", views.pesquisar_espaco, name="filtragem_agendamentos_sala"),
    path("deletar_agendamentos/<int:id>", views.deleta_agendamento, name="deleta_agendamento"),
]