from rest_framework import serializers
from message.models import Message
from user.serializers import UserAbstractSerializer
from user.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = UserAbstractSerializer(read_only=True)
    receiver = UserAbstractSerializer(read_only=True)
    receiver_id = serializers.PrimaryKeyRelatedField(
        source='receiver',
        queryset=User.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'receiver_id',
            'content',
        ]
