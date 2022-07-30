from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None
