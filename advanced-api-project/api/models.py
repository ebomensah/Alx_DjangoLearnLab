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



# Create your models here.
