from rest_framework.generics import ListAPIView

from auction.models import Auction
from auction.serializers import PopularAuctionSerializer


class MostPopularAPIView(ListAPIView):
    queryset = Auction.objects.in_progress().select_related('product', 'owner').order_by('-product_groups_count')[:3]
    serializer_class = PopularAuctionSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        """
        현재 진행중이면서 참가자가 많은 경매(인기 있는 경매) 3개를 반환합니다.
        """
        return self.list(request, *args, **kwargs)
