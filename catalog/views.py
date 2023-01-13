from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    context = {'num_books': num_books,
               'num_instances': num_instances,
               'num_authors': num_authors}
    return render(request, 'catalog\index.html', context)

class BookListView(generic.ListView):
    model = Book
