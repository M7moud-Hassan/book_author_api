from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from author.serializers import AuthorRegistrationSerializer, AuthorLoginSerializer


@api_view(['POST'])
def register_author(request):
    serializer = AuthorRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({'message': 'User registered successfully'})


@api_view(['POST'])
def login_author(request):
    serializer = AuthorLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)
