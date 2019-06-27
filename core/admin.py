from django.contrib import admin
from core.models import Book, Category
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
