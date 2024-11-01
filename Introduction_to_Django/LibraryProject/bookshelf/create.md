#Command:
book = Book.objects.create(
title="1984", 
author="George Orwell", 
publication_year=1949
)
book.save()

#Expected Output: No output but the book should be saved in the database
