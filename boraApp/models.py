from django.db import models

# Create your models here.

class Lugar (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    esporte = models.CharField(max_length=255)

    class Meta:
        app_label = 'boraApp.models'

class Agendamento (models.Model):
    id = models.AutoField(primary_key=True)
    quadra = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    localidade = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    class Meta:
        app_label = 'boraApp.models'