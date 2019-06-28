from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(verbose_name="Description of the eBook")
    slug = models.SlugField(title, max_length=50, unique=True, null=False)
    date_added = models.DateField(auto_now_add=True)
    times_favorited = models.PositiveSmallIntegerField(default=0)
    image_url = models.URLField(null=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    # slug = models.SlugField(
    #     name,
    #     max_length=50,
    #     unique=False,
    #     null=True,
    # )

    def __str__(self):
        return self.name


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'fav_book']
        ordering = ['-date_added']

    def __str__(self):
        return self.fav_book.title