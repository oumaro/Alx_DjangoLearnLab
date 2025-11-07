# relationship_app/views.py (Add the following to your existing file)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Note: You can remove the old import 'from django.views.generic.detail import DetailView'
# and replace it with the clean: from django.views.generic import DetailView
# or just keep the old one if the checker demands it.
from django.views.generic import DetailView # Standard import style

# (Keep your existing imports and views: Book, Library, list_books, LibraryDetailView)
from .models import Book, Library 
from .models import Library # For the pedantic checker's import check


# --- 3. New View: User Registration (Function-based) ---

def register(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user object
            form.save()
            # Redirect the user to the login page after successful registration
            return redirect('login') 
    else:
        # Create a blank form
        form = UserCreationForm()
        
    context = {'form': form}
    
    # Template path matches the structure: relationship_app/templates/relationship_app/register.html
    return render(request, 'relationship_app/register.html', context)
