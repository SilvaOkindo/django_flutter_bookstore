from django.contrib import admin
from .models import Book, Author, Category, Review, Publisher


# Register your models here.

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cover_image']


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Review)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book', 'rating']


@admin.register(Publisher)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
