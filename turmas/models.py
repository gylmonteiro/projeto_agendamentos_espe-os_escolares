from django.db import models

# Create your models here.
class Turma(models.Model):
    choice_series = (('1', 'PRIMEIRO ANO'), ('2', 'SEGUNDO ANO'),('3', 'TERCEIRO ANO'))
    choice_modalidade = (('I', 'INTEGRAL'),('I.T', 'INTEGRAL | TÉCNICO'))
    
    serie = models.CharField(max_length=1, choices=choice_series)
    modalidade =models.CharField(max_length=3, choices=choice_modalidade)
    ano_inicio = models.IntegerField()
    numero_alunos = models.IntegerField()


    def __str__(self) -> str:
        return f"Turma: {self.get_serie_display()} | Modalidade: {self.get_modalidade_display()}"