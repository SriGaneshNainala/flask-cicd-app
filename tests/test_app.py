import unittest
from app import create_app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'running')

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_greet(self):
        response = self.client.get('/api/greet/SRE')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('Hello, SRE!', data['message'])


if __name__ == '__main__':
    unittest.main()
