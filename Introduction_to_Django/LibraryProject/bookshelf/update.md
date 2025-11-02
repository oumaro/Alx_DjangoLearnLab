# Update Operation - Book Model

## Objective
Update the title of the book "1984" to "Nineteen Eighty-Four" and save the changes to the database.

## Steps to Perform in Django Shell

### 1. Import the Book Model
```python
from bookshelf.models import Book
```

### 2. Retrieve the Book
```python
# Get the book to update
book = Book.objects.get(id=1)
```

**Expected Output:**
