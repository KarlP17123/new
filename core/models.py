from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]