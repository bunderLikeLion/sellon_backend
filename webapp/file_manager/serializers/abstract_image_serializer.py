from rest_framework import serializers

from file_manager.models import Image


class AbstractImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(
        use_url=True,
        required=True,
        error_messages={
            'invalid': '이미지를 첨부해주세요.',
        }
    )

    class Meta:
        model = Image
        fields = [
            'id',
            'file',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
