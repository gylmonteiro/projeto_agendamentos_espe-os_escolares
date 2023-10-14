from django.shortcuts import render
from django.http import HttpResponse
from .models import Agendamento, Espaco, Horario
from turmas.models import Turma
from datetime import datetime
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
    

def pesquisar_espaco(request):
    espacos = Espaco.objects.all()
    if request.method == "GET":
        return render (request, "pesquisa_espacos.html", {'espacos': espacos})
    elif request.method == "POST":
        horarios = Horario.objects.all()
        data = request.POST.get('data')
        data_formatada =  datetime.strptime(data, '%Y-%m-%d').date()
        espaco_id = request.POST.get('espaco')
        espaco_filter = Espaco.objects.filter(pk=espaco_id)[0]
        agendamentos_sala = Agendamento.objects.filter(espaco=espaco_filter)

        return render (request, "listagem_agendamentos_sala.html", {'espaco': espaco_filter, 'horarios': horarios, 'agendamentos_sala':agendamentos_sala, 'data': data_formatada} )

# def lista_agendamentos_sala(request):
#     if request.method == "POST":
#         return render(request, "listagem_agendamentos_sala.html")