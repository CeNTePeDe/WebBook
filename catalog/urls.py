from django.urls import path
from .views import index, LoanedBookByUserListView, BookCreate, BookDelete,BookUpdate, BookDetailView
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    ]
urlpatterns += [
    url(r'^mybooks/$', LoanedBookByUserListView.as_view(), name='my-borrowed'),
    url(r'^book/(?P<bookid>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'book/create/$', BookCreate.as_view(), name='book_create'),
    url(r'book/update/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_update'),
    url(r'book/delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
]
