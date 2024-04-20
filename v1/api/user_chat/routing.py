from django.urls import path

from v1.api.user_chat.consumers import ChatConsumer


websocket_urlpatterns = [
    path('ws/ac/', ChatConsumer.as_asgi()),
]
