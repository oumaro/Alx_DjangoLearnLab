# Retrieve Operation - Book Model

## Objective
Retrieve and display all attributes of the book created in the previous step.

## Steps to Perform in Django Shell

### 1. Import the Book Model
```python
from bookshelf.models import Book
```

### 2. Retrieve the Book by ID
```python
# Retrieve the book with ID 1
book = Book.objects.get(id=1)
```

**Expected Output:**
