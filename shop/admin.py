from django.contrib import admin
from .models import Genre, Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author','price','available']
    list_filter = ['available',]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}