from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def authors(request):
    authors = Author.get_all()
    context = {
        'authors': authors,
        'title': 'List of Authors'
    }
    return render(request, 'author/authors.html', context)


def author(request, author_id):
    author = Author.get_by_id(author_id=author_id)
    context = {
        'author': author,
    }
    return render(request, 'author/author.html', context)