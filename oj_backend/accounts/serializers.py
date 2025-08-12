from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, data):
        print("Entered Register Serializer")
        username = data["username"]
        email = data["email"]
        password = data["password"]

        user = User.objects.filter(username=username)

        if user.exists():
            raise serializers.ValidationError('Username already exists')
        user = User.objects.create_user(username=username, email=email,password=password)
        user.save()
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required = True,
        write_only = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
    )
    class Meta:
        model = User
        fields = ['username', 'password']
    def validate(self, data):
        print("Entered Login Serializer")
        print(data)
        username = data["username"]
        password = data["password"]

        # user = User.objects.filter(username=username).first()

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User with this username does not exist')
        else:
            print("User exists")
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError('Incorrect password')
        token = RefreshToken.for_user(user)
        print("returning token")
        data = {
            "username" : user.username,
            "token" : {
                "refresh" : str(token),
                "access" : str(token.access_token)
            }
        }
        print(data)
        return data

