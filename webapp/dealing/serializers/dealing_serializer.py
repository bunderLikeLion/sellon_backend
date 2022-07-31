from rest_framework import serializers
from dealing.models.dealing import Dealing


class DealingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealing
        fields = '__all__'
