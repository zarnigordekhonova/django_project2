from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def book_size(request):
    return HttpResponse('<h1>Book size--> 400+ pages, Price--> $4.3,<hr/>')

def book_desc(request):
    return HttpResponse('<h1>Bookcover--> hardcover, Cover color--> Black<hr/>')