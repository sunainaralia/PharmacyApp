from .utils import Util
from django.utils.encoding import DjangoUnicodeDecodeError
from xml.dom import ValidationErr
from .models import User
from rest_framework import serializers
import os
import random


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = (
            "user_name",
            "email",
            "password",
            "password2",
            "is_blocked",
            "created_at",
            "is_admin",
            "role",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password does not match."
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ("email", "password")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "user_name")


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=250, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=250, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password do not match."
            )
        return attrs

    def save(self):
        password = self.validated_data.get("password")
        user = self.context.get("user")
        user.set_password(password)
        user.save()


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            user = User.objects.get(email=value)

            def generate_random_password():
                return "".join(random.choices("0123456789", k=4))

            otp = generate_random_password()
            body = "Your OTP is " + otp
            # Send Mail
            data = {
                "subject": "Reset Password",
                "body": body,
                "to_email": user.email,
                "otp": otp,
                "user_id": user.id,
            }
            Util.send_email(data)
            return data
        else:
            raise serializers.ValidationError("You are not a registered user.")


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=250, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=250, style={"input_type": "password"}, write_only=True
    )
    entered_otp = serializers.CharField(max_length=30)

    class Meta:
        fields = ["password", "password2", "entered_otp"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            password2 = attrs.get("password2")
            entered_otp = attrs.get("entered_otp")
            uid = self.context.get("user_id")
            token = self.context.get("otp")
            if entered_otp != token:
                raise serializers.ValidationError("otp is not correct")
            if password != password2:
                raise serializers.ValidationError(
                    "Password and Confirm Password does not match."
                )
            id = uid
            user = User.objects.get(id=id)
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            raise ValidationErr("Token is invalid or expired")
