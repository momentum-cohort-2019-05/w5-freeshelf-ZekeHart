from django import forms

from .models import Book


class FavoriteToggle(forms.Form):
    favorited = forms.BooleanField(required=False, initial=False)