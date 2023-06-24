from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from django.contrib.auth.models import Group

from .serializers import AuthorRegistrationSerializer, LoginSerializer, AuthorSerializerTop, \
    UserRegistrationSerializer
from rest_framework_simplejwt.tokens import  UntypedToken


@api_view(['GET'])
def get_top_authors(request):
    top_authors = Author.objects.annotate(num_books=Count('book')).order_by('-num_books')[:50]
    serializer = AuthorSerializerTop(top_authors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_author(request):
    serializer = AuthorRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    check = Author.objects.filter(email=request.data['email']).first()
    if check:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "email": ["email already exits"]
        })
    user = serializer.save()

    # Assign user to the "Authors" group
    authors_group, _ = Group.objects.get_or_create(name='Authors')
    authors_group.user_set.add(user)
    serializer2 = LoginSerializer(data=request.data)
    serializer2.is_valid(raise_exception=True)
    return Response(serializer2.validated_data)


@api_view(['POST'])
def register_reader(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    check = Author.objects.filter(email=request.data['email']).first()
    if check:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "email": ["email already exits"]
        })
    user = serializer.save()

    # Assign user to the "Authors" group
    authors_group,_ = Group.objects.get_or_create(name='Readers')
    authors_group.user_set.add(user)
    serializer2 = LoginSerializer(data=request.data)
    serializer2.is_valid(raise_exception=True)
    return Response(serializer2.validated_data)


@api_view(['POST'])
def login_author(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)


@api_view(['POST'])
def is_token_expired(request):
    try:
        data = UntypedToken(request.data['token'])
        return Response({'expired': False})
    except:
        return Response({'expired': True})
