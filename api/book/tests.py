
from django.test import TestCase, Client


class BooAPITestCase(TestCase):

    def test_api_list_book_view(self):
        client = Client()
        response = client.get('/home/books/',headers={
            "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjMxNjMxLCJpYXQiOjE2ODc2MjgwMzEsImp0aSI6ImQxNjFkYTdhMGM0OTRmMjBiOTQ2MTQwNzI3MjNmYjc4IiwidXNlcl9pZCI6MX0.vMpI8Ic2XabP1r6szM7Yn8XSN8P1O4_TcfIOTVYupvo',
            'Content-Type': 'multipart/form-data'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})

    def test_api_create_book_view(self):
            client = Client()
            response = client.get('/home/create_book/',{
                'name':'name of book'
            }, headers={
                "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjMxNjMxLCJpYXQiOjE2ODc2MjgwMzEsImp0aSI6ImQxNjFkYTdhMGM0OTRmMjBiOTQ2MTQwNzI3MjNmYjc4IiwidXNlcl9pZCI6MX0.vMpI8Ic2XabP1r6szM7Yn8XSN8P1O4_TcfIOTVYupvo',
                'Content-Type': 'multipart/form-data'
            })

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"message": "Success"})


    def test_api_update_book_view(self):
        client = Client()
        response = client.get('/home/update_book/',{
            'id':1,
            'name':'new name book'
        },headers={
            "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjMxNjMxLCJpYXQiOjE2ODc2MjgwMzEsImp0aSI6ImQxNjFkYTdhMGM0OTRmMjBiOTQ2MTQwNzI3MjNmYjc4IiwidXNlcl9pZCI6MX0.vMpI8Ic2XabP1r6szM7Yn8XSN8P1O4_TcfIOTVYupvo',
            'Content-Type': 'multipart/form-data'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})

    def test_api_delete_book_view(self):
        client = Client()
        response = client.get('/home/delete_book/',{
            'id':1,
        },headers={
            "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjMxNjMxLCJpYXQiOjE2ODc2MjgwMzEsImp0aSI6ImQxNjFkYTdhMGM0OTRmMjBiOTQ2MTQwNzI3MjNmYjc4IiwidXNlcl9pZCI6MX0.vMpI8Ic2XabP1r6szM7Yn8XSN8P1O4_TcfIOTVYupvo',
            'Content-Type': 'multipart/form-data'
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "Success"})

    def test_api_create_page_view(self):
        client = Client()
        response = client.get('/home/create_page/', {
           'book_id':1,
            'number':'2',
            'content':'<p>title</p>'
        }, headers={
            "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjMxNjMxLCJpYXQiOjE2ODc2MjgwMzEsImp0aSI6ImQxNjFkYTdhMGM0OTRmMjBiOTQ2MTQwNzI3MjNmYjc4IiwidXNlcl9pZCI6MX0.vMpI8Ic2XabP1r6szM7Yn8XSN8P1O4_TcfIOTVYupvo',
            'Content-Type': 'multipart/form-data'
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "Success"})