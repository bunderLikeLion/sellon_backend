from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from auction.models import Auction
from auction.serializers.auction_serializers import AuctionSerializer


class MyAuctionAPIView(ListAPIView):

    def get_queryset(self):
        return Auction.objects.all() \
            .select_related('product', 'owner') \
            .prefetch_related('product__product_category') \
            .filter(owner=self.request.user)

    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        OrderingFilter,
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ['product__product_category_id']
    search_fields = ['title']
    ordering_fields = [
        'product_groups_count',
        'interested_auctions_count',
        'created_at',
        'updated_at'
    ]
