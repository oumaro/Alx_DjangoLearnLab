# relationship_app/models.py 

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Standard Library Models (Assumed Existing) ---

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    library = models.ManyToManyField(Library, related_name='book_inventory', blank=True) 

    def __str__(self):
        return self.title

    # Task 4 FIX: Custom Permissions for CRUD operations
    class Meta:
        permissions = [
            ("can_add_book", "Can add new book entries"),
            ("can_change_book", "Can edit existing book entries"),
            ("can_delete_book", "Can delete book entries"),
        ]

# --- User Profile for RBAC (Task 3 Fix) ---

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    """Extends the built-in User model with a role field."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'

# Signals to automatically create UserProfile when a new User is created/saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
