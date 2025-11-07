# relationship_app/models.py

from django.db import models

# --- 1. ForeignKey Relationship: One Author has Many Books ---

class Author(models.Model):
    """The 'One' side of the relationship."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """The 'Many' side of the relationship."""
    title = models.CharField(max_length=200)
    
    # ForeignKey to Author. If an Author is deleted, all their Books are deleted (CASCADE).
    # related_name='books' allows us to call author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# --- 2. ManyToMany Relationship: Many Libraries have Many Books ---

class Library(models.Model):
    """One Library can hold Many Books, and one Book can be in Many Libraries."""
    name = models.CharField(max_length=100)
    
    # ManyToManyField to Book.
    # related_name='libraries' allows us to call book.libraries.all()
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# --- 3. OneToOne Relationship: One Library has One Librarian ---

class Librarian(models.Model):
    """One Librarian is assigned to exactly one Library."""
    name = models.CharField(max_length=100)
    
    # OneToOneField to Library. Deleting the Library deletes the Librarian.
    # The 'Library' instance can now be accessed via library.librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.name} ({self.library.name})"
