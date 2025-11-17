from bookshelf.models import Book
# Retrieve the book with ID 1
book = Book.objects.get(id=1)

# Update the title field
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Display the updated title to confirm
print(book.title)

Nineteen Eighty-Four
