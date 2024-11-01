#Command
Book.objects.delete()

#Confirm deletion
Book.objects.all()

#Expected output: QuerySet([], 0) indicating no books are found