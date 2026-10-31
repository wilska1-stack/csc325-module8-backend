from rest_framework.test import APITestCase


class GreetingTests(APITestCase):
    def test_greeting_uses_name(self):
        response = self.client.get("/api/greeting/", {"name": "Kyle"})
        self.assertEqual(response.json(), {"message": "Hello, Kyle!", "length": 12})

    def test_greeting_defaults_to_world(self):
        response = self.client.get("/api/greeting/")
        self.assertEqual(response.json(), {"message": "Hello, world!", "length": 13})

    def test_greeting_includes_message_length(self):
        response = self.client.get("/api/greeting/", {"name": "Ada"})
        data = response.json()
        self.assertEqual(data["length"], len(data["message"]))
