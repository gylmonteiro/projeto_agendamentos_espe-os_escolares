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
        turma = request.POST.get('turma')
    

        Turma.objects.create(serie=serie, modalidade=modalidade, ano_inicio=ano_inicio, numero_alunos=numero_alunos, turma=turma)
        return redirect("listagem_turmas")
    
def turmas_detalhes(request):

    turmas = Turma.objects.all()
    if request.method == "GET":
        return render(request,"listagem_turmas.html", {'turmas': turmas})
    
def deletar_turmas(request, id):
    turma = Turma.objects.filter(pk=id)
    turma.delete()
    return redirect("listagem_turmas")

def atualizar_turmas(request, id):
    turma = Turma.objects.get(pk=id) 
    if request.method == "GET":
        
        return render(request, "formulario_atualizacao_turmas.html", {"turma": turma})
    elif request.method == "POST":
        
        turma_nomenclatura = request.POST.get("turma")
        numero_alunos = request.POST.get('numero_alunos')
        ano_inicio  = request.POST.get('ano_inicio')
        
        if turma_nomenclatura:
            turma.turma = turma_nomenclatura

        if numero_alunos:
            turma.numero_alunos  = numero_alunos

        if ano_inicio:
            turma.ano_inicio = ano_inicio
        turma.save()
        return redirect("listagem_turmas")