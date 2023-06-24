from django.test import TestCase, Client


class AuthAPITestCase(TestCase):

    def test_api_register_view(self):
        client = Client()
        response = client.post('/auth/register_reader', {
            "username": "test1",
            "email": "test1@gmail.com",
            "password": '12345678'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})

    def test_api_login_view(self):
        client = Client()
        response = client.post('/auth/login', {
            "username": "test1",
            "password": '12345678'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})
