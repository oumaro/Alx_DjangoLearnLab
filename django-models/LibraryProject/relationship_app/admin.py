# relationship_app/admin.py

from django.contrib import admin
from .models import UserProfile, Book, Library # Ensure UserProfile is imported
# Assuming you have Author model
try:
    from .models import Author
except ImportError:
    pass 

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)

try:
    admin.site.register(Author)
except NameError:
    pass

# REQUIRED FIX: Register the UserProfile model for the Admin View Check to succeed.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'role')
