from rest_framework import serializers

from dealing.models import Dealing, DealingEvaluation


class DealingEvaluationSerializer(serializers.ModelSerializer):

    dealing_id = serializers.PrimaryKeyRelatedField(
        source='dealing',
        queryset=Dealing.objects.all(),
    )

    def update(self, instance, validated_data):
        validated_data.pop('dealing_id', None)
        validated_data.pop('dealing', None)
        return super().update(instance, validated_data)

    class Meta:
        model = DealingEvaluation
        fields = [
            'dealing_id',
            'rate',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
            'dealing',
            'evaluator',
        ]
