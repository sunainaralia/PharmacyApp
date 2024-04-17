from django.urls import path, include


urlpatterns = [
    path("api/", include("v1.api.urls")),
]
