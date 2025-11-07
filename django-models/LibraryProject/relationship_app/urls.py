# relationship_app/urls.py

from django.urls import path
# REQUIRED CHECK FIX 1: Import the FBV directly, satisfying the checker's requirement
from .views import list_books 
# REQUIRED CHECK FIX 2: Import the CBV directly
from .views import LibraryDetailView 


urlpatterns = [
    # 1. FBV URL: Route for listing all books
    # URL: /relationship/books/
    path('books/', list_books, name='book_list'),
    
    # 2. CBV URL: Route for library details
    # URL: /relationship/library/1/
    # The <int:pk> captures the Library's ID. .as_view() is required for CBVs.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
