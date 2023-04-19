from django.contrib import admin
from .models import Author, Category


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "categories",)


admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)