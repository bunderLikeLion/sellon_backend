from rest_framework import serializers
from product.models import ProductGroup
from user.serializers import UserAbstractSerializer
from auction.serializers import AuctionSerializer
from auction.models import Auction


class ProductGroupSerializer(serializers.ModelSerializer):
    user = UserAbstractSerializer(read_only=True)
    auction = AuctionSerializer(read_only=True)
    auction_id = serializers.PrimaryKeyRelatedField(
        source='auction',
        queryset=Auction.objects.all(),
        write_only=True,
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
        ]
