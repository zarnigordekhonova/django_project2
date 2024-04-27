from django.urls import path
from home.views import get_book_name, get_book_author

urlpatterns = [
    path('book_name', get_book_name),
    path('book_author', get_book_author)
]