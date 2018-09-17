from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    cnpj = models.CharField(max_length=30)
    razao = models.CharField(max_length=200)
    fantazia = models.CharField(max_length=200)
    contato = models.CharField(max_length=30)

    def __str__(self):
        return self.fantazia


class Sistemas(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    numero = models.AutoField(primary_key=True)
    nomeFantazia = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_ini = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    reclamado = models.TextField()
    sistema = models.ForeignKey(Sistemas, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
       return str(self.numero)

    def valida(self):
        self.data_ini = timezone.now()
        self.save()
