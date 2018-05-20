from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ShopUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='users_profile_pictures', blank=True)
    age = models.PositiveIntegerField(verbose_name='age')
