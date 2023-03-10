from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .forms import AuthorForm, ContactForm
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = cache.get('num_books')
    if not num_books:
        num_books = Book.objects.all().count()
        cache.set('num_books', num_books, 60)

    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='5').count()
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
    template_name = 'catalog/book_detail.html'
    pk_url_kwarg = 'book_pk'


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

    # paginate_by = 10

    def get_queryset(self):
        return not BookInstance.objects.filter(
            borrower=self.request.user).filter(status__exact='4').order_by('due_back')


def authors_add(request):
    author = Author.objects.all()
    authors_form = AuthorForm()
    context = {
        'form': authors_form,
        'author': author
    }
    return render(request, 'catalog/authors_add.html', context)


def create(request):
    if request.method == 'POST':
        author = Author()
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death')
        author.save()
        return HttpResponseRedirect('/authors_add/')


def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/authors_add/')
    except Author.DoesNotExist:
        return HttpResponseRedirect('<h1>Автор не найден</h1>')


def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author = Author()
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death')
        author.save()
        return HttpResponseRedirect('/authors_add/')
    else:
        return render(request, 'catalog/edit1.html', {'author': author})


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'catalog/contact.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')