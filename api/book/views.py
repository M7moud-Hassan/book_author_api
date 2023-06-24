from django.db.models import F
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book, Pages
from .serializers import BookSerializer, PageSerializer, BookSerializerSave, BookSerializerView
from author.models import  Author
from django.contrib.auth.models import User

@api_view(['GET'])
def get_index(request):
    pages = Pages.objects.all().count()
    books = Book.objects.all().count()
    authors_count = User.objects.filter(groups__name='Authors').count()
    readers_count = User.objects.filter(groups__name='Readers').count()
    return Response({'pages': pages, 'books': books, 'authors': authors_count,'readers':readers_count})

@api_view(['GET'])
def book_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 8
    books = Book.objects.all().order_by('?')
    paginated_books = paginator.paginate_queryset(books, request)
    serializer = BookSerializer(paginated_books, many=True)
    return paginator.get_paginated_response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_list_author(request,pk):
    paginator = PageNumberPagination()
    paginator.page_size = 8
    author=Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    paginated_books = paginator.paginate_queryset(books, request)
    serializer = BookSerializer(paginated_books, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail_view(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializerView(book)
    return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def book_create(request):
    serializer = BookSerializerSave(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    pages=Pages.objects.filter(book=book)
    pages.delete()
    book.delete()
    return Response(status=204)


@api_view(['GET'])
def page_list(request, pk):
    paginator = PageNumberPagination()
    paginator.page_size = 8
    pages = Pages.objects.filter(book=Book.objects.get(id=pk))
    paginated_pages = paginator.paginate_queryset(pages, request)
    serializer = PageSerializer(paginated_pages, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def page_detail(request, pk):
    page = Pages.objects.get(pk=pk)
    serializer = PageSerializer(page)
    return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def page_create(request):
    serializer = PageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def page_update(request, pk):
    page = Pages.objects.get(pk=pk)
    serializer = PageSerializer(page, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def page_delete(request, pk):
    page = Pages.objects.get(pk=pk)
    Pages.objects.filter(number__gt=page.number, book=page.book).update(number=F('number') - 1)
    page.delete()
    return Response(status=204)
