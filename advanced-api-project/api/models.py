from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Model to represent an author.
#    The 'name' field stores the author's name.
 #   """

class Book(models.Model):

    #Model to represent a book.
   # The 'title' field stores the book's title.
    #The 'publication_year' field stores the year the book was published.
    #The 'author' field establishes a foreign key relationship with the Author model.
    
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField(default = 2000)
    author = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name = 'books', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BlogPost(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now_add=True, null = True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"

# Create your models here.
