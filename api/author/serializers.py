from rest_framework import serializers
from .models import  Author
from rest_framework_simplejwt.tokens import RefreshToken


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'email']


class AuthorLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = Author.objects.filter(username=data['username']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            data['access_token'] = str(refresh.access_token)
            data['refresh_token'] = str(refresh)
            data['user'] = AuthorSerializer(user).data
        else:
            raise serializers.ValidationError('Incorrect username or password')
        return data


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
