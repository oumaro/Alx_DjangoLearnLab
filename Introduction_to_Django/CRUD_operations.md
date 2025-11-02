# CRUD Operations Documentation - Book Model

This document provides a comprehensive guide to performing CRUD (Create, Read, Update, Delete) operations on the Book model in the bookshelf Django app.

---

## Table of Contents
1. [Setup](#setup)
2. [Create Operation](#create-operation)
3. [Retrieve Operation](#retrieve-operation)
4. [Update Operation](#update-operation)
5. [Delete Operation](#delete-operation)
6. [Summary](#summary)

---

## Setup

### Prerequisites
1. Django project created: `LibraryProject`
2. App created: `bookshelf`
3. Book model defined in `bookshelf/models.py`
4. Migrations applied

### Starting the Django Shell
```bash
python manage.py shell
```

### Import the Book Model
```python
from bookshelf.models import Book
```

---

## Create Operation

### Objective
Create a new Book instance with title "1984", author "George Orwell", and publication year 1949.

### Command
```python
# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

### Output
```python
# No immediate visible output, but the object is created
```

### Verification
```python
print(book)
# Output: 1984 by George Orwell (1949)

print(f"Book ID: {book.id}")
# Output: Book ID: 1

print(f"Title: {book.title}")
# Output: Title: 1984

print(f"Author: {book.author}")
# Output: Author: George Orwell

print(f"Publication Year: {book.publication_year}")
# Output: Publication Year: 1949
```

### Result
✅ Successfully created a Book instance with:
- **ID**: 1
- **Title**: 1984
- **Author**: George Orwell
- **Publication Year**: 1949

---

## Retrieve Operation

### Objective
Retrieve and display all attributes of the book created in the previous step.

### Command
```python
# Retrieve the book by ID
book = Book.objects.get(id=1)
```

### Output
```python
# No immediate visible output, but the object is retrieved
```

### Display All Attributes
```python
# Using __str__ method
print(book)
# Output: 1984 by George Orwell (1949)

# Individual attributes
print(f"ID: {book.id}")
# Output: ID: 1

print(f"Title: {book.title}")
# Output: Title: 1984

print(f"Author: {book.author}")
# Output: Author: George Orwell

print(f"Publication Year: {book.publication_year}")
# Output: Publication Year: 1949
```

### Alternative Retrieval Methods
```python
# Retrieve by title
book = Book.objects.get(title="1984")
print(book)
# Output: 1984 by George Orwell (1949)

# Retrieve all books
all_books = Book.objects.all()
print(all_books)
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Count all books
count = Book.objects.count()
print(f"Total books: {count}")
# Output: Total books: 1

# Filter by author
books = Book.objects.filter(author="George Orwell")
for book in books:
    print(book)
# Output: 1984 by George Orwell (1949)
```

### Result
✅ Successfully retrieved the Book instance with all attributes intact.

---

## Update Operation

### Objective
Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

### Commands
```python
# Step 1: Retrieve the book
book = Book.objects.get(id=1)

# Step 2: Display current title
print(f"Current Title: {book.title}")
# Output: Current Title: 1984

# Step 3: Update the title
book.title = "Nineteen Eighty-Four"

# Step 4: Save the changes
book.save()

# Step 5: Verify the update
print(f"Updated Title: {book.title}")
# Output: Updated Title: Nineteen Eighty-Four
```

### Complete Update Sequence
```python
from bookshelf.models import Book

# Retrieve
book = Book.objects.get(id=1)
print(f"Before: {book.title}")
# Output: Before: 1984

# Update
book.title = "Nineteen Eighty-Four"

# Save
book.save()

# Verify
print(f"After: {book.title}")
# Output: After: Nineteen Eighty-Four

# Confirm by retrieving again
updated_book = Book.objects.get(id=1)
print(updated_book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
```

### Alternative Update Method
```python
# Using update() on QuerySet
Book.objects.filter(id=1).update(title="Nineteen Eighty-Four")
# Output: 1 (number of rows affected)
```

### Result
✅ Successfully updated the book's title from "1984" to "Nineteen Eighty-Four".

**Updated Book Details:**
- **ID**: 1
- **Title**: Nineteen Eighty-Four
- **Author**: George Orwell
- **Publication Year**: 1949

---

## Delete Operation

### Objective
Delete the book instance and confirm deletion by retrieving all books.

### Commands
```python
# Step 1: Retrieve the book
book = Book.objects.get(id=1)
print(f"Book to delete: {book}")
# Output: Book to delete: Nineteen Eighty-Four by George Orwell (1949)

# Step 2: Delete the book
result = book.delete()
print(f"Deletion result: {result}")
# Output: Deletion result: (1, {'bookshelf.Book': 1})
```

### Verification
```python
# Method 1: Count all books
count = Book.objects.count()
print(f"Total books after deletion: {count}")
# Output: Total books after deletion: 0

# Method 2: Retrieve all books
all_books = Book.objects.all()
print(f"All books: {all_books}")
# Output: All books: <QuerySet []>

# Method 3: Try to retrieve the deleted book
try:
    deleted_book = Book.objects.get(id=1)
    print(deleted_book)
except Book.DoesNotExist:
    print("✓ Book with ID 1 does not exist - deletion confirmed!")
# Output: ✓ Book with ID 1 does not exist - deletion confirmed!
```

### Complete Delete Sequence
```python
from bookshelf.models import Book

# Check initial count
print(f"Books before deletion: {Book.objects.count()}")
# Output: Books before deletion: 1

# Retrieve and delete
book = Book.objects.get(id=1)
print(f"Deleting: {book}")
# Output: Deleting: Nineteen Eighty-Four by George Orwell (1949)

result = book.delete()
print(f"Deletion result: {result}")
# Output: Deletion result: (1, {'bookshelf.Book': 1})

# Verify deletion
print(f"Books after deletion: {Book.objects.count()}")
# Output: Books after deletion: 0

# Confirm deletion
try:
    Book.objects.get(id=1)
except Book.DoesNotExist:
    print("✓ Book successfully deleted!")
# Output: ✓ Book successfully deleted!
```

### Result
✅ Successfully deleted the book from the database.

**Deletion Confirmation:**
- Book count: 0
- QuerySet empty: `<QuerySet []>`
- Attempting to retrieve raises `Book.DoesNotExist` exception

---

## Summary

### CRUD Operations Overview

| Operation | Command | Result |
|-----------|---------|--------|
| **Create** | `Book.objects.create(title="1984", author="George Orwell", publication_year=1949)` | New book created with ID 1 |
| **Retrieve** | `Book.objects.get(id=1)` | Book retrieved successfully |
| **Update** | `book.title = "Nineteen Eighty-Four"; book.save()` | Title updated successfully |
| **Delete** | `book.delete()` | Book deleted, database empty |

### Key Django ORM Methods Used

1. **Create Operations:**
   - `objects.create()` - Create and save in one step
   - `save()` - Save a new or modified instance

2. **Retrieve Operations:**
   - `objects.get()` - Get a single object
   - `objects.all()` - Get all objects
   - `objects.filter()` - Get objects matching criteria
   - `objects.count()` - Count objects

3. **Update Operations:**
   - Modify attributes and call `save()`
   - `objects.update()` - Bulk update

4. **Delete Operations:**
   - `delete()` - Delete an instance or QuerySet

### Important Notes

1. **Create**: Use `objects.create()` to create and save in one step, or instantiate and call `save()`.

2. **Retrieve**: 
   - `get()` returns a single object (raises exception if not found or multiple exist)
   - `filter()` returns a QuerySet (can be empty or contain multiple objects)
   - Always handle `DoesNotExist` exceptions

3. **Update**: 
   - Changes to attributes are in-memory only until `save()` is called
   - Use `update()` on QuerySets for bulk updates (more efficient)

4. **Delete**: 
   - `delete()` permanently removes objects from the database
   - Returns a tuple: (count, {model: count})
   - Consider soft deletes for important data

### Best Practices

1. Always use try-except blocks when using `get()`
2. Use `filter()` with `first()` for safer single-object retrieval
3. Verify operations with count checks or retrievals
4. Use transactions for related operations
5. Consider using `update_or_create()` for upsert operations
6. Be cautious with bulk deletes

---

## Testing in Django Shell

To test all operations in sequence:
```python
# Import
from bookshelf.models import Book

# CREATE
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book}")

# RETRIEVE
retrieved_book = Book.objects.get(id=book.id)
print(f"Retrieved: {retrieved_book}")

# UPDATE
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated: {retrieved_book}")

# DELETE
retrieved_book.delete()
print(f"Remaining books: {Book.objects.count()}")
```

**Expected Output:**
