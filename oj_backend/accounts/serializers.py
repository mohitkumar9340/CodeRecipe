from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, data):
        username = data["username"]
        email = data["email"]
        password = data["password"]

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data["username"]
        password = data["password"]

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        token = RefreshToken.for_user(user)
        return {
            "username": user.username,
            "token": {
                "refresh": str(token),
                "access": str(token.access_token)
            }
        }
