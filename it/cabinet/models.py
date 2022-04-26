from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="cabinet/img/")
    vk = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user