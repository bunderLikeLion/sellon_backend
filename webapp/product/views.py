from django.db import transaction
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.permissions import IsProductEditableOrDestroyable, IsProductGroupEditableOrDestroyable
from .models import Product, ProductCategory, ProductGroup
from product.serializers import ProductSerializer, ProductCategorySerializer, ProductGroupSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsProductEditableOrDestroyable,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None


class ProductGroupViewSet(ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    permission_classes = [
        IsProductGroupEditableOrDestroyable,
    ]
    search_fields = ['auction']
    # TODO: 다른 것들도 필드 설정하기
    # TODO: list API에서 auction_id 없으면 404
    # TODO: list API에서 자기거 아닌건 배제하기
    # TODO: 자기가 만든 경매에 물건 그룹 못올리게 하기

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        # NOTE: 그룹에 올린 상품은 AUCTION에 올린 상태가 됩니다.
        # TODO: 이거 ProductGroupItem 모델에서 처리
        # TODO: Auction 모델에 finish? 메서드 만들고 거기서 종료처리시키기
        return instance

    def perform_update(self, serializer):
        # TODO: 수정했을 때, product status가 적절히 다 바뀌어야 함.
        return serializer.save()

    @transaction.atomic
    def perform_destroy(self, instance):
        # TODO: model에서 그룹에 올렸던 상품을 다시 HIDDEN_STATUS로 변경합니다.
        instance.delete()
