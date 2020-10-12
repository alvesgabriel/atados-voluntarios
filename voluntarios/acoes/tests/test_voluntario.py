from django.urls import reverse


def test_add_voluntario(client, voluntario):
    resp = client.post(reverse("voluntarios-list"), voluntario)
    assert resp.status_code == 201


def test_get_voluntario(client, voluntario_post):
    resp = client.get(reverse("voluntarios-detail", kwargs={"pk": voluntario_post["id"]}), voluntario_post)
    assert resp.status_code == 200
    assert resp.json() == voluntario_post


def test_update_voluntario(client, voluntario_post):
    voluntario_post["nome"] = "Frodo"
    resp = client.put(
        reverse("voluntarios-detail", kwargs={"pk": voluntario_post["id"]}),
        voluntario_post,
        content_type="application/json",
    )
    assert resp.status_code == 200
    assert resp.json() == voluntario_post


def test_delete_voluntario(client, voluntario_post):
    resp = client.delete(reverse("voluntarios-detail", kwargs={"pk": voluntario_post["id"]}))
    assert resp.status_code == 204
