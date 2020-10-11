from rest_framework import serializers
from voluntarios.acoes import models


class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acao
        fields = "__all__"
