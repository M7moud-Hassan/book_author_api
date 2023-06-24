from django.urls import path

from .views import *

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('book_list_author/<int:pk>/',book_list_author,name='book_list_author'),
    path('create_book/', book_create, name='book-create'),
    path('book_detail/<int:pk>/',book_detail,name='book_detail'),
    path('book_update/<int:pk>/',book_update,name='book_update'),
    path('page_list/<int:pk>/',page_list,name='page_list'),
    path('page_create/',page_create,name='page_list'),
    path('page_update/<int:pk>/',page_update,name='page_update'),
    path('page_delete/<int:pk>/',page_delete,name='page_delete'),
    path('book_delete/<int:pk>/',book_delete,name='book_delete'),
    path('get_index/',get_index,name='get_index'),
    path('book_detail_view/<int:pk>/',book_detail_view,name='book_detail_view')
]
