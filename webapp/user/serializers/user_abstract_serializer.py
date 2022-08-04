from rest_framework import serializers

from file_manager.serializers.abstract_image_serializer import AbstractImageSerializer
from user.models import User


class UserAbstractSerializer(serializers.ModelSerializer):

    avatar = AbstractImageSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'avatar',
        ]
        read_only_fields = [
            'id',
            'username',
            'email',
        ]
