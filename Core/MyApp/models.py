from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(null=True, blank=True, upload_to='profile_pic')
  
  def __str__(self) -> str:
    return f'{self.user.username} + "profile"'