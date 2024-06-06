from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(('password'), max_length=128)

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
