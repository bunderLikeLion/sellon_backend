from rest_framework import serializers

from user.models import User


class UserAbstractSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(
        use_url=True,
    )

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
