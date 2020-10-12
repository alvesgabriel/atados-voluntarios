from rest_framework import viewsets
from voluntarios.acoes import models, serializers


class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = models.Voluntario.objects.all().order_by("nome")
    serializer_class = serializers.VoluntarioDetailSerializer


class AcaoViewSet(viewsets.ModelViewSet):
    queryset = models.Acao.objects.all().order_by("nome")
    serializer_class = serializers.AcaoSerializer

    def get_serializer_class(self):
        if self.action in ("create", "partial_update", "update"):
            return serializers.AcaoCreateSerializer
        if self.action in ("retrieve", "list"):
            return serializers.AcaoDetailSerializer
