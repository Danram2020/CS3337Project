from django.urls import path
from . import views

from bookMng.views import Register

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),

    # About us
    path('aboutUs', views.about_us, name='aboutUs'),

    # Search
    path('searchResult', views.searchResult, name='searchResult'),

    # Favourite
    path('book_favourite/<int:book_id>', views.book_favourite, name='book_favourite'),
    path('book_unfavourite/<int:book_id>', views.book_unfavourite, name='book_unfavourite'),
    path('favourite', views.book_favourite_list, name='favourite'),
]
