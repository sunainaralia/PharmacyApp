from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer, ChangePasswordSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# GENERATE TOKEN MANNUALLY
def get_token_for_user(user):
    refress = RefreshToken.for_user(user)
    return {
        "refress": str(refress),
        "access": str(refress.access_token),
    }


# USER REGISTRATION VIEW
class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({"message": "Registration Successfully", "token": token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER LOGIN VIEW
class LoginView(APIView):

    def post(self, request):
        print(request)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_token_for_user(user)
                return Response({"message": "Login Successfully", "token": token}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {
                    'non_field_errors': ['Email or Password is not valid']
                }}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER PROFILE VIEW
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = ProfileSerializer(request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CHANGE USER PASSWORD
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data, context={
            'user': request.user
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Password Changed Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
