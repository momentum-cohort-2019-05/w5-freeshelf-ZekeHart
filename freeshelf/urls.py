"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('', RedirectView.as_view(url='/all-books/')),
    path('freeshelf/', views.freeshelf, name='freeshelf'),
    path('all-books/', views.all_books, name='all-books'),
    path('favorites_list/', views.favorites_list, name='favorites_list'),
    # path('specific_book/', views.specific_book, name='specific_book'),
    # path('books/', views.BookListView.as_view(), name='books'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('admin/', admin.site.urls),
    path('favorite_toggle/<slug>',
         views.favorite_toggle,
         name='favorite-toggle'),
    # path('all-books/<slug>',
    #      views.BookDetailView.as_view(),
    #      name='book-detail'),
    path('categories/<int:pk>', views.category_detail, name='category-detail'),
    path('all-books/<slug>', views.specific_book, name='specific_book'),
    path('accounts/', include('registration.backends.simple.urls')),
]
