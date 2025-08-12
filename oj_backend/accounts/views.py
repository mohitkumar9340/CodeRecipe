from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class UserRegisterView(APIView):
    # queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print("got a register hit")
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    def post(self, request):
        # return Response(request.data, status= 201)
        print("got a login hit")
        print(request.data)
        # breakpoint()
        serializer = UserLoginSerializer(data=request.data)
        print("serializer: ", serializer)
        if(serializer.is_valid()):
            print("serializer: ", serializer)
            print("serializer: ", serializer.data)
            print("it's valid")

            return Response(serializer.validated_data, status=201)
        return Response(serializer.errors, status=400)
        print("serializer: ", serializer)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=201)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        })

class GuestLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        data = {
            "username": "Guest",
            "password": "guest"
        }
        serializer = UserLoginSerializer(data=data)
        if(serializer.is_valid()):
            print("serializer: ", serializer)
            print("serializer: ", serializer.data)
            return Response(serializer.validated_data, status=201)
        return Response(serializer.errors, status=400)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        u = User.objects.get(username=user.username)
        return Response({
            "firstname": u.first_name,
            "lastname": u.last_name,
            "username": u.username,
            "email": u.email
        })