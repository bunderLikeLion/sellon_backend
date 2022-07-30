from rest_framework import serializers

from file_manager.models import Image
from user.serializers import UserAbstractSerializer


class ImageSerializer(serializers.ModelSerializer):
    uploader = UserAbstractSerializer(read_only=True)
    file = serializers.ImageField(required=True, use_url=True)

    class Meta:
        model = Image
        fields = [
            'id',
            'file',
            'uploader',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
