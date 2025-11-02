# Delete Operation - Book Model

## Objective
Delete the book instance from the database and confirm the deletion by attempting to retrieve all books.

## Steps to Perform in Django Shell

### 1. Import the Book Model
```python
from bookshelf.models import Book
```

### 2. Retrieve the Book to Delete
```python
# Get the book to delete
book = Book.objects.get(id=1)
print(f"Book to delete: {book}")
```

**Expected Output:**
