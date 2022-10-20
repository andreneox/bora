from django.db import models

# Create your models here.

class Lugar(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    esporte = models.CharField(max_length=255)

class Agendamento(models.Model):
    quadra = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    #localidade = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    inicio = models.TimeField()
    fim = models.DateTimeField()
