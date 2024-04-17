from django.urls import path, include


urlpatterns = [
    path("user/", include('v1.api.account.urls')),
]
