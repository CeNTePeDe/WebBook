from django.urls import path
from .views import index, LoanedBookByUserListView
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    # url(r'^book/(?P<bookid>\d+)/$', BookDetailView.as_view(), name='book-detail'),
]
urlpatterns += [
    url(r'^mybooks/$', LoanedBookByUserListView.as_view(), name='my-borrowed')
]
