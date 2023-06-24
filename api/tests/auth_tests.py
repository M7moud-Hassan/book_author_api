from unittest import TestCase
from  author.models import Author

class AuthorModelTestCase(TestCase):
    def test_Author_creation(self):
        Author.objects.create(username='mahmoud',email='')