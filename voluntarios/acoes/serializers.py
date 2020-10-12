from rest_framework import serializers
from voluntarios.acoes import models


class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Voluntario
        fields = "__all__"


class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acao
        fields = "__all__"
