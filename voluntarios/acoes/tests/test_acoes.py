import pytest
from django.urls import reverse
from model_bakery import baker
from voluntarios.acoes import serializers
from voluntarios.acoes.models import Acao


@pytest.fixture
def acao(db):
    acao_modelo = baker.make(Acao)
    return serializers.AcaoSerializer(acao_modelo).data


def test_add_acao(client, acao):
    resp = client.post(reverse("acoes-list"), acao)
    assert resp.status_code == 201


@pytest.fixture
def acao_post(client, acao):
    resp = client.post(reverse("acoes-list"), acao)
    return resp.json()


def test_get_acao(client, acao_post):
    resp = client.get(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    assert resp.status_code == 200


def test_update_acao(client, acao_post):
    acao_post["nome"] = "Destruir o Um Anel"
    resp = client.put(
        reverse("acoes-detail", kwargs={"pk": acao_post["id"]}), acao_post, content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.json() == acao_post


def test_delete_acao(client, acao_post):
    resp = client.delete(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    assert resp.status_code == 204
