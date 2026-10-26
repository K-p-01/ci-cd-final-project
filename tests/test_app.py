"""Unit tests for the Flask application."""

import unittest

from app import app


class AppTests(unittest.TestCase):
    """Basic endpoint checks run by nose."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CI/CD Final Project", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "status": "ok",
            "service": "cicd-final-project",
        })


if __name__ == "__main__":
    unittest.main()
