# Retrieve the book with ID 1 (Assuming this ID was used in the create step)
book = Book.objects.get(id=1)

# Display the attributes of the retrieved book
print(book.title)
print(book.author)
print(book.publication_year)
