from rest_framework.test import APITestCase


class GreetingTests(APITestCase):
    def test_greeting_uses_name(self):
        response = self.client.get("/api/greeting/", {"name": "Kyle"})
        self.assertEqual(response.json(), {"message": "Hello, Kyle!"})

    def test_greeting_defaults_to_world(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.json(), {"message": "Hello, world!"})
