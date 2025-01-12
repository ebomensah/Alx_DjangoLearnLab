from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=220, unique=True)
    email = models.EmailField()
    date_joined=models.DateTimeField(auto_now_add=True)
    bio = models.TextField (blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True, default='default.jpg'
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username


# Create your models here.
