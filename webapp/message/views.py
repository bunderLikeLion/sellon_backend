from rest_framework.viewsets import ModelViewSet
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMessageEditableOrDestroyable


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [
        IsAuthenticated,
        IsMessageEditableOrDestroyable
    ]

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)
