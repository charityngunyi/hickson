from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

# profile that will be used to describe available bloggers to viewers

class CustomUser(AbstractUser):
    # will inherit all default for now which can be enhanced in future
	profile_type = models.CharField(
        max_length=10, choices=[("seeker", "Seeker"), ("owner", "Owner"), ("admin", "admin"), ], default='seeker'
    )
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	Occupation_title = models.CharField(max_length=50)
	Occupation_description = models.CharField(max_length=250)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	country = models.CharField(max_length=50)
	town = models.CharField(max_length=50)
	contacts = models.CharField(max_length=250)
	hobby = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.username