from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(User):
    image = models.ImageField(upload_to='images/')
