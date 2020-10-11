from rest_framework import serializers
from voluntarios.voluntario import models


class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Voluntario
        fields = "__all__"
