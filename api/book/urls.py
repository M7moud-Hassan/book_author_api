from django.urls import path

from .views import *

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('create_book/', book_create, name='book-create'),
    path('book_detail/<int:pk>/',book_detail,name='book_detail'),
    path('book_update/<int:pk>/',book_update,name='book_update'),
    path('page_list/<int:pk>/',page_list,name='page_list'),
    path('page_create/',page_create,name='page_list'),
    path('page_update/<int:pk>/',page_update,name='page_update'),
    path('page_delete/<int:pk>/',page_delete,name='page_delete')
]
