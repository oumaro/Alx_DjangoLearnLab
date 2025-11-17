# Update Operation

## Objective
Update the title of the book "1984" to "Nineteen Eighty-Four" and save the changes to the database.

## Steps

### 1. Retrieve the Book
```python
from bookshelf.models import Book

# Get the book to update
book = Book.objects.get(id=1)
```

**Expected Output:**
