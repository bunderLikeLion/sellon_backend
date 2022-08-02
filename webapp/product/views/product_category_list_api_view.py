from rest_framework.generics import ListAPIView

from product.models import ProductCategory
from product.serializers import ProductCategorySerializer


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None
