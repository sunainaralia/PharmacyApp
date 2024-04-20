# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from v1.api.user_chat.urls import urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pharmacy_api.settings')

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": URLRouter(urlpatterns),
#     }
# )

# In your Django project's routing.py or asgi.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path, include

from v1.api.user_chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('', ChatConsumer.as_asgi()),
        ])
    ),
})
