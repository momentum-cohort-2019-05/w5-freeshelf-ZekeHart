# Generated by Django 2.2.2 on 2019-06-26 12:38

from django.db import migrations
from django.utils.text import slugify


def slugify_title(apps, schema_editor):
    Book = apps.get_model('core', 'Book')
    for book in Book.objects.all():
        book.slug = slugify(book.title)
        book.save()


def do_nothing(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_book_slug'),
    ]

    operations = [migrations.RunPython(slugify_title, do_nothing)]