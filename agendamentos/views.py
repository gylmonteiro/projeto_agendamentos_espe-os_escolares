from django.shortcuts import render
from django.http import HttpResponse
from .models import Agendamento, Espaco, Horario
from turmas.models import Turma
# Create your views here.
def listar_agendamentos(request):
    if request.method == "GET":
        agendamentos = Agendamento.objects.all()
        return render(request, "listagem_agendamentos.html", {"agendamentos": agendamentos})
    

def criar_agendamento(request):
    espacos = Espaco.objects.all()
    turmas = Turma.objects.all()
    horarios = Horario.objects.all()
    if request.method == "GET":
        return render(request, 'formulario_agendamento.html', {"espacos": espacos, "turmas": turmas, "horarios": horarios})