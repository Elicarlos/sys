from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    codigo = models.ForeingKey('auth.User', on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=30)
    razao = models.CharField(max_length=200)
    fantazia = models.CharField(max_length=200)
    sistema = models.CharField(max_length=30)
    contato = models.CharField(max_length=30)





class Atendimento(models.Model):
    numero = models.
    data_ini =
    data_fim
    reclamado =


class Tecnico(models.Model):
    codigo = 
    nome = models.CharField(max_length=200)
