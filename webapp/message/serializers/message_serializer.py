from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from dealing.models import Dealing
from message.models import Message
from user.serializers import UserAbstractSerializer


class MessageSerializer(ModelSerializer):

    dealing_id = serializers.PrimaryKeyRelatedField(
        source='dealing',
        queryset=Dealing.objects.all(),
        write_only=True,
    )
    sender = UserAbstractSerializer(read_only=True)
    receiver = UserAbstractSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'dealing_id',
            'receiver',
            'sender',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
