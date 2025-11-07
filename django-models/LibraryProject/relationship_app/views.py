# relationship_app/views.py

from django.shortcuts import render
# Ensure Book is imported so Book.objects.all() works
from .models import Book, Library 
from django.views.generic import DetailView

# --- 1. Function-based View (FBV) ---
def list_books(request):
    """Lists all books and their authors."""
    
    # **FIXED/REQUIRED LINE:** Uses Book.objects.all() 
    # and select_related('author') for good practice (single query).
    all_books = Book.objects.select_related('author').all()
    
    context = {
        'books': all_books,
        'view_type': 'Function-based View (FBV)'
    }
    
    # **FIXED/REQUIRED LINE:** Calls render with the correct template name
    # Note: It MUST NOT include the app name in the template path here.
    return render(request, 'list_books.html', context)

# --- 2. Class-based View (CBV) ---
class LibraryDetailView(DetailView):
    # ... (Keep the rest of the LibraryDetailView code as is)
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')
