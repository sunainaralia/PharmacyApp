from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView  # type: ignore
import json
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
    SendPasswordResetEmailSerializer,
    PasswordResetSerializer,
    LoginWithUserNameSerializer,
)
from v1.renderers import ErrorRenderer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# GENERATE TOKEN MANNUALLY
def get_token_for_user(user):
    refress = RefreshToken.for_user(user)
    return {
        "refress": str(refress),
        "access": str(refress.access_token),
    }


# USER REGISTRATION VIEW
class RegistrationView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response(
                {
                    "message": "Registration Successfully",
                    "token": token,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER LOGIN with email
class LoginView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                if not user.is_blocked:
                    details = User.objects.get(email=email)
                    user_detail = {
                        "user_name": details.user_name,
                        "email": details.email,
                        "id": details.id,
                        "role": details.role,
                    }
                    token = get_token_for_user(user)
                    return Response(
                        {
                            "message": "Login Successfully",
                            "token": token,
                            "data": user_detail,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"errors": {"non_field_errors": ["you are blocked"]}},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["email or password is not correct"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER PROFILE VIEW
class ProfileView(APIView):
    renderer_classes = [ErrorRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CHANGE USER PASSWORD
class ChangePasswordView(APIView):
    renderer_classes = [ErrorRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            details = request.user
            user_detail = {
                "user_name": details.user_name,
                "email": details.email,
                "id": details.id,
                "role": details.role,
            }
            return Response(
                {"message": "Password Changed Successfully", "data": user_detail},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# SEND MAIL FOR RESET PASSWORD
class SendPasswordResetEmailView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data["email"]["otp"])
            return Response(
                {
                    "message": "Password reset link send. Please check your email",
                    "otp": serializer.validated_data["email"]["otp"],
                    "user_id": serializer.validated_data["email"]["user_id"],
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# RESET USER PASSWORD
class PasswordResetView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request, pk, otp, format=None):
        serializer = PasswordResetSerializer(
            data=request.data, context={"user_id": pk, "otp": otp}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "Password Reset Successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# login user with username
class LoginWithUserNameView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request):
        serializer = LoginWithUserNameSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("user_name")
            password = serializer.data.get("password")
            user_data = User.objects.get(user_name=username)
            print(user_data)
            email = user_data.email
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if not user.is_blocked:
                    token = get_token_for_user(user)
                    user_detail = {
                        "user_name": user.user_name,
                        "email": user.email,
                        "id": user.id,
                        "role": user.role,
                    }
                    return Response(
                        {
                            "msg": "login user successfully",
                            "token": token,
                            "Data": user_detail,
                        }
                    )
                else:
                    return Response(
                        {"errors": {"non_field_errors": ["you are blocked"]}},
                        status=status.HTTP_404_NOT_FOUND,
                    )

            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["username or password is not correct"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
