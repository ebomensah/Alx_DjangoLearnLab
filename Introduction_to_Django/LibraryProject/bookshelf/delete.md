From bookshelf.models import Book
#Command
book.delete()

#Confirm deletion
Book.objects.all()

#Expected output: QuerySet([], 0) indicating no books are found
