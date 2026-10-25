import pytest

from app import create_app


@pytest.fixture()
def client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.db")})
    return app.test_client()


def test_health_and_security_headers(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
    assert "X-Content-Type-Options" in response.headers


def test_account_crud(client):
    payload = {"first_name": "Ada", "last_name": "Lovelace", "email": "ada@example.com"}
    created = client.post("/accounts", json=payload)
    assert created.status_code == 201
    account_id = created.json["id"]

    assert client.get("/accounts").json[0]["email"] == payload["email"]
    assert client.get(f"/accounts/{account_id}").status_code == 200

    updated = {**payload, "last_name": "Byron"}
    assert client.put(f"/accounts/{account_id}", json=updated).json["last_name"] == "Byron"
    assert client.delete(f"/accounts/{account_id}").status_code == 204
    assert client.get(f"/accounts/{account_id}").status_code == 404


def test_validation_and_missing_account(client):
    assert client.post("/accounts", json={"email": "bad"}).status_code == 400
    assert client.get("/accounts/999").status_code == 404
    assert client.delete("/accounts/999").status_code == 404


def test_cors_preflight(client):
    response = client.options(
        "/accounts",
        headers={"Origin": "https://example.com", "Access-Control-Request-Method": "GET"},
    )
    assert response.status_code == 200
    assert "Access-Control-Allow-Origin" in response.headers
