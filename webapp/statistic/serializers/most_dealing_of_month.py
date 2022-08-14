from rest_framework import serializers

from file_manager.serializers.abstract_image_serializer import AbstractImageSerializer
from user.serializers import UserAbstractSerializer
from dealing.models import Dealing


class MostProductDealingOfMonthSerializer(serializers.ModelSerializer):

    product_group__user = UserAbstractSerializer()
    avatar = AbstractImageSerializer()

    class Meta:
        model = Dealing
        fields = [

        ]
