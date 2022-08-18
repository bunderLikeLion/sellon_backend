from auction.models import InterestedAuction
from auction.serializers import InterestedAuctionSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django.utils import timezone


class InterestedAuctionViewSet(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = InterestedAuctionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'auction'

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return InterestedAuction.objects.filter(user=self.request.user, auction__end_at__gte=timezone.now())
