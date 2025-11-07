# relationship_app/query_samples.py

import os
import django

# Configure Django environment for standalone script execution
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

print("--- 🐘 Starting Data Setup ---")

# --- CLEANUP (Good practice for repeatable scripts) ---
Librarian.objects.all().delete()
Library.objects.all().delete()
Book.objects.all().delete()
Author.objects.all().delete()

# --- SETUP: Creating Data for Relationships ---

# 1. Authors & Books (ForeignKey)
author_a = Author.objects.create(name="Jane Austen")
author_b = Author.objects.create(name="George Orwell")

book1 = Book.objects.create(title="Pride and Prejudice", author=author_a)
book2 = Book.objects.create(title="Emma", author=author_a)
book3 = Book.objects.create(title="1984", author=author_b)

# 2. Libraries & ManyToMany
library_central = Library.objects.create(name="Central City Library")
library_south = Library.objects.create(name="South End Branch")

library_central.books.add(book1, book3) # M2M Linkage
library_south.books.add(book1, book2)   # M2M Linkage

# 3. Librarians (OneToOne)
librarian_central = Librarian.objects.create(name="Ms. Eleanor Vance", library=library_central)
librarian_south = Librarian.objects.create(name="Mr. David Smith", library=library_south)

print("Data Setup Complete.\n" + "="*50)

# --- QUERY 1: ForeignKey (Reverse Lookup) ---
print("Query all books by a specific author (Jane Austen):")
jane_books_qs = author_a.books.all() 
for book in jane_books_qs:
    print(f"  - {book.title}")
print("\n" + "="*50)

# --- QUERY 2: ManyToMany (Forward Lookup) ---
print("List all books in a library (Central City Library):")
central_books_qs = library_central.books.all()
for book in central_books_qs:
    print(f"  - {book.title}")
print("\n" + "="*50)

# --- QUERY 3: OneToOne (Reverse Lookup) ---
print("Retrieve the librarian for a library (South End Branch):")
try:
    # Reverse lookup uses the lowercase model name: library_instance.librarian
    librarian = library_south.librarian 
    print(f"  - The librarian for {library_south.name} is {librarian.name}")
except Librarian.DoesNotExist:
    print(f"  - No librarian found for {library_south.name}")
print("\n" + "="*50)
