# django_models/settings.py (at the bottom)

# Redirect after successful login
LOGIN_REDIRECT_URL = '/'  # Redirects to the homepage (or '/relationship/books/' if you prefer)

# Redirect after successful logout
LOGOUT_REDIRECT_URL = 'login' # Redirects to the login page (using the URL name)
