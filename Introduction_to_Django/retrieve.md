# Retrieve Operation

## Objective
Retrieve and display all attributes of the book created in the previous step.

## Steps

### 1. Retrieve the Book by ID
```python
from bookshelf.models import Book

# Retrieve the book with ID 1
book = Book.objects.get(id=1)
```

**Expected Output:**
