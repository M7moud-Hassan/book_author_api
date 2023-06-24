from django.db.models import F
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book, Pages
from .serializers import BookSerializer, PageSerializer, BookSerializerSave, BookSerializerView
from author.models import Author
from django.contrib.auth.models import User


@api_view(['GET'])
def get_index(request):
    pages = Pages.objects.all().count()
    books = Book.objects.all().count()
    authors_count = User.objects.filter(groups__name='Authors').count()
    readers_count = User.objects.filter(groups__name='Readers').count()
    return Response({'pages': pages, 'books': books, 'authors': authors_count, 'readers': readers_count})


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_list(request):
    if request.user.has_perm('book.view_book'):
        paginator = PageNumberPagination()
        paginator.page_size = 8
        books = Book.objects.all()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_list_author(request, pk):
    if request.user.has_perm('book.view_book'):
        try:
            paginator = PageNumberPagination()
            paginator.page_size = 8
            author = Author.objects.get(id=pk)
            books = Book.objects.filter(author=author)
            paginated_books = paginator.paginate_queryset(books, request)
            serializer = BookSerializer(paginated_books, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Author.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_detail(request, pk):
    if request.user.has_perm('book.view_book'):
        try:
            book = Book.objects.get(pk=pk)

            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def book_detail_view(request, pk):
    if request.user.has_perm('book.view_book'):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializerView(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def book_create(request):
    if request.user.has_perm('book.add_book'):
        serializer = BookSerializerSave(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def book_update(request, pk):
    if request.user.has_perm('book.change_book'):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def book_delete(request, pk):
    if request.user.has_perm('book.delete_book'):
        try:
            book = Book.objects.get(pk=pk)
            pages = Pages.objects.filter(book=book)
            pages.delete()
            book.delete()
            return Response(status=204)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def page_list(request, pk):
    if request.user.has_perm('book.view_pages'):
        try:
            paginator = PageNumberPagination()
            paginator.page_size = 8
            pages = Pages.objects.filter(book=Book.objects.get(id=pk))
            paginated_pages = paginator.paginate_queryset(pages, request)
            serializer = PageSerializer(paginated_pages, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def page_create(request):
    if request.user.has_perm('book.add_pages'):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def page_update(request, pk):
    if request.user.has_perm('book.change_pages'):
        try:
            page = Pages.objects.get(pk=pk)
            serializer = PageSerializer(page, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Pages.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def page_delete(request, pk):
    if request.user.has_perm('book.delete_pages'):
        try:
            page = Pages.objects.get(pk=pk)
            Pages.objects.filter(number__gt=page.number, book=page.book).update(number=F('number') - 1)
            page.delete()
            return Response(status=204)
        except Pages.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'per': 'not allow'}, status=status.HTTP_401_UNAUTHORIZED)
