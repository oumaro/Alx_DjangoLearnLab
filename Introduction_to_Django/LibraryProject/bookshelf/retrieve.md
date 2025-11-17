from bookshelf.models import Book

# Retrieve the book with ID 1 (Assuming this is the primary key of the created book)
book = Book.objects.get(id=1)

# Display the attributes of the retrieved book
print(book.title)
print(book.author)
print(book.publication_year)
1984
George Orwell
1949
