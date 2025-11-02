from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Book model.
    """
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to filter by in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Fields to search
    search_fields = ('title', 'author')
    
    # Ordering
    ordering = ('title',)
    
    # Fields to display in the form
    fields = ('title', 'author', 'publication_year')
