from rest_framework import generics
from rest_framework.response import Response
from .models import Chat, Group
from .serializers import ChatSerializer, GroupSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        group_name = self.kwargs.get('group_name')
        group, _ = Group.objects.get_or_create(name=group_name)
        serializer.save(group=group)

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
