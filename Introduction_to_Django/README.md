# Introduction to Django

## Overview
This directory contains completed tasks for the ALX Django Learning Lab's introductory module. It demonstrates fundamental Django concepts including project setup, app creation, model definition, and CRUD operations.

## Repository Information
- **GitHub Repository**: Alx_DjangoLearnLab
- **Directory**: Introduction_to_Django
- **Project**: LibraryProject
- **App**: bookshelf

---

## Tasks Completed

### Task 0: Django Development Environment Setup ✅
- Installed Django
- Created LibraryProject
- Ran development server
- Explored project structure
- **Documentation**: `LibraryProject/README.md`

### Task 1: Implementing and Interacting with Django Models ✅
- Created `bookshelf` app
- Defined `Book` model with fields: title, author, publication_year
- Created and applied migrations
- Performed CRUD operations via Django shell
- **Documentation**: 
  - `create.md` - CREATE operation
  - `retrieve.md` - RETRIEVE operation
  - `update.md` - UPDATE operation
  - `delete.md` - DELETE operation
  - `CRUD_operations.md` - Complete CRUD documentation

---

## Project Structure
---

## Book Model

### Model Definition
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
```

### Model Features
- **Fields**: title, author, publication_year
- **String Representation**: "Title by Author (Year)"
- **Ordering**: Alphabetically by title
- **Admin Interface**: Configured with list display, filters, and search

---

## CRUD Operations Summary

| Operation | Command | Result |
|-----------|---------|--------|
| **Create** | `Book.objects.create(title="1984", author="George Orwell", publication_year=1949)` | New book created |
| **Retrieve** | `Book.objects.get(id=1)` | Book retrieved |
| **Update** | `book.title = "Nineteen Eighty-Four"; book.save()` | Title updated |
| **Delete** | `book.delete()` | Book deleted |

See individual markdown files for detailed documentation of each operation.

---

## Getting Started

### Prerequisites
```bash
# Ensure Python and pip are installed
python --version
pip --version

# Install Django
pip install django
```

### Setup Instructions

1. **Navigate to the project directory**:
```bash
cd Introduction_to_Django/LibraryProject
```

2. **Apply migrations** (if not already done):
```bash
python manage.py migrate
```

3. **Create a superuser** (optional, for admin access):
```bash
python manage.py createsuperuser
```

4. **Run the development server**:
```bash
python manage.py runserver
```

5. **Access the application**:
- Main site: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

### Using Django Shell
```bash
# Open Django shell
python manage.py shell

# Import the Book model
from bookshelf.models import Book

# Perform CRUD operations
# See CRUD_operations.md for detailed examples
```

---

## Key Learning Outcomes

### Task 0: Environment Setup
✅ Understanding Django project structure  
✅ Configuring Django settings  
✅ Running the development server  
✅ Exploring Django's file organization  

### Task 1: Django Models
✅ Creating Django applications  
✅ Defining models with appropriate field types  
✅ Creating and applying migrations  
✅ Using Django ORM for database operations  
✅ Performing CRUD operations  
✅ Working with the Django shell  

---

## Technologies Used

- **Python**: 3.8+
- **Django**: 4.2+
- **Database**: SQLite3 (default)
- **Version Control**: Git

---

## Author
ALX Django Learning Lab Participant

## License
This project is created for educational purposes as part of the ALX Django Learning Lab.

---

**Last Updated**: November 2, 2025  
**Status**: Completed ✅  
**Django Version**: 4.2+  
**Python Version**: 3.8+
