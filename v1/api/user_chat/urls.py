from django.urls import path
from .views import ChatListCreateView, GroupListCreateView

urlpatterns = [
    path('chat/<str:group_name>/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('group/', GroupListCreateView.as_view(), name='group-list-create'),
]
