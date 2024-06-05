from django.contrib import admin
from .models import CustomUser  # Import your custom User model

admin.site.register(CustomUser)  # Register your custom User model with the admin site
