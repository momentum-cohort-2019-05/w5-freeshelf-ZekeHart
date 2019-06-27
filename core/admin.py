from django.contrib import admin
from core.models import Book
# Register your models here.

admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
