from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    ProfileView,
    ChangePasswordView,
    SendPasswordResetEmailView,
    PasswordResetView,
)

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="change_password",
    ),
    path(
        'resetpassword/<pk>/<otp>/', PasswordResetView.as_view(), name="reset-password"
    ),
]
