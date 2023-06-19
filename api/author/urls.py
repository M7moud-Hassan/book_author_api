from django.urls import path
from .views import *

urlpatterns = [
    path('register',register_author,name='register'),
    path('login',login_author,name='login')
]