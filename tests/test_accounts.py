import tempfile
import unittest
from pathlib import Path

from app import create_app


class AccountsTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        database = str(Path(self.temp_dir.name) / "test.db")
        app = create_app({"TESTING": True, "DATABASE": database})
        self.client = app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_health_and_security_headers(self):
        info = self.client.get("/")
        self.assertEqual(info.json, {"name": "Account REST API Service", "version": "1.0"})
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})
        self.assertIn("X-Content-Type-Options", response.headers)

    def test_account_crud(self):
        payload = {
            "first_name": "Ada",
            "last_name": "Lovelace",
            "email": "ada@example.com",
        }
        created = self.client.post("/accounts", json=payload)
        self.assertEqual(created.status_code, 201)
        account_id = created.json["id"]

        self.assertEqual(self.client.get("/accounts").json[0]["email"], payload["email"])
        self.assertEqual(self.client.get(f"/accounts/{account_id}").status_code, 200)

        updated = {**payload, "last_name": "Byron"}
        response = self.client.put(f"/accounts/{account_id}", json=updated)
        self.assertEqual(response.json["last_name"], "Byron")
        self.assertEqual(self.client.delete(f"/accounts/{account_id}").status_code, 204)
        self.assertEqual(self.client.get(f"/accounts/{account_id}").status_code, 404)

    def test_course_account_schema(self):
        payload = {
            "name": "John Doe",
            "email": "john@doe.com",
            "address": "123 Main St.",
            "phone_number": "555-1212",
        }
        response = self.client.post("/accounts", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], payload["name"])
        self.assertEqual(response.json["address"], payload["address"])

    def test_validation_and_missing_account(self):
        response = self.client.post("/accounts", json={"email": "bad"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.get("/accounts/999").status_code, 404)
        self.assertEqual(self.client.delete("/accounts/999").status_code, 404)

    def test_cors_preflight(self):
        response = self.client.options(
            "/accounts",
            headers={
                "Origin": "https://example.com",
                "Access-Control-Request-Method": "GET",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Access-Control-Allow-Origin", response.headers)
