from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.permissions import IsProductEditableOrDestroyable
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsProductEditableOrDestroyable,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
