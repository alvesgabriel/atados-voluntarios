import pytest
from django.urls import reverse
from model_bakery import baker

from voluntarios.acoes import serializers
from voluntarios.acoes.models import Voluntario


@pytest.fixture
def voluntario(db):
    voluntario_modelo = baker.make(Voluntario)
    return serializers.VoluntarioSerializer(voluntario_modelo).data


@pytest.fixture
def voluntario_post(client, voluntario):
    resp = client.post(reverse("voluntarios-list"), voluntario, content_type="application/json")
    return resp.json()


@pytest.fixture
def voluntarios_list(db):
    return baker.make(Voluntario, 2)
