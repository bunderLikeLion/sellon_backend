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
    queryset = ProductGroup.objects.all().select_related('user')
    filterset_fields = ['auction', 'user']
    # TODO: Auction 모델에 finish? 메서드 만들고 그거 이용해서 종료처리시키기

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return instance
