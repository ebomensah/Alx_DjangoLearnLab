from .models import Book, Author, Library, Librarian

#Query all books by a specific author
Author.objects.get(name=author_name)
Book.objects.filter(author=author)



#List all books in a library
Library.objects.get(name=library_name)
library_name.books.all()


#Retrieve the librarian for a library
Library.objects.get(name=library_name)
Librarian.objects.get(library=library_name)

