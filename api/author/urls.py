from django.urls import path
from .views import *

urlpatterns = [
    path('register_author',register_author,name='register'),
    path('register_reader', register_reader, name='register_reader'),
    path('login',login_author,name='login'),
    path('is_token_expired',is_token_expired,name='is_token_expired'),
    path('get_top_authors/',get_top_authors,name='authors_list')
]