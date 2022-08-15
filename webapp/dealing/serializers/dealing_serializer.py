from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method

from auction.models import Auction
from auction.serializers import AuctionSerializer
from dealing.models.dealing import Dealing
from product.models import ProductGroup
from product.serializers import ProductSerializer, ProductGroupSerializer


class DealingSerializer(serializers.ModelSerializer):
    auction = AuctionSerializer(read_only=True)
    auction_id = serializers.PrimaryKeyRelatedField(
        source='auction',
        queryset=Auction.objects.all(),
        write_only=True,
    )
    product = ProductSerializer(read_only=True)
    product_group = ProductGroupSerializer(read_only=True)
    product_group_id = serializers.PrimaryKeyRelatedField(
        source='product_group',
        queryset=ProductGroup.objects.all(),
        write_only=True,
    )
    is_evaluated = serializers.SerializerMethodField(source='is_evaluated')
    last_message_sent_at = serializers.SerializerMethodField(source='last_message_sent_at')

    class Meta:
        model = Dealing
        fields = [
            'id',
            'auction',
            'auction_id',
            'product',
            'product_group',
            'product_group_id',
            'completed_at',
            'created_at',
            'updated_at',
            'is_evaluated',
            'last_message_sent_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
            'completed_at',
        ]

    @property
    def current_user(self):
        return self.context.get('request').user

    @property
    def is_anonymous_user(self):
        return self.current_user.is_anonymous

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_evaluated(self, dealing) -> bool:
        if self.is_anonymous_user:
            return False
        return dealing.dealing_evaluations.filter(evaluator=self.current_user).exists()

    @swagger_serializer_method(serializer_or_field=serializers.DateTimeField)
    def get_last_message_sent_at(self, dealing):
        if self.is_anonymous_user:
            return ''
        messages = dealing.messages.order_by('-updated_at')

        if len(messages) < 1:
            return ''
        return messages[0].created_at
