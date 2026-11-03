from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Author, BlogPost


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']
    list_filter = ['author', 'created_on']
    search_fields = ['title', 'content']
