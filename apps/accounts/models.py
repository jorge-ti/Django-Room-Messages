from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return str(self.user)