from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='2').count()
    num_authors = Author.objects.count()
    # добавим сессии
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'num_authors': num_authors,
               'num_visits': num_visits, }
    return render(request, 'catalog\index.html', context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/catalog.html'
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book
    # template_name = 'catalog/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    '''Универсальный класс для представления списка книг,
    находящихся в заказеу текущего пользователя'''
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return not BookInstance.objects.filter(
            borrower=self.request.user).filter(status__exact='2').order_by('due_back')



