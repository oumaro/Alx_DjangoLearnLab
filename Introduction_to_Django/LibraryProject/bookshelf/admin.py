from django.contrib import admin
from .models import Book

# Define a custom Admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model in the Django admin.
    """
    # 1. Customize the list view columns: Display title, author, and publication_year.
    list_display = ('title', 'author', 'publication_year')

    # 2. Add search functionality for the title and author fields.
    search_fields = ('title', 'author')

    # 3. Add list filters to easily filter books by publication year.
    list_filter = ('publication_year',)

    # 4. Make 'title' a link to the change view. (It's often the default, but good to include)
    list_display_links = ('title',)

    # 5. Add a simple date hierarchy (optional, but nice for dates)
    # date_hierarchy = 'publication_year' # Use if publication_year was a DateField

# Register the Book model with the custom configuration
admin.site.register(Book, BookAdmin)
