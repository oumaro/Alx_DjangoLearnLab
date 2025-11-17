# Create Operation - Book Model

## Objective
Create a new Book instance in the database with the title "1984", author "George Orwell", and publication year 1949.

## Steps to Perform in Django Shell

### 1. Open Django Shell
```bash
python manage.py shell
```

### 2. Import the Book Model
```python
from bookshelf.models import Book
```

### 3. Create a Book Instance
```python
# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

**Expected Output:**
