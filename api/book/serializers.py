from rest_framework import serializers

from author.serializers import AuthorSerializer
from .models import Book, Pages


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

class BookSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'

class BookSerializerView(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'image', 'author', 'pages']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        author_data = data.pop('author')
        pages_data = self.get_pages(instance.author,data['id'])  # Get pages data

        # Merge author and pages data
        data['author'] = author_data
        data['pages'] = pages_data

        return data

    def get_pages(self, author,id):
        return PageSerializer(Pages.objects.filter(book__author=author,book__id=id), many=True).data
