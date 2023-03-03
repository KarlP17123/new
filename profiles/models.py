from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.username
