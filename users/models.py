from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank = True, null = True)
    is_whole = models.BooleanField(default=False)
    is_retail = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
