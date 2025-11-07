# relationship_app/urls.py (Update the file to include these new patterns)

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, register
from .views import LibraryDetailView

urlpatterns = [
    # Existing Views
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # --- New Authentication Views ---

    # 1. Login View (Uses Django's built-in LoginView)
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    
    # 2. Logout View (Uses Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(
        # LOGOUT_REDIRECT_URL in settings handles redirection after the view runs
        template_name='relationship_app/logout.html'
    ), name='logout'),
    
    # 3. Registration View (Uses our custom function)
    path('register/', register, name='register'),
]
