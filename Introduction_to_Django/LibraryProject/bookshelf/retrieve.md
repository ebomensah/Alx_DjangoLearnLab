#Command
retrieve_book= Book.objects.get(title = "1984")
print(retrieve_book)

#Expected output: <Book: 1984>
