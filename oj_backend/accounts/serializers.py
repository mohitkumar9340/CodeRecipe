from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, data):
        username = data["username"]
        email = data["email"]
        password = data["password"]

        user = User.objects.filter(username=username)
        if user.exists():
            raise serializers.ValidationError('Username already exists')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data["username"]
        password = data["password"]

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User with this username does not exist')
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password')
        token = RefreshToken.for_user(user)
        return {
            "username": user.username,
            "token": {
                "refresh": str(token),
                "access": str(token.access_token)
            }
        }
