from django.urls import path
from v1.api.user_chat.consumers import ChatConsumer


websocket_urlpatterns = [
    path('v1/api/chat/<str:group_name>', ChatConsumer.as_asgi()),
]
