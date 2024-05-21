from django.contrib import admin

# Register your models here.
from .models import Book, Note

admin.site.register(Book)
admin.site.register(Note)