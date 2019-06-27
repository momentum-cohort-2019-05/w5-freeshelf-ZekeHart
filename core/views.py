from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from core.models import Book


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


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book