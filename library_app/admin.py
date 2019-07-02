from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Author, Book, Sale

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Sale)

