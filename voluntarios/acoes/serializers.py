from rest_framework import serializers
from voluntarios.acoes import models


class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acao
        fields = (
            "id",
            "nome",
            "instituicao",
            "cep",
            "endereco",
            "bairro",
            "cidade",
            "descricao",
            "data_criacao",
        )


class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Voluntario
        fields = (
            "id",
            "nome",
            "sobrenome",
            "bairro",
            "cidade",
        )


class VoluntarioDetailSerializer(serializers.ModelSerializer):
    acoes = AcaoSerializer(many=True, read_only=True)

    class Meta:
        model = models.Voluntario
        fields = (
            "id",
            "nome",
            "sobrenome",
            "bairro",
            "cidade",
            "acoes",
        )


class AcaoCreateSerializer(serializers.ModelSerializer):
    voluntarios = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Voluntario.objects.all(), required=False
    )

    class Meta:
        model = models.Acao
        fields = (
            "id",
            "nome",
            "instituicao",
            "cep",
            "endereco",
            "bairro",
            "cidade",
            "descricao",
            "data_criacao",
            "voluntarios",
        )


class AcaoDetailSerializer(serializers.ModelSerializer):
    voluntarios = VoluntarioSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = models.Acao
        fields = (
            "id",
            "nome",
            "instituicao",
            "cep",
            "endereco",
            "bairro",
            "cidade",
            "descricao",
            "data_criacao",
            "voluntarios",
        )
