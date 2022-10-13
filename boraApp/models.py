from django.db import models

# Create your models here.

class Lugar (models.Model):
    id = models.AutoField()
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    esporte = models.CharField(max_length=255)

class Agendamento (models.Model):
    id = models.AutoField()
    localidade = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()