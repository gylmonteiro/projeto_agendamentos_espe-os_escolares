from django.db import models

# Create your models here.
class Turma(models.Model):
    choice_series = (('1', 'PRIMEIRO ANO'), ('2', 'SEGUNDO ANO'),('3', 'TERCEIRO ANO'))
    choice_modalidade = (('I', 'INTEGRAL'),('I.T', 'INTEGRAL | TÉCNICO'))
    choice_turno = (('M', 'MATUTINO'), ('V', 'VESPERTINO'), ('N', 'NOTURNO'))
    
    serie = models.CharField(max_length=1, choices=choice_series)
    modalidade =models.CharField(max_length=3, choices=choice_modalidade)
    turma = models.CharField(max_length=1, default="A")
    ano_inicio = models.IntegerField()
    turno = models.CharField(max_length=1, choices=choice_turno, default='M')
    numero_alunos = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.get_serie_display()} | {self.get_modalidade_display()}"