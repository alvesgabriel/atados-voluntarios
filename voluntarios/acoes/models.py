from django.db import models


class Acao(models.Model):
    nome = models.CharField(max_length=128)
    instituica = models.CharField(max_length=64)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=256)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
