# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, register, LibraryDetailView
# New Imports: Add the new views here
from .views import admin_view, librarian_view, member_view 

urlpatterns = [
    # ... [Keep all existing URLs: book_list, library_detail, login, logout, register] ...
    
    # --- New Role-Based URLs ---
    
    # Admin URL
    path('admin_only/', admin_view, name='admin_view'),
    
    # Librarian URL
    path('librarian_desk/', librarian_view, name='librarian_view'),
    
    # Member URL
    path('member_zone/', member_view, name='member_view'),
]
