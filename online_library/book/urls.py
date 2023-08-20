from django.urls import path, include
from .views import index, add_book, edit_book, details_book, delete_book

urlpatterns = [
    path('', index, name='home-page'),
    path('add/', add_book, name='add-book'),
    path('edit/<int:book_id>/', edit_book, name='edit-book'),
    path('details/<int:book_id>/', details_book, name='details-book'),
    path('delete/<int:book_id>/', delete_book, name='delete-book')
]
