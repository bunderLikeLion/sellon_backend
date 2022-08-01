from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from .models import Message
from .permissions import IsMessageEditableOrDestroyable
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [
        IsAuthenticated,
        IsMessageEditableOrDestroyable
    ]
    filter_backends = [OrderingFilter]
    search_fields = ['receiver']
    ordering = ['created_at']

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)

    def get_queryset(self):
        sender_id = self.request.user.id
        return super().get_queryset().filter(sender=sender_id)
