from rest_framework import serializers

from user.models import User


class UserDealingRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'avatar',
            'completed_dealings_count',
        ]
        read_only_fields = [
            'id',
            'username',
            'completed_dealings_count',
        ]

        order_by = [
            '-completed_dealings_count',
        ]
