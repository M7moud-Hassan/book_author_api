from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book, Pages
from .serializers import BookSerializer, PageSerializer


# Create your views here.
@api_view(['GET'])
def book_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    books = Book.objects.all()
    paginated_books = paginator.paginate_queryset(books, request)
    serializer = BookSerializer(paginated_books, many=True)
    return paginator.get_paginated_response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response(status=204)


# Page API Endpoints

@api_view(['GET'])
def page_list(request):
    pages = Pages.objects.all()
    serializer = PageSerializer(pages, many=True)
    return Response(serializer.data)


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
    page.delete()
    return Response(status=204)
