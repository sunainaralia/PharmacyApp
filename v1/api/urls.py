from django.urls import path, include


urlpatterns = [
<<<<<<< HEAD
    path("user/", include('v1.api.account.urls')),
    path("medical/", include('v1.api.medical_side.urls')),
=======
    path("user/", include("v1.api.account.urls")),
    path("doctor/", include("v1.api.doctor.urls")),
    path("rating/", include("v1.api.rating.urls")),
>>>>>>> origin/main
]
