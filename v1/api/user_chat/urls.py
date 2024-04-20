from django.urls import path
from .consumers import ChatConsumer


urlpatterns = [
    path('ws/ac/', ChatConsumer.as_asgi()),
]
