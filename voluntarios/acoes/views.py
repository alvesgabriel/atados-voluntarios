from rest_framework import viewsets
from voluntarios.acoes import models, serializers


class AcaoViewSet(viewsets.ModelViewSet):
    queryset = models.Acao.objects.all().order_by("nome")
    serializer_class = serializers.AcaoSerializer
