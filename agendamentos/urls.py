from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_agendamentos, name="lista_agendamentos"),
    path("agendar_espaco", views.criar_agendamento, name="agenda_sala")
    
]