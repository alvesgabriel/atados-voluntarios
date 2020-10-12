import pytest
from django.urls import reverse
from model_bakery import baker
from voluntarios.acoes import serializers
from voluntarios.acoes.models import Acao


@pytest.fixture
def acao(db):
    acao_modelo = baker.make(Acao)
    return serializers.AcaoDetailSerializer(acao_modelo).data


def test_add_acao(client, acao):
    resp = client.post(reverse("acoes-list"), acao)
    assert resp.status_code == 201


@pytest.fixture
def acao_post(client, acao, voluntario):
    acao["voluntarios"] = [voluntario["id"]]
    resp = client.post(reverse("acoes-list"), acao, content_type="application/json")
    acao_post = resp.json()
    acao_post["voluntarios_display"] = [voluntario]
    return acao_post


def test_get_acao(client, acao_post):
    resp = client.get(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    assert resp.status_code == 200


def test_update_acao(client, acao_post):
    acao_post["nome"] = "Destruir o Um Anel"
    acao_post.pop("voluntarios_display")
    resp = client.put(
        reverse("acoes-detail", kwargs={"pk": acao_post["id"]}), acao_post, content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.json() == acao_post


def test_delete_acao(client, acao_post):
    resp = client.delete(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    assert resp.status_code == 204


def test_get_voluntario_in_acoes(client, acao_post):
    resp = client.get(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    acao_json = resp.json()
    assert len(acao_json.get("voluntarios")) == 1
    assert acao_json.get("voluntarios") == acao_post["voluntarios_display"]


def test_update_voluntarios_in_acoes(client, acao_post, voluntarios_list):
    acao_post["voluntarios"] = [voluntario.id for voluntario in voluntarios_list]
    client.put(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}), acao_post, content_type="application/json")
    resp = client.get(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    acao_json = resp.json()
    assert len(acao_json.get("voluntarios")) == 2


def test_update_zero_voluntarios_in_acoes(client, acao_post):
    acao_post["voluntarios"] = []
    client.put(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}), acao_post, content_type="application/json")
    resp = client.get(reverse("acoes-detail", kwargs={"pk": acao_post["id"]}))
    acao_json = resp.json()
    assert len(acao_json.get("voluntarios")) == 0


def test_add_acao_with_repeat_voluntario(client, acao, voluntario):
    acao["voluntarios"] = [voluntario, voluntario]
    resp = client.post(reverse("acoes-list"), acao, content_type="application/json")
    assert resp.status_code == 400
