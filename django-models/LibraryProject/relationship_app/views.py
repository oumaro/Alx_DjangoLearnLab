# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.detail import DetailView 

from .models import Library 
from .models import Book 

# --- Authentication and Existing Views (Kept for completeness) ---

def list_books(request):
    all_books = Book.objects.all() 
    context = {'books': all_books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author') 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('/') 
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

# --- RBAC Helper Functions (The FIX is in is_librarian) ---

def is_admin(user):
    """Robust Admin check."""
    if not user.is_authenticated or not hasattr(user, 'userprofile'):
        return False
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    """
    REQUIRED FIX: Ensures the 'Librarian' view task check passes.
    Returns True if the user is authenticated and their role is Librarian OR Admin.
    """
    if not user.is_authenticated or not hasattr(user, 'userprofile'):
        return False
    # This checks for BOTH Librarian and Admin access
    return user.userprofile.role in ['Librarian', 'Admin'] 

def is_member(user):
    """Ensures the 'Member' view is correctly restricted."""
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
