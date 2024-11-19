from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    author= models.CharField(max_length=120)
    author = models.ForeignKey(Author, related_name='books', on_delete= models.CASCADE)

    def __str__(self):
            return f"{self.title} by {self.author}


    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
        

        
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



class UserProfile(models.Model):
    role_choices = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    role=models.CharField(max_length=20, choices = role_choices, default = 'Member')
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            if not hasattr(instance, 'profile'):
                UserProfile.objects.create(user=instance)
    

        
