from django.urls import path
from description.views import book_size, book_desc

urlpatterns = [
    path('size', book_size),
    path('description', book_desc)
]