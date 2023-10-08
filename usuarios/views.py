from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cadastrar_usuario(request):
    return render(request, 'formulario_login.html')