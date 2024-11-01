#Command
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()

#Expected output: No output, but the book title should be updated
