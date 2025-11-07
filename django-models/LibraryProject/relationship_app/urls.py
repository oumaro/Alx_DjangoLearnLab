# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books, LibraryDetailView, register,
    admin_view, librarian_view, member_view,
    book_add, book_edit, book_delete 
)

urlpatterns = [
    # Task 1: Core Views
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Task 2: Authentication Views
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
    path('register/', register, name='register'),
    
    # Task 3: Role-Based Views
    path('admin_only/', admin_view, name='admin_view'),
    path('librarian_desk/', librarian_view, name='librarian_view'),
    path('member_zone/', member_view, name='member_view'),
    
    # Task 4: Secured CRUD Views
    path('books/add/', book_add, name='book_add'),
    path('books/<int:pk>/edit/', book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),
]
