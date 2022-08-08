from rest_framework import serializers

from dealing.models import Dealing, DealingEvaluation
from dealing.serializers import DealingSerializer


class UserEvaluationSerializer(serializers.ModelSerializer):
    dealing = DealingSerializer(
        read_only=True,
    )
    dealing_id = serializers.PrimaryKeyRelatedField(
        source='dealing',
        queryset=Dealing.objects.all(),
        write_only=True,
    )

    class Meta:
        model = DealingEvaluation
        fields = [
            'id',
            'dealing',
            'dealing_id',
            'rate',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
            'dealing'
        ]
