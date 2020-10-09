def test_admin_status_code(client):
    resp = client.get("/admin")
    assert resp.status_code == 301
