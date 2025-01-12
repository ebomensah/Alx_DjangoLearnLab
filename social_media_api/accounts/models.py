from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.fields import related


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=220, unique=True)
    email = models.EmailField(unique=True)
    date_joined=models.DateTimeField(auto_now=True)
    bio = models.TextField (blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True, default='default.jpg'
    )
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='followingset', blank=True
    )
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followersset', blank=True
    )

    def __str__(self):
        return self.username


# Create your models here.
