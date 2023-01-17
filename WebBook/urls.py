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
from catalog.views import index, BookListView, BookDetailView, AuthorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    # path('book/<int:bookid>/', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]
