from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    #adding fields into the database
    age = models.PositiveIntegerField(null = True, blank = True)
    experience = models.PositiveIntegerField(null = True, blank=True)