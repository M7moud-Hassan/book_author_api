from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Book(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Pages(models.Model):
    id = models.AutoField
    number = models.PositiveIntegerField()
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
