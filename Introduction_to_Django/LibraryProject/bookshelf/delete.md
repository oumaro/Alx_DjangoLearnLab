from bookshelf.models import Book
# Retrieve the book instance
book = Book.objects.get(id=1)

# Delete the instance. This returns the number of objects deleted.
book.delete()

# Confirm deletion by retrieving all books. The QuerySet should now be empty.
print(Book.objects.all())
(<QuerySet []>, 1)
