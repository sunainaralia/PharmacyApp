from .utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from xml.dom import ValidationErr
from .models import User
from rest_framework import serializers
import os


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('user_name', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                'Password and Confirm Password does not match.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'user_name',)


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=250,
                                     style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=250,
                                      style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError(
                'Password and Confirm Password does not match.')
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        FRONTEND_URL = os.environ.get('FRONTEND_URL')
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print()
            token = PasswordResetTokenGenerator().make_token(user)
            link = f'{FRONTEND_URL}/api/user/reset-password/'+uid+'/'+token

            body = 'Click following link to reset password'+link
            # Send Mail
            data = {
                'subject': 'Reset Password',
                'body': body,
                'to_email': user.email
            }
            print(data)
            Util.send_email(data)
            return attrs

        else:
            raise ValidationErr("Your are not Registred User")


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=250,
                                     style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=250,
                                      style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError(
                    'Password and Confirm Password does not match.')
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr("Token is invalid or expired")

            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationErr("Token is invalid or expired")
