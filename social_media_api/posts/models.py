from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from notifications.models import Notification 


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.pk: 
            print("A new Post is being created:", self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
       return self.title


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'post')



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author=models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)

    def __str__(self):
        return f"comment by {self.author} on {self.post.title}"


  #  slug= models.SlugField(unique=True, blank=True)

# Create your models here.


