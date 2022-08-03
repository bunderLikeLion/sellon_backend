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

    def create(self, request, *args, **kwargs):
        """
        경매장을 생성합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        경매장 상세 정보를 반환합니다.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        경매장 정보를 모두 수정합니다.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        경매장 정보를 부분 수정합니다.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        경매장을 삭제합니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        경매장 목록을 반환합니다.
        """
        return super().list(request, *args, **kwargs)
