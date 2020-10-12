from django.db import models


class Voluntario(models.Model):
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    acoes = models.ManyToManyField("Acao", through="Inscrito")


class Acao(models.Model):
    nome = models.CharField(max_length=128)
    instituicao = models.CharField(max_length=64)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=256)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    voluntarios = models.ManyToManyField(
        Voluntario, through="Inscrito", through_fields=("acao", "voluntario"), related_name="voluntarios"
    )


class Inscrito(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
