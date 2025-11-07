# relationship_app/models.py

from django.db import models

# --- ForeignKey Relationship: One Author has Many Books ---

class Author(models.Model):
    """
    The 'One' side of the ForeignKey relationship.
    An Author can have multiple Books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The 'Many' side of the ForeignKey relationship.
    A Book has one Author.
    """
    title = models.CharField(max_length=200)
    # The ForeignKey relationship: models.CASCADE means if the Author is deleted, 
    # all their books are also deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# --- ManyToMany Relationship: Many Libraries have Many Books ---

class Library(models.Model):
    """
    One side of the ManyToMany relationship.
    A Library can contain many Books.
    """
    name = models.CharField(max_length=100)
    # The ManyToMany relationship: A Library can have multiple Books, and a Book 
    # can be in multiple Libraries.
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# --- OneToOne Relationship: One Library has One Librarian ---

class Librarian(models.Model):
    """
    One side of the OneToOne relationship.
    A Librarian is assigned to exactly one Library (and vice versa).
    """
    name = models.CharField(max_length=100)
    # The OneToOne relationship: Links one Librarian record to exactly one Library record.
    # The 'on_delete=models.CASCADE' means if the Library is deleted, the Librarian record is deleted too.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Librarian: {self.name}"
