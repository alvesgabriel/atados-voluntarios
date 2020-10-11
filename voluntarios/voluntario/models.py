from django.db import models


class Voluntario(models.Model):
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
