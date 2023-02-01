from django.urls import path


from .views import index, LoanedBookByUserListView, BookCreate, BookDelete, BookUpdate, BookDetailView, ContactFormView
from django.conf.urls import url
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(index), name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    ]
urlpatterns += [
    url(r'^mybooks/$', LoanedBookByUserListView.as_view(), name='my-borrowed'),
    url(r'book/create/$', BookCreate.as_view(), name='book_create'),
    url(r'book/update/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_update'),
    url(r'book/delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
]
