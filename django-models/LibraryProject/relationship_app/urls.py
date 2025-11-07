# relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # FBV URL: path('', ...)
    # URL: /relationship/books/
    path('books/', views.list_books, name='book_list'),
    
    # CBV URL: path('<pk>/', ...)
    # URL: /relationship/library/1/ (where 1 is the Library's primary key)
    # The .as_view() method is required to route a request to a CBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
