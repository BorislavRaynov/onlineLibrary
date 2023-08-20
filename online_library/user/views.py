from django.shortcuts import render, redirect
from .models import Profile
from online_library.book.models import Book
from .forms import EditProfileForm, DeleteProfileForm
# Create your views here.

def details_profile(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'online_library/user/profile.html', context=context)

def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)
    books = Book.objects.all()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'form': form,
        'profile': profile,
        'books': books
    }

    return render(request, 'online_library/user/edit-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()
    books = Book.objects.all()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        books.delete()
        return redirect('home-page')

    context = {
        'profile': profile,
        'books': books,
        'form': form
    }

    return render(request, 'online_library/user/delete-profile.html', context=context)
