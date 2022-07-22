from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    profile_photo = models.ImageField(
        upload_to="users/", blank=True, null=True)
    email = models.EmailField(unique=True, max_length=200)