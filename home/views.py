from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_book_name(request):
    return HttpResponse('<h1>Book title--> Marthin Eden<hr/>')


def get_book_author(request):
    return HttpResponse('<h1>Book author--> Jack London<hr/>')
