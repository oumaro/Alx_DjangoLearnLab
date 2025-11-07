# relationship_app/query_samples.py

import os
import django
# Set up Django environment manually for standalone script execution
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.db.models import Count

print("--- Data Setup: Populating the Database ---")

# 1. Create Authors
author_a = Author.objects.create(name="Jane Austen")
author_b = Author.objects.create(name="George Orwell")

# 2. Create Books (ForeignKey)
book1 = Book.objects.create(title="Pride and Prejudice", author=author_a)
book2 = Book.objects.create(title="Emma", author=author_a)
book3 = Book.objects.create(title="1984", author=author_b)

# 3. Create Libraries
library_central = Library.objects.create(name="Central City Library")
library_south = Library.objects.create(name="South End Branch")

# 4. Add Books to Libraries (ManyToMany)
# Central Library has P&P and 1984
library_central.books.add(book1, book3)
# South Library has all three books
library_south.books.add(book1, book2, book3)

# 5. Create Librarians (OneToOne)
# Note: The 'library' field is a OneToOne link to the Library instance
librarian_central = Librarian.objects.create(name="Ms. Eleanor Vance", library=library_central)
librarian_south = Librarian.objects.create(name="Mr. David Smith", library=library_south)

print("Setup Complete.\n" + "="*50)

# --- QUERY 1: ForeignKey (Reverse Lookup) ---
# Objective: Query all books by a specific author (Jane Austen).

print("1. Query all books by a specific author (Jane Austen):")
# Use the 'related_name' ('books') defined on the ForeignKey field in the Book model.
jane_books = author_a.books.all() 
for book in jane_books:
    print(f"  - {book.title}")
print("\n" + "="*50)

# --- QUERY 2: ManyToMany (Forward Lookup) ---
# Objective: List all books in a library (Central City Library).

print("2. List all books in a library (Central City Library):")
# Use the ManyToMany field name ('books') on the Library model.
central_books = library_central.books.all()
for book in central_books:
    print(f"  - {book.title}")
print("\n" + "="*50)

# --- QUERY 3: OneToOne (Forward Lookup) ---
# Objective: Retrieve the librarian for a library (South End Branch).

print("3. Retrieve the librarian for a library (South End Branch):")
try:
    # Use the related field name which is the lower-case model name if not specified.
    # In the Librarian model, the primary key *is* the OneToOneField, making the lookup direct.
    librarian = library_south.librarian 
    print(f"  - The librarian for {library_south.name} is {librarian.name}")
except Librarian.DoesNotExist:
    print(f"  - No librarian found for {library_south.name}")
print("\n" + "="*50)


# --- BONUS QUERY: ManyToMany (Reverse Lookup) ---
# Objective: List all libraries that have a specific book (1984).

print("4. BONUS: List all libraries that have the book '1984':")
# Use the 'related_name' ('libraries') defined on the ManyToMany field in the Library model.
nineteen_eighty_four = Book.objects.get(title="1984")
libraries_with_book = nineteen_eighty_four.libraries.all()
for library in libraries_with_book:
    print(f"  - {library.name}")
