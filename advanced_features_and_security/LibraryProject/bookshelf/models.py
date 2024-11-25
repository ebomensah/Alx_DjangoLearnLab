from multiprocessing import Value
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractUser, UserManager
from django.conf import settings



class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    author= models.CharField(max_length=120)
    author = models.ForeignKey(Author, related_name='books', on_delete= models.CASCADE)

    class Meta:
        permissions = [
            ("can_create", "can_create"),
            ("can_edit", "can_edit"),
            ("can_delete", "can_delete"),
            ("can_view", "can_view"),
        ]
        

        def __str__(self):
            return self.title
        

        
class Library(models.Model):
    name = models.CharField(max_length=120)
    books = models.CharField(max_length=120)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=120)
    library= models.CharField(max_length=120)
    library = models.OneToOneField(Library, related_name='librarians', on_delete= models.CASCADE)

    def __str__(self):
        return self.name



class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not username: 
            raise Value('The username field must be set')
        
        user = self.model(
            email= self.normalize_email(email), 
            username = username, 
            first_name=first_name, 
            last_name=last_name,
            date_of_birth=date_of_birth, 
            profile_picture=profile_photo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password=None):
        user = self.create_user(
            email= self.normalize_email(email), 
            username = username, 
            first_name=first_name, 
            last_name=last_name,
            is_superuser = True,
            is_admin=True,
            is_superadmin=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user
        
    

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(
        upload_to='profile_image/', blank=True, null=True, default='default.jpg')
    is_staff = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email 


class UserProfile(models.Model):
    role_choices = (
        ('Admins', 'Admins'),
        ('Editors', 'Editors'),
        ('Viewers', 'Viewers'),
    )
    role=models.CharField(max_length=20, choices = role_choices, default = 'Viewers')
    user = models.OneToOneField (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userprofile")
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            if not hasattr(instance, 'profile'):
                UserProfile.objects.create(user=instance)
    

        
