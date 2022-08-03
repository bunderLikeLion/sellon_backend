from rest_framework.viewsets import ModelViewSet

from auction.models import Auction
from auction.permissions import IsAuctionEditableOrDestroyable
from auction.serializers.auction_serializers import AuctionSerializer


class AuctionViewSet(ModelViewSet):
    queryset = Auction.objects.all().select_related('product', 'owner')
    serializer_class = AuctionSerializer
    permission_classes = [IsAuctionEditableOrDestroyable]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

