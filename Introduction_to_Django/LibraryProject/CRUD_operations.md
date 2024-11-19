#Creating a new Book instance
#Command:
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

#Expected Output: No output but the book should be saved in the database


#Retrieving a book
#Command
retrieve_book= Book.object.all()
print(retrieve_book)

#Expected output: <Book: 1984>


#Updating a book
#Command
Book.objects.get(title = "1984")
title = "Nineteen Eighty-Four"
book.save()

#Expected output: No output, but the book title should be updated


#Deleting a book instance
#Command
Book.objects.delete()

#Confirm deletion
Book.objects.all()

#Expected output: QuerySet([], 0) indicating no books are found