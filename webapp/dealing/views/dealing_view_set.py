from django.db.models import Q
from django.core.exceptions import PermissionDenied

from rest_framework.filters import OrderingFilter

from config.model_view_set import BaseModelViewSet
from dealing.models import Dealing
from dealing.serializers import DealingSerializer
from dealing.permissions import OnlyAuctionOwnerCreateDealingPermission


class DealingViewSet(BaseModelViewSet):
    serializer_class = DealingSerializer
    permission_classes = [
        OnlyAuctionOwnerCreateDealingPermission
    ]
    filter_backends = [OrderingFilter]
    ordering_fields = [
        'created_at',
        'updated_at',
    ]
    ordering = [
        '-updated_at',
    ]

    # TODO: 거래가 종료되었는지를 판단하는 API 를 따로 제공해야 하는가? 상대방이 거래 종료하면 프론트에서 캐치할 수 있나?

    def get_queryset(self):
        if self.is_anonymous_user:
            return Dealing.objects.none()

        return Dealing.objects.filter(
            Q(product__user=self.current_user) | Q(product_group__user=self.current_user)
        )

    def perform_create(self, serializer):
        auction = serializer.validated_data['auction']
        if auction.owner != self.current_user:
            # FIXME: 에러메세지가 잘 노출이 안됨.
            raise PermissionDenied('경매장을 연 사람만 거래를 생성할 수 있습니다.')

        return serializer.save(
            product=auction.product,
        )

    def create(self, request, *args, **kwargs):
        """
        경매장에서 상품 목록을 선택하여 거래를 생성합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        거래 상세 정보를 반환합니다.
        """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        거래 목록을 반환합니다.
        """
        return super().list(request, *args, **kwargs)
