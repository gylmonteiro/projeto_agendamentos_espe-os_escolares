from django.urls import path
from . import views

urlpatterns = [
    path("lista_agendamentos/", views.listar_agendamentos, name="lista_agendamentos"),
    path("agendar_espaco/", views.criar_agendamento, name="agenda_sala"),
    path("", views.pesquisar_espaco, name="pesquisa_espaco"),
    path("filtragem_agendamentos_por_sala/", views.pesquisar_espaco, name="filtragem_agendamentos_sala"),
    # path("agendamentos_por_sala/", views.lista_agendamentos_sala, name="agendamentos_sala"),
]