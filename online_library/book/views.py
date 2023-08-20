from django.shortcuts import render, redirect
from .models import Book
from online_library.user.models import Profile
from online_library.user.forms import RegisterProfileForm
from online_library.book.forms import AddBookForm
# Create your views here.

def index(request):
    profile = Profile.objects.first()
    books = Book.objects.all()
    form = RegisterProfileForm()

    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'profile': profile,
        'books': books,
        'form': form
    }

    return render(request, 'online_library/book/home-page.html', context=context)

def add_book(request):
    form = AddBookForm()
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'form': form
    }

    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            context["books"] = Book.objects.all()
            return render(request, 'online_library/book/home-page.html', context=context)

    return render(request, 'online_library/book/add-book.html', context=context)

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    books = Book.objects.all()
    form = AddBookForm(instance=book)
    profile = Profile.objects.first()
    context = {
        'book': book,
        'profile': profile,
        'form': form,
        'books': books
    }
    if request.method == 'POST':
        form = AddBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            return render(request, 'online_library/book/home-page.html', context=context)

    return render(request, 'online_library/book/edit-book.html', context=context)



def details_book(request, book_id):
    book = Book.objects.get(id=book_id)
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'book': book
    }

    if request.method == 'POST':
        book.delete()
        return render(request, 'online_library/book/home-page.html', context=context)

    return render(request, 'online_library/book/book-details.html', context=context)

def delete_book(request, book_id):
    profile = Profile.objects.first()
    book = Book.objects.get(id=book_id)
    book.delete()
    books = Book.objects.all()
    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'online_library/book/home-page.html', context=context)
