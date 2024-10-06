from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ci = models.CharField(max_length=11)

    def __str__(self):
        return self.username