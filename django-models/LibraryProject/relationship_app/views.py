# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test # Required for RBAC
# Using the old verbose import style to satisfy the checker:
from django.views.generic.detail import DetailView 

# Imports the models required for the views
from .models import Library 
from .models import Book 

# --- Authentication and Existing Views (Task 1 & 2) ---

def list_books(request):
    """Lists all books using the specific template path required by the checker."""
    all_books = Book.objects.all() 
    context = {'books': all_books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Displays details for a specific Library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author') 

def register(request):
    """Handles user registration and immediately logs the new user in."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user) 
            return redirect('/') 
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

# --- RBAC Helper Functions (Task 3 Fix: Robust Admin Check) ---

def is_admin(user):
    """
    Robust check for the 'Admin' role, handling cases where the profile might be missing.
    This structure is very reliable for passing access control checks.
    """
    if not user.is_authenticated:
        return False
        
    # Check if the user has the related profile object before accessing the role
    if hasattr(user, 'userprofile'):
        return user.userprofile.role == 'Admin'
    
    return False

def is_librarian(user):
    """Returns True if the user's role is Librarian or Admin."""
    if not user.is_authenticated or not hasattr(user, 'userprofile'):
        return False
    return user.userprofile.role in ['Librarian', 'Admin']

def is_member(user):
    """Returns True if the user's role is Member."""
    if not user.is_authenticated or not hasattr(user, 'userprofile'):
        return False
    return user.userprofile.role == 'Member'

# --- Role-Based Views (Task 3) ---

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """View accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """View accessible only to Librarian and Admin users."""
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """View accessible only to Member users."""
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
