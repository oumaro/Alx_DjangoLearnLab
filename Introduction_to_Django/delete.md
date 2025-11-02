# Delete Operation

## Objective
Delete the book instance from the database and confirm the deletion by attempting to retrieve all books.

## Steps

### 1. Retrieve the Book to Delete
```python
from bookshelf.models import Book

# Get the book to delete
book = Book.objects.get(id=1)
print(f"Book to delete: {book}")
```

**Expected Output:**
