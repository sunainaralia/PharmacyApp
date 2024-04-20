from django.urls import path, include


urlpatterns = [
    path("user/", include("v1.api.account.urls")),
    path("doctor/", include("v1.api.doctor.urls")),
    path("rating/", include("v1.api.rating.urls")),
    path("chat/", include("v1.api.user_chat.urls")),
]
