from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Turma
# Create your views here.
def turmas(request):
    if request.method ==  "GET":
        return render(request, "formulario_cadastro_turmas.html")
    elif request.method == "POST":

        serie = request.POST.get('serie')
        modalidade = request.POST.get('modalidade')
        numero_alunos = request.POST.get('numero_alunos')
        ano_inicio  = request.POST.get('ano_inicio')

        turma = Turma.objects.create(serie=serie, modalidade=modalidade, ano_inicio=ano_inicio, numero_alunos=numero_alunos)
        return redirect("cadastrar_turmas")
    
def turmas_detalhes(request):

    turmas = Turma.objects.all()
    if request.method == "GET":
        return render(request,"listagem_turmas.html", {'turmas': turmas})