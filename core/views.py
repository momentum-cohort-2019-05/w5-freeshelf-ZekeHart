from django.shortcuts import render
from django.views import generic
from core.models import Book

# Create your views here.
# def


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book