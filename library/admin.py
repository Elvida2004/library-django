from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Author, Publisher, Genre, City

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'genre', 'year')
    list_filter = ('genre', 'publisher', 'year')
    search_fields = ('title', 'author__lastname', 'author__name', 'author__surname')
    ordering = ('title',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'name', 'surname')
    search_fields = ('lastname', 'name', 'surname')
    ordering = ('lastname', 'name', 'surname')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')
    list_filter = ('city',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)