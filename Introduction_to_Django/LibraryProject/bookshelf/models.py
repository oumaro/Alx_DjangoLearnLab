from django.db import models


class Book(models.Model):
    """
    Model representing a book in the library.
    
    Attributes:
        title (str): The title of the book, max 200 characters
        author (str): The author's name, max 100 characters
        publication_year (int): The year the book was published
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        """String representation of the Book model."""
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        """Meta options for the Book model."""
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
