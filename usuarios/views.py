from django.shortcuts import render
from django.http import HttpResponse
from . models import Tipo
# Create your views here.
def acessar(request):
    return render(request, 'formulario_login.html')


def cadastrar_usuario(request):
    tipos = Tipo.objects.all()
    if request.method == "GET":
        return render(request, 'formulario_cadastro.html', {'tipos': tipos})