from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #tag = models.ManyToManyField('Tag', related_name = 'posts')
    tags = TaggableManager()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.published_date}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', 
    upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username} Profile"
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name