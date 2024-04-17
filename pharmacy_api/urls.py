from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('v1.api.account.urls')),
    path('api/medical/side/', include('v1.api.medical_side.urls')),
]
