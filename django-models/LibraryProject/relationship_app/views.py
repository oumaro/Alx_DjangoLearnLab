# relationship_app/views.py (Add the following to the end of the file)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test # New Import!
# ... [Keep all existing imports] ...

# --- RBAC Helper Functions ---

def is_admin(user):
    """Returns True if the user's role is Admin."""
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Returns True if the user's role is Librarian or Admin (Admin can do Librarian tasks)."""
    return user.is_authenticated and user.userprofile.role in ['Librarian', 'Admin']

def is_member(user):
    """Returns True if the user's role is Member."""
    # Note: We keep this simple, but often all logged-in users are members.
    return user.is_authenticated and user.userprofile.role == 'Member'

# --- Role-Based Views (Using @user_passes_test) ---

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
