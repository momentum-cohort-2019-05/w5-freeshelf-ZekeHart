from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from core.models import Book, Category
from django.contrib.auth.decorators import login_required


# Create your views here.
def freeshelf(request):
    num_books = Book.objects.count()
    return render(request, 'freeshelf.html', {
        'num_books': num_books,
    })


def all_books(request):
    valid_sorts = ['title', 'author', 'date_added']

    sort = request.GET.get('sort', default='date_added')
    if sort not in valid_sorts:
        sort = 'date_added'
    sorted_books = Book.objects.all().order_by(sort)

    return render(request, 'core/all-books.html', {
        "sorted_books": sorted_books,
        "sort": sort,
        "valid_sorts": valid_sorts,
    })


@login_required
def favorites_list(request):
    return render(request, 'favorites_list.html', {})


def specific_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'core/specific_book.html', {'book': book})


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category


# class BookDetailView(generic.DetailView):
#     model = Book

# class BookListView(generic.ListView):
#     model = Book