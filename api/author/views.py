from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .models import  Author

from .serializers import AuthorRegistrationSerializer, AuthorLoginSerializer
from rest_framework_simplejwt.tokens import AccessToken, UntypedToken


@api_view(['POST'])
def register_author(request):
    serializer = AuthorRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    check=Author.objects.filter(email=request.data['email']).first()
    if check:
        return  Response(status=status.HTTP_400_BAD_REQUEST,data={
            "email":["email already exits"]
        })
    user = serializer.save()
    serializer2 = AuthorLoginSerializer(data=request.data)
    serializer2.is_valid(raise_exception=True)
    return Response(serializer2.validated_data)


@api_view(['POST'])
def login_author(request):
    serializer = AuthorLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)

@api_view(['POST'])
def is_token_expired(request):
    try:
        data = UntypedToken(request.data['token'])
        return Response({'expired':False})
    except:
        return Response({'expired':True})
