from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class GreetingEndpointTests(APITestCase):
    def test_greeting_uses_name_from_query(self):
        response = self.client.get("/api/greeting/", {"name": "Kyle"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Hello, Kyle!")

    def test_greeting_defaults_to_world(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.json()["message"], "Hello, world!")
