from rest_framework import serializers
from .models import Author
from rest_framework_simplejwt.tokens import RefreshToken
from book.models import Pages, Book
from django.contrib.auth.models import User, Group


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'image']


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username']


class AuthorSerializerTop(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    pages_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'username', 'image', 'books_count', 'pages_count']

    def get_books_count(self, author):
        return Book.objects.filter(author=author).count()

    def get_pages_count(self, author):
        return Pages.objects.filter(book__author=author).count()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            data['access_token'] = str(refresh.access_token)
            data['refresh_token'] = str(refresh)
            data['group'] = Group.objects.filter(user=user).first().name if user.groups.exists() else None
            if data['group'] == 'Authors':
                data['user'] = AuthorSerializer(Author.objects.filter(id=user.id).first()).data
            elif data['group'] == 'Readers':
                data['user'] = ReaderSerializer(user).data
            else:
                raise serializers.ValidationError('group is None')
        else:
            raise serializers.ValidationError('Incorrect username or password')
        data.pop('password', None)
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AuthorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True)

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        user = Author.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])

        if image:
            user.image = image
        user.save()
        return user

    class Meta:
        model = Author
        fields = ['username', 'email', 'password', 'image']
