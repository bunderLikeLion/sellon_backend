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
    queryset = Product.objects.all()
    filterset_fields = ['product_category', 'quantity', 'quality', 'status']

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

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
