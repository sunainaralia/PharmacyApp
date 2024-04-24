from django.urls import path

from v1.api.user_chat.consumers import ChatConsumer


websocket_urlpatterns = [
    path('v1/api/chat/', ChatConsumer.as_asgi()),
]
