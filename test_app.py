import unittest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


class TestFastAPIApp(unittest.TestCase):

    def test_home(self):
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Hello from my DevOps deployment!"},
        )

    def test_health(self):
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_add(self):
        response = client.get("/add/10/20")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 30})


if __name__ == "__main__":
    unittest.main()