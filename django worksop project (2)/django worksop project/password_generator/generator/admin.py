# myapp/admin.py

from django.contrib import admin
from .models import GeneratedPassword

@admin.register(GeneratedPassword)
class GeneratedPasswordAdmin(admin.ModelAdmin):
    list_display = ('password', 'created_at')
    search_fields = ('password',)
