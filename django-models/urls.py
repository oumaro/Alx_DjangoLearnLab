# django_models/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Link the app's URLs to a base path, e.g., '/relationship/'
    path('relationship/', include('relationship_app.urls')),
]
