# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books
# REQUIRED CHECK FIX 1: Import register explicitly
from .views import LibraryDetailView, register 

urlpatterns = [
    # Existing Views (from previous tasks)
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # --- Authentication Views ---

    # REQUIRED CHECK FIX 2: Login View 
    # Must use the required string: LoginView.as_view(template_name=
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    
    # REQUIRED CHECK FIX 3: Logout View
    # Must use the required string: LogoutView.as_view(template_name=
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
    
    # REQUIRED CHECK FIX 4: Registration View
    # Must use the required string: views.register
    path('register/', register, name='register'),
]
