from django.urls import path
from .views import details_profile, edit_profile, delete_profile

urlpatterns = [
    path('', details_profile, name='details-profile'),
    path('edit/', edit_profile, name='edit-profile'),
    path('delete/', delete_profile, name='delete-profile')
]
