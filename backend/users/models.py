from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

# profile that will be used to describe available bloggers to viewers

class CustomUser(AbstractUser):
    profile_type = models.CharField(
        max_length=10,
        choices=[("seeker", "Seeker"), ("owner", "Owner"), ("admin", "admin")],
        default='seeker'
    )
    first_name = models.CharField(max_length=50, blank=True)  # Optional during registration and update
    last_name = models.CharField(max_length=50, blank=True)  # Optional during registration and update
    Occupation_title = models.CharField(max_length=50, blank=True)  # Optional during registration and update
    Occupation_description = models.CharField(max_length=250, blank=True)  # Optional during registration and update
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)  # Optional during registration and update
    country = models.CharField(max_length=50, blank=True)  # Optional during registration and update
    town = models.CharField(max_length=50, blank=True)  # Optional during registration and update
    contacts = models.CharField(max_length=250, blank=True)  # Optional during registration and update
    hobby = models.CharField(max_length=100, blank=True)  # Optional during registration and update

    def __str__(self):
        return self.username
