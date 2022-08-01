from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from auction.models import Auction
from auction.permissions import IsAuctionEditableOrDestroyable
from auction.serializers.auction_serializers import AuctionSerializer
from product.models import Product


class AuctionViewSet(ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuctionEditableOrDestroyable]

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        instance.product.status = Product.IN_AUCTION_STATUS
        instance.save()
        return instance
