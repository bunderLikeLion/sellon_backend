from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from product.permissions import IsProductEditableOrDestroyable
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsProductEditableOrDestroyable,
    ]
    queryset = Product.objects.all().select_related('user', 'product_category', 'thumbnail')
    filterset_fields = ['product_category', 'quantity', 'quality', 'status']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        인벤토리에 물폼을 생성합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        상품 정보를 반환합니다. 아래의 경우에만 조회 가능합니다.
        - 자신의 인벤토리에 있는 물품(자신의 물품)
        - 경매장에 올라와 있는 물품
        - 자신과 거래하고 있는 물품
        - 자신과 거래 완료한 물품
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        상품 정보를 수정합니다.
        - 자신의 물품인 경우만 수정 가능합니다.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        상품 정보를 부분 수정합니다.
        - 자신의 물품인 경우만 수정 가능합니다.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        상품을 삭제합니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        자신의 인벤토리에 있는 물품 목록을 모두 반환합니다.
        """
        queryset = self.filter_queryset(self.get_queryset().filter(user=self.request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
