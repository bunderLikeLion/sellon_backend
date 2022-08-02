from rest_framework.viewsets import ModelViewSet

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

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
