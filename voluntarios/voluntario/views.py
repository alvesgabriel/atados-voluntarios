from rest_framework import viewsets
from voluntarios.voluntario import models
from voluntarios.voluntario.serializers import VoluntarioSerializer


class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = models.Voluntario.objects.all().order_by("nome")
    serializer_class = VoluntarioSerializer
