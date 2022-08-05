from rest_framework import serializers

from auction.models import Auction
from product.models import ProductGroup, Product

from user.serializers import UserAbstractSerializer
from auction.serializers import AuctionSerializer
from .product_serializer import ProductSerializer


class ProductGroupSerializer(serializers.ModelSerializer):
    user = UserAbstractSerializer(read_only=True)
    auction = AuctionSerializer(read_only=True)
    auction_id = serializers.PrimaryKeyRelatedField(
        source='auction',
        queryset=Auction.objects.all(),
        write_only=True,
    )
    products = ProductSerializer(read_only=True, many=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        source='products',
        many=True,
        write_only=True,
        queryset=Product.objects.all(),
    )

    class Meta:
        model = ProductGroup
        fields = [
            'id',
            'user',
            'auction_id',
            'auction',
            'money',
            'description',
            'products',
            'product_ids',
        ]
        read_only_fields = [
            'auction'
        ]
        extra_kwargs = {
            'auction_id': {
                'required': True,
            },
            'products': {
                'required': True,
            }
        }
