from auction.models import Auction, InterestedAuction
from auction.serializers import AuctionSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.serializers import UserAbstractSerializer


class InterestedAuctionSerializer(ModelSerializer):
    user = UserAbstractSerializer(read_only=True)
    auction = AuctionSerializer(read_only=True)
    auction_id = serializers.PrimaryKeyRelatedField(
        source='auction',
        queryset=Auction.objects.all(),
        write_only=True,
    )

    class Meta:
        model = InterestedAuction
        fields = [
            'id',
            'user',
            'auction_id',
            'auction',
        ]
