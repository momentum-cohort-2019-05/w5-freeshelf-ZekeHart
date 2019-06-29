from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from core.models import Book, Category, UserFavorite
from core.forms import FavoriteToggle
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages


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
    have_favorited = []
    if not request.user.is_anonymous:
        for fav in UserFavorite.objects.filter(user=request.user):
            have_favorited.append(fav.fav_book)
    return render(request, 'core/specific_book.html', {
        'book': book,
        'have_favorited': have_favorited
    })


def favorite_toggle(request, slug):
    book = get_object_or_404(Book, slug=slug)
    has_favorited = UserFavorite.objects.filter(user=request.user,
                                                fav_book=book)

    if not has_favorited:
        make_fav = UserFavorite(user=request.user, fav_book=book)
        make_fav.save()
        messages.success(request,
                         f'You added { book.title } to your favorites!')
    else:
        has_favorited.delete()
        messages.success(request,
                         f'You removed { book.title } from your favorites.')
    return HttpResponseRedirect(request.GET.get("next"))


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    book_list = Book.objects.filter(category=category)
    return render(request, 'core/category_detail.html', {
        'category': category,
        'book_list': book_list
    })


class CategoryListView(generic.ListView):
    model = Category


# attempt to do favorites wuth forms
# def specific_book(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     if request.method == 'POST':
#         form = FavoriteToggle(request.POST)
#         if form.is_valid():
#             form_input = form.cleaned_data['form_input']
#             if form_input:
#                 add_fav = UserFavorite(user=request.user, favorite_book=book)
#                 book.times_favorited += 1
#                 book.save()
#                 add_fav.save()
#             else:
#                 remove_fav = UserFavorite.objects.filter(
#                     user=request.user).filter(favorite_book=book).first()
#                 book.times_favorited -= 1
#                 book.save()
#                 remove_fav.delete()
#         return redirect(to='book-detail', slug=slug)
#     form = FavoriteToggle()
#     book = Book.objects.get(slug=slug)
#     fave_list = book.userfavorite_set.all()
#     have_favorited = []
#     for favorite in fave_list:
#         have_favorited.append(favorite.user)
#     return render(request, 'core/specific_book.html', {
#         'have_favorited': have_favorited,
#         'book': book,
#         'form': form
#     })

# class CategoryDetailView(generic.DetailView):
#     model = Category

# class BookDetailView(generic.DetailView):
#     model = Book

# class BookListView(generic.ListView):
#     model = Book