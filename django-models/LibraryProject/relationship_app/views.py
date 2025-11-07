# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# --- 1. Function-based View (FBV) ---
def list_books(request):
    """Lists all books and their authors."""
    # Get all Book objects and select_related('author') for performance.
    # This avoids a separate database query for the author's name for every book.
    all_books = Book.objects.select_related('author').all()
    
    context = {
        'books': all_books,
        'view_type': 'Function-based View (FBV)'
    }
    
    # Renders the HTML template
    return render(request, 'list_books.html', context)

# --- 2. Class-based View (CBV) using DetailView ---
class LibraryDetailView(DetailView):
    """Displays details for a specific Library, including all its books."""
    
    # 1. Specify the model this view will operate on
    model = Library
    
    # 2. Specify the template to be used
    template_name = 'library_detail.html'
    
    # 3. Specify the name of the object in the template context
    # By default, it would be 'library', but we'll keep it explicit.
    context_object_name = 'library'

    # (Optional) Override get_queryset for performance/prefetching
    def get_queryset(self):
        # Prefetch the 'books' M2M relationship to avoid N+1 queries
        return Library.objects.prefetch_related('books__author')
