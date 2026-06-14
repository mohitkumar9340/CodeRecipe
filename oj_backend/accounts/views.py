from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            first_error = next(iter(errors.values()))
            msg = first_error[0] if isinstance(first_error, list) else first_error
            return Response({"message": msg, "errors": errors}, status=400)

        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "token": {
                "refresh": str(token),
                "access": str(token.access_token)
            }
        }, status=201)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            first_error = next(iter(serializer.errors.values()))
            msg = first_error[0] if isinstance(first_error, list) else first_error
            return Response({"message": msg, "errors": serializer.errors}, status=400)

        return Response({
            "message": "Login successful",
            **serializer.validated_data
        }, status=200)


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
        guest, created = User.objects.get_or_create(
            username="Guest",
            defaults={"email": "guest@example.com"}
        )
        if created:
            guest.set_password("guest")
            guest.save()

        user = User.objects.get(username="Guest")
        token = RefreshToken.for_user(user)
        return Response({
            "message": "Guest login successful",
            "username": user.username,
            "token": {
                "refresh": str(token),
                "access": str(token.access_token)
            }
        }, status=200)


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        name = f"{user.first_name} {user.last_name}".strip()
        return Response({
            "firstname": user.first_name,
            "lastname": user.last_name,
            "name": name or user.username,
            "username": user.username,
            "email": user.email
        })
