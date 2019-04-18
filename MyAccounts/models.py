from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField()
    joinDate = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=100, choices=[('male', 'male'), ('female', 'female')])