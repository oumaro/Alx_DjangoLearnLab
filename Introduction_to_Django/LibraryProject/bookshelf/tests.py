from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    """
    Test cases for the Book model.
    """
    
    def setUp(self):
        """
        Set up test data.
        """
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )
    
    def test_book_creation(self):
        """
        Test that a book can be created successfully.
        """
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.publication_year, 1949)
    
    def test_book_str_method(self):
        """
        Test the string representation of a book.
        """
        expected_str = "1984 by George Orwell (1949)"
        self.assertEqual(str(self.book), expected_str)
    
    def test_book_fields(self):
        """
        Test that book fields have correct max lengths.
        """
        title_max_length = self.book._meta.get_field('title').max_length
        author_max_length = self.book._meta.get_field('author').max_length
        
        self.assertEqual(title_max_length, 200)
        self.assertEqual(author_max_length, 100)
    
    def test_book_ordering(self):
        """
        Test that books are ordered by title.
        """
        Book.objects.create(
            title="Animal Farm",
            author="George Orwell",
            publication_year=1945
        )
        
        books = Book.objects.all()
        self.assertEqual(books[0].title, "Animal Farm")
        self.assertEqual(books[1].title, "1984")


# To run tests:
# python manage.py test bookshelf
