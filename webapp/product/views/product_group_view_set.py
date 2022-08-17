from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from product.permissions import IsProductGroupEditableOrDestroyable
from product.models import ProductGroup
from product.serializers import ProductGroupSerializer
from rest_framework.permissions import IsAuthenticated


class ProductGroupViewSet(ModelViewSet):
    serializer_class = ProductGroupSerializer
    permission_classes = [
        IsAuthenticated,
        IsProductGroupEditableOrDestroyable,
    ]
    filterset_fields = ['auction', 'user']

    def get_queryset(self):
        if self.action == 'list':
            return ProductGroup.objects.all().select_related('user').filter(products__isnull=False).distinct()
        return ProductGroup.objects.all().select_related('user')

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return instance

    def create(self, request, *args, **kwargs):
        """
        경매장에 상품 그룹을 등록합니다.
        - auction_id 를 param으로 첨부해야 합니다.
        - product_ids 를 배열로 첨부해야 합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        상품 그룹의 상세 내용을 반환합니다.
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        상품 그룹을 수정합니다.
        - 경매장에 참여하는 물품 목록/돈 등을 수정할 때 사용합니다.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        상품 그룹을 수정합니다.
        - 경매장에 참여하는 물품 목록/돈 등을 수정할 때 사용합니다.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        상품 그룹을 삭제합니다.
        - 종료된 경매장에 등록한 상품 그룹은 삭제할 수 없습니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        경매장에 등록한 상품 그룹 목록을 반환합니다.
        - [중요] auction(auction_id 아님)을 param으로 첨부해야 합니다.
        - [중요] user(user_id 아님)를 param으로 첨부하여, 특정 유저가 올린 물품 그룹을 얻어낼 수 있습니다. (자신의 물품 목록을 이 API로 얻어내면 됩니다.)
        """
        return super().list(request, *args, **kwargs)
