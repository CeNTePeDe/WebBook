"""WebBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf.urls import url

from WebBook import settings
from catalog.models import Book
from catalog.views import index, BookListView, BookDetailView, AuthorListView, LoanedBookByUserListView, authors_add, \
    edit1, delete, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    path('book/<int:book_pk>/', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    path('authors_add/', authors_add, name='authors_add'),
    path('edit1/<int:id>/', edit1, name='edit1'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^mybooks/$', LoanedBookByUserListView.as_view(), name='my-borrowed'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
