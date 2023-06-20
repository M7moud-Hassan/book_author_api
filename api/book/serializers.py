from rest_framework import serializers
from .models import Book, Pages


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
