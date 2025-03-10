from django.contrib import admin
from .models import About  # Import the About model

# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_on")  # Display these fields in the admin panel