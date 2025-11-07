"""
Sample queries demonstrating Django ORM relationships.

To run these queries:
1. First, ensure your Django environment is set up:
   python manage.py shell
   
2. Then import and run the functions:
   from relationship_app.query_samples import *
   query_books_by_author("Author Name")
   list_books_in_library("Library Name")
   retrieve_librarian_for_library("Library Name")
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    
    This demonstrates the use of ForeignKey relationship.
    Uses the related_name 'books' to access all books by an author.
    
    Args:
        author_name (str): The name of the author
        
    Returns:
        QuerySet: All books by the specified author
    """
    try:
        # Method 1: Using get() and related_name
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None
    
    # Alternative Method 2: Using filter() directly on Book model
    # books = Book.objects.filter(author__name=author_name)


def list_books_in_library(library_name):
    """
    List all books in a library.
    
    This demonstrates the use of ManyToManyField relationship.
    Uses the related field 'books' to access all books in a library.
    
    Args:
        library_name (str): The name of the library
        
    Returns:
        QuerySet: All books in the specified library
    """
    try:
        # Using get() and ManyToManyField
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        return books
    
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    
    This demonstrates the use of OneToOneField relationship.
    Uses the related_name 'librarian' to access the librarian of a library.
    
    Args:
        library_name (str): The name of the library
        
    Returns:
        Librarian: The librarian managing the specified library
    """
    try:
        # Method 1: Using get() and related_name
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        
        print(f"\nLibrarian for {library_name}:")
        print(f"  - {librarian.name}")
        
        return librarian
    
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None
    
    # Alternative Method 2: Using filter() directly on Librarian model
    # librarian = Librarian.objects.get(library__name=library_name)


# Additional utility function to demonstrate reverse relationships
def get_libraries_with_book(book_title):
    """
    Get all libraries that contain a specific book.
    Demonstrates reverse ManyToMany relationship.
    
    Args:
        book_title (str): The title of the book
        
    Returns:
        QuerySet: All libraries containing the specified book
    """
    try:
        book = Book.objects.get(title=book_title)
        libraries = book.libraries.all()
        
        print(f"\nLibraries containing '{book_title}':")
        for library in libraries:
            print(f"  - {library.name}")
        
        return libraries
    
    except Book.DoesNotExist:
        print(f"Book '{book_title}' not found.")
        return None


# Sample data creation function for testing
def create_sample_data():
    """
    Creates sample data for testing the queries.
    Run this in Django shell before testing the query functions.
    """
    # Create Authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create Books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    
    # Create Libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4)
    
    # Create Librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!")
    print("\nYou can now test the queries with:")
    print("  query_books_by_author('J.K. Rowling')")
    print("  list_books_in_library('Central Library')")
    print("  retrieve_librarian_for_library('Central Library')")
