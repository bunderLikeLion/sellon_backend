from rest_framework import serializers

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
            'updated_at'
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
            'completed_at',
        ]
