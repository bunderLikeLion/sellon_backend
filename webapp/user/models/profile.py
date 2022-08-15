from django.db import models
from .user import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatars/avatars.png', upload_to='avatars/')

    def __str__(self):
        return f'{self.user.username} Profile'
