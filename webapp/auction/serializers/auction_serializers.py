from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from auction.models import Auction
from config.serializers import IntegerChoiceField
from product.models import Product
from product.serializers.product_abstract_serializer import ProductAbstractSerializer
from user.serializers import UserAbstractSerializer


class AuctionSerializer(ModelSerializer):
    owner = UserAbstractSerializer(read_only=True)
    product = ProductAbstractSerializer(read_only=True)

    dealing_type = IntegerChoiceField(choices=Auction.DEALING_TYPES)

    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Auction
        fields = [
            'id',
            'owner',
            'product_id',
            'product',
            'description',
            'start_at',
            'end_at',
            'created_at',
            'updated_at',
            'dealing_type',
            'product_groups_count'
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {}
