from rest_framework import serializers

from user.models import User


class UserAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
        read_only_fields = [
            'id',
            'username',
            'email',
        ]
