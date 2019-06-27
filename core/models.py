from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(verbose_name="Description of the eBook")
    slug = models.SlugField(title, max_length=50, unique=True, null=False)
    date_added = models.DateField(auto_now_add=True)

    image_url = models.URLField(null=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name