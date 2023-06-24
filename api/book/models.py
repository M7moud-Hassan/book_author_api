from django.db import models
from author.models import Author


# Create your models here
class Book(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Pages(models.Model):
    id = models.AutoField
    number = models.PositiveIntegerField()
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
