from django.shortcuts import render,redirect
from .models import Agendamento, Espaco, Horario
from turmas.models import Turma
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
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
        # Recebendo usuario através da sessão de login
        usuario_logado = request.user
        # Formatação do campo data para que possa ser usando na instância do objeto agendamento
        data_formatada = datetime.strptime(data, "%d/%m/%Y")      
        turma_id = request.POST.get("turma")
        turma = Turma.objects.get(pk=turma_id)
        # rever essas partes do código
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

        # Resgatar usuario logado 
        usuario_ativo = request.user
        # Mensagem para informar que o usuário deverá ter cadastrado e estar logado para poder realizar o agendamento
        
        if request.user.is_anonymous:
            messages.add_message(request, constants.WARNING, 'Para realizar o agendamento, você deverá estar logado!')
        else:
            messages.add_message(request, constants.SUCCESS, 'Você consegue fazer o agendamento para os horários disponíveis!')

        return render (request, "listagem_agendamentos_sala.html", {'espaco': espaco_filter, 'horarios': horarios_disponiveis, 'agendamentos_sala':agendamentos_sala, 'data': data_formatada, 'usuario': usuario_ativo} )

def deleta_agendamento(request, id):
    agendamento = Agendamento.objects.get(pk=id)
    Agendamento.delete(agendamento)
    messages.add_message(request, constants.SUCCESS, 'Agendamento desmarcado com sucesso')
    return redirect("pesquisa_espaco")