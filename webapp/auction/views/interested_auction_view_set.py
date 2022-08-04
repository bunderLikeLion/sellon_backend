from auction.models import InterestedAuction
from auction.permissions import IsInterestedAuctionEditableOrDestroyable
from auction.serializers.interested_auction_serializers import InterestedAuctionSerializer
from django.db import transaction
from rest_framework.viewsets import ModelViewSet


class InterestedAuctionViewSet(ModelViewSet):
    queryset = InterestedAuction.objects.all()
    serializer_class = InterestedAuctionSerializer
    permission_classes = [IsInterestedAuctionEditableOrDestroyable]

    @transaction.atomic
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
