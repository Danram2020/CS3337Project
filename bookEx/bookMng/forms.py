from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Favourite


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class FavouriteForm(ModelForm):
    class Meta:
        model = Favourite
        fields = [
            'book',
        ]
