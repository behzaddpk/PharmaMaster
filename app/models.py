from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 


# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, 'Admin'),
        (2, 'User')
    )
    user_type = models.CharField(choices=USER_TYPE, max_length=25, default=1)