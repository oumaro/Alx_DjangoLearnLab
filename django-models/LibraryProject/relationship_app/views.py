# relationship_app/views.py

from django.shortcuts import render
from .models import Book 
# ... other imports (Library, DetailView, etc.)

def list_books(request):
    """
    Renders a simple text list of book titles and their authors.
    """
    # 1. Get the data
    # select_related('author') ensures author name is fetched in one query.
    all_books = Book.objects.select_related('author').all()
    
    context = {
        'books': all_books, # Passes the QuerySet to the template
    }
    
    # 2. Render the correct template name (MUST be 'list_books.html' only)
    return render(request, 'list_books.html', context)
