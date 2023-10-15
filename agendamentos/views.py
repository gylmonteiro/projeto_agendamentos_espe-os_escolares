from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Agendamento, Espaco, Horario
from turmas.models import Turma
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
# Create your views here.
def listar_agendamentos(request):
    if request.method == "GET":
        agendamentos = Agendamento.objects.all()
        return render(request, "listagem_agendamentos.html", {"agendamentos": agendamentos})
    
@login_required(login_url='acessar')
def criar_agendamento(request):
    # Receber todos os valores da que são disponibilizados na listagem de espaços disponíveis
    espaco = request.GET.get('espaco')
    data = request.GET.get('data')
  
    horario = request.GET.get('horario')
    
    # Filtrar os campos para listagem
    horario_filtrado = Horario.objects.get(id=horario)
    espaco_filtrado = Espaco.objects.get(id=espaco)

    # Consultar a lista de turmas que estão disponíveis no banco
    turmas = Turma.objects.all()
    
    if request.method == "GET":
        return render(request, 'formulario_agendamento.html', {"espaco": espaco_filtrado,"turmas": turmas, "horario": horario_filtrado, "data": data})
    
    if request.method =="POST":
        usuario_logado = request.user
        data_formatada = datetime.strptime(data, "%d/%m/%Y")      
        turma_id = request.POST.get("turma")
        turma = Turma.objects.get(pk=turma_id)
        espaco = espaco_filtrado
        usuario = usuario_logado
        

        Agendamento.objects.create(data_agendamento=data_formatada, turma=turma, espaco = espaco, responsavel=usuario, horario=horario_filtrado)
        return redirect("filtragem_agendamentos_sala")
    

def pesquisar_espaco(request):
    espacos = Espaco.objects.all()
    if request.method == "GET":
        return render (request, "pesquisa_espacos.html", {'espacos': espacos})
    elif request.method == "POST":
        # receber todos os horaríos
        horarios_disponiveis = Horario.objects.all()

        # formatar data para o campo django
        data = request.POST.get('data')
    
        data_formatada =  datetime.strptime(data, '%Y-%m-%d').date()
        # filtrando espaço através dos dados originados do POST na pesquisa de filtragem
        espaco_id = request.POST.get('espaco')
        espaco_filter = Espaco.objects.filter(pk=espaco_id)[0]
        agendamentos_sala = Agendamento.objects.filter(espaco=espaco_filter, data_agendamento=data_formatada)
        horarios_em_uso = agendamentos_sala.values_list('horario', flat=True)
        horarios_disponiveis = horarios_disponiveis.exclude(ordem__in=horarios_em_uso)

        return render (request, "listagem_agendamentos_sala.html", {'espaco': espaco_filter, 'horarios': horarios_disponiveis, 'agendamentos_sala':agendamentos_sala, 'data': data_formatada} )

