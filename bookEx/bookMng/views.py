from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import MainMenu

from .forms import BookForm
from .forms import CommentForm

from django.http import HttpResponseRedirect

from .models import Book
from .models import Comment

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  })


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


def about_us(request):
    return render(request,
                  'bookMng/aboutUs.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# Search

def searchResult(request):
    book = None
    books = Book.objects.all()
    # books = Book.objects.filter(username=request.user)
    searched = False;
    if request.method == 'POST':
        try:
            searchValue = request.POST.get("searchvalue")
            for b in books:
                if b.name == searchValue:
                    book = b
                    searched = True
                    break
        except Exception:
            print("Error occurred")

    return render(request,
                  'bookMng/searchResult.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'searched': searched,
                      'book': book
                  })


# Favourite
def book_favourite_list(request):
    books = Book.objects.filter(favourite=True)
    return render(request,
                  'bookMng/favourite.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  })


def book_favourite(request, book_id):
    book = Book.objects.get(id=book_id)
    book.favourite = True
    book.save()

    return render(request,
                  'bookMng/book_favourite.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


def book_unfavourite(request, book_id):
    book = Book.objects.get(id=book_id)
    book.favourite = False;
    book.save()

    return render(request,
                  'bookMng/book_favourite.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


# Comment
def comment_list(request, book_id):
    book = Book.objects.get(id=book_id)
    # name = book.name
    comments = Comment.objects.filter(book_id=book_id)
    return render(request,
                  'bookMng/comment_list.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'comments': comments,
                      'book': book
                  })


def post_comment(request, book_id):
    book = Book.objects.get(id=book_id)
    submitted = False
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.username = request.user
                comment.book = book.name
                comment.book_id = book.id
            except Exception:
                pass
            comment.save()
            submitted = True
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postcomment.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book
                  })


def delete_comment(request, cm_id):
    comment = Comment.objects.get(id=cm_id)
    comment.delete()
    return render(request,
                  'bookMng/comment_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

# Rating
def post_rating(request, book_id):
    book = Book.objects.get(id=book_id)
    submitted = False
    if request.method == 'POST':
        try:
            rating = request.POST.get("rating")
            book.rate = rating
        except Exception:
            pass
        book.save()
        submitted = True
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/post_rating.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book
                  })
# def rating_list(request):

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
