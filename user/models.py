from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='user', null=True)


# Create your models here.
