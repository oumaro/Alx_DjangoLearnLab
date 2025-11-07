# relationship_app/views.py

from django.shortcuts import render

# REQUIRED CHECK FIX: Import DetailView using the specific path the checker demands.
# Note: This is an older, more verbose import style.
from django.views.generic.detail import DetailView 

# Imports the models required for the views (from previous fix)
from .models import Library 
from .models import Book 

# --- 1. Function-based View (FBV) ---
def list_books(request):
    # ... (Keep the rest of the list_books function as is)
    all_books = Book.objects.all() 
    context = {'books': all_books}
    return render(request, 'relationship_app/list_books.html', context)

# --- 2. Class-based View (CBV) using DetailView ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library, listing all available books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')
