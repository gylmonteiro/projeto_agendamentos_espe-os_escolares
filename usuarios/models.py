from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Tipo(models.Model):
    choice_funcoes = (("C", "COORDENADOR"), ("P", "PROFESSOR"), ("D", "DIRETOR"), ("A", "ALUNO"), ("AP", "APOIO_PEDAGOGICO"))
    funcao = models.CharField(max_length=60, choices=choice_funcoes, unique=True )

    def __str__(self) -> str:
        return self.funcao
    

class Usuario(AbstractUser):
    tipos = models.ManyToManyField(Tipo)
    matricula = models.IntegerField(unique=True, null=True)
    cpf = models.CharField(max_length=12, unique=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} | Matrícula: {self.matricula}"