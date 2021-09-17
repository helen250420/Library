from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from order.models import Order


def books(request):
    books = Book.get_all()
    context = {
        'books': books,
        'title': 'List of books'
    }
    return render(request, 'book/books.html', context)


def book(request, book_id):
    book = Book.get_by_id(book_id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book/book.html', context)

def no_order(request):
    unorder = Book.get_all()
    order = Order.get_all()
    context = {
        'books': unorder,
        'order': order
    }
    return render(request, 'book/no_ordering.html')