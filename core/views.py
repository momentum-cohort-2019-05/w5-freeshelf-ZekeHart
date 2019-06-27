from django.shortcuts import render
from django.views import generic
from core.models import Book


# Create your views here.
def freeshelf(request):
    num_books = Book.objects.count()
    return render(request, 'freeshelf.html', {
        'num_books': num_books,
    })


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book