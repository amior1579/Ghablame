from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):

    def __str__(self):
        return f'{self.id},{self.username}'
