from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Tipo, Usuario
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
def acessar(request):
    return render(request, 'formulario_login.html')


def cadastrar_usuario(request):
    tipos = Tipo.objects.all()
    if request.method == "GET":
        return render(request, 'formulario_cadastro.html',{'tipos': tipos})
    elif request.method == "POST":
        try:
            usuario = Usuario()
            usuario.first_name = request.POST.get('nome')
            usuario.last_name = request.POST.get('sobrenome')
            usuario.username = request.POST.get('nome_de_usuario')
            usuario.email = request.POST.get('email')
            usuario.cpf = request.POST.get('cpf')
            usuario.matricula = request.POST.get('matricula')

            # confirmação de senha: Nesta etapa podemos fazer a verificação se as senhas são idênticas
            senha = request.POST.get('senha')
            confirma_senha = request.POST.get('confirma_senha')
            
            if senha != confirma_senha or len(senha) < 6:
                # inserir a menssagem de erro e redirecionar para o formulário de cadastro
                messages.add_message(request, constants.ERROR, 'As senhas não coincidem ou são menores que 6 caracteres')
                return redirect('cadastrar_usuario')
            
            usuario.save()
            tipos = request.POST.getlist('tipos')

            for tipo in tipos:
                tipo_temp = Tipo.objects.get(funcao=tipo)
                usuario.tipos.add(tipo_temp)

            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')

            return render(request, 'formulario_login.html')
        except:
            messages.add_message(request, constants.ERROR, 'Seu cadastro não pode ser realizado. Procure o administrador do sistema')

            return redirect('cadastrar_usuario')

        
    