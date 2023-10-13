from django.db import models
from turmas.models import Turma
from usuarios.models import Usuario
# Create your models here.
class Espaco(models.Model):
    
    choies_tipos = (('A', 'AUDITÓRIO'), ('S', 'SALA DE AULA'), ('L', 'LABORATÓRIO'), ('G', 'GINÁSIO'), ('B', 'BIBLIOTECA'), ('V', 'SALA DE VÍDEO'), ('Q', 'QUADRA') )
    nome_sala = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choies_tipos, default="S")
    descricao = models.TextField(blank=True, null=True)
    max_ocupacao = models.IntegerField()
    disponibildiade = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.nome_sala} - {self.get_tipo_display()}"
    
class Horario(models.Model):
    ordem = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.ordem}º | {self.descricao}"
    

class Agendamento(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_agendamento = models.DateField()
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)
    espaco = models.ForeignKey(Espaco, on_delete=models.SET_NULL, null=True, blank=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Data: {self.data_agendamento} | Turma: {self.turma} | Responsável: {self.responsavel}"

